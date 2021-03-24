#!/usr/bin/env python
# coding: utf-8

import serial
import time
arduinoData=serial.Serial('COM4', 115200)
time.sleep(1)
while(1==1) :
    while (arduinoData.inWaiting()==0) :
        pass
    dataPacket=arduinoData.readline()
    dataPacket= str(dataPacket,'utf-8')
    splitPacket=dataPacket.split(',')
    Yaw=float(splitPacket[0])
    Pitch=float(splitPacket[1])
    Roll=float(splitPacket[2])
    print("Yaw: ",Yaw," Pitch:",Pitch," Roll:",Roll)
    time.sleep(0.1)

