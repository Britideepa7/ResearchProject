import os
import mysql.connector # type: ignore
import paho.mqtt.client as mqtt

MQTT_BROKER = 'broker.hivemq.com'
MQTT_PORT = 1883
TOPIC = 'shopping_mall/transactions'

db_config = {
    'user': 'root',
    'password': os.getenv('MYSQL_ROOT_PASSWORD', 'rootpassword'),
    'host': 'mysql-db',
    'database': 'shopping_mall'
}

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT Broker with result code {rc}")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"Message received on topic {msg.topic}: {msg.payload.decode()}")
    process_message(msg.payload.decode())

def process_message(message):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    
    customer_id, total_amount = message.split(',')
    query = "INSERT INTO purchases (customer_id, total_amount) VALUES (%s, %s)"
    cursor.execute(query, (customer_id, total_amount))
    conn.commit()
    cursor.close()
    conn.close()

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_forever()

if __name__ == "__main__":
    main()
