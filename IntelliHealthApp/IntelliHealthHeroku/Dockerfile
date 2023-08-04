#FROM ubuntu:latest
#LABEL authors="tianquan"

# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container to /app
WORKDIR /

# Add the current directory contents into the container at /app
ADD . .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME PRD

# Run app.py when the container launches
CMD gunicorn app:app
