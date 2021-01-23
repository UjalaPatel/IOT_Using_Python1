import sqlite3
import datetime
import paho.mqtt.client as mqtt

db = sqlite3.connect("externaldb")
cur = db.cursor()

def on_message(client,userdata,message):
    print(message.topic + " " + str(message.payload)+"\n")
    decodeData = message.payload.decode("utf-8")
    print(decodeData)
    

client = mqtt.Client()
client.on_message = on_message
client.connect("broker.hivemq.com",1883)
client.subscribe("badsuratSaurabh",qos=0)
client.loop_forever()