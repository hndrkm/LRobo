import serial
import pymysql
import datetime
db = pymysql.connect("localhost","root","","bdTemp")
cursor = db.cursor()
arduino = serial.Serial('COM12',baudrate=9600, timeout=1.0)
while True:
    line = arduino.readline()
    #line=line[1:len(line)-2]
    print(line)
    hora=datetime.datetime.now()
    dato=hora.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    sql = "INSERT INTO temmm(date, datos) \
    VALUES ('{0}','{1}')".format(dato,line.decode("utf-8"))
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print ("error",sql)
        db.rollback()
db.close()
