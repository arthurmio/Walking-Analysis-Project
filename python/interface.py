# -------------------------------------------------------
# -------------------------------------------------------
# Projet : Walking Analysis Project
# Titre  : Interface arduino avec lissage courbe
# Auteur : Mathéo Gourdon - Arthur Mariano - Ianis Trigui
# Date   : 06/04/2021
# Github : arthurmio
# Python : version 3.9.2
# -------------------------------------------------------
# -------------------------------------------------------
import sys
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
import time
import serial

try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

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

def serialConnect():
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
	decompte = 0
	arduinoData=serial.Serial('COM4', 115200)
	time.sleep(1)
	while(decompte<50) : # nomre d'acquisitions
		while (arduinoData.inWaiting()==0) :
			pass
		# lecture du yaw/pitch/roll de l'arduino
		dataPacket  = arduinoData.readline()
		dataPacket  = str(dataPacket,'utf-8')
		splitPacket = dataPacket.split(',')
		temps = float(splitPacket[0])
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
		f.write(str(index)+ ' ')
		f.write(str(temps)+ ' ')
		f.write(str(Yaw)+ ' ')
		f.write(str(Pitch)+ ' ')
		f.write(str(Roll)+ '\n')
		decompte += 1
	return x_vals1, y_vals11, y_vals12, y_vals13, x_vals2, y_vals21, y_vals22, y_vals23, x_vals3, y_vals31, y_vals32, y_vals33, x_vals4, y_vals41, y_vals42, y_vals43, x_vals5, y_vals51, y_vals52, y_vals53, x_vals6, y_vals61, y_vals62, y_vals63, x_vals7, y_vals71, y_vals72, y_vals73,

# appel fonction serialConnect()
x_vals1,y_vals11,y_vals12,y_vals13, x_vals2, y_vals21, y_vals22, y_vals23,x_vals3, y_vals31, y_vals32, y_vals33, x_vals4, y_vals41, y_vals42, y_vals43, x_vals5, y_vals51, y_vals52, y_vals53, x_vals6, y_vals61, y_vals62, y_vals63, x_vals7, y_vals71, y_vals72, y_vals73 = serialConnect()


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

