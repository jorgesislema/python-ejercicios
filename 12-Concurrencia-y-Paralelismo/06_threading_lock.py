"""
Ejercicio 6: Uso de Lock

Objetivo: Proteger recursos compartidos con threading.Lock.

Instrucciones:
- Escribe un programa donde varios hilos incrementan una variable global protegida por un Lock.
"""

import threading

contador = 0
lock = threading.Lock()

def incrementar():
    global contador
    for _ in range(1000):
        with lock:
            contador += 1

hilos = [threading.Thread(target=incrementar) for _ in range(10)]
for h in hilos:
    h.start()
for h in hilos:
    h.join()

print(f"Contador final: {contador}")
