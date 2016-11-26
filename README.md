# Dockerfile testing

[![](https://images.microbadger.com/badges/image/dimorinny/testinfra.svg)](https://microbadger.com/images/dimorinny/testinfra "Get your own image badge on microbadger.com")

This repo was created to explain how to use [this](https://hub.docker.com/r/dimorinny/testinfra/) image to test an environment of your dockerfiles.

It may be useful if you use continuous integration for docker containers and want to be sure that your images work properly.

## Why is it better to do it in docker container?
Perhaps you are going to use this method with some CI servers such as TeamCity or Travis CI. And you don't want to install required dependencies on build agents.

## How does it work?
To test the environment of docker container [testinfra](https://github.com/philpep/testinfra) is used, which allows you to check infrastructure environment on both local and remote hosts. To build docker images and running containers the [pytest](https://github.com/pytest-dev/pytest) built-in [fixture mechanism](http://doc.pytest.org/en/latest/fixture.html) is used. For every package docker client from testinfra container builds an image from package’s Dockerfile and runs container. After that, user’s tests from this package runs.

## Usage
To test your Dockerfiles you should create Python package with both Dockerfiles and your tests for every image that you have (see [check commands](https://github.com/dimorinny/dockerfile-testing/blob/master/sample/commands/) and [file](https://github.com/dimorinny/dockerfile-testing/blob/master/sample/copy/) examples). Then, you should run [this](https://hub.docker.com/r/dimorinny/testinfra/) container with your tests and docker.sock as volumes (-v option). For example:

```
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v <SOME_PATH>/sample/:/test dimorinny/testinfra
```

Sample output:

```
============================= test session starts ==============================
platform linux -- Python 3.6.0b2, pytest-3.0.3, py-1.4.31, pluggy-0.4.0 -- /usr/local/bin/python3.6
cachedir: .cache
rootdir: /test, inifile:
plugins: testinfra-1.4.2
collecting ... collected 4 items

commands/test_image.py::TestAlpainEnvironmentTest::test_curl_exists[commands] PASSED
commands/test_image.py::TestAlpainEnvironmentTest::test_docker_exists[commands] PASSED
copy/test_image.py::TestAlpainEnvironmentTest::test_copied_file_exists[copy/docker] PASSED
copy/test_image.py::TestAlpainEnvironmentTest::test_copied_file_content[copy/docker] PASSED
=========================== 4 passed in 0.88 seconds ===========================
```
For sample, how to use it with CI, look it this [repo](https://github.com/dimorinny/docker-android-sdk), that use Travis CI for testing image environment.
