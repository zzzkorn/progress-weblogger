from logger.models import Message
from logger.serializers.device import DeviceShortSerializer
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    device = DeviceShortSerializer()

    class Meta:
        model = Message
        fields = [
            "id",
            "timestamp",
            "device",
            "data",
            "raw_data",
            "message_type",
            "packet_type",
            "transcribed",
        ]
