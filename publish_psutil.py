import time
import paho.mqtt.client as mqtt
import psutil

def on_connect(client,userdata,flags,rc):
    print(f"Conected with result {rc}")
    
client = mqtt.Client()
client.on_connect = on_connect
client.connect("broker.emqx.io",1883,60)
cpuPerData = psutil.cpu_percent(interval = 20)
ramPerData = psutil.virtual_memory().percent
data_payload = "field1 = " +str(cpuPerData) + "field2 = " + str(ramPerData) 
client.publish(topic="topic1",payload=data_payload,qos=0,retain=False)


#for i in range(5):
    #client.publish(topic="topic1",payload=f"hello!!! {i}",qos=0,retain=False)
    #print(f"send {i} to topic1")
    #time.sleep(1)
client.loop_forever()