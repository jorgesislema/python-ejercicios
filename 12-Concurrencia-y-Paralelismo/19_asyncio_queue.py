"""
Ejercicio 19: Queue con asyncio

Objetivo: Compartir datos entre tareas asíncronas usando asyncio.Queue.

Instrucciones:
- Escribe un programa donde una tarea productora ponga datos en una cola y una tarea consumidora los saque e imprima.
"""

import asyncio

async def productor(q):
    for i in range(5):
        print(f"Produciendo {i}")
        await q.put(i)
        await asyncio.sleep(0.5)
    await q.put(None)

async def consumidor(q):
    while True:
        item = await q.get()
        if item is None:
            break
        print(f"Consumiendo {item}")

async def main():
    q = asyncio.Queue()
    await asyncio.gather(productor(q), consumidor(q))

asyncio.run(main())
