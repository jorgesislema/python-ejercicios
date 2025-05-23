"""
Ejercicio 8: Funciones Recursivas

Objetivo:
- Comprender el concepto de recursividad en programación
- Aprender a implementar funciones recursivas en Python
- Entender los casos base y casos recursivos
- Conocer las ventajas y limitaciones de la recursividad

Las funciones recursivas son aquellas que se llaman a sí mismas para resolver
un problema dividiéndolo en subproblemas más pequeños del mismo tipo.
Cada función recursiva debe tener al menos un caso base (condición de terminación)
y un caso recursivo.
"""

# 1. Factorial recursivo
print("1. Factorial recursivo")
print("-" * 50)

def factorial(n):
    """Calcula el factorial de un número usando recursividad.
    
    Args:
        n (int): Número para calcular su factorial
        
    Returns:
        int: El factorial de n
    """
    # Caso base
    if n == 0 or n == 1:
        return 1
    
    # Caso recursivo
    return n * factorial(n - 1)

# Probar la función factorial
for i in range(6):
    print(f"{i}! = {factorial(i)}")

# Explicación paso a paso de factorial(4)
print("\nExplicación paso a paso de factorial(4):")
print("factorial(4) = 4 * factorial(3)")
print("factorial(3) = 3 * factorial(2)")
print("factorial(2) = 2 * factorial(1)")
print("factorial(1) = 1  <- Caso base")
print("factorial(2) = 2 * 1 = 2")
print("factorial(3) = 3 * 2 = 6")
print("factorial(4) = 4 * 6 = 24")
print("-" * 50)

# 2. Secuencia de Fibonacci recursiva
print("2. Secuencia de Fibonacci recursiva")
print("-" * 50)

def fibonacci(n):
    """Calcula el n-ésimo número de la secuencia de Fibonacci recursivamente.
    
    Args:
        n (int): Posición en la secuencia (empezando por 0)
        
    Returns:
        int: El n-ésimo número de Fibonacci
    """
    # Casos base
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Caso recursivo
    return fibonacci(n - 1) + fibonacci(n - 2)

# Mostrar los primeros números de Fibonacci
print("Primeros números de la secuencia de Fibonacci:")
for i in range(10):
    print(f"fibonacci({i}) = {fibonacci(i)}")

# Explicación visual del árbol de recursión para fibonacci(5)
print("\nExplicación del árbol de recursión para fibonacci(5):")
print("fibonacci(5) = fibonacci(4) + fibonacci(3)")
print("fibonacci(4) = fibonacci(3) + fibonacci(2)")
print("fibonacci(3) = fibonacci(2) + fibonacci(1)")
print("fibonacci(2) = fibonacci(1) + fibonacci(0)")
print("fibonacci(1) = 1  <- Caso base")
print("fibonacci(0) = 0  <- Caso base")
print("Subiendo de vuelta por el árbol...")
print("fibonacci(2) = 1 + 0 = 1")
print("fibonacci(3) = 1 + 1 = 2")
print("fibonacci(4) = 2 + 1 = 3")
print("fibonacci(5) = 3 + 2 = 5")
print("-" * 50)

# 3. Suma de elementos en una lista recursivamente
print("3. Suma de elementos en una lista recursivamente")
print("-" * 50)

def suma_lista(lista):
    """Suma los elementos de una lista usando recursividad.
    
    Args:
        lista (list): Lista de números
        
    Returns:
        int o float: La suma de los elementos
    """
    # Caso base: lista vacía
    if not lista:
        return 0
    
    # Caso recursivo: el primer elemento más la suma del resto
    return lista[0] + suma_lista(lista[1:])

# Probar la función
numeros = [1, 2, 3, 4, 5]
print(f"Lista: {numeros}")
print(f"Suma: {suma_lista(numeros)}")

