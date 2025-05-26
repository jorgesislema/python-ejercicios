"""
Ejercicio 8: Funciones que retornan funciones

Objetivo: Comprender cómo una función puede devolver otra función.

Instrucciones:
- Escribe una función que reciba un mensaje y devuelva una función que imprima ese mensaje.
- Prueba el resultado llamando a la función devuelta.
"""

def crear_saludador(mensaje):
    def saludar():
        print(mensaje)
    return saludar

saludo = crear_saludador("¡Hola, mundo!")
saludo()
