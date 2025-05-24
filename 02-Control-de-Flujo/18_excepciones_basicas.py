"""
Ejercicio 18: Manejo básico de excepciones

Objetivo: Introducir el manejo de errores con try-except.

Instrucciones:
- Escribe un programa que pida dos números y muestre el resultado de la división, controlando la división por cero.
"""

try:
    a = float(input("Introduce el numerador: "))
    b = float(input("Introduce el denominador: "))
    resultado = a / b
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
