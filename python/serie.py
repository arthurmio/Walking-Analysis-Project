import time
import serial
import matplotlib.pyplot as plt
from itertools import count
from serie import *

# fig = plt.figure()
# ax = fig.add_subplot(111)
# fig.show()

# x_vals = []
# y_vals = []

def serialConnect():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    fig.show()
    
    x_vals  = []
    y_vals1 = []
    y_vals2 = []
    y_vals3 = []
    index = count()
    # lecture du port série
    arduinoData=serial.Serial('COM4', 115200)
    time.sleep(1)
    while(1==1) :
        while (arduinoData.inWaiting()==0) :
            pass
        # lecture du yaw/pitch/roll de l'arduino
        dataPacket=arduinoData.readline()
        dataPacket= str(dataPacket,'utf-8')
        splitPacket=dataPacket.split(',')
        Yaw=float(splitPacket[0])
        Pitch=float(splitPacket[1])
        Roll=float(splitPacket[2])
        print("Yaw: ",Yaw," Pitch:",Pitch," Roll:",Roll)
    
        # mise des valeurs du yaw/pitch/roll sur le graphique
        x_vals.append(next(index))
        y_vals1.append(Yaw)
        y_vals2.append(Pitch)
        y_vals3.append(Roll)
        ax.plot(x_vals, y_vals1, color='b')
        ax.plot(x_vals, y_vals2, color='r')
        ax.plot(x_vals, y_vals3, color='green')
        fig.canvas.draw()
        

serialConnect()