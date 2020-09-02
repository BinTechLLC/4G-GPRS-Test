#!/usr/bin/python3.7
import serial
import time
from time import sleep,strftime
runOnce = True
ser = serial.Serial('/dev/ttyS0',115200,timeout=1.0)
if(runOnce):
    sendPrefix="AT+"
    sendCommand="CSQ"
    sendSuffix="\r"
    sendData = bytes(sendPrefix+sendCommand+sendSuffix,'utf-8')
    ser.write(sendData)
    #sleep(1.0)
    serResponse = ser.read(1024)
    print(serResponse.decode('utf-8'))
    #sleep(1.0)
    sendPrefix="AT+"
    sendCommand="CMGF=1"
    sendSuffix="\r"
    sendData = bytes(sendPrefix+sendCommand+sendSuffix,'utf-8')
    ser.write(sendData)
    #sleep(1.0)
    serResponse = ser.read(1024)
    print(serResponse.decode('utf-8'))
    sendPrefix="AT+"
    sendCommand="CGPSPWR=1"
    sendSuffix="\r"
    sendData = bytes(sendPrefix+sendCommand+sendSuffix,'utf-8')
    ser.write(sendData)
    #sleep(1.0)
    serResponse = ser.read(1024)
    print(serResponse.decode('utf-8'))
    sleep(1.0)
    runOnce = False
print("Serial  Conn: "+str(ser.name))
print("Serial Avail: "+str(ser.is_open)+"\n")
sendPrefix="AT+CGNS"
sendCommand="INF"
sendSuffix="\r"
while True:
    sendData = bytes(sendPrefix+sendCommand+sendSuffix,'utf-8')
    try:
        ser.write(sendData)
        #print("\n")
    except Exception:
        print(Exception)
    serResponse = ser.read(1024)
    listA = str(serResponse).split(',')
    print("__________________________________")
    print("Fix Status: "+listA[1]+"     0=Disconnected, 1=Connected")
    print("UTC Date Time: "+listA[2])
    print("Latitude: "+listA[3])
    print("Longitude: "+listA[4])
    print("Altitude: "+listA[5]+" Meters")
    print("Speed: "+listA[6]+" Km/H")
    print("Cardinal: "+listA[7])
    print("Num of Sat: "+listA[14]+"\n")
    #print("\n")
    time.sleep(0.1)

ser.close()


