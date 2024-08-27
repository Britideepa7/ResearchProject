import paho.mqtt.client as mqtt
import json
import time

MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "shopping-mall/customer-details"

def publish_customer_details(client):
    customer_details = {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    client.publish(MQTT_TOPIC, json.dumps(customer_details))
    print("Published customer details")

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

while True:
    publish_customer_details(client)
    time.sleep(5)

client.loop_forever()
