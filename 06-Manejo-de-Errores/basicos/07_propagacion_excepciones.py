"""
Ejercicio 7: Propagación de Excepciones

Objetivo: Comprender cómo se propagan las excepciones y cuándo atraparlas.

Instrucciones:
1. Crea tres funciones anidadas: nivel1, nivel2 y nivel3.
2. La función nivel3 genera una excepción.
3. Observa cómo se propaga la excepción a través de las diferentes funciones.
4. Maneja la excepción en diferentes niveles y observa el comportamiento.
"""

def nivel3(x):
    """Función del nivel más profundo que genera una excepción."""
    print("Entrando a nivel3")
    
    if x == 0:
        raise ValueError("¡No se puede dividir entre cero!")
    
    resultado = 10 / x
    print(f"nivel3: El resultado es {resultado}")
    print("Saliendo de nivel3")
    return resultado

def nivel2(x):
    """Función intermedia que llama a nivel3."""
    print("Entrando a nivel2")
    
    try:
        resultado = nivel3(x)
        print("nivel2: Todo salió bien en nivel3")
    except ValueError as e:
        print(f"nivel2: ¡Error capturado! - {e}")
        # Opciones:
        # 1. Propagar la excepción original
        # raise
        
        # 2. Propagar una nueva excepción
        # raise RuntimeError("Error en el nivel 2") from e
        
        # 3. Manejar la excepción sin propagarla
        return None
    
    print("Saliendo de nivel2")
    return resultado

def nivel1(x):
    """Función de nivel superior que llama a nivel2."""
    print("Entrando a nivel1")
    
    try:
        resultado = nivel2(x)
        print(f"nivel1: Todo salió bien, resultado = {resultado}")
    except Exception as e:
        print(f"nivel1: ¡Error capturado! - {e}")
        return None
    
    print("Saliendo de nivel1")
    return resultado

def main():
    print("=== Caso 1: Sin excepciones ===")
    nivel1(5)
    
    print("\n=== Caso 2: Con excepción (x=0) ===")
    nivel1(0)

if __name__ == "__main__":
    main()
