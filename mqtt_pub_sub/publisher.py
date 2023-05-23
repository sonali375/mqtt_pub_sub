import paho.mqtt.client as mqtt


class Publisher:
    def __init__(self):
        self.broker_address = "localhost"
        self.broker_port = 1883
        self.topic = "Task"

        # Create a MQTT client
        self.client = mqtt.Client()

    def publisher_connection(self, message):
        """
        :param message:
        :return:
        """
        # Connect to the MQTT broker
        self.client.connect(self.broker_address, self.broker_port)

        # Publish a message to the topic
        # message = "Hello, Its me Sonali!"
        self.client.publish(self.topic, message)

        # Disconnect from the MQTT broker
        self.client.disconnect()


if __name__ == "__main__":
    while True:
        mqtt_pub_obj = Publisher()
        user_message = input("Enter message here: ")
        mqtt_pub_obj.publisher_connection(message=user_message)
