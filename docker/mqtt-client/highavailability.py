import paho.mqtt.client as mqtt
import json
import time
import numpy as np
from roundrobin.basic_rr import basic
import matplotlib.pyplot as plt

QOS = 0

get_roundrobin = basic(["broker.hivemq.com","test.mosquitto.org","127.0.0.1"])
#get_roundrobin = basic(["127.0.0.1"])

#''.join([get_roundrobin() for _ in range(7)])


message1 = {"title":"Four Days After Prime Day, Amazon Slashes The Price Of AirPods Max To A Record Low", "content": "As the autumn leaves begin to fall and the crisp October air settles in, Amazon has decided to extend its Prime Day festivities and offers a great opportunity for audiophiles. This Sunday, a particul… "}
message2 = {"title": "Yes, there were humans controlling Tesla's bartending robots behind the scenes", "content": "An image of Tesla's Optimus robot serving drinks at the company's We,Robot event. The robots were remotely controlled by humans.TeslaTesla's robots serving drinks and talking to guests at the.. "}
message3 = {"title": "WSJ: Apple Is No Longer in Talks to Join OpenAI Investment Round","content": "Tom Dotan and Berber Jin, reporting late last night for The Wall Street Journal (News+): Apple is no longer in talks to participate in an OpenAI funding round expected to raise as much as $6.5 bil… "}
message4 = {"title": "Bye-bye bots: Altera's game-playing AI agents get backing from Eric Schmidt | TechCrunch", "content": "Autonomous, AI-based players are coming to a gaming experience near you, and a new startup, Altera, is joining the fray to build this new guard of AI agents.\r\nThe company announced Wednesday that it … "}

def on_connect(mqttc, userdata, flags, rc):
        mqttc.subscribe(topic1)
        mqttc.subscribe(topic2)
        mqttc.subscribe(topic3)
        mqttc.subscribe(topic4)

        mqttc.publish(topic1, json.dumps(message1,indent=4),qos=QOS)
        mqttc.publish(topic2,json.dumps(message2,indent=4),qos=QOS)
        mqttc.publish(topic3,json.dumps(message3,indent=4), qos=QOS)
        mqttc.publish(topic4,json.dumps(message4,indent=4), qos=QOS)

def on_message(mqttc, userdata, msg):
        tdecode = time.time()-t_con1
        tdecode_array.append(tdecode)
        tdecode_max = max(tdecode_array)
        tdecode_average = sum(tdecode_array) / len(tdecode_array)
        tdecode_min = min(tdecode_array)
        np.savetxt('brake.out', tdecode_array, delimiter=',')#To save the RTTarray(tdecode_array)values helps to plot the figure
        print('topic1: %s' % topic1)
        print('topic2: %s' % topic2)
        print('topic3: %s' % topic3)
        print('topic4: %s' % topic4)

       # mqttc.publish(topic1,topic2,topic3,topic4, message, qos=QOS)
       # print("broker with choice()",broker)
def on_log(mqttc, userdata, level, buf):
        print(level, buf)

tdecode_array = []

topic1 = "Business news"
topic2 = "Tesla news"
topic3 = "Investment news"
topic4 = "Techcrunch news"

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_log = on_log
x = get_roundrobin()
print('x', x)
mqttc.connect(x)#we can test with different mqtt public brokers,loopback and also mininet

t_start = time.time()

i=0
tif = 0
tstart = time.time()
while(i<=400): #(time.time()-tstart < 60):
     mqttc.loop()
     if i in [100, 200, 300]: 
         print ("\n\n\n\n\n\n\n\nInside If condition\n\n\n\n\n\n\n\n\n\n")
         x1 = get_roundrobin()
         print('x1',x1)
         tifs = time.time()
         mqttc.connect(x1)
         tif = time.time() - tifs
         i+=1 
         continue
     i = i+1
     t_con1 = time.time() - tif
     tif = 0


else:
    t_total = time.time()-t_start
    print('t_total',t_total)
    print('num of time samples', len(tdecode_array))
    plt.figure()
    plt.subplot(121)
    plt.xlabel('Message Transmission')
    plt.ylabel('Round Trip Time (RTT) in seconds')
    plt.title('RTT for MQTT Messages')
    plt.legend()
    plt.plot(tdecode_array)
    plt.subplot(122)
    plt.boxplot(tdecode_array)
    plt.xlabel('Message Transmission')
    plt.ylabel('Round Trip Time (RTT) in seconds')
    plt.title('RTT for Messages in Boxplot')
    plt.legend()
    plt.show()
