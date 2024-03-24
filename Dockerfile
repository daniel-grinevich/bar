# Use a specific version of the official Python image as the base image
FROM python:3.12-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /bar

# Update pip
RUN pip install --upgrade pip

# Copy only the requirements file into the container at /bar
COPY ./requirements.txt /bar/

# Install any dependencies specified in requirements.txt
RUN pip install -r requirements.txt
RUN pip freeze

# Copy the rest of the local code to the container
COPY . /bar/
