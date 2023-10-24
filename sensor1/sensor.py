import paho.mqtt.client as mqtt
import json, os
import time
import random
import logging

# Configure the logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Device1")

# MQTT Broker Configuration
broker_address = os.environ.get("BROKER")
# broker_address = "mqtt-broker-host"
client = mqtt.Client("Device1")

# Device ID and Initial State
device_id = "device1"
is_registered = False

# Function to handle MQTT connection and reconnection
def connect_mqtt():
    while True:
        try:
            client.connect(broker_address)
            return True
        except Exception as e:
            logger.error(f"MQTT Connection Error: {e}")
            time.sleep(5)  # Wait for 5 seconds before retrying

# Connect to MQTT broker
if connect_mqtt():
    logger.info("Connected to MQTT broker")
else:
    logger.error("Failed to connect to MQTT broker")

# Define the registration and deregistration messages
registration_message = {"message_type": "registration", "device_id": device_id}
deregistration_message = {"message_type": "deregistration", "device_id": device_id}

# Function to send an update message with a random value
def send_update_message():
    update_message = {
        "message_type": "update",
        "device_id": device_id,
        "value": random.randint(0, 100)
    }
    client.publish("connect", json.dumps(update_message), retain=False)

# Main loop
while True:
    try:
        if not is_registered:
            # Send registration message
            client.publish("connect", json.dumps(registration_message))
            is_registered = True

        # Send update messages with a 5-second interval for 2 minutes
        update_end_time = time.time() + 120  # 2 minutes
        while time.time() < update_end_time:
            send_update_message()
            time.sleep(5)  # 5-second interval

        # Send deregistration message
        client.publish("connect", json.dumps(deregistration_message))
        is_registered = False

        # Sleep for 1 minute
        time.sleep(20)

    except KeyboardInterrupt:
        break
    except Exception as e:
        logger.error(f"Exception: {e}")
        if not connect_mqtt():
            logger.error("Failed to reconnect to MQTT broker")

# Disconnect from the MQTT broker
client.disconnect()
