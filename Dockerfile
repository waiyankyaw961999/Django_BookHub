# base image
FROM python:3.10.0

#maintainer
LABEL Author="WaiYanKyaw"

ENV PYTHONBUFFERED 1

#switch to /app directory so that everything runs from here
WORKDIR /usr/src/app
RUN pip3 install --upgrade pip
#copy the app code to image working directory
COPY requirements.txt ./
#let pip install required packages
RUN pip3 install -r requirements.txt
