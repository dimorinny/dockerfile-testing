FROM python:3.7-alpine

MAINTAINER didika914@gmail.com

COPY requirements.txt requirements.txt

RUN apk add --update docker && \
    pip3 install -U pip && \
    pip3 install -r requirements.txt && \
    rm requirements.txt

COPY conftest.py conftest.py

WORKDIR /test
CMD pytest -v
