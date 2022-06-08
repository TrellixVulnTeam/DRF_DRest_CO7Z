FROM python:alpine
# MAINTAINER Gorelov Gleb

WORKDIR /home/oem/DRF_DRest/cars
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

