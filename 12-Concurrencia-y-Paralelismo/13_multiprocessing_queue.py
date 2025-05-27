"""
Ejercicio 13: Queue en multiprocessing

Objetivo: Compartir datos entre procesos usando multiprocessing.Queue.

Instrucciones:
- Escribe un programa donde un proceso productor ponga datos en una cola y un proceso consumidor los saque e imprima.
"""

from multiprocessing import Process, Queue
import time

def productor(q):
    for i in range(5):
        print(f"Produciendo {i}")
        q.put(i)
        time.sleep(0.5)
    q.put(None)

def consumidor(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumiendo {item}")

q = Queue()
p1 = Process(target=productor, args=(q,))
p2 = Process(target=consumidor, args=(q,))
p1.start()
p2.start()
p1.join()
p2.join()
