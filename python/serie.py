import time
import serial
import matplotlib.pyplot as plt
from itertools import count

def serialConnect():
    fig = plt.figure()
    #ax = fig.add_subplot(111) # à modifier?
    fig.show()
    
    x_vals1 = [] # arduino 1
    x_vals2 = [] # arduino 2

    y_vals1 = [] # Yaw
    y_vals2 = [] # Pitch
    y_vals3 = [] # Roll
    index = count()

    # lecture du port série
    arduinoData=serial.Serial('COM4', 115200)
    time.sleep(1)
    while(1==1) :
        while (arduinoData.inWaiting()==0) :
            pass
        # lecture du yaw/pitch/roll de l'arduino
        dataPacket  = arduinoData.readline()
        dataPacket  = str(dataPacket,'utf-8')
        splitPacket = dataPacket.split(',')
        index = float(splitPacket[0])
        Yaw   = float(splitPacket[1])
        Pitch = float(splitPacket[2])
        Roll  = float(splitPacket[3])
        print("index: ",index,"Yaw: ",Yaw," Pitch:",Pitch," Roll:",Roll)
        if(index==1): # arduino1
            x_vals1.append(next(index))
            y_vals1.append(Yaw)
            y_vals2.append(Pitch)
            y_vals3.append(Roll)
            ax.plot(x_vals1, y_vals1, color='b', linewidth=1)
            ax.plot(x_vals1, y_vals2, color='r', linewidth=1)
            ax.plot(x_vals1, y_vals3, color='green', linewidth=1)
            ax.subplot(2,1,1)
            fig.canvas.draw()
        elif(index==2): # arduino2
            x_vals2.append(next(index))
            y_vals1.append(Yaw)
            y_vals2.append(Pitch)
            y_vals3.append(Roll)
            ax.plot(x_vals2, y_vals1, color='b', linewidth=1)
            ax.plot(x_vals2, y_vals2, color='r', linewidth=1)
            ax.plot(x_vals2, y_vals3, color='green', linewidth=1)
            ax.subplot(2,1,2)
            fig.canvas.draw()

serialConnect()