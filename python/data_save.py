# -------------------------------------------------------
# -------------------------------------------------------
# Projet : Walking Analysis Project
# Titre  : Sauvegarde data fichier + affichage graphique
# Auteur : Mathéo Gourdon - Arthur Mariano - Ianis Trigui
# Date   : 31/03/2021
# Github : arthurmio
# -------------------------------------------------------
# -------------------------------------------------------

import math
import sys
import numpy as np
import time
import serial
import matplotlib.pyplot as plt
from itertools import count

# --------------------
# -- INITIALISATION --
# --------------------
# Creation variable pour affichage
# -- Jambe droite --
# arduino 1
x_vals1  = []
y_vals11 = [] # Yaw1
y_vals12 = [] # Pitch1
y_vals13 = [] # Roll1

# arduino 2
x_vals2  = []
y_vals21 = [] # Yaw2
y_vals22 = [] # Pitch2
y_vals23 = [] # Roll2

# arduino 3
x_vals3  = []
y_vals31 = [] # Yaw3
y_vals32 = [] # Pitch3
y_vals33 = [] # Roll3

# -- Jambe gauche --
# arduino 4
x_vals4  = []
y_vals41 = [] # Yaw4
y_vals42 = [] # Pitch4
y_vals43 = [] # Roll4

# arduino 5
x_vals5  = []
y_vals51 = [] # Yaw5
y_vals52 = [] # Pitch5
y_vals53 = [] # Roll5

# arduino 6
x_vals6  = []
y_vals61 = [] # Yaw6
y_vals62 = [] # Pitch6
y_vals63 = [] # Roll6

# -- Centrale --
# arduino 7
x_vals7  = []
y_vals71 = [] # Yaw7
y_vals72 = [] # Pitch7
y_vals73 = [] # Roll7

decompte = 0

# -- Création du fichier.txt --
i=0
while(i==0):
    try:
        fichier = input ("Veuillez entrer un nom de fichier '.txt' pour votre acquisition : ")
        f = open(fichier, 'w')
        # data = np.loadtxt(fichier)
        i=1
    except:
        print("Veuillez bien taper le nom du fichier et de bien écrire l'extension '.txt'\n")
print("\nVeuillez patienter, le programme est entrain de calculer ...\n")

# ------------------
# -- LECTURE DATA --
# ------------------
# lecture du port série
arduinoData=serial.Serial('COM4', 115200)
time.sleep(1)
while(decompte<30) :
    while (arduinoData.inWaiting()==0) :
        pass
    # lecture du yaw/pitch/roll de l'arduino
    dataPacket  = arduinoData.readline()
    dataPacket  = str(dataPacket,'utf-8')
    splitPacket = dataPacket.split(',')
    time  = float(splitPacket[0])
    index = float(splitPacket[1])
    Yaw   = float(splitPacket[2])
    Pitch = float(splitPacket[3])
    Roll  = float(splitPacket[4])
    if(index==1):
        x_vals1.append(time)
        y_vals11.append(Yaw)
        y_vals12.append(Pitch)
        y_vals13.append(Roll)
    elif(index==2):
        x_vals2.append(time)
        y_vals21.append(Yaw)
        y_vals22.append(Pitch)
        y_vals23.append(Roll)
    if(index==3):
        x_vals3.append(time)
        y_vals31.append(Yaw)
        y_vals32.append(Pitch)
        y_vals33.append(Roll)
    elif(index==4):
        x_vals4.append(time)
        y_vals41.append(Yaw)
        y_vals42.append(Pitch)
        y_vals43.append(Roll)
    if(index==5):
        x_vals5.append(time)
        y_vals51.append(Yaw)
        y_vals52.append(Pitch)
        y_vals53.append(Roll)
    if(index==6):
        x_vals6.append(time)
        y_vals61.append(Yaw)
        y_vals62.append(Pitch)
        y_vals63.append(Roll)
    elif(index==7):
        x_vals7.append(time)
        y_vals71.append(Yaw)
        y_vals72.append(Pitch)
        y_vals73.append(Roll)
    print("index: ",index, "Yaw: ",Yaw," Pitch:",Pitch," Roll:",Roll)
    f.write(str(index)+ ' ')
    f.write(str(time)+ ' ')
    f.write(str(decompte)+ ' ')
    f.write(str(Yaw)+ ' ')
    f.write(str(Pitch)+ ' ')
    f.write(str(Roll)+ '\n')
    decompte += 1

