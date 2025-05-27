"""
Ejercicio 20: Timeout con asyncio

Objetivo: Controlar el tiempo de espera de una tarea asíncrona.

Instrucciones:
- Escribe un programa que lance una tarea que puede tardar y la cancele si supera 2 segundos usando asyncio.wait_for.
"""

import asyncio

async def tarea_lenta():
    print("Tarea lenta iniciada")
    await asyncio.sleep(5)
    print("Tarea lenta terminada")

async def main():
    try:
        await asyncio.wait_for(tarea_lenta(), timeout=2)
    except asyncio.TimeoutError:
        print("¡Timeout alcanzado!")

asyncio.run(main())
