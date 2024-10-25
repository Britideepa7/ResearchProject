import paho.mqtt.client as mqtt
import time
import numpy as np

QOS = 0

message = "I am in Germany"

def on_connect(mqttc, userdata, flags, rc):
    mqttc.subscribe(topic)
    mqttc.publish(topic, message, qos=QOS)


def on_message(mqttc, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    tdecode = time.time()-t_con
    tdecode_array.append(tdecode)
    tdecode_max = max(tdecode_array)
    tdecode_average = sum(tdecode_array) / len(tdecode_array)
    tdecode_min = min(tdecode_array)
    print('Current: %s' % tdecode)
    print('Maximum: %s' % tdecode_max)
    print('Average: %s' % tdecode_average)
    print('Minimum: %s' % tdecode_min)
    print('tdecode_array: %s' % tdecode_array)
    np.savetxt('tdecodehivemq0.out', tdecode_array, delimiter=',')#To save the RTTarray(tdecode_array)values helps to plot the figure
    print('topic: %s' % topic)
    mqttc.publish(topic, message, qos=QOS)


def on_log(mqttc, userdata, level, buf):
    print(level, buf)
tdecode_array = []
topic = "hello world"
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_log = on_log
mqttc.connect("broker.hivemq.com")
mqttc.connect("test.mosquitto.org")



#we can test with different mqtt public brokers,loopback and also mininet

i=0
while(i<40):
    mqttc.loop()
    i=i+1
    t_con = time.time()