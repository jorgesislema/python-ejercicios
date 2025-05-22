"""
Ejercicio 1: Operaciones Matemáticas Avanzadas

Objetivo: Utilizar el módulo math y otras técnicas para realizar operaciones matemáticas avanzadas.

Instrucciones:
1. Implementa funciones para calcular operaciones matemáticas complejas.
2. Utiliza el módulo math para funciones trigonométricas, logarítmicas, etc.
3. Trabaja con constantes matemáticas como π y e.
4. Implementa algoritmos matemáticos básicos.
"""

import math
import random
import numpy as np
from decimal import Decimal, getcontext

def main():
    # Constantes matemáticas
    print("=== Constantes Matemáticas ===")
    print(f"Pi (π): {math.pi}")
    print(f"e (número de Euler): {math.e}")
    print(f"Tau (τ = 2π): {math.tau}")
    print(f"Infinito: {math.inf}")
    print(f"NaN (Not a Number): {math.nan}")
    
    # Funciones trigonométricas
    print("\n=== Funciones Trigonométricas ===")
    angulo_grados = 45
    angulo_radianes = math.radians(angulo_grados)
    print(f"Ángulo en grados: {angulo_grados}°")
    print(f"Ángulo en radianes: {angulo_radianes}")
    
    print(f"Seno: sin({angulo_grados}°) = {math.sin(angulo_radianes)}")
    print(f"Coseno: cos({angulo_grados}°) = {math.cos(angulo_radianes)}")
    print(f"Tangente: tan({angulo_grados}°) = {math.tan(angulo_radianes)}")
    
    # Funciones trigonométricas inversas
    valor = 0.5
    print(f"\nArcoseno: arcsin({valor}) = {math.degrees(math.asin(valor))}°")
    print(f"Arcocoseno: arccos({valor}) = {math.degrees(math.acos(valor))}°")
    print(f"Arcotangente: arctan({valor}) = {math.degrees(math.atan(valor))}°")
    
    # Funciones hiperbólicas
    print("\n=== Funciones Hiperbólicas ===")
    x = 1.0
    print(f"Seno hiperbólico: sinh({x}) = {math.sinh(x)}")
    print(f"Coseno hiperbólico: cosh({x}) = {math.cosh(x)}")
    print(f"Tangente hiperbólica: tanh({x}) = {math.tanh(x)}")
    
    # Logaritmos y exponenciales
    print("\n=== Logaritmos y Exponenciales ===")
    numero = 10
    print(f"Logaritmo natural: ln({numero}) = {math.log(numero)}")
    print(f"Logaritmo en base 10: log10({numero}) = {math.log10(numero)}")
    print(f"Logaritmo en base 2: log2({numero}) = {math.log2(numero)}")
    print(f"Logaritmo en base personalizada: log8({numero}) = {math.log(numero, 8)}")
    
    print(f"Exponencial: e^{x} = {math.exp(x)}")
    print(f"2^10 = {math.pow(2, 10)}")
    
    # Funciones de redondeo
    print("\n=== Funciones de Redondeo ===")
    valor_decimal = 3.7
    print(f"Valor original: {valor_decimal}")
    print(f"Redondeo (round): {round(valor_decimal)}")
    print(f"Techo (ceil): {math.ceil(valor_decimal)}")
    print(f"Suelo (floor): {math.floor(valor_decimal)}")
    print(f"Truncamiento (trunc): {math.trunc(valor_decimal)}")
    
    # Raíces y potencias
    print("\n=== Raíces y Potencias ===")
    numero = 16
    print(f"Raíz cuadrada de {numero}: {math.sqrt(numero)}")
    print(f"Raíz cúbica de {numero}: {numero ** (1/3)}")
    print(f"Raíz n-ésima (n=4) de {numero}: {numero ** (1/4)}")
    
    # Valor absoluto y signo
    print("\n=== Valor Absoluto y Signo ===")
    valor_negativo = -42
    print(f"Valor original: {valor_negativo}")
    print(f"Valor absoluto: {abs(valor_negativo)}")
    print(f"Signo (-1, 0, 1): {math.copysign(1, valor_negativo)}")
    
    # Precisión numérica con decimal
    print("\n=== Precisión Numérica con Decimal ===")
    getcontext().prec = 30  # Establecer precisión
    
    a = Decimal('1.1')
    b = Decimal('2.2')
    c = a + b
    
    print(f"Usando float: 1.1 + 2.2 = {1.1 + 2.2}")
    print(f"Usando Decimal: {a} + {b} = {c}")
    
    # Cálculo del factorial
    print("\n=== Cálculo del Factorial ===")
    for n in range(6):
        print(f"{n}! = {math.factorial(n)}")
    
    # Combinatoria: coeficientes binomiales
    print("\n=== Combinatoria ===")
    n, k = 10, 3
    comb = math.comb(n, k)
    print(f"Combinaciones de {n} elementos tomados de {k} en {k}: C({n},{k}) = {comb}")
    
    perm = math.perm(n, k)
    print(f"Permutaciones de {n} elementos tomados de {k} en {k}: P({n},{k}) = {perm}")
    
    # Algoritmo de Euclides para MCD y mcm
    print("\n=== Máximo Común Divisor y Mínimo Común Múltiplo ===")
    a, b = 48, 18
    
    mcd = math.gcd(a, b)
    mcm = (a * b) // mcd  # Fórmula: mcm(a,b) = (a*b)/mcd(a,b)
    
    print(f"MCD({a}, {b}) = {mcd}")
    print(f"MCM({a}, {b}) = {mcm}")
    
    # Estadísticas básicas
    print("\n=== Estadísticas Básicas ===")
    datos = [12, 8, 15, 17, 10, 9, 13, 11]
    print(f"Datos: {datos}")
    
    # Sin usar módulos estadísticos
    print(f"Media: {sum(datos) / len(datos)}")
    
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    if n % 2 == 0:
        mediana = (datos_ordenados[n//2-1] + datos_ordenados[n//2]) / 2
    else:
        mediana = datos_ordenados[n//2]
    
    print(f"Mediana: {mediana}")
    
    # Usando numpy para estadísticas más avanzadas
    print(f"Desviación estándar: {np.std(datos)}")
    print(f"Varianza: {np.var(datos)}")
    
    # Ejercicios para el usuario
    print("\n=== EJERCICIOS PARA PRACTICAR ===")
    print("1. Implementa una función que calcule el área y el volumen de una esfera dado su radio")
    print("2. Crea una función que resuelva ecuaciones cuadráticas (ax² + bx + c = 0)")
    print("3. Implementa el método de Newton-Raphson para encontrar raíces de funciones")
    print("4. Desarrolla una función que calcule la serie de Fibonacci hasta el término n-ésimo usando la fórmula cerrada")

if __name__ == "__main__":
    main()
