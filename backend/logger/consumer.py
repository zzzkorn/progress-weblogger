import json

from channels.generic.websocket import WebsocketConsumer


class LoggerConsumer(WebsocketConsumer):
    # groups = ["broadcast"]

    def connect(self):
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        # message = text_data_json['message']
        # self.send(text_data=json.dumps(dict(message=message)))
        # Called with either text_data or bytes_data for each frame
        # You can call:
        # self.send(text_data="Hello world!")
        # # Or, to send a binary frame:
        # self.send(bytes_data="Hello world!")
        # # Want to force-close the connection? Call:
        # self.close()
        # # Or add a custom WebSocket error code!
        # self.close(code=4123)

    def disconnect(self, close_code):
        pass
