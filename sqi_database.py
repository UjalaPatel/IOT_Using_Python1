import spidev
import sqlite3
import datetime
import time

db = sqlite3.connect("externaldb")
cur = db.connect()

spi = spidev.SpiDev(0,0)
spi.open(0,0)
msg = 0xAA

spi.max_speed_hz = 115200
while 1:
    spi.writebytes([0x4,0x86])
    data = spi.readbytes(1)
    print(data)
    sql = """Insert into tblspi(message,datetime) values(?,?)"""
    dataset = (data,datetime.datetime.now())
    cur.execute(sql,dataset)
    time.sleep(1)
    
