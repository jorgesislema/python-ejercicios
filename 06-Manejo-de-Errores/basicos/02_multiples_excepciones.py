"""
Ejercicio 2: Múltiples Excepciones

Objetivo: Practicar el manejo de diferentes tipos de excepciones.

Instrucciones:
1. Crea una función que tome una lista y un índice como argumentos.
2. Intenta acceder al elemento en la posición indicada por el índice.
3. Maneja las posibles excepciones:
   - IndexError: si el índice está fuera de rango.
   - TypeError: si la lista no es realmente una lista.
"""

def obtener_elemento(lista, indice):
    try:
        # Intentar acceder al elemento
        elemento = lista[indice]
        return elemento
    except IndexError:
        # Manejar error de índice fuera de rango
        return f"Error: El índice {indice} está fuera de rango. La lista solo tiene {len(lista)} elementos."
    except TypeError:
        # Manejar error si el primer argumento no es una lista (o similar)
        return "Error: El primer argumento debe ser una lista u objeto similar."

# Ejemplos de uso
def main():
    # Caso 1: Lista válida e índice válido
    print(obtener_elemento([10, 20, 30, 40], 2))  # Debería devolver 30
    
    # Caso 2: Lista válida e índice fuera de rango
    print(obtener_elemento([10, 20, 30, 40], 10))  # Debería manejar IndexError
    
    # Caso 3: No es una lista
    print(obtener_elemento(123, 0))  # Debería manejar TypeError

# Ejecutar el programa
if __name__ == "__main__":
    main()