# Explicación paso a paso
print("\nExplicación paso a paso de suma_lista([1, 2, 3, 4, 5]):")
print("suma_lista([1, 2, 3, 4, 5]) = 1 + suma_lista([2, 3, 4, 5])")
print("suma_lista([2, 3, 4, 5]) = 2 + suma_lista([3, 4, 5])")
print("suma_lista([3, 4, 5]) = 3 + suma_lista([4, 5])")
print("suma_lista([4, 5]) = 4 + suma_lista([5])")
print("suma_lista([5]) = 5 + suma_lista([])")
print("suma_lista([]) = 0  <- Caso base")
print("suma_lista([5]) = 5 + 0 = 5")
print("suma_lista([4, 5]) = 4 + 5 = 9")
print("suma_lista([3, 4, 5]) = 3 + 9 = 12")
print("suma_lista([2, 3, 4, 5]) = 2 + 12 = 14")
print("suma_lista([1, 2, 3, 4, 5]) = 1 + 14 = 15")
print("-" * 50)

# 4. Máximo común divisor (algoritmo de Euclides)
print("4. Máximo común divisor (algoritmo de Euclides)")
print("-" * 50)

def mcd(a, b):
    """Calcula el máximo común divisor de dos números usando el algoritmo de Euclides.
    
    Args:
        a (int): Primer número
        b (int): Segundo número
        
    Returns:
        int: El máximo común divisor de a y b
    """
    # Caso base
    if b == 0:
        return a
    
    # Caso recursivo
    return mcd(b, a % b)

# Probar la función
a, b = 48, 18
print(f"MCD de {a} y {b}: {mcd(a, b)}")

a, b = 101, 103
print(f"MCD de {a} y {b}: {mcd(a, b)}")

# Explicación paso a paso
print("\nExplicación paso a paso de mcd(48, 18):")
print("mcd(48, 18) = mcd(18, 48 % 18) = mcd(18, 12)")
print("mcd(18, 12) = mcd(12, 18 % 12) = mcd(12, 6)")
print("mcd(12, 6) = mcd(6, 12 % 6) = mcd(6, 0)")
print("mcd(6, 0) = 6  <- Caso base")
print("-" * 50)

# 5. Torres de Hanoi
print("5. Torres de Hanoi")
print("-" * 50)

def hanoi(n, origen, auxiliar, destino):
    """Resuelve el problema de las Torres de Hanoi.
    
    Args:
        n (int): Número de discos
        origen (str): Poste de origen
        auxiliar (str): Poste auxiliar
        destino (str): Poste de destino
    """
    # Caso base: un solo disco
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return
    
    # Caso recursivo
    # 1. Mover n-1 discos de origen a auxiliar
    hanoi(n-1, origen, destino, auxiliar)
    # 2. Mover el disco n de origen a destino
    print(f"Mover disco {n} de {origen} a {destino}")
    # 3. Mover n-1 discos de auxiliar a destino
    hanoi(n-1, auxiliar, origen, destino)

# Resolver Torres de Hanoi para 3 discos
print("Solución para Torres de Hanoi con 3 discos:")
hanoi(3, 'A', 'B', 'C')
print("-" * 50)

# 6. Invertir una cadena recursivamente
print("6. Invertir una cadena recursivamente")
print("-" * 50)

def invertir_cadena(cadena):
    """Invierte una cadena usando recursividad.
    
    Args:
        cadena (str): Cadena a invertir
        
    Returns:
        str: Cadena invertida
    """
    # Caso base: cadena vacía o de un solo carácter
    if len(cadena) <= 1:
        return cadena
    
    # Caso recursivo: último carácter + resto invertido
    return cadena[-1] + invertir_cadena(cadena[:-1])

# Probar la función
texto = "Python"
print(f"Texto original: {texto}")
print(f"Texto invertido: {invertir_cadena(texto)}")

# Explicación paso a paso
print("\nExplicación paso a paso de invertir_cadena('Python'):")
print("invertir_cadena('Python') = 'n' + invertir_cadena('Pytho')")
print("invertir_cadena('Pytho') = 'o' + invertir_cadena('Pyth')")
print("invertir_cadena('Pyth') = 'h' + invertir_cadena('Pyt')")
print("invertir_cadena('Pyt') = 't' + invertir_cadena('Py')")
print("invertir_cadena('Py') = 'y' + invertir_cadena('P')")
print("invertir_cadena('P') = 'P'  <- Caso base")
print("invertir_cadena('Py') = 'y' + 'P' = 'yP'")
print("invertir_cadena('Pyt') = 't' + 'yP' = 'tyP'")
print("invertir_cadena('Pyth') = 'h' + 'tyP' = 'htyP'")
print("invertir_cadena('Pytho') = 'o' + 'htyP' = 'ohtyP'")
print("invertir_cadena('Python') = 'n' + 'ohtyP' = 'nohtyP'")
print("-" * 50)

