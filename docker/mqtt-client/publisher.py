import paho.mqtt.client as mqtt

MQTT_BROKER = 'broker.hivemq.com'
MQTT_PORT = 1883
TOPIC = 'shopping_mall/transactions'

def publish_message(message):
    client = mqtt.Client()
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.publish(TOPIC, message)
    client.disconnect()

if __name__ == "__main__":
    customer_id = 1
    total_amount = 100.50
    message = f"{customer_id},{total_amount}"
    publish_message(message)
