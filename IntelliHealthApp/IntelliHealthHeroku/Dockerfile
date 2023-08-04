FROM ubuntu:latest
LABEL authors="tianquan"

# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container to /app
WORKDIR /

# Add the current directory contents into the container at /app
ADD . .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME PRD

# Run app.py when the container launches
CMD gunicorn -b 0.0.0.0:5000 app:app