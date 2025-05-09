from vistas.menu import menu2
from programas.suma import sumar2
from programas.restas import restar2
from vistas.lineas import lineas

import threading
import time
import os
from datetime import datetime

mostrar_reloj = True

def reloj_en_vivo():
    while mostrar_reloj:
        os.system("clear") 
        print("Hora:", datetime.now().strftime("%H:%M:%S"))
        lineas(25)
        menu2()
        time.sleep(1)

hilo_reloj = threading.Thread(target=reloj_en_vivo)
hilo_reloj.daemon = True
hilo_reloj.start()

programa = True
while programa:
    try:
        r = int(input("[?] "))
    except ValueError:
        print("Por favor, escribe un número válido.")
        time.sleep(1)
        continue

    if r == 1:
        print("Sumar dos números")
        sumar2()
    elif r == 2:
        print("Resta de dos números")
        restar2()
    elif r == 0:
        print("Salir del programa")
        programa = False
        mostrar_reloj = False  
    else:
        print("Opción inválida.")
     

