from random import choice
from random import randrange

from django.core.management import BaseCommand
from logger.models import Device
from logger.models import Message


class Command(BaseCommand):
    def _reset(self):
        print("Delete data")
        Device.objects.all().delete()
        Message.objects.all().delete()

    def _generate_devices(self, count: int):
        print(f"generate_hosts x{count} times")
        for i in range(1, count):
            Device(
                description=f" Устройство {i}",
                ip_address=(
                    f"{randrange(1, 255)}."
                    f"{randrange(1, 255)}."
                    f"{randrange(1, 255)}."
                    f"{randrange(1, 255)}"
                ),
            ).save()

    def _generate_dialog(self):
        device = choice(Device.objects.all())
        Message(
            message_type="info",
            data="Установленно соединение",
            device=device,
        ).save()
        Message(
            packet_type="sent",
            device=device,
            message_type="packet",
            raw_data=b"Send Message",
        ).save()
        Message(
            packet_type="received",
            device=device,
            message_type="packet",
            raw_data=b"Receive Message",
        ).save()
        Message(
            message_type="error",
            data="Произошла ошибка",
            device=device,
        ).save()
        Message(
            message_type="info",
            data="Соединение прервано",
            device=device,
        ).save()

    def _generate_message_history(self, count: int):
        print(f"generate_message_history x{count} times")
        for i in range(count):
            self._generate_dialog()

    def handle(self, *args, **options):
        self._reset()
        self._generate_devices(10)
        self._generate_message_history(20)
