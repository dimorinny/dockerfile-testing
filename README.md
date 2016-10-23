# Dockerfiles testing
This repo is creating to explain, how to use [this](https://hub.docker.com/r/dimorinny/testinfra/) image for testing environment of your dockerfiles.

It can be useful if you use continues integration for your docker images and want to make sure, that your images works properly.

## Why do it in docker container?
Probably you will use this method with some CI server such as Teamcity or Travis CI. And you don't want to install required dependencies on agents.

## How it works?
For testing environment on docker containers I use [testinfra](https://github.com/philpep/testinfra) and [pytest](https://github.com/pytest-dev/pytest) which allows me to customize backend for running commands.

## Usages
For testing your Dockerfiles you should create Python package with [conftest.py](https://github.com/dimorinny/dockerfiles-testing/blob/master/sample/conftest.py) file and for every image creating package with Dockerfile and your test (see [example](https://github.com/dimorinny/dockerfiles-testing/blob/master/sample/alpine/)). After that you should run [this](https://hub.docker.com/r/dimorinny/testinfra/) container with your tests and docker.sock as volumes. For example:
```
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v <SOME_PATH>/sample/:/test dimorinny/testinfra
```