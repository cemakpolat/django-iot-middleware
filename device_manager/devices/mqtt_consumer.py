import paho.mqtt.client as mqtt
import json, logging
from .models import Device, Measurement  # Import your Django models
from django.conf import settings

BROKER_URL= settings.MQTT_BROKER_HOST
TOPIC = settings.MQTT_CENTRAL_TOPIC

def on_connect(client, userdata, flags, rc):
    logging.info("Connected to MQTT broker with result code " + str(rc))
    client.subscribe(TOPIC)
    logging.info(f"Django is connected to the topic {TOPIC}")
    # Subscribe to MQTT topics, if needed

def on_message(client, userdata, message):
    try:
        payload = json.loads(message.payload.decode("utf-8"))
        device_id = payload['device_id']
        message_type = payload['message_type']
        if message_type == 'registration':
            # Create a new device
            try:#
                device_available  = Device.objects.filter(device_id=device_id).exists()
                if device_available:
                    device = Device.objects.get(device_id=device_id)
                    logging.warning("Device is already available")
                else:
                    logging.warning("Device is not available")
                    device = Device(device_id=device_id)
                    device.save()
            except Device.DoesNotExist:
                logging.error("Device doesn't exist")

        elif message_type == 'update':
            # Find the device and create a measurement
            device_available  = Device.objects.filter(device_id=device_id).exists()
            if device_available:
                device = Device.objects.get(device_id=device_id)
                measurement = Measurement(device=device, value=payload['value'])
                # print(device_id, message_type, payload)
                measurement.save()
            else:
                logging.warning("Device is not available")

        elif message_type == 'deregistration':
            # Delete the device and its measurements
            device_available  = Device.objects.filter(device_id=device_id).exists()
            if device_available:
                Device.objects.filter(device_id=device_id).delete()
        else:
            logging.warning(f"Unknown message type is sent, message:{payload}")
    except json.JSONDecodeError:
        # The message is not valid JSON
        logging.error(f"Received a non-JSON message on topic {message.topic}: {message.payload.decode()}")


    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_URL, 1883, 60)

    
