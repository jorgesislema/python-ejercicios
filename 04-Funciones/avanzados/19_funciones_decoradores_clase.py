"""
Ejercicio 19: Decoradores de clase

Objetivo: Aplicar decoradores a métodos de clase y comprender su funcionamiento.

Instrucciones:
- Escribe un decorador que registre el nombre del método cada vez que se llama a un método de una clase.
"""

def registrar_llamada(func):
    def wrapper(*args, **kwargs):
        print(f"Llamando a: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class Calculadora:
    @registrar_llamada
    def sumar(self, a, b):
        return a + b

calc = Calculadora()
print(calc.sumar(2, 3))
