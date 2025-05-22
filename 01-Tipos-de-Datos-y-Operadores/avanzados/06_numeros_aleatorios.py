"""
Ejercicio 6: Números Aleatorios y Probabilidad

Objetivo: Aprender a generar y trabajar con números aleatorios y distribuciones de probabilidad.

Instrucciones:
1. Utilizar los módulos random y numpy.random para generar números aleatorios.
2. Implementar ejemplos con diferentes distribuciones de probabilidad.
3. Aplicar números aleatorios en simulaciones y muestreos.
4. Entender la importancia de establecer semillas para reproducibilidad.
"""

import random
import time
import statistics
import math
try:
    import numpy as np
    import matplotlib.pyplot as plt
    numpy_available = True
except ImportError:
    print("Nota: Los módulos numpy y/o matplotlib no están instalados.")
    print("Algunas funcionalidades avanzadas no estarán disponibles.")
    numpy_available = False

def main():
    # Introducción a números aleatorios
    print("=== Introducción a Números Aleatorios ===")
    print("Los números aleatorios son fundamentales en simulaciones,")
    print("criptografía, juegos, muestreos y muchos otros campos.")
    
    # Generación básica con el módulo random
    print("\n=== Generación Básica con el Módulo random ===")
    
    # Establecer una semilla para reproducibilidad
    random.seed(42)
    print("Semilla establecida a 42 para reproducibilidad")
    
    # Números aleatorios entre 0 y 1
    for i in range(5):
        print(f"Número aleatorio {i+1}: {random.random()}")
    
    # Restablecer la semilla al tiempo actual para variabilidad
    random.seed(int(time.time()))
    print("\nSemilla restablecida al tiempo actual")
    
    # Enteros aleatorios en un rango
    print("\n=== Enteros Aleatorios en un Rango ===")
    
    # Entre 1 y 100
    for i in range(5):
        print(f"Entero aleatorio entre 1 y 100: {random.randint(1, 100)}")
    
    # Selección aleatoria de elementos
    print("\n=== Selección Aleatoria de Elementos ===")
    
    colores = ["rojo", "verde", "azul", "amarillo", "negro", "blanco"]
    
    # Seleccionar un elemento aleatorio
    print(f"Color aleatorio: {random.choice(colores)}")
    
    # Seleccionar múltiples elementos sin repetición
    muestra = random.sample(colores, 3)
    print(f"Muestra de 3 colores sin repetición: {muestra}")
    
    # Seleccionar múltiples elementos con posible repetición
    muestra_con_repeticion = [random.choice(colores) for _ in range(3)]
    print(f"Muestra de 3 colores con posible repetición: {muestra_con_repeticion}")
    
    # Barajar una lista
    baraja = colores.copy()
    random.shuffle(baraja)
    print(f"Lista barajada: {baraja}")
    
    # Distribuciones de probabilidad con el módulo random
    print("\n=== Distribuciones de Probabilidad con el Módulo random ===")
    
    # Distribución uniforme (entre 0 y 1)
    print("\nDistribución Uniforme (entre 0 y 1):")
    uniforme = [random.random() for _ in range(1000)]
    print(f"Media: {statistics.mean(uniforme):.4f}")
    print(f"Desviación estándar: {statistics.stdev(uniforme):.4f}")
    
    # Distribución uniforme (en un rango)
    print("\nDistribución Uniforme (entre -10 y 10):")
    uniforme_rango = [random.uniform(-10, 10) for _ in range(1000)]
    print(f"Media: {statistics.mean(uniforme_rango):.4f}")
    print(f"Desviación estándar: {statistics.stdev(uniforme_rango):.4f}")
    
    # Distribución triangular
    print("\nDistribución Triangular (entre 0 y 10, con pico en 5):")
    triangular = [random.triangular(0, 10, 5) for _ in range(1000)]
    print(f"Media: {statistics.mean(triangular):.4f}")
    print(f"Desviación estándar: {statistics.stdev(triangular):.4f}")
    
    # Generación de números aleatorios con diferentes distribuciones usando NumPy
    if numpy_available:
        print("\n=== Distribuciones de Probabilidad con NumPy ===")
        
        # Establecer semilla para reproducibilidad
        np.random.seed(42)
        
        # Distribución normal (gaussiana)
        print("\nDistribución Normal (media=0, desviación=1):")
        normal = np.random.normal(0, 1, 1000)
        print(f"Media: {np.mean(normal):.4f}")
        print(f"Desviación estándar: {np.std(normal):.4f}")
        
        # Distribución exponencial
        print("\nDistribución Exponencial (lambda=1):")
        exponencial = np.random.exponential(1, 1000)
        print(f"Media: {np.mean(exponencial):.4f}")
        print(f"Desviación estándar: {np.std(exponencial):.4f}")
        
        # Distribución de Poisson
        print("\nDistribución de Poisson (lambda=5):")
        poisson = np.random.poisson(5, 1000)
        print(f"Media: {np.mean(poisson):.4f}")
        print(f"Desviación estándar: {np.std(poisson):.4f}")
        
        # Distribución binomial
        print("\nDistribución Binomial (n=10, p=0.5):")
        binomial = np.random.binomial(10, 0.5, 1000)
        print(f"Media: {np.mean(binomial):.4f}")
        print(f"Desviación estándar: {np.std(binomial):.4f}")
        
        # Visualización de distribuciones (comentado, ya que requiere matplotlib)
        """
        plt.figure(figsize=(12, 8))
        
        plt.subplot(2, 2, 1)
        plt.hist(normal, bins=30, alpha=0.7)
        plt.title('Distribución Normal')
        
        plt.subplot(2, 2, 2)
        plt.hist(exponencial, bins=30, alpha=0.7)
        plt.title('Distribución Exponencial')
        
        plt.subplot(2, 2, 3)
        plt.hist(poisson, bins=30, alpha=0.7)
        plt.title('Distribución de Poisson')
        
        plt.subplot(2, 2, 4)
        plt.hist(binomial, bins=30, alpha=0.7)
        plt.title('Distribución Binomial')
        
        plt.tight_layout()
        plt.show()
        """
    
    # Aplicaciones prácticas
    print("\n=== Aplicaciones Prácticas ===")
    
    # Simulación de lanzamiento de moneda
    print("\n1. Simulación de Lanzamiento de Moneda")
    
    def lanzar_moneda(n):
        """Simula n lanzamientos de moneda y devuelve la proporción de caras."""
        lanzamientos = [random.choice(["cara", "cruz"]) for _ in range(n)]
        caras = lanzamientos.count("cara")
        return caras / n
    
    # Simulaciones con diferente número de lanzamientos
    for n in [10, 100, 1000, 10000]:
        proporcion = lanzar_moneda(n)
        print(f"{n} lanzamientos: Proporción de caras = {proporcion:.4f}")
    
    # Simulación de lanzamiento de dados
    print("\n2. Simulación de Lanzamiento de Dados")
    
    def lanzar_dados(n, caras=6):
        """Simula n lanzamientos de un dado de 'caras' caras."""
        return [random.randint(1, caras) for _ in range(n)]
    
    # Lanzar un dado de 6 caras 1000 veces
    lanzamientos = lanzar_dados(1000)
    
    # Calcular frecuencias
    frecuencias = {i: lanzamientos.count(i) for i in range(1, 7)}
    for cara, freq in frecuencias.items():
        print(f"Cara {cara}: {freq} veces ({freq/1000:.4f})")
    
    # Generación de contraseñas aleatorias
    print("\n3. Generación de Contraseñas Aleatorias")
    
    def generar_password(longitud=12, incluir_mayusculas=True, incluir_numeros=True, incluir_simbolos=True):
        """Genera una contraseña aleatoria."""
        caracteres = "abcdefghijklmnopqrstuvwxyz"
        
        if incluir_mayusculas:
            caracteres += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if incluir_numeros:
            caracteres += "0123456789"
        if incluir_simbolos:
            caracteres += "!@#$%^&*()-_=+[]{}|;:,.<>?/"
        
        return ''.join(random.choice(caracteres) for _ in range(longitud))
    
    # Generar contraseñas con diferentes configuraciones
    print(f"Contraseña básica (sólo minúsculas): {generar_password(incluir_mayusculas=False, incluir_numeros=False, incluir_simbolos=False)}")
    print(f"Contraseña con letras y números: {generar_password(incluir_simbolos=False)}")
    print(f"Contraseña completa: {generar_password()}")
    
    # Simulación de Monte Carlo para aproximar Pi
    print("\n4. Aproximación de Pi mediante Simulación de Monte Carlo")
    
    def aproximar_pi(n):
        """Aproxima el valor de Pi usando el método de Monte Carlo."""
        dentro_circulo = 0
        
        for _ in range(n):
            # Generar punto aleatorio en el cuadrado unitario
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            
            # Verificar si el punto está dentro del círculo unitario
            if x**2 + y**2 <= 1:
                dentro_circulo += 1
        
        # La proporción de puntos dentro del círculo aproxima π/4
        return (dentro_circulo / n) * 4
    
    # Aproximaciones con diferente número de puntos
    for n in [1000, 10000, 100000]:
        pi_aprox = aproximar_pi(n)
        error = abs(pi_aprox - math.pi)
        print(f"{n} puntos: π ≈ {pi_aprox:.6f} (error: {error:.6f})")
    
    # Ejercicios para el usuario
    print("\n=== EJERCICIOS PARA PRACTICAR ===")
    print("1. Implementa una función que simule el lanzamiento de n dados y calcule la probabilidad de obtener cada suma posible")
    print("2. Desarrolla un generador de números de lotería que evite patrones obvios (como números consecutivos)")
    print("3. Crea un simulador del problema de Monty Hall y analiza los resultados para diferentes estrategias")
    print("4. Implementa el algoritmo de Fisher-Yates para barajar una lista de forma más eficiente que random.shuffle()")

if __name__ == "__main__":
    main()
