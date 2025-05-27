"""
Ejercicio 2: Varios hilos

Objetivo: Lanzar varios hilos simultáneamente.

Instrucciones:
- Escribe un programa que cree 5 hilos, cada uno imprimiendo su número de hilo.
"""

import threading

def imprimir_numero(n):
    print(f"Hilo número {n}")

hilos = []
for i in range(5):
    t = threading.Thread(target=imprimir_numero, args=(i,))
    hilos.append(t)
    t.start()

for t in hilos:
    t.join()
