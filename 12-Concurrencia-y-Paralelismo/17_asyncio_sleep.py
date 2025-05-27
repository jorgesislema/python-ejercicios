"""
Ejercicio 17: Pausa con asyncio.sleep

Objetivo: Usar asyncio.sleep para simular tareas asíncronas.

Instrucciones:
- Escribe un programa que imprima un mensaje, espere 2 segundos y luego imprima otro mensaje usando async/await.
"""

import asyncio

async def tarea():
    print("Inicio de la tarea async")
    await asyncio.sleep(2)
    print("Fin de la tarea async")

asyncio.run(tarea())
