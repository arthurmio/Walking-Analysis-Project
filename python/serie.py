#!/usr/bin/env python
# coding: utf-8

# creation de la connexion serie
from serial import *
# Port série ttyACM0
# Vitesse de baud : 9600
# Timeout en lecture : 1 sec
# Timeout en écriture : 1 sec
with Serial(port="/dev/ttyACM0", baudrate=9600, timeout=1, writeTimeout=1) as port_serie:
    if port_serie.isOpen():
        while True:
            ligne = port_serie.read_line()
            print ligne
nombre = input("Entrez un nombre : ")
port_serie.write(nombre.encode('ascii'))
