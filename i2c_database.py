from smbus import SMBus
import sqlite3
import datetime

db = sqlite3.connect("externaldb")
cur = db.cursor()

#cur.execute("drop table if exist tblexternal")
#sql = """create table tblexternal(id integer(3) primary key autoincrement,datetime current_timestamp)"""
#cur.execute(sql)
#db.commit()

addr = 0x8
bus = SMBus(1)

numb = 1

print("Enter 1 for ON or 0 for OFF")
while nub == 1:
    ledstate = input(">>>>   ")
    
    if leadstate == "1":
        bus.write_byte(addr,0x1)
        block = bus.read_byte_data(8,1)
        sql = """Insert into tbli2c(message,datetime) values(?,?)"""
        data = (block,datetime.datetime.now())
        cur.execute(sql,data)
        db.commit()
        print(block)
    elif ledstate == "0":
        bus.write_byte(addr , 0x0)
    else:
        numb =0
