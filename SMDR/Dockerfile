FROM python:3.10-slim-buster

ENV PYTHONBUFFERED 1

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

RUN apt-get install -y git
RUN apt-get install -y vim

WORKDIR /app

COPY requirements.txt /app
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app

RUN chmod +x entryfile.sh
