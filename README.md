# Dockerfile testing
This repo was created to explain how to use [this](https://hub.docker.com/r/dimorinny/testinfra/) image to test an environment of your dockerfiles.

It may be useful if you use continuous integration for docker containers and want to be sure that your images work properly.

## Why is it better do it in docker container?
Perhaps you are going to use this method with some CI servers such as TeamCity or Travis CI. And you don't want install required dependencies on build agents.

## How does it work?
To test the environment of docker container [testinfra](https://github.com/philpep/testinfra) is used, which allows you to check infrastructure environment on both local and remote hosts. To building docker images and running containers the [pytest](https://github.com/pytest-dev/pytest) built-in [fixture mechanism](http://doc.pytest.org/en/latest/fixture.html) is used. For every package docker client from testinfra container builds an image from package’s Dockerfile and runs container. After that, user’s tests from this package runs.

## Usage
To test your Dockerfiles you should create Python package with [conftest.py](https://github.com/dimorinny/dockerfiles-testing/blob/master/sample/conftest.py) file and also create packages with both Dockerfiles and your tests for every image that you have (see [example](https://github.com/dimorinny/dockerfiles-testing/blob/master/sample/alpine/)). Then, you should run [this](https://hub.docker.com/r/dimorinny/testinfra/) container with your tests and docker.sock as volumes (-v option). For example:

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