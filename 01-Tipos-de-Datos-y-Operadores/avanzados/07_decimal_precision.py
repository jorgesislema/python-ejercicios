"""
Ejercicio 7: Precisión Decimal y Números Grandes

Objetivo: Aprender a trabajar con números de alta precisión y números extremadamente grandes.

Instrucciones:
1. Utilizar el módulo decimal para operaciones de punto flotante con precisión controlada.
2. Trabajar con números grandes utilizando el tipo de dato int y el módulo math.
3. Explorar el módulo fractions para manejar fracciones exactas.
4. Implementar ejemplos que demuestren las limitaciones de los tipos de datos numéricos estándar.
"""

import decimal
from decimal import Decimal
import math
import fractions
from fractions import Fraction
import sys

def main():
    # Limitaciones de los flotantes de punto fijo
    print("=== Limitaciones de los Flotantes de Punto Fijo ===")
    
    # Problema clásico de precisión flotante
    resultado_flotante = 0.1 + 0.2
    print(f"0.1 + 0.2 = {resultado_flotante}")
    print(f"¿0.1 + 0.2 == 0.3? {resultado_flotante == 0.3}")
    
    # Error de redondeo acumulativo
    suma = 0.0
    for _ in range(10):
        suma += 0.1
    print(f"Suma de 0.1 diez veces: {suma}")
    print(f"¿La suma es exactamente 1.0? {suma == 1.0}")
    
    # Módulo decimal para precisión controlada
    print("\n=== Módulo decimal para Precisión Controlada ===")
    
    # Configurar la precisión global
    decimal.getcontext().prec = 28
    print(f"Precisión decimal configurada a: {decimal.getcontext().prec} dígitos")
    
    # Resolver el problema de 0.1 + 0.2 con Decimal
    a = Decimal('0.1')
    b = Decimal('0.2')
    resultado_decimal = a + b
    
    print(f"Usando Decimal: 0.1 + 0.2 = {resultado_decimal}")
    print(f"¿Usando Decimal: 0.1 + 0.2 == 0.3? {resultado_decimal == Decimal('0.3')}")
    
    # Suma acumulativa con Decimal
    suma_decimal = Decimal('0')
    for _ in range(10):
        suma_decimal += Decimal('0.1')
    
    print(f"Suma de Decimal('0.1') diez veces: {suma_decimal}")
    print(f"¿La suma es exactamente 1.0? {suma_decimal == Decimal('1.0')}")
    
    # Operaciones con diferente precisión
    print("\n=== Operaciones con Diferente Precisión ===")
    
    # Cambiar temporalmente la precisión
    with decimal.localcontext() as ctx:
        ctx.prec = 50  # Aumentar la precisión a 50 dígitos
        
        resultado = Decimal('1') / Decimal('7')
        print(f"1/7 con 50 dígitos de precisión: {resultado}")
    
    # La precisión vuelve a la configuración global
    resultado = Decimal('1') / Decimal('7')
    print(f"1/7 con la precisión global: {resultado}")
    
    # Redondeo controlado
    print("\n=== Redondeo Controlado ===")
    
    # Diferentes modos de redondeo
    modos = [
        decimal.ROUND_DOWN,
        decimal.ROUND_UP,
        decimal.ROUND_HALF_UP,
        decimal.ROUND_HALF_DOWN,
        decimal.ROUND_CEILING,
        decimal.ROUND_FLOOR,
        decimal.ROUND_05UP
    ]
    
    valor = Decimal('1.125')
    print(f"Valor a redondear: {valor}")
    
    for modo in modos:
        with decimal.localcontext() as ctx:
            ctx.rounding = modo
            resultado = valor.quantize(Decimal('0.1'))
            print(f"Modo {modo}: {resultado}")
    
    # Comparación entre float y Decimal en cálculos financieros
    print("\n=== Comparación en Cálculos Financieros ===")
    
    def calcular_interes_float(principal, tasa, periodos):
        """Calcula el interés compuesto usando float."""
        return principal * (1 + tasa) ** periodos
    
    def calcular_interes_decimal(principal, tasa, periodos):
        """Calcula el interés compuesto usando Decimal."""
        return Decimal(str(principal)) * (Decimal('1') + Decimal(str(tasa))) ** Decimal(str(periodos))
    
    principal = 1000.00
    tasa = 0.05
    periodos = 10
    
    resultado_float = calcular_interes_float(principal, tasa, periodos)
    resultado_decimal = calcular_interes_decimal(principal, tasa, periodos)
    
    print(f"Principal: ${principal}, Tasa: {tasa*100}%, Periodos: {periodos}")
    print(f"Resultado con float: ${resultado_float:.2f}")
    print(f"Resultado con Decimal: ${resultado_decimal:.2f}")
    print(f"Diferencia: ${abs(resultado_float - float(resultado_decimal)):.10f}")
    
    # Trabajando con fracciones exactas
    print("\n=== Trabajando con Fracciones Exactas ===")
    
    # Crear fracciones
    f1 = Fraction(1, 3)
    f2 = Fraction(2, 5)
    
    print(f"f1 = {f1}")
    print(f"f2 = {f2}")
    
    # Operaciones aritméticas
    print(f"f1 + f2 = {f1 + f2}")
    print(f"f1 - f2 = {f1 - f2}")
    print(f"f1 * f2 = {f1 * f2}")
    print(f"f1 / f2 = {f1 / f2}")
    
    # Convertir un float a fracción
    f3 = Fraction(0.5)  # Exacto porque 0.5 es representable exactamente en binario
    f4 = Fraction(0.1)  # Aproximación porque 0.1 no es representable exactamente en binario
    
    print(f"Fraction(0.5) = {f3}")
    print(f"Fraction(0.1) = {f4}")
    
    # Convertir un string a fracción
    f5 = Fraction('0.1')  # Exacto porque se interpreta como Decimal
    print(f"Fraction('0.1') = {f5}")
    
    # Simplificación automática
    f6 = Fraction(6, 8)
    print(f"Fraction(6, 8) = {f6}  # Simplificado automáticamente")
    
    # Límites de los valores numéricos en Python
    print("\n=== Límites de los Valores Numéricos en Python ===")
    
    # Tamaño máximo de un int
    print("Python tiene enteros de precisión arbitraria (limitados sólo por la memoria disponible)")
    
    # Ejemplo de número grande
    num_grande = 2 ** 100
    print(f"2^100 = {num_grande}")
    
    # Número factorial grande
    factorial_30 = math.factorial(30)
    print(f"30! = {factorial_30}")
    
    # Límites de float
    print(f"Máximo float positivo: {sys.float_info.max}")
    print(f"Mínimo float positivo: {sys.float_info.min}")
    print(f"Epsilon de la máquina: {sys.float_info.epsilon}")
    
    # Valores especiales de punto flotante
    print("\n=== Valores Especiales de Punto Flotante ===")
    
    # Infinito
    infinito_positivo = float('inf')
    infinito_negativo = float('-inf')
    
    print(f"Infinito positivo: {infinito_positivo}")
    print(f"Infinito negativo: {infinito_negativo}")
    print(f"¿Es infinito? {math.isinf(infinito_positivo)}")
    
    # NaN (Not a Number)
    nan = float('nan')
    print(f"NaN: {nan}")
    print(f"¿Es NaN? {math.isnan(nan)}")
    
    # Operaciones que producen NaN
    print(f"0.0 / 0.0 = {0.0 / 0.0 if hasattr(float, 'nan') else 'Error (división por cero)'}")
    
    # Operaciones con infinito
    print(f"1.0 / 0.0 = {1.0 / 0.0 if hasattr(float, 'inf') else 'Error (división por cero)'}")
    print(f"1.0 + infinito = {1.0 + infinito_positivo}")
    print(f"infinito - infinito = {infinito_positivo - infinito_positivo}")
    
    # Ejemplos prácticos
    print("\n=== Ejemplos Prácticos ===")
    
    # Cálculo del número e con alta precisión
    def calcular_e(precision):
        """Calcula el número e con la precisión especificada."""
        with decimal.localcontext() as ctx:
            ctx.prec = precision
            
            e = Decimal(1)
            factorial = Decimal(1)
            
            for i in range(1, precision):
                factorial *= i
                e += Decimal(1) / factorial
                
            return e
    
    e_30 = calcular_e(30)
    print(f"e con 30 dígitos de precisión: {e_30}")
    
    # Cálculo de Pi con la fórmula de Leibniz
    def calcular_pi(iteraciones):
        """Aproxima Pi usando la serie de Leibniz: π/4 = 1 - 1/3 + 1/5 - 1/7 + ..."""
        with decimal.localcontext() as ctx:
            ctx.prec = 50  # Alta precisión para el cálculo
            
            pi = Decimal(0)
            signo = Decimal(1)
            
            for i in range(iteraciones):
                denominador = Decimal(2 * i + 1)
                pi += signo / denominador
                signo = -signo
                
            return pi * 4
    
    pi_1000 = calcular_pi(1000)
    print(f"π aproximado con 1000 iteraciones: {pi_1000}")
    print(f"Error respecto a math.pi: {abs(float(pi_1000) - math.pi)}")
    
    # Cálculo de raíz cuadrada con alta precisión
    def raiz_cuadrada(n, precision):
        """Calcula la raíz cuadrada de n con la precisión especificada."""
        with decimal.localcontext() as ctx:
            ctx.prec = precision
            
            n_decimal = Decimal(n)
            aproximacion = n_decimal / 2  # Valor inicial
            
            # Método de Newton-Raphson
            for _ in range(100):  # Máximo 100 iteraciones
                nueva_aproximacion = (aproximacion + n_decimal / aproximacion) / 2
                
                if abs(nueva_aproximacion - aproximacion) < Decimal('1e-' + str(precision)):
                    break
                    
                aproximacion = nueva_aproximacion
                
            return aproximacion
    
    raiz_2 = raiz_cuadrada('2', 30)
    print(f"√2 con 30 dígitos de precisión: {raiz_2}")
    
    # Ejercicios para el usuario
    print("\n=== EJERCICIOS PARA PRACTICAR ===")
    print("1. Implementa una función que calcule el factorial de un número grande (por ejemplo, 100!) usando el módulo decimal")
    print("2. Crea una calculadora que realice operaciones aritméticas básicas con fracciones exactas")
    print("3. Desarrolla un programa que calcule π con mayor precisión usando el algoritmo de Chudnovsky")
    print("4. Implementa una función para convertir entre diferentes unidades de medida con precisión decimal garantizada")

if __name__ == "__main__":
    main()
