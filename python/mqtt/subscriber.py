import paho.mqtt.client as mqtt 
import time

############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    print(message.mess) 
    print()

def on_connect(client, obj, flags, rc):
    print("connect: " + str(rc))

def on_log(client, userdata, obj, buff):
    pass
    #print("log: " + str(buff))


broker_address="<BROKER_IP>"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P1") #create new instance

client.on_message=on_message #attach function to callback
print("connecting to broker")

client.connect(broker_address) #connect to broker

print("Subscribing to topic","viz/request")
client.subscribe("viz/request")

client.loop_forever() #start the loop
