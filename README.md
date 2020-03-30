<H5> Artifactory-os commands:</H5>

_build docker image_ 
```
docker build . -t artifactory-cpp
```


_run docker image with persistent volume in /tmp/artifactory and port to localhost:8080_
```
docker run -v /tmp/artifactory/data:/opt/artifactory-cpp-ce-6.18.0/data -v /tmp/artifactory/etc:/opt/artifactory-cpp-ce-6.18.0/etc -p 8080:8081 -d artifactory-cpp
```

<H5> Intermediate steps: </H5>

_add artifactory repository to conan remote_
```
conan remote add <REMOTE-NAME> http://localhost:8080/artifactory/api/conan/conan-local
```

<H5>Conan commands:</H5>

```
conan install . --install-folder=tmp/build
conan build . --source-folder=tmp/source --build-folder=tmp/build
conan package . --build-folder=tmp/build --package-folder=tmp/package
conan export-pkg . 
conan upload ruter-check -r <REMOTE-NAME> --all
```