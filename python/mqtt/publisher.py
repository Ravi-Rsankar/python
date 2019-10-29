import paho.mqtt.client as mqtt 
import time
import json

############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

def on_connect(client, obj, flags, rc):
    print("connect: " + str(rc))

def on_log(client, userdata, obj, buff):
    pass
    #print("log: " + str(buff))


broker_address="172.31.1.164"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P2") #create new instance

client.on_message=on_message #attach function to callback
print("connecting to broker")

client.connect(broker_address) #connect to broker

client.loop_start() #start the loop
query = {
    "vars" : ["MAY91CX210","PI_06106"],
    "start_value":1570390090000-60*60000,
    "end_value":1570390090000,
    "sample_value": 1,
    "sample_unit": "hours",
    "round":3,
    "type":"object"
}

print("Publishing message to topic","viz/request")
res = client.publish("viz/request",json.dumps(query))
print(res)

res2 = client.publish("viz/request",json.dumps(query))
print(res2)
time.sleep(4) # wait

client.loop_stop() #stop the loop