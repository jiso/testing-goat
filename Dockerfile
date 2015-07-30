FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /goat
WORKDIR /goat
ADD requirements.txt /goat/
RUN pip install -r requirements.txt
ADD . /goat/
