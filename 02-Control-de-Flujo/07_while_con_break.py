"""
Ejercicio 7: while con break

Objetivo: Usar break para salir de un bucle.

Instrucciones:
- Escribe un programa que pida números al usuario hasta que introduzca un número negativo.
"""

while True:
    n = int(input("Introduce un número (negativo para salir): "))
    if n < 0:
        print("¡Hasta luego!")
        break
    print(f"Has introducido: {n}")
