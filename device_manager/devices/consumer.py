import json
from channels.generic.websocket import AsyncWebsocketConsumer

class DeviceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.device_id = self.scope['url_route']['kwargs']['device_id']
        self.room_group_name = f"{self.device_id}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        await self.send(text_data=json.dumps({"message": message}))
        
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    

    async def device_created(self, event):
        await self.send(text_data=json.dumps({
            'event': 'device.created',
            'device_id': event['device_id'],
        }))

    async def measurement_created(self, event):
        await self.send(text_data=json.dumps({
            'event': 'measurement.created',
            'device_id': event['device_id'],
            'value': event['value'],
        }))

    async def device_deleted(self, event):
        await self.send(text_data=json.dumps({
            'event': 'device.deleted',
            'device_id': event['device_id'],
        }))
