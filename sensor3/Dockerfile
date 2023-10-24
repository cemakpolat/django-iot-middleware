# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the sensor script to the container
COPY sensor.py .

# Install MQTT library or any other dependencies your sensor script requires
RUN pip install paho-mqtt

# Run the sensor script
# CMD ["python", "sensor.py"]

