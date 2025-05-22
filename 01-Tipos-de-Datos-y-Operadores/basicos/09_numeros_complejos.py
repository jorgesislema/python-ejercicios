"""
Ejercicio 9: Números Complejos

Objetivo: Aprender a trabajar con números complejos en Python.

Instrucciones:
1. Crear y manipular números complejos.
2. Realizar operaciones aritméticas con números complejos.
3. Extraer la parte real e imaginaria de un número complejo.
4. Calcular el módulo y argumento de un número complejo.
"""

def main():
    # Creación de números complejos
    print("=== Creación de Números Complejos ===")
    
    # Usando la notación literal con j
    z1 = 3 + 4j
    print(f"z1 = 3 + 4j: {z1}")
    
    # Usando la función complex()
    z2 = complex(2, 5)
    print(f"z2 = complex(2, 5): {z2}")
    
    # A partir de variables
    real = 1
    imag = 2
    z3 = complex(real, imag)
    print(f"z3 = complex({real}, {imag}): {z3}")
    
    # Operaciones aritméticas básicas
    print("\n=== Operaciones Aritméticas Básicas ===")
    
    # Suma
    suma = z1 + z2
    print(f"z1 + z2 = {z1} + {z2} = {suma}")
    
    # Resta
    resta = z1 - z2
    print(f"z1 - z2 = {z1} - {z2} = {resta}")
    
    # Multiplicación
    multiplicacion = z1 * z2
    print(f"z1 * z2 = {z1} * {z2} = {multiplicacion}")
    
    # División
    division = z1 / z2
    print(f"z1 / z2 = {z1} / {z2} = {division}")
    
    # Potencia
    potencia = z1 ** 2
    print(f"z1 ** 2 = {z1} ** 2 = {potencia}")
    
    # Acceso a partes de un número complejo
    print("\n=== Acceso a Partes de un Número Complejo ===")
    
    # Parte real
    real_z1 = z1.real
    print(f"Parte real de z1 = {real_z1}")
    
    # Parte imaginaria
    imag_z1 = z1.imag
    print(f"Parte imaginaria de z1 = {imag_z1}")
    
    # Conjugado
    conj_z1 = z1.conjugate()
    print(f"Conjugado de z1 = {conj_z1}")
    
    # Cálculos comunes con números complejos
    print("\n=== Cálculos Comunes con Números Complejos ===")
    
    # Módulo o magnitud (distancia al origen)
    import math
    modulo_z1 = abs(z1)
    print(f"Módulo de z1 = |{z1}| = {modulo_z1}")
    
    # Argumento o fase (ángulo en radianes)
    import cmath
    arg_z1 = cmath.phase(z1)
    print(f"Argumento de z1 en radianes = {arg_z1}")
    print(f"Argumento de z1 en grados = {math.degrees(arg_z1):.2f}°")
    
    # Forma polar (r, θ)
    r = abs(z1)
    theta = cmath.phase(z1)
    print(f"z1 en forma polar: ({r:.2f}, {theta:.2f} rad)")
    
    # Conversión de forma polar a rectangular
    z_polar = cmath.rect(r, theta)
    print(f"Conversión de polar a rectangular: cmath.rect({r:.2f}, {theta:.2f}) = {z_polar}")
    
    # Funciones matemáticas con números complejos
    print("\n=== Funciones Matemáticas con Números Complejos ===")
    
    # Raíz cuadrada
    raiz_z1 = cmath.sqrt(z1)
    print(f"Raíz cuadrada de z1 = √{z1} = {raiz_z1}")
    
    # Exponencial
    exp_z1 = cmath.exp(z1)
    print(f"Exponencial de z1 = e^{z1} = {exp_z1}")
    
    # Logaritmo natural
    log_z1 = cmath.log(z1)
    print(f"Logaritmo natural de z1 = ln({z1}) = {log_z1}")
    
    # Funciones trigonométricas
    sin_z1 = cmath.sin(z1)
    cos_z1 = cmath.cos(z1)
    print(f"Seno de z1 = sin({z1}) = {sin_z1}")
    print(f"Coseno de z1 = cos({z1}) = {cos_z1}")
    
    # Aplicaciones de números complejos
    print("\n=== Aplicaciones de Números Complejos ===")
    
    # Ejemplo: Resolución de ecuación cuadrática con raíces complejas
    # x² + x + 1 = 0
    a, b, c = 1, 1, 1
    
    # Fórmula cuadrática
    discriminante = b**2 - 4*a*c
    x1 = (-b + cmath.sqrt(discriminante)) / (2*a)
    x2 = (-b - cmath.sqrt(discriminante)) / (2*a)
    
    print(f"Soluciones de x² + x + 1 = 0:")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
    
    # Verificación
    print(f"Verificación x1: {a}*({x1})² + {b}*({x1}) + {c} = {a*x1**2 + b*x1 + c}")
    print(f"Verificación x2: {a}*({x2})² + {b}*({x2}) + {c} = {a*x2**2 + b*x2 + c}")
    
    # Ejercicios para el usuario
    print("\n=== EJERCICIOS PARA PRACTICAR ===")
    print("1. Calcula la suma, resta, multiplicación y división de (2-3j) y (1+j)")
    print("2. Convierte el número complejo 1+j a su forma polar y luego de vuelta a su forma rectangular")
    print("3. Resuelve la ecuación cuadrática x² - 4x + 13 = 0 usando números complejos")
    print("4. Calcula e^(πj) usando cmath.exp() y compara el resultado con -1 (Fórmula de Euler)")

if __name__ == "__main__":
    main()