# --------------------------
# --- Fenetre principale ---
# --------------------------
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        self.controller = controller
        frame  = tk.Frame(self,  bg='white')
        frame1 = tk.Frame(frame, bg='white')
        frame2 = tk.Frame(frame, bg='white')
        frame3 = tk.Frame(frame, bg='white')

        label  = tk.Label(frame1, text="Walking Analysis Project", bg="white", font=("Nueva Std",20))
        label.pack()

        # Creation graphe
        xs_7  = np.array(x_vals7)
        ys_71 = np.array(y_vals71)
        ys_72 = np.array(y_vals72)
        ys_73 = np.array(y_vals73)
        # lissage courbe
        model71 = make_interp_spline(xs_7, ys_71)
        model72 = make_interp_spline(xs_7, ys_72)
        model73 = make_interp_spline(xs_7, ys_73)
        xs7  = np.linspace(min(x_vals7),max(x_vals7),500)
        ys71 = model71(xs7)
        ys72 = model72(xs7)
        ys73 = model73(xs7)
        figure = Figure(figsize=(5,4), dpi=100)
        plot1 = figure.add_subplot(111)
        plot1.grid()
        plot1.set_title("Centrale")         # Titre
        plot1.set_xlabel('time(s)')         # Légende abscisse
        plot1.set_ylabel('Yaw/Pitch/Roll')  # Légende ordonnée
        plot1.plot(xs7,ys71,color='b', linewidth=1, label='Yaw')   # Tracé du Yaw
        plot1.plot(xs7,ys72,color='g', linewidth=1, label='Pitch') # Tracé du Pitch
        plot1.plot(xs7,ys73,color='r', linewidth=1, label='Roll')  # Tracé du Roll
        canvas = FigureCanvasTkAgg(figure, frame2)
        canvas.get_tk_widget().pack()
        
        # Creation bouton
        button1 = tk.Button(frame3, text="Jambe Gauche",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(frame3, text="Jambe Droite",
                            command=lambda: controller.show_frame("PageTwo"))
        button_quit = tk.Button(frame3, text="Quit",
                            command=exitApp)
        button1.pack(side="left", padx=100)
        button2.pack(side="right", padx=100)
        button_quit.pack(side='right', padx=10)
        
        frame1.grid(row=1, column=0)
        frame2.grid(row=2, column=0)
        frame3.grid(row=3, column=0)

        frame.pack(expand="yes")

# ----------------------------
# --- Fenetre jambe gauche ---
# ----------------------------
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        self.controller = controller
        frame  = tk.Frame(self,  bg='white')
        frame1 = tk.Frame(frame, bg='white')
        frame2 = tk.Frame(frame, bg='white')
        frame3 = tk.Frame(frame, bg='white')

        #img = tk.PhotoImage(file='./python/photos/logo.png')
        #img = img.subsample(2,2)
        #img.resize((30,20))
        #logo = tk.Label(frame1, image = img)
        label  = tk.Label(frame1, text="Walking Analysis Project / Jambe Gauche", bg="white", font=("Nueva Std",20))
        #logo.pack(side='left')
        label.pack()

        # Creation graphe
        xs_1  = np.array(x_vals1)
        ys_11 = np.array(y_vals11)
        ys_12 = np.array(y_vals12)
        ys_13 = np.array(y_vals13)
        xs_2  = np.array(x_vals2)
        ys_21 = np.array(y_vals21)
        ys_22 = np.array(y_vals22)
        ys_23 = np.array(y_vals23)
        xs_3  = np.array(x_vals3)
        ys_31 = np.array(y_vals31)
        ys_32 = np.array(y_vals32)
        ys_33 = np.array(y_vals33)
        # lissage courbe
        model11 = make_interp_spline(xs_1, ys_11)
        model12 = make_interp_spline(xs_1, ys_12)
        model13 = make_interp_spline(xs_1, ys_13)
        model21 = make_interp_spline(xs_2, ys_21)
        model22 = make_interp_spline(xs_2, ys_22)
        model23 = make_interp_spline(xs_2, ys_23)
        model31 = make_interp_spline(xs_3, ys_31)
        model32 = make_interp_spline(xs_3, ys_32)
        model33 = make_interp_spline(xs_3, ys_33)
        xs1  = np.linspace(min(x_vals1),max(x_vals1),500)
        xs2  = np.linspace(min(x_vals2),max(x_vals2),500)
        xs3  = np.linspace(min(x_vals3),max(x_vals3),500)
        ys11 = model11(xs1)
        ys12 = model12(xs1)
        ys13 = model13(xs1)
        ys21 = model21(xs2)
        ys22 = model22(xs2)
        ys23 = model23(xs2)
        ys31 = model31(xs3)
        ys32 = model32(xs3)
        ys33 = model33(xs3)
        figure = Figure(figsize=(5,4), dpi=100)
        plot1  = figure.add_subplot(311)
        plot1.grid()
        plot1.set_title("Jambe droite haut", fontsize=8) # Titre
        # plot1.plot(x_vals1,y_vals11,color='b',linewidth=1, label='Yaw1')   # Tracé du Yaw
        # plot1.plot(x_vals1,y_vals12,color='g',linewidth=1, label='Pitch1') # Tracé du Pitch
        # plot1.plot(x_vals1,y_vals13,color='r',linewidth=1, label='Roll1')  # Tracé du Roll
        plot1.plot(xs1,ys11,color='b',linewidth=1, label='Yaw1')   # Tracé du Yaw
        plot1.plot(xs1,ys12,color='g',linewidth=1, label='Pitch1') # Tracé du Pitch
        plot1.plot(xs1,ys13,color='r',linewidth=1, label='Roll1')  # Tracé du Roll
        
        plot2 = figure.add_subplot(312)
        plot2.grid()
        plot2.set_title("Jambe droite milieu", fontsize=8) # Titre
        # plot2.plot(x_vals2,y_vals21,color='b',linewidth=1, label='Yaw1')   # Tracé du Yaw
        # plot2.plot(x_vals2,y_vals22,color='g',linewidth=1, label='Pitch1') # Tracé du Pitch
        # plot2.plot(x_vals2,y_vals23,color='r',linewidth=1, label='Roll1')  # Tracé du Roll
        plot2.plot(xs2,ys21,color='b',linewidth=1, label='Yaw1')   # Tracé du Yaw
        plot2.plot(xs2,ys22,color='g',linewidth=1, label='Pitch1') # Tracé du Pitch
        plot2.plot(xs2,ys23,color='r',linewidth=1, label='Roll1')  # Tracé du Roll

        plot3 = figure.add_subplot(313)
        plot3.grid()
        plot3.set_title("Jambe droite bas", fontsize=8) # Titre
        plot3.set_xlabel('time(s)', fontsize=8)         # Légende abscisse
        plot3.set_ylabel('Yaw/Pitch/Roll', fontsize=8)  # Légende ordonnée
        # plot3.plot(x_vals3,y_vals31,color='b',linewidth=1, label='Yaw1')   # Tracé du Yaw
        # plot3.plot(x_vals3,y_vals32,color='g',linewidth=1, label='Pitch1') # Tracé du Pitch
        # plot3.plot(x_vals3,y_vals33,color='r',linewidth=1, label='Roll1')  # Tracé du Roll
        plot3.plot(xs3,ys31,color='b',linewidth=1, label='Yaw1')   # Tracé du Yaw
        plot3.plot(xs3,ys32,color='g',linewidth=1, label='Pitch1') # Tracé du Pitch
        plot3.plot(xs3,ys33,color='r',linewidth=1, label='Roll1')  # Tracé du Roll

        canvas = FigureCanvasTkAgg(figure, frame2)
        canvas.get_tk_widget().pack()
        
		# Creation bouton
        button1 = tk.Button(frame3, text="Centrale",
                            command=lambda: controller.show_frame("StartPage"))
        button2 = tk.Button(frame3, text="Jambe Droite",
                            command=lambda: controller.show_frame("PageTwo"))
        button_quit = tk.Button(frame3, text="Quit",
                            command=exitApp)
        button1.pack(side="left", padx=100)
        button2.pack(side="right", padx=100)
        button_quit.pack(side='right', padx=10)
        
        frame1.grid(row=1, column=0)
        frame2.grid(row=2, column=0)
        frame3.grid(row=3, column=0)

        frame.pack(expand="yes")

# ----------------------------
# --- Fenetre jambe droite ---
# ----------------------------
class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        self.controller = controller
        frame  = tk.Frame(self,  bg='white')
        frame1 = tk.Frame(frame, bg='white')
        frame2 = tk.Frame(frame, bg='white')
        frame3 = tk.Frame(frame, bg='white')

        label  = tk.Label(frame1, text="Walking Analysis Project / Jambe Droite", bg="white", font=("Nueva Std",20))
        label.pack()

        # Creation graphe
        xs_4  = np.array(x_vals4)
        ys_41 = np.array(y_vals41)
        ys_42 = np.array(y_vals42)
        ys_43 = np.array(y_vals43)
        xs_5  = np.array(x_vals5)
        ys_51 = np.array(y_vals51)
        ys_52 = np.array(y_vals52)
        ys_53 = np.array(y_vals53)
        xs_6  = np.array(x_vals6)
        ys_61 = np.array(y_vals61)
        ys_62 = np.array(y_vals62)
        ys_63 = np.array(y_vals63)
        # lissage courbe
        model41 = make_interp_spline(xs_4, ys_41)
        model42 = make_interp_spline(xs_4, ys_42)
        model43 = make_interp_spline(xs_4, ys_43)
        model51 = make_interp_spline(xs_5, ys_51)
        model52 = make_interp_spline(xs_5, ys_52)
        model53 = make_interp_spline(xs_5, ys_53)
        model61 = make_interp_spline(xs_6, ys_61)
        model62 = make_interp_spline(xs_6, ys_62)
        model63 = make_interp_spline(xs_6, ys_63)
        xs4  = np.linspace(min(x_vals4),max(x_vals4),500)
        xs5  = np.linspace(min(x_vals5),max(x_vals5),500)
        xs6  = np.linspace(min(x_vals6),max(x_vals6),500)
        ys41 = model41(xs4)
        ys42 = model42(xs4)
        ys43 = model43(xs4)
        ys51 = model51(xs5)
        ys52 = model52(xs5)
        ys53 = model53(xs5)
        ys61 = model61(xs6)
        ys62 = model62(xs6)
        ys63 = model63(xs6)
        figure = Figure(figsize=(5,4), dpi=100)
        plot1  = figure.add_subplot(311)
        plot1.grid()
        plot1.set_title("Jambe gauche haut", fontsize=8) # Titre
        # plot1.plot(x_vals4,y_vals41,color='b',linewidth=1, label='Yaw1')   # Tracé du Yaw
        # plot1.plot(x_vals4,y_vals42,color='g',linewidth=1, label='Pitch1') # Tracé du Pitch
        # plot1.plot(x_vals4,y_vals43,color='r',linewidth=1, label='Roll1')  # Tracé du Roll
        plot1.plot(xs4,ys41,color='b',linewidth=1, label='Yaw1')   # Tracé du Yaw
        plot1.plot(xs4,ys42,color='g',linewidth=1, label='Pitch1') # Tracé du Pitch
        plot1.plot(xs4,ys43,color='r',linewidth=1, label='Roll1')  # Tracé du Roll
        
        plot2 = figure.add_subplot(312)
        plot2.grid()
        plot2.set_title("Jambe gauche milieu", fontsize=8) # Titre
        # plot2.plot(x_vals5,y_vals51,color='b',linewidth=1, label='Yaw1')   # Tracé du Yaw
        # plot2.plot(x_vals5,y_vals52,color='g',linewidth=1, label='Pitch1') # Tracé du Pitch
        # plot2.plot(x_vals5,y_vals53,color='r',linewidth=1, label='Roll1')  # Tracé du Roll
        plot1.plot(xs5,ys51,color='b',linewidth=1, label='Yaw1')   # Tracé du Yaw
        plot1.plot(xs5,ys52,color='g',linewidth=1, label='Pitch1') # Tracé du Pitch
        plot1.plot(xs5,ys53,color='r',linewidth=1, label='Roll1')  # Tracé du Roll

        plot3 = figure.add_subplot(313)
        plot3.grid()
        plot3.set_title("Jambe gauche bas", fontsize=8) # Titre
        plot3.set_xlabel('time(s)', fontsize=8)         # Légende abscisse
        plot3.set_ylabel('Yaw/Pitch/Roll', fontsize=8)  # Légende ordonnée
        # plot3.plot(x_vals6,y_vals61,color='b',linewidth=1, label='Yaw1')   # Tracé du Yaw
        # plot3.plot(x_vals6,y_vals62,color='g',linewidth=1, label='Pitch1') # Tracé du Pitch
        # plot3.plot(x_vals6,y_vals63,color='r',linewidth=1, label='Roll1')  # Tracé du Roll
        plot1.plot(xs6,ys61,color='b',linewidth=1, label='Yaw1')   # Tracé du Yaw
        plot1.plot(xs6,ys62,color='g',linewidth=1, label='Pitch1') # Tracé du Pitch
        plot1.plot(xs6,ys63,color='r',linewidth=1, label='Roll1')  # Tracé du Roll

        canvas = FigureCanvasTkAgg(figure, frame2)
        canvas.get_tk_widget().pack()
        
		# Creation bouton
        button1 = tk.Button(frame3, text="Jambe Gauche",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(frame3, text="Centrale",
                            command=lambda: controller.show_frame("StartPage"))
        button_quit = tk.Button(frame3, text="Quit",
                            command=exitApp)
        button1.pack(side="left", padx=100)
        button2.pack(side="right", padx=100)
        button_quit.pack(side='right', padx=10)
        
        frame1.grid(row=1, column=0)
        frame2.grid(row=2, column=0)
        frame3.grid(row=3, column=0)

        frame.pack(expand="yes")

# fonction pour fermer les fenetres
def exitApp():
    sys.exit()

if __name__ == "__main__":
    app = SampleApp()
    app.title("Moniteur Serie Arduino")
    app.geometry("700x500")
    app.minsize(300,200)
    app.maxsize(1080,720)
    app.config(background='white')
    app.mainloop()

