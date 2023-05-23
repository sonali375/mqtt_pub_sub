import paho.mqtt.client as mqtt
broker_address = "localhost"
broker_port = 1883
topic = "Task"


# Callback function when a message is received and convert into python readable format
def on_message(elf, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")


# Create a MQTT client instance
client = mqtt.Client()

# Assign the on_message callback function
client.on_message = on_message
client.connect(broker_address, broker_port)
client.subscribe(topic)

# Start the MQTT client loop to process messages
client.loop_start()
try:
    while True:
        pass
except KeyboardInterrupt:
    pass

# Disconnect from the MQTT broker
client.disconnect()
