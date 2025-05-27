"""
Ejercicio 18: Varias tareas con asyncio

Objetivo: Ejecutar varias tareas asíncronas en paralelo.

Instrucciones:
- Escribe un programa que lance 3 tareas asíncronas que impriman mensajes con diferentes pausas.
"""

import asyncio

async def tarea(n, pausa):
    print(f"Tarea {n} iniciada")
    await asyncio.sleep(pausa)
    print(f"Tarea {n} terminada")

async def main():
    await asyncio.gather(
        tarea(1, 1),
        tarea(2, 2),
        tarea(3, 3)
    )

asyncio.run(main())
