"""
Ejercicio 11: Generadores avanzados

Objetivo: Crear generadores personalizados para flujos de datos complejos.

Instrucciones:
- Escribe un generador que produzca los números primos de forma infinita.
- Usa next() para mostrar los primeros 10 primos.
"""

def generador_primos():
    n = 2
    while True:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                break
        else:
            yield n
        n += 1

primos = generador_primos()
for _ in range(10):
    print(next(primos))
