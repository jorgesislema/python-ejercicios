"""
Ejercicio 10: Recursividad avanzada

Objetivo: Practicar recursividad con problemas complejos.

Instrucciones:
- Escribe una función recursiva para calcular el n-ésimo número de la sucesión de Fibonacci de forma eficiente (usa memoización).
"""

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

print([fibonacci(i) for i in range(10)])
