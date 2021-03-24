#!/usr/bin/env python
# coding: utf-8

from tkinter import *
import matplotlib
matplotlib.use("TkAgg")

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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
	frame = Frame(window, bg='white') #bd=1, relief=SUNKEN
	
	frame1 = Frame(frame, bg='white')
	frame2 = Frame(frame, bg='white')
	frame3 = Frame(frame, bg='white')
	
	# creation de la console
	console = Label(frame1, text="Console", bg="white")#, padx=300, pady=200)
	console.pack(side='left')
	
	# creation graphe
	figure = Figure(figsize=(5,4), dpi=100)
	plot = figure.add_subplot(1, 1, 1)
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













# # Sélection du port COM
# port = Label(window, text="selectPort : ")
# champPort = Entry(window)
# port.place(x=5, y=10, width = 80, height=25)
# champPort.place(x=90, y=10, width = 160, height=25)

#Mise en place d'un widget de label
#l = LabelFrame(window, text="Configuration", padx=300, pady=200)
#l.pack(fill="both", expand="yes")
#Label(l).pack()
