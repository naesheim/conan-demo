FROM tomcat:9-jdk11-openjdk

ENV ARTIFACTORY_VERSION 6.18.0

RUN apt-get update && apt-get install openssl unzip

ENV ARTIFACTORY_HOME /opt/artifactory-cpp-ce-${ARTIFACTORY_VERSION}

RUN wget -O /tmp/artifactory.zip https://bintray.com/jfrog/artifactory/download_file?file_path=jfrog-artifactory-cpp-ce-${ARTIFACTORY_VERSION}.zip
RUN unzip /tmp/artifactory.zip -d /opt \
&& mv ${ARTIFACTORY_HOME}/etc ${ARTIFACTORY_HOME}/etc.default \
&& rm /tmp/artifactory.zip

CMD ${ARTIFACTORY_HOME}/bin/artifactory.sh                          