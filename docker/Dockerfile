# Use an official Python runtime as a parent image
FROM python:3.7

# Set the working directory to /src
WORKDIR /src

# Copy the current directory contents into the container at /src
COPY ./src /src

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
# EXPOSE 80

# Define environment variable
ENV NAME World
ENV MINING_BASE_PATH /host/
