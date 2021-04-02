#!/usr/bin/env python
# coding: utf-8

from tkinter import *
import matplotlib
matplotlib.use("TkAgg")

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from serie import *

import time
import serial


#-------------creation de l'interface graphique---------------

# creation de la fenetre
window = Tk()

# fonction fermeture de fenetre
def close_window():
	window.destroy()

def interfaceGraphique():
	# Personnalisation fenetre
	window.title("Moniteur série arduino")
	window.geometry("700x500")
	window.minsize(300,200)
	window.maxsize(1080,720)
	window.config(background='white')
	
	# creation frame
	frame  = Frame(window, bg='white') #bd=1, relief=SUNKEN
	
	frame1 = Frame(frame, bg='white')
	frame2 = Frame(frame, bg='white')
	frame3 = Frame(frame, bg='white')
	
	# creation de la console
	console = Label(frame1, text="Console", bg="white")#, padx=300, pady=200)
	
	console.pack(side='left')
	
	# creation graphe
	print("Calcul en cours...")
	x_vals = []
	y_vals = []
	x_vals,y_vals = serialConnect()
	figure = Figure(figsize=(5,4), dpi=100)
	plot1 = figure.add_subplot(311)
	plot1.plot(x_vals,y_vals)
	plot1.grid()
	plot2 = figure.add_subplot(312)
	plot2.plot(x_vals,y_vals)
	plot2.grid()
	plot3 = figure.add_subplot(313)
	plot3.plot(x_vals,y_vals)
	plot3.grid()

	canvas = FigureCanvasTkAgg(figure, frame2)
	canvas.get_tk_widget().pack()
	
	# creation bouton
	bouton_connect = Button(frame3, text='Connect')
	bouton_quit    = Button(frame3, text='Quit', command=close_window)
	bouton_acq     = Button(frame3, text='Acquistion')
	bouton_stop    = Button(frame3, text='Stop')
	
	bouton_connect.pack(side='left', padx=10)
	bouton_quit.pack(side='left', padx=10)
	bouton_acq.pack(side='right', padx=10)
	bouton_stop.pack(side='right', padx=10)
	
	#bouton_connect.grid(row=0, column=0, padx=10)
	#bouton_quit.grid(row=0, column=10)
	#bouton_acq.grid(row=0, column=2, padx=50)
	#bouton_stop.grid(row=0, column=3)#, ipadx=2)
	
	
	frame1.grid(row=1, column=0)
	frame2.grid(row=2, column=0)
	frame3.grid(row=3, column=0)
	
	frame.pack(expand="yes")
	
	# Affichage fenetre
	window.mainloop()

def serialConnect():
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
		temps  = float(splitPacket[0])
		index = float(splitPacket[1])
		Yaw   = float(splitPacket[2])
		Pitch = float(splitPacket[3])
		Roll  = float(splitPacket[4])
		if(index==1):
			x_vals1.append(temps)
			y_vals11.append(Yaw)
			y_vals12.append(Pitch)
			y_vals13.append(Roll)
		elif(index==2):
			x_vals2.append(temps)
			y_vals21.append(Yaw)
			y_vals22.append(Pitch)
			y_vals23.append(Roll)
		elif(index==3):
			x_vals3.append(temps)
			y_vals31.append(Yaw)
			y_vals32.append(Pitch)
			y_vals33.append(Roll)
		elif(index==4):
			x_vals4.append(temps)
			y_vals41.append(Yaw)
			y_vals42.append(Pitch)
			y_vals43.append(Roll)
		elif(index==5):
			x_vals5.append(temps)
			y_vals51.append(Yaw)
			y_vals52.append(Pitch)
			y_vals53.append(Roll)
		elif(index==6):
			x_vals6.append(temps)
			y_vals61.append(Yaw)
			y_vals62.append(Pitch)
			y_vals63.append(Roll)
		elif(index==7):
			x_vals7.append(temps)
			y_vals71.append(Yaw)
			y_vals72.append(Pitch)
			y_vals73.append(Roll)
		print("index: ",index, "Yaw: ",Yaw," Pitch:",Pitch," Roll:",Roll)
		# f.write(str(index)+ ' ')
		# f.write(str(temps)+ ' ')
		# f.write(str(Yaw)+ ' ')
		# f.write(str(Pitch)+ ' ')
		# f.write(str(Roll)+ '\n')
		decompte += 1
	return x_vals7, y_vals71