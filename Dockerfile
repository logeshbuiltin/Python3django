FROM python:3.9

MAINTAINER purush

ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y
RUN mkdir /ipl
WORKDIR /ipl
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt