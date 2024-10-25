import paho.mqtt.client as mqtt

# Callback when a message is received
def on_message(client, userdata, msg):
    print('in function')
    print(f"Received message: '{msg.payload.decode()}' on topic '{msg.topic}'")

# Create an MQTT client
client = mqtt.Client()

print('run')

# Connect to the broker
client.connect("broker.hivemq.com")

print('connected')

# Subscribe to the topics
client.subscribe("Business news")
print('subscribed Business news')

client.subscribe("Tesla news")
print('subscribed Tesla news')

client.subscribe("Investment news")
print('subscribed Investment news')

client.subscribe("Techcrunch news")
print('subscribed Techcrunch news')

# Set up the message handling function
client.on_message = on_message


# Loop to keep the client listening for messages
client.loop_forever()