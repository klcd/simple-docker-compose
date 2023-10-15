# Use an official Python runtime as a base image
FROM python:3.8-slim-buster

# Set the working directory in the container to /usr/src/app
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app

# Install any needed packages specified in requirements.txt
RUN pip install mongoengine

RUN apt update && apt install -y vim
