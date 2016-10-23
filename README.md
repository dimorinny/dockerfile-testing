# Dockerfiles testing
This repo is creating to explain, how to use [this](https://hub.docker.com/r/dimorinny/testinfra/) image for testing environment of your dockerfiles.

It can be useful if you use continues integration for your docker containers and want to make sure, that your images works properly.

## Why do it in docker container?
Probably you will use this method with some CI server such as Teamcity or Travis CI. And you don't want to install required dependencies on agents.

## How it works?
For testing environment on docker containers I use [testinfra](https://github.com/philpep/testinfra) which allows check infrastructure environment on local and remote hosts. For building docker images and running containers I use [fixture mechanism](http://doc.pytest.org/en/latest/fixture.html) from [pytest](https://github.com/pytest-dev/pytest). For every package docker client from [testinfra](https://hub.docker.com/r/dimorinny/testinfra/) container build image from Dockerfile in this package and run container. After that your tests from this package run on started container.

## Usages
For testing your Dockerfiles you should create Python package with [conftest.py](https://github.com/dimorinny/dockerfiles-testing/blob/master/sample/conftest.py) file and for every image creating package with Dockerfile and your test (see [example](https://github.com/dimorinny/dockerfiles-testing/blob/master/sample/alpine/)). After that you should run [this](https://hub.docker.com/r/dimorinny/testinfra/) container with your tests and docker.sock as volumes. For example:
```
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v <SOME_PATH>/sample/:/test dimorinny/testinfra
```

Sample output:

```
============================= test session starts =============================
platform linux -- Python 3.6.0b2, pytest-3.0.3, py-1.4.31, pluggy-0.4.0 -- /usr/local/bin/python3.6
cachedir: .cache
rootdir: /test, inifile:
plugins: testinfra-1.4.2
collecting ... collected 2 items

alpine/test_image.py::TestAlpainEnvironmentTest::test_curl_exists[alpine] PASSED
alpine/test_image.py::TestAlpainEnvironmentTest::test_docker_exists[alpine] PASSED

=========================== 2 passed in 0.40 seconds ===========================
```