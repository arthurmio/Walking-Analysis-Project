import math
import sys
import numpy as np
import time
import serial
import matplotlib.pyplot as plt
from itertools import count

# Code pour sauvegarder data dans un fichier + affichage sur graphique

# Creation variable pour affichage
x_vals1 = [] # arduino 1
#x_vals2 = [] # arduino 2

y_vals1 = [] # Yaw
y_vals2 = [] # Pitch
y_vals3 = [] # Roll

index = count()
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

# lecture du port série
arduinoData=serial.Serial('COM4', 115200)
time.sleep(1)
while(decompte<20) :
    while (arduinoData.inWaiting()==0) :
        pass
    # lecture du yaw/pitch/roll de l'arduino
    dataPacket  = arduinoData.readline()
    dataPacket  = str(dataPacket,'utf-8')
    splitPacket = dataPacket.split(',')
    #index = float(splitPacket[0])
    Yaw   = float(splitPacket[0])
    Pitch = float(splitPacket[1])
    Roll  = float(splitPacket[2])
    x_vals1.append(decompte)
    y_vals1.append(Yaw)
    y_vals2.append(Pitch)
    y_vals3.append(Roll)
    print("Yaw: ",Yaw," Pitch:",Pitch," Roll:",Roll)
    f.write(str(decompte)+ ' ')
    f.write(str(Yaw)+ ' ')
    f.write(str(Pitch)+ ' ')
    f.write(str(Roll)+ '\n')
    decompte += 1

f.close() # fermeture fichier

plt.plot(x_vals1,y_vals1,color='b',linewidth=1) # Tracé du Yaw
plt.plot(x_vals1,y_vals2,color='g',linewidth=1) # Tracé du Pitch
plt.plot(x_vals1,y_vals3,color='r',linewidth=1) # Tracé du Roll
plt.title("Analyse de la marche")    # Titre
plt.xlabel('x')                      # Légende abscisse
plt.ylabel('y')                      # Légende ordonnée
plt.grid()                           # Ajout d'une grille
plt.show()                           # Afficher
