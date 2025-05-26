"""
Ejercicio 12: Decoradores parametrizables

Objetivo: Crear decoradores que acepten argumentos.

Instrucciones:
- Escribe un decorador que reciba un mensaje y lo imprima antes y después de ejecutar la función decorada.
"""

def decorador_mensaje(mensaje):
    def decorador(func):
        def wrapper(*args, **kwargs):
            print(f"[Antes] {mensaje}")
            resultado = func(*args, **kwargs)
            print(f"[Después] {mensaje}")
            return resultado
        return wrapper
    return decorador

@decorador_mensaje("Ejecución de la función")
def saludar():
    print("¡Hola!")

saludar()
