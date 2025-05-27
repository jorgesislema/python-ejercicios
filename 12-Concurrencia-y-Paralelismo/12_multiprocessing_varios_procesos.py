"""
Ejercicio 12: Varios procesos

Objetivo: Lanzar varios procesos simultáneamente.

Instrucciones:
- Escribe un programa que cree 3 procesos, cada uno imprimiendo su número de proceso.
"""

from multiprocessing import Process

def imprimir_numero(n):
    print(f"Proceso número {n}")

procesos = []
for i in range(3):
    p = Process(target=imprimir_numero, args=(i,))
    procesos.append(p)
    p.start()

for p in procesos:
    p.join()
