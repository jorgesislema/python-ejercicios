"""
Ejercicio 18: Generadores con estado interno

Objetivo: Crear generadores que mantengan un estado complejo entre iteraciones.

Instrucciones:
- Escribe un generador que produzca los números de la sucesión de Fibonacci y recuerde cuántos ha generado.
"""

def generador_fibonacci():
    a, b = 0, 1
    contador = 0
    while True:
        yield a, contador
        a, b = b, a + b
        contador += 1

fib = generador_fibonacci()
for _ in range(7):
    valor, pos = next(fib)
    print(f"Fibonacci[{pos}] = {valor}")
