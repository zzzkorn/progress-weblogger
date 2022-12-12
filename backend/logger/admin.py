from django.contrib import admin
from logger.models import Device
from logger.models import Message

admin.site.register(Device)
admin.site.register(Message)
