# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables for Python
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE device_manager.settings

# Set the working directory to /app
WORKDIR /app

# Copy your Django project code into the container
COPY . /app
COPY start_servers.sh /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose the port that Uvicorn will run on
EXPOSE 8000