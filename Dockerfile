# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /wk/app

RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ] 