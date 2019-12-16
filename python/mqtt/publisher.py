import paho.mqtt.client as mqtt 
import time
import json

broker_address="<BROKER_IP>"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P2") #create new instance

print("connecting to broker")

client.connect(broker_address) #connect to broker

client.loop_start() #start the loop
query = {
    "data" : ["abc","123"]
}

print("Publishing message to topic","viz/request")
res = client.publish("viz/request",json.dumps(query))
print(res)

time.sleep(4) # wait
client.disconnect() #disconnect publisher
