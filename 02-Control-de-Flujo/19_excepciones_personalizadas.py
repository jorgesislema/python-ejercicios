"""
Ejercicio 19: Excepciones personalizadas

Objetivo: Crear y usar excepciones definidas por el usuario.

Instrucciones:
- Escribe un programa que defina una excepción personalizada para edades negativas y la utilice al pedir la edad.
"""

class EdadNegativaError(Exception):
    pass

try:
    edad = int(input("Introduce tu edad: "))
    if edad < 0:
        raise EdadNegativaError("La edad no puede ser negativa.")
    print(f"Tu edad es: {edad}")
except EdadNegativaError as e:
    print(f"Error: {e}")
