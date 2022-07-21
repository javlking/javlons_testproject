FROM ubuntu:latest
MAINTAINER Javlon
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev libpq-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ['python']
CMD ['app.py', 'functions/main.py']