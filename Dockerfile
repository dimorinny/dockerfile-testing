FROM python:3.6-alpine

MAINTAINER didika914@gmail.com

RUN apk add --update docker && \
    pip3 install testinfra && \
    pip3 install PyHamcrest

WORKDIR /test
CMD pytest -v
