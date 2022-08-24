# pull official base image
FROM python:3.9.6-slim

# set work directory
WORKDIR /home/merin/Desktop/Projects/Healthcare-SDMR-application/SMDR

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 0

# install dependencies
RUN apt-get update \
    && apt-get install -y \
            && apt-get install libpq-dev gcc \
            && apt-get install psycopg2 \ 
            && apt-get install zlib1g-dev


RUN pip3 install --upgrade pip
COPY ./dev_requirements.txt .
RUN pip3 install -r dev_requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /home/merin/Desktop/Projects/Healthcare-SDMR-application/SMDR/entrypoint.sh
RUN chmod +x /home/merin/Desktop/Projects/Healthcare-SDMR-application/SMDR/entrypoint.sh


COPY . .


ENTRYPOINT ['/home/merin/Desktop/Projects/Healthcare-SDMR-application/SMDR/entrypoint.sh']