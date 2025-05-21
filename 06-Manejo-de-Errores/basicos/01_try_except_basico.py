"""
Ejercicio 1: Try-Except Básico

Objetivo: Aprender a manejar errores de división por cero.

Instrucciones:
1. Solicita al usuario dos números enteros.
2. Intenta dividir el primer número entre el segundo.
3. Maneja el error ZeroDivisionError que ocurre si el segundo número es cero.
4. Muestra un mensaje adecuado al usuario en caso de error.
"""

def main():
    try:
        # Solicitar números al usuario
        num1 = int(input("Introduce el primer número: "))
        num2 = int(input("Introduce el segundo número: "))
        
        # Intentar realizar la división
        resultado = num1 / num2
        
        # Mostrar el resultado
        print(f"El resultado de {num1} / {num2} es: {resultado}")
        
    except ZeroDivisionError:
        # Manejar el error específico de división por cero
        print("¡Error! No es posible dividir entre cero.")
        
    except ValueError:
        # Manejar errores de conversión de tipos
        print("¡Error! Debes introducir números enteros válidos.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
