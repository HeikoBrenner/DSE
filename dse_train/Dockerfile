# # # Using lightweight alpine image
# # FROM python:3.6-alpine

# # # Installing packages
# # RUN apk update
# # RUN pip install --upgrade pip
# # RUN pip install py-numpy

# # # Defining working directory and adding source code
# # WORKDIR /usr/src/app
# # ADD requirements.txt /app/requirements.txt
# # #COPY dseapp ./dseapp

# # # Install API dependencies
# # RUN pip install -r /app/requirements.txt

# # # Start app
# # EXPOSE 5000
# # ENTRYPOINT ["/usr/src/app/bootstrap.sh"]


# # The Google App Engine python runtime is Debian Jessie with Python installed
# # and various os-level packages to allow installation of popular Python
# # libraries. The source is on github at:
# #   https://github.com/GoogleCloudPlatform/python-docker
# FROM gcr.io/google-appengine/python

# # Create a virtualenv for the application dependencies.
# # If you want to use Python 2, add the -p python2.7 flag.
# RUN virtualenv -p python3.6 /env

# # Set virtualenv environment variables. This is equivalent to running
# # source /env/bin/activate. This ensures the application is executed within
# # the context of the virtualenv and will have access to its dependencies.
# ENV VIRTUAL_ENV /env
# ENV PATH /env/bin:$PATH

# ADD requirements.txt /app/requirements.txt
# RUN pip install -r /app/requirements.txt

# # Install dependencies.
# #WORKDIR /usr/src/app
# # COPY requirements.txt ./
# # RUN pip install -r requirements.txt

# #COPY /model app/model
# # Add application code.
# #COPY app ./dseapp
# #COPY ./ ./
# #COPY . /app/model
# #COPY . /model
# ADD . /app

# CMD [ "python", "./main.py" ]
# #ENTRYPOINT ["bootstrap.sh"]

# #CMD honcho start -f /app/procfile $PROCESSES


FROM ubuntu:latest
RUN apt-get update -y
#RUN apt-get pip install --upgrade pip
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD [ "python", "main.py" ]