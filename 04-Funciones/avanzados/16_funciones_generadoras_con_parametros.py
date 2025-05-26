"""
Ejercicio 16: Generadores con parámetros

Objetivo: Crear generadores que acepten parámetros para modificar su comportamiento.

Instrucciones:
- Escribe un generador que reciba un número inicial y un paso, y produzca una secuencia infinita.
"""

def generador_secuencia(inicio=0, paso=1):
    actual = inicio
    while True:
        yield actual
        actual += paso

# Ejemplo de uso
sec = generador_secuencia(10, 5)
for _ in range(5):
    print(next(sec))