# 7. Búsqueda binaria recursiva
print("7. Búsqueda binaria recursiva")
print("-" * 50)

def busqueda_binaria(lista, elemento, inicio=0, fin=None):
    """Busca un elemento en una lista ordenada usando búsqueda binaria recursiva.
    
    Args:
        lista (list): Lista ordenada donde buscar
        elemento: Elemento a buscar
        inicio (int): Índice de inicio para la búsqueda
        fin (int): Índice de fin para la búsqueda
        
    Returns:
        int: Índice del elemento si se encuentra, -1 si no está en la lista
    """
    # Inicializar fin si es la primera llamada
    if fin is None:
        fin = len(lista) - 1
    
    # Caso base 1: No se encontró el elemento
    if inicio > fin:
        return -1
    
    # Calcular el punto medio
    medio = (inicio + fin) // 2
    
    # Caso base 2: Elemento encontrado
    if lista[medio] == elemento:
        return medio
    
    # Casos recursivos
    if lista[medio] > elemento:
        # Buscar en la mitad izquierda
        return busqueda_binaria(lista, elemento, inicio, medio - 1)
    else:
        # Buscar en la mitad derecha
        return busqueda_binaria(lista, elemento, medio + 1, fin)

# Lista ordenada para probar
numeros_ordenados = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(f"Lista ordenada: {numeros_ordenados}")

# Buscar elementos
elemento = 7
indice = busqueda_binaria(numeros_ordenados, elemento)
print(f"Buscando {elemento}: {'Encontrado en índice ' + str(indice) if indice != -1 else 'No encontrado'}")

elemento = 10
indice = busqueda_binaria(numeros_ordenados, elemento)
print(f"Buscando {elemento}: {'Encontrado en índice ' + str(indice) if indice != -1 else 'No encontrado'}")
print("-" * 50)

# 8. Limitaciones y problemas de la recursividad
print("8. Limitaciones y problemas de la recursividad")
print("-" * 50)

print("Limitaciones de la recursividad en Python:")
print("1. Límite de profundidad de recursión (por defecto 1000 llamadas)")
print("2. Mayor consumo de memoria por la pila de llamadas")
print("3. Problemas de rendimiento en comparación con soluciones iterativas")
print("4. Riesgo de desbordamiento de pila (stack overflow)")

# Ejemplo del límite de recursión
import sys
print(f"\nLímite actual de recursión en Python: {sys.getrecursionlimit()}")

# Fibonacci ineficiente
print("\nFibonacci recursivo es ineficiente para números grandes:")
print("Para fibonacci(30), se realizan millones de llamadas recursivas")
print("Una implementación iterativa o con memoización es mucho más eficiente")

# Solución con memoización
print("\nFibonacci con memoización (programación dinámica):")
def fibonacci_memo(n, memo={}):
    """Versión optimizada de Fibonacci usando memoización."""
    if n in memo:
        return memo[n]
    
    if n <= 1:
        resultado = n
    else:
        resultado = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    
    memo[n] = resultado
    return resultado

# Calcular fibonacci(30) con memoización
resultado = fibonacci_memo(30)
print(f"fibonacci_memo(30) = {resultado}")
print("-" * 50)

"""
EJERCICIOS PROPUESTOS:

1. Implementa una función recursiva llamada 'potencia(base, exponente)' que
   calcule la potencia de un número sin utilizar el operador **. Debe funcionar
   para exponentes enteros positivos y negativos.

2. Crea una función recursiva 'es_palindromo(cadena)' que determine si una
   cadena es un palíndromo (se lee igual de izquierda a derecha que de derecha
   a izquierda, ignorando espacios y mayúsculas/minúsculas).

3. Implementa una función recursiva 'contar_apariciones(lista, elemento)' que
   cuente cuántas veces aparece un elemento específico en una lista o sublistas.
   La lista puede contener otras listas anidadas, por ejemplo:
   contar_apariciones([1, [2, 1], [1, [3, 1]]], 1) debería retornar 4.
"""
