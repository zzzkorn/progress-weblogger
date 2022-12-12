from logger.models import Device
from rest_framework import serializers


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ["id", "ip_address", "description", "message_count"]
