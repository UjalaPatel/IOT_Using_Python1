import time
import paho.mqtt.client as mqtt
import sqlite3
import datetime

db = sqlite3.connect("mqttdb.db")
cur = db.cursor()

def on_message(client,userdata,msg):
    print(msg.topic+"  "+str(msg.payload)+"\n")
    decodeData = msg.payload.decode("utf-8")
    #time.sleep(1)
    sql = """insert into tblmqtt(msg,curtime) values(?,?);"""
    data_tuple = (decodeData,datetime.datetime.now())
    cur.execute(sql,data_tuple)
    db.commit()
    print(decodeData)
    
cur.execute("select * from tblmqtt order by id limit 5")
data = cur.fetchall()

for row in data:
    print(row)
    time.sleep(1)
    
client = mqtt.Client()
client.on_message = on_message
client.connect("broker.emqx.io",1883)
client.subscribe("mscit/testing3",qos=0)
client.loop_forever()
db.close()
