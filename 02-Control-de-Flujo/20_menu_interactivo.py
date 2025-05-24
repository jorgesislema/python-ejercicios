"""
Ejercicio 20: Menú interactivo

Objetivo: Integrar estructuras de control en un menú.

Instrucciones:
- Escribe un programa que muestre un menú con varias opciones y permita al usuario elegir hasta que decida salir.
"""

while True:
    print("\nMenú principal:")
    print("1. Saludar")
    print("2. Sumar dos números")
    print("3. Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        print("¡Hola!")
    elif opcion == "2":
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        print(f"La suma es: {a + b}")
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida.")
