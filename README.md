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


<H4> Conan example</H4>

consists of:
- **parse-lib**, a header-only library.
- **lib-test**, an executable with the other library as a dependency.

`cd parse-lib`

_create a **parse-lib** package and test the package in **test-lib** project_:
`conan create . naesheim/test --test-folder ../lib-test/`


this is the equivelant of:
* install **parse-lib** dependencies
* package **parse-lib** library
* change directory to **test-lib**
* install **test-lib** dependencies including the generated **parse-lib** library
* generate the binary
* test the binary