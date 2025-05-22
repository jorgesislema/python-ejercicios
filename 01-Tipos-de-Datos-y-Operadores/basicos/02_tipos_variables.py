"""
Ejercicio 2: Tipos de Variables y Conversión

Objetivo: Aprender a trabajar con diferentes tipos de datos y realizar conversiones entre ellos.

Instrucciones:
1. Crea variables de diferentes tipos (int, float, str, bool).
2. Imprime el tipo de cada variable.
3. Realiza conversiones entre diferentes tipos de datos.
4. Muestra ejemplos de operaciones con conversión automática y explícita.
"""

def main():
    # Declaración de variables de diferentes tipos
    entero = 42
    flotante = 3.14159
    texto = "Python"
    booleano = True
    
    # Imprimiendo el tipo de cada variable
    print("=== Tipos de Variables ===")
    print(f"Variable: {entero}, Tipo: {type(entero)}")
    print(f"Variable: {flotante}, Tipo: {type(flotante)}")
    print(f"Variable: {texto}, Tipo: {type(texto)}")
    print(f"Variable: {booleano}, Tipo: {type(booleano)}")
    
    # Conversiones explícitas entre tipos
    print("\n=== Conversiones Explícitas ===")
    
    # De entero a otros tipos
    print(f"Entero a flotante: {entero} -> {float(entero)}, Tipo: {type(float(entero))}")
    print(f"Entero a texto: {entero} -> {str(entero)}, Tipo: {type(str(entero))}")
    print(f"Entero a booleano: {entero} -> {bool(entero)}, Tipo: {type(bool(entero))}")
    
    # De flotante a otros tipos
    print(f"Flotante a entero: {flotante} -> {int(flotante)}, Tipo: {type(int(flotante))}")
    print(f"Flotante a texto: {flotante} -> {str(flotante)}, Tipo: {type(str(flotante))}")
    print(f"Flotante a booleano: {flotante} -> {bool(flotante)}, Tipo: {type(bool(flotante))}")
    
    # De texto a otros tipos (cuando sea posible)
    texto_numerico = "123"
    texto_decimal = "45.67"
    print(f"Texto a entero (si contiene un número): '{texto_numerico}' -> {int(texto_numerico)}")
    print(f"Texto a flotante (si contiene un número): '{texto_decimal}' -> {float(texto_decimal)}")
    
    # De booleano a otros tipos
    print(f"Booleano a entero: {booleano} -> {int(booleano)}")
    print(f"Booleano a flotante: {booleano} -> {float(booleano)}")
    print(f"Booleano a texto: {booleano} -> {str(booleano)}")
    
    # Errores comunes de conversión (comentados para evitar errores de ejecución)
    print("\n=== Errores Comunes en Conversiones (ejemplos) ===")
    print("Intentar convertir un texto no numérico a entero: int('Python') -> ValueError")
    print("Intentar convertir un texto con caracteres no decimales a flotante: float('12.34.56') -> ValueError")
    
    # Casos especiales y conversiones interesantes
    print("\n=== Casos Especiales ===")
    print(f"Valor vacío a booleano: bool('') -> {bool('')}")
    print(f"Cero a booleano: bool(0) -> {bool(0)}")
    print(f"Texto 'False' a booleano: bool('False') -> {bool('False')}")
    
    # Ejercicios para el usuario
    print("\n=== EJERCICIOS PARA PRACTICAR ===")
    print("1. Convierte la cadena '3.14159' a un número flotante y multiplícalo por 2")
    print("2. Convierte el entero 255 a su representación en texto y concatena ' es el valor máximo de un byte'")
    print("3. Convierte el valor booleano False a su representación en texto y cuenta su longitud")
    print("4. Intenta convertir diferentes valores a booleano y analiza cuáles se convierten a True y cuáles a False")

if __name__ == "__main__":
    main()
