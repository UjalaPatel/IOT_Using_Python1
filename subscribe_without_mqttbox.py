import time
import paho.mqtt.client as mqtt
import sqlite3

db = sqlite3.connect("mqttdb")
cur = db.cursor()

def on_message(client,userdata,msg):
    print(msg.topic+"  "+str(msg.payload)+"\n")
    decodeData = msg.payload.decode("utf-8")
    sql = """insert into tblmqtt(msg) values(?);"""
    data_tuple = (decodeData,)
    cur.execute(sql,data_tuple)
    db.commit()
    print(decodeData)
    
client = mqtt.Client()
client.on_message = on_message
client.connect("broker.emqx.io",1883)
client.subscribe("topic1",qos=0)
client.loop_forever()
db.close()