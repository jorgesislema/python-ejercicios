"""
Ejercicio 1: Números y Operaciones Básicas

Objetivo: Practicar operaciones aritméticas básicas con números.

Instrucciones:
1. Crea variables para almacenar diferentes tipos de números (enteros y flotantes).
2. Realiza operaciones de suma, resta, multiplicación, división, división entera, 
   módulo y potencia.
3. Imprime los resultados con mensajes descriptivos.
"""

def main():
    # Declaración de variables
    num_entero1 = 10
    num_entero2 = 3
    num_flotante1 = 5.5
    num_flotante2 = 2.25
    
    # Operaciones con enteros
    print("=== Operaciones con números enteros ===")
    print(f"Números: {num_entero1} y {num_entero2}")
    print(f"Suma: {num_entero1} + {num_entero2} = {num_entero1 + num_entero2}")
    print(f"Resta: {num_entero1} - {num_entero2} = {num_entero1 - num_entero2}")
    print(f"Multiplicación: {num_entero1} * {num_entero2} = {num_entero1 * num_entero2}")
    print(f"División: {num_entero1} / {num_entero2} = {num_entero1 / num_entero2}")
    print(f"División entera: {num_entero1} // {num_entero2} = {num_entero1 // num_entero2}")
    print(f"Módulo: {num_entero1} % {num_entero2} = {num_entero1 % num_entero2}")
    print(f"Potencia: {num_entero1} ** {num_entero2} = {num_entero1 ** num_entero2}")
    
    # Operaciones con flotantes
    print("\n=== Operaciones con números flotantes ===")
    print(f"Números: {num_flotante1} y {num_flotante2}")
    print(f"Suma: {num_flotante1} + {num_flotante2} = {num_flotante1 + num_flotante2}")
    print(f"Resta: {num_flotante1} - {num_flotante2} = {num_flotante1 - num_flotante2}")
    print(f"Multiplicación: {num_flotante1} * {num_flotante2} = {num_flotante1 * num_flotante2}")
    print(f"División: {num_flotante1} / {num_flotante2} = {num_flotante1 / num_flotante2}")
    print(f"División entera: {num_flotante1} // {num_flotante2} = {num_flotante1 // num_flotante2}")
    print(f"Módulo: {num_flotante1} % {num_flotante2} = {num_flotante1 % num_flotante2}")
    print(f"Potencia: {num_flotante1} ** {num_flotante2} = {num_flotante1 ** num_flotante2}")
    
    # Operaciones mixtas
    print("\n=== Operaciones mixtas ===")
    print(f"Entero + Flotante: {num_entero1} + {num_flotante1} = {num_entero1 + num_flotante1}")
    print(f"Flotante / Entero: {num_flotante1} / {num_entero2} = {num_flotante1 / num_entero2}")
    
    # Ejercicios para el usuario
    print("\n=== EJERCICIOS PARA PRACTICAR ===")
    print("1. Calcula el área de un círculo con radio 7 (usa 3.14159 como valor de PI)")
    print("2. Convierte una temperatura de 98.6 grados Fahrenheit a Celsius (Fórmula: (F - 32) * 5/9)")
    print("3. Calcula cuántos segundos hay en 2 días, 5 horas, 30 minutos y 15 segundos")

if __name__ == "__main__":
    main()
