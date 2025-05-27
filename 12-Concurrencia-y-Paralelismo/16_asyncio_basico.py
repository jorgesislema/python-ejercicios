"""
Ejercicio 16: Asyncio básico

Objetivo: Crear y ejecutar una corrutina simple con asyncio.

Instrucciones:
- Escribe un programa que imprima un mensaje usando una función async y await.
"""

import asyncio

async def saludar():
    print("Hola desde asyncio")

asyncio.run(saludar())
