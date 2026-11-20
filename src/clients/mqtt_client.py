from paho.mqtt.client import Client

class MqttClient(Client):
    def __init__(self, host: str = 'tcp://broker.hivemq.com'):
        super().__init__()
        self.host = host
        self.client = Client.connect(self, host=host)


    def subscribe_on_broker(self, broker_name: str = None):
        return self.client.subscribe()




