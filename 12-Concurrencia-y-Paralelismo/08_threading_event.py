"""
Ejercicio 8: Uso de Event

Objetivo: Sincronizar hilos usando threading.Event.

Instrucciones:
- Escribe un programa donde un hilo espere a que otro hilo le envíe una señal usando Event.
"""

import threading
import time

evento = threading.Event()

def esperar():
    print("Esperando señal...")
    evento.wait()
    print("¡Señal recibida!")

def enviar():
    time.sleep(2)
    print("Enviando señal...")
    evento.set()

hilo1 = threading.Thread(target=esperar)
hilo2 = threading.Thread(target=enviar)
hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()
