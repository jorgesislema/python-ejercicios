"""
Ejercicio 5: Manejo de Excepciones en Bucles

Objetivo: Aprender a manejar excepciones dentro de bucles sin interrumpir el programa.

Instrucciones:
1. Crea una función que convierta una lista de strings a números enteros.
2. Maneja las excepciones para los elementos que no puedan convertirse.
3. Devuelve una lista con los números convertidos exitosamente.
"""

def convertir_a_enteros(lista_strings):
    """
    Convierte una lista de strings a enteros, ignorando elementos no válidos.
    
    Args:
        lista_strings: Lista de strings que se intentarán convertir a enteros
    
    Returns:
        Una tupla con dos elementos:
        - Lista de enteros convertidos exitosamente
        - Lista de elementos que no pudieron convertirse
    """
    enteros = []
    no_validos = []
    
    for i, valor_str in enumerate(lista_strings):
        try:
            entero = int(valor_str)
            enteros.append(entero)
        except ValueError:
            # Agregar a la lista de valores no válidos junto con su posición
            no_validos.append((i, valor_str))
            continue
    
    return enteros, no_validos

def main():
    # Lista de ejemplo con valores mixtos
    valores = ['10', '20', 'treinta', '40', 'cincuenta', '60', '70.5']
    
    print(f"Lista original: {valores}")
    
    # Convertir valores
    enteros, no_validos = convertir_a_enteros(valores)
    
    print(f"Números convertidos: {enteros}")
    
    if no_validos:
        print(f"No se pudieron convertir {len(no_validos)} elemento(s):")
        for posicion, valor in no_validos:
            print(f"  - Posición {posicion}: '{valor}'")

if __name__ == "__main__":
    main()
