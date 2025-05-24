"""
Ejercicio 3: if-elif-else

Objetivo: Comprender el uso de múltiples condiciones.

Instrucciones:
- Escribe un programa que pida una nota (0-10) y muestre si es insuficiente, suficiente, bien, notable o sobresaliente.
"""

nota = float(input("Introduce tu nota (0-10): "))

if nota < 5:
    print("Insuficiente")
elif nota < 6:
    print("Suficiente")
elif nota < 7:
    print("Bien")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")
