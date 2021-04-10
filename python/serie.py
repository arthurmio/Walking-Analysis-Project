# -------------------------------------------------------
# -------------------------------------------------------
# Projet : Walking Analysis Project
# Titre  : Affichage courbe en temps réel
# Auteur : Mathéo Gourdon - Arthur Mariano - Ianis Trigui
# Date   : 10/04/2021
# Github : arthurmio
# Python : version 3.9.2
# -------------------------------------------------------
# -------------------------------------------------------
import time
import serial
import matplotlib.pyplot as plt
from itertools import count
from serie import *

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
        Yaw=float(splitPacket[2])
        Pitch=float(splitPacket[3])
        Roll=float(splitPacket[4])
        print("Yaw: ",Yaw," Pitch:",Pitch," Roll:",Roll)

        # mise des valeurs du yaw/pitch/roll sur le graphique
        x_vals.append(next(index))
        y_vals1.append(Yaw)
        y_vals2.append(Pitch)
        y_vals3.append(Roll)
        ax.grid()
        ax.set_title("Affichage temps réel")
        ax.plot(x_vals, y_vals1, color='b')
        ax.plot(x_vals, y_vals2, color='r')
        ax.plot(x_vals, y_vals3, color='g')
        fig.canvas.draw()


serialConnect() 