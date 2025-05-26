"""
Ejercicio 17: Decoradores múltiples

Objetivo: Comprender cómo aplicar varios decoradores a una función.

Instrucciones:
- Escribe dos decoradores diferentes y aplícalos a una misma función.
"""

def decorador1(func):
    def wrapper(*args, **kwargs):
        print("[Decorador 1] Antes")
        resultado = func(*args, **kwargs)
        print("[Decorador 1] Después")
        return resultado
    return wrapper

def decorador2(func):
    def wrapper(*args, **kwargs):
        print("[Decorador 2] Antes")
        resultado = func(*args, **kwargs)
        print("[Decorador 2] Después")
        return resultado
    return wrapper

@decorador1
@decorador2
def saludar():
    print("¡Hola!")

saludar()
