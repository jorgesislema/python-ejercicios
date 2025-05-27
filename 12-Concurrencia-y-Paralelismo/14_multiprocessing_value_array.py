"""
Ejercicio 14: Value y Array en multiprocessing

Objetivo: Compartir variables entre procesos usando Value y Array.

Instrucciones:
- Escribe un programa donde dos procesos incrementen un valor compartido.
"""

from multiprocessing import Process, Value
import time

def incrementar(valor):
    for _ in range(1000):
        with valor.get_lock():
            valor.value += 1

valor = Value('i', 0)
procesos = [Process(target=incrementar, args=(valor,)) for _ in range(2)]
for p in procesos:
    p.start()
for p in procesos:
    p.join()
print(f"Valor final: {valor.value}")
