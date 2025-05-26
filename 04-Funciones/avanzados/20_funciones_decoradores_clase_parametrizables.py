"""
Ejercicio 20: Decoradores de clase parametrizables

Objetivo: Crear decoradores de clase que acepten parámetros.

Instrucciones:
- Escribe un decorador de clase que reciba un mensaje y lo imprima cada vez que se llame a un método decorado.
"""

def decorador_mensaje_clase(mensaje):
    def decorador(func):
        def wrapper(*args, **kwargs):
            print(f"[{mensaje}] Llamando a: {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorador

class Operaciones:
    @decorador_mensaje_clase("Suma ejecutada")
    def sumar(self, a, b):
        return a + b

op = Operaciones()
print(op.sumar(5, 7))
