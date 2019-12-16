import paho.mqtt.client as mqtt 
import time
import json

broker_address="172.31.1.164"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P2") #create new instance

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

time.sleep(4) # wait
client.disconnect() #disconnect publisher