f.close() # fermeture fichier

# ---------------
# -- AFFICHAGE --
# ---------------
# affichage jambe droite
plt.figure(1)
plt.subplot(311)
plt.title("Jambe droite haut") # Titre
plt.xlabel('time(ms)')         # Légende abscisse
plt.ylabel('Yaw/Pitch/Roll')   # Légende ordonnée
plt.plot(x_vals1,y_vals11,color='b',linewidth=1, label='Yaw1')   # Tracé du Yaw
plt.plot(x_vals1,y_vals12,color='g',linewidth=1, label='Pitch1') # Tracé du Pitch
plt.plot(x_vals1,y_vals13,color='r',linewidth=1, label='Roll1')  # Tracé du Roll

plt.subplot(312)
plt.title("Jambe droite milieu") # Titre
plt.xlabel('time(ms)')           # Légende abscisse
plt.ylabel('Yaw/Pitch/Roll')     # Légende ordonnée
plt.plot(x_vals2,y_vals21,color='b',linewidth=1, label='Yaw2')   # Tracé du Yaw
plt.plot(x_vals2,y_vals22,color='g',linewidth=1, label='Pitch2') # Tracé du Pitch
plt.plot(x_vals2,y_vals23,color='r',linewidth=1, label='Roll2')  # Tracé du Roll

plt.subplot(313)
plt.title("Jambe droite bas") # Titre
plt.xlabel('time(ms)')        # Légende abscisse
plt.ylabel('Yaw/Pitch/Roll')  # Légende ordonnée
plt.plot(x_vals3,y_vals31,color='b',linewidth=1, label='Yaw3')   # Tracé du Yaw
plt.plot(x_vals3,y_vals32,color='g',linewidth=1, label='Pitch3') # Tracé du Pitch
plt.plot(x_vals3,y_vals33,color='r',linewidth=1, label='Roll3')  # Tracé du Roll

# affichage jambe gauche
plt.figure(2)
plt.subplot(311)
plt.title("Jambe Gauche haut") # Titre
plt.xlabel('time(ms)')         # Légende abscisse
plt.ylabel('Yaw/Pitch/Roll')   # Légende ordonnée
plt.plot(x_vals4,y_vals41,color='b',linewidth=1, label='Yaw4')   # Tracé du Yaw
plt.plot(x_vals4,y_vals42,color='g',linewidth=1, label='Pitch4') # Tracé du Pitch
plt.plot(x_vals4,y_vals43,color='r',linewidth=1, label='Roll4')  # Tracé du Roll

plt.subplot(312)
plt.title("Jambe Gauche milieu") # Titre
plt.xlabel('time(ms)')           # Légende abscisse
plt.ylabel('Yaw/Pitch/Roll')     # Légende ordonnée
plt.plot(x_vals5,y_vals51,color='b',linewidth=1, label='Yaw5')   # Tracé du Yaw
plt.plot(x_vals5,y_vals52,color='g',linewidth=1, label='Pitch5') # Tracé du Pitch
plt.plot(x_vals5,y_vals53,color='r',linewidth=1, label='Roll5')  # Tracé du Roll

plt.subplot(313)
plt.title("Jambe Gauche bas") # Titre
plt.xlabel('time(ms)')        # Légende abscisse
plt.ylabel('Yaw/Pitch/Roll')  # Légende ordonnée
plt.plot(x_vals6,y_vals61,color='b',linewidth=1, label='Yaw6')   # Tracé du Yaw
plt.plot(x_vals6,y_vals62,color='g',linewidth=1, label='Pitch6') # Tracé du Pitch
plt.plot(x_vals6,y_vals63,color='r',linewidth=1, label='Roll6')  # Tracé du Roll

# affichage centrale
plt.figure(3)
plt.title("Centrale")        # Titre
plt.xlabel('time(ms)')       # Légende abscisse
plt.ylabel('Yaw/Pitch/Roll') # Légende ordonnée
plt.plot(x_vals7,y_vals71,color='b',linewidth=1, label='Yaw7')   # Tracé du Yaw
plt.plot(x_vals7,y_vals72,color='g',linewidth=1, label='Pitch7') # Tracé du Pitch
plt.plot(x_vals7,y_vals73,color='r',linewidth=1, label='Roll7')  # Tracé du Roll

plt.grid() # Ajout d'une grille
plt.show() # Afficher
