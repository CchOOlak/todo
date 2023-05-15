FROM python:3.10-alpine

RUN mkdir -p /code
ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt