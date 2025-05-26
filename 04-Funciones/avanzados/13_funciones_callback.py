"""
Ejercicio 13: Funciones callback

Objetivo: Comprender el uso de funciones callback en Python.

Instrucciones:
- Escribe una función que reciba otra función como callback y la ejecute después de realizar una tarea.
"""

def tarea_con_callback(tarea, callback):
    print("Ejecutando tarea...")
    tarea()
    print("Ejecutando callback...")
    callback()

# Ejemplo de uso
def principal():
    print("Tarea principal realizada.")
def final():
    print("Callback ejecutado.")

tarea_con_callback(principal, final)
