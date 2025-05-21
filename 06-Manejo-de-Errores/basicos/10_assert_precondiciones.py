"""
Ejercicio 10: Assert y Precondiciones

Objetivo: Aprender a usar assert para verificar precondiciones en funciones.

Instrucciones:
1. Implementa funciones matemáticas que requieren ciertas precondiciones.
2. Usa assert para verificar esas precondiciones.
3. Compara el uso de assert con el lanzamiento explícito de excepciones.
"""

def calcular_raiz_cuadrada(numero):
    """
    Calcula la raíz cuadrada de un número.
    
    Args:
        numero: El número para calcular su raíz cuadrada (debe ser no negativo)
        
    Returns:
        La raíz cuadrada del número
        
    Raises:
        AssertionError: Si el número es negativo
    """
    # Verificación con assert
    assert numero >= 0, f"No se puede calcular la raíz cuadrada de un número negativo ({numero})."
    
    return numero ** 0.5

def dividir(numerador, denominador):
    """
    Divide dos números.
    
    Args:
        numerador: El numerador de la división
        denominador: El denominador de la división (no puede ser cero)
        
    Returns:
        El resultado de la división
        
    Raises:
        ValueError: Si el denominador es cero
    """
    # Verificación con excepción explícita (mejor para validación de datos de usuario)
    if denominador == 0:
        raise ValueError("El denominador no puede ser cero.")
    
    return numerador / denominador

def calcular_porcentaje(valor, total):
    """
    Calcula qué porcentaje representa un valor respecto a un total.
    
    Args:
        valor: El valor a calcular su porcentaje
        total: El valor total de referencia (debe ser no cero)
        
    Returns:
        El porcentaje como un valor entre 0 y 100
    """
    # Podemos usar assert para verificaciones internas (condición de programación)
    assert total != 0, "El total no puede ser cero para calcular un porcentaje."
    
    # Podemos usar validación explícita para entrada de usuario
    if valor < 0 or total < 0:
        raise ValueError("Ni el valor ni el total pueden ser negativos.")
    
    return (valor / total) * 100

def main():
    try:
        # Casos para probar raíz cuadrada
        print("=== Raíz cuadrada ===")
        print(f"Raíz cuadrada de 16: {calcular_raiz_cuadrada(16)}")
        print(f"Raíz cuadrada de 0: {calcular_raiz_cuadrada(0)}")
        # Este provocará un AssertionError
        # print(f"Raíz cuadrada de -4: {calcular_raiz_cuadrada(-4)}")
        
        # Casos para probar división
        print("\n=== División ===")
        print(f"10 / 2 = {dividir(10, 2)}")
        # Este provocará un ValueError
        # print(f"5 / 0 = {dividir(5, 0)}")
        
        # Casos para probar porcentaje
        print("\n=== Porcentaje ===")
        print(f"50 es el {calcular_porcentaje(50, 200)}% de 200")
        print(f"75 es el {calcular_porcentaje(75, 100)}% de 100")
        # Este provocará un AssertionError
        # print(f"10 es el {calcular_porcentaje(10, 0)}% de 0")
        
    except AssertionError as e:
        print(f"Error de aserción: {e}")
    except ValueError as e:
        print(f"Error de valor: {e}")
    
    print("\n=== Diferencias entre assert y excepciones ===")
    print("- Las aserciones (assert) se usan para verificar condiciones que NUNCA deberían fallar.")
    print("- Las excepciones explícitas se usan para manejar errores esperados (validación de entrada).")
    print("- Las aserciones pueden desactivarse con optimizaciones (-O), las excepciones siempre actúan.")

if __name__ == "__main__":
    main()
