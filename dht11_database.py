import adafruit_dht
import time
import RPi.GPIO as GPIO
import datetime
import sqlite3

GIPO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.IN)

db = sqlite3.connect("externaldb")
cur = db.cursor()

dhtDevice = adafruit_dht.DHT11(14)
while True:
    try:
        temp_c = dhtDevice.temperature
        temp_f = temp_c * (9/5) +32
        humidity = dhtDevice.humidity
        sql = """insert into tbldht(temprature_c,temprature_f,humidity,createdDate) values(?,?,?,?)"""
        data = (tempc,temp_f,humidity,datetime.datetime.now())
        cur.execute(sql,data)
        db.commit()
        print("temp: {:.1f} F/ {:.1f} C/ Humidity: {}%".format(temp_f,temp_c,humidity))
        time.sleep(1)
    except RuntimeError as error:
        print(error.args[0])
    time.sleep(5.0)

