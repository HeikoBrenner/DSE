FROM ubuntu:latest
RUN apt-get update -y
#RUN apt-get pip install --upgrade pip
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD [ "python", "main.py" ]

# FROM python:3.6-alpine
# RUN apk update
# ENV INSTALL_PATH /bsawf
# RUN mkdir -p $INSTALL_PATH
# WORKDIR $INSTALL_PATH
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# COPY . .
# CMD [ "python", "main.py" ]