# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /wk/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "manage.py" "runserver", "0.0.0.0:8000" ]