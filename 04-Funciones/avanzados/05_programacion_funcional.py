"""
Ejercicio 5: Programación Funcional en Python

Objetivo: Comprender y aplicar los principios de la programación funcional en Python.

La programación funcional es un paradigma de programación que trata la computación como 
la evaluación de funciones matemáticas y evita el cambio de estado y datos mutables. 
Python, aunque no es un lenguaje puramente funcional, ofrece características que permiten 
programar en este estilo, lo que puede resultar en código más conciso, predecible y fácil de probar.

Instrucciones:
1. Explorar los conceptos fundamentales de la programación funcional
2. Comprender cómo aplicar estos conceptos en Python
3. Implementar ejemplos utilizando técnicas funcionales
4. Analizar las ventajas y desventajas de este paradigma
"""

# ------------------------------------------------------------------------------------------
# 1. Principios de la Programación Funcional
# ------------------------------------------------------------------------------------------
print("\n1. Principios de la Programación Funcional")
print("-" * 70)
print("Los principios clave de la programación funcional incluyen:")
print("- Inmutabilidad: No modificar datos después de su creación")
print("- Funciones puras: Sin efectos secundarios y con salidas predecibles")
print("- Funciones de primera clase: Las funciones son ciudadanos de primera clase")
print("- Transparencia referencial: Una expresión puede ser reemplazada por su valor")
print("- Recursión: Preferir recursión sobre iteración con estado mutable")

# ------------------------------------------------------------------------------------------
# 2. Funciones Puras
# ------------------------------------------------------------------------------------------
print("\n2. Funciones Puras")
print("-" * 70)
print("Una función pura:")
print("- Siempre produce el mismo resultado para los mismos argumentos")
print("- No causa efectos secundarios (no modifica variables externas)")
print("- No depende del estado externo (solo de sus parámetros)")

# Ejemplo de función pura
def sumar(a, b):
    """Función pura que suma dos números."""
    return a + b

# Ejemplo de función impura
contador = 0

def incrementar_contador():
    """Función impura que modifica una variable global."""
    global contador
    contador += 1
    return contador

print("\nDemostración de funciones puras vs. impuras:")
print(f"Sumar(3, 4): {sumar(3, 4)}")
print(f"Sumar(3, 4) de nuevo: {sumar(3, 4)}")  # Siempre devuelve 7

print(f"Incrementar contador: {incrementar_contador()}")
print(f"Incrementar contador de nuevo: {incrementar_contador()}")  # Valor diferente

# ------------------------------------------------------------------------------------------
# 3. Inmutabilidad y Estructuras de Datos
# ------------------------------------------------------------------------------------------
print("\n3. Inmutabilidad y Estructuras de Datos")
print("-" * 70)
print("La inmutabilidad sugiere que los datos no deben cambiar después de su creación.")
print("En Python, algunas estructuras son inmutables (tuplas, strings) y otras son")
print("mutables (listas, diccionarios).")

# Ejemplo de programación con inmutabilidad
def agregar_elemento(tupla, elemento):
    """Agrega un elemento a una tupla de forma inmutable."""
    return tupla + (elemento,)  # Crea una nueva tupla

mi_tupla = (1, 2, 3)
nueva_tupla = agregar_elemento(mi_tupla, 4)

print(f"\nTupla original: {mi_tupla}")  # No cambia
print(f"Nueva tupla: {nueva_tupla}")    # Nueva tupla con el elemento adicional

# Contraste con enfoque mutable
def agregar_a_lista(lista, elemento):
    """Agrega un elemento a una lista de forma mutable."""
    lista.append(elemento)  # Modifica la lista original
    return lista

mi_lista = [1, 2, 3]
agregar_a_lista(mi_lista, 4)

print(f"Lista original (modificada): {mi_lista}")  # La lista original cambia

# ------------------------------------------------------------------------------------------
# 4. Funciones de Orden Superior en Programación Funcional
# ------------------------------------------------------------------------------------------
print("\n4. Funciones de Orden Superior en Programación Funcional")
print("-" * 70)
print("Las funciones de orden superior son fundamentales en la programación funcional.")
print("Permiten abstraer patrones comunes y crear código más declarativo.")

# Ejemplos de funciones de orden superior en programación funcional
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map: aplicar una operación a cada elemento
cuadrados = list(map(lambda x: x**2, numeros))

# filter: seleccionar elementos según un criterio
pares = list(filter(lambda x: x % 2 == 0, numeros))

# reduce: combinar elementos
from functools import reduce
suma = reduce(lambda a, b: a + b, numeros)

print("\nEjemplos de operaciones funcionales:")
print(f"Números originales: {numeros}")
print(f"Cuadrados (map): {cuadrados}")
print(f"Números pares (filter): {pares}")
print(f"Suma total (reduce): {suma}")

# ------------------------------------------------------------------------------------------
# 5. Composición de Funciones
# ------------------------------------------------------------------------------------------
print("\n5. Composición de Funciones")
print("-" * 70)
print("La composición de funciones permite combinar múltiples funciones en una sola.")
print("Es una técnica poderosa en programación funcional.")

# Definimos algunas funciones simples
def duplicar(x):
    return x * 2

def incrementar(x):
    return x + 1

def cuadrado(x):
    return x ** 2

# Composición manual
def componer2(f, g):
    """Compone dos funciones f y g."""
    return lambda x: f(g(x))

# Creamos nuevas funciones a través de composición
duplicar_y_sumar = componer2(incrementar, duplicar)
sumar_y_cuadrado = componer2(cuadrado, incrementar)

print("\nComposición de funciones:")
print(f"duplicar(5): {duplicar(5)}")
print(f"incrementar(5): {incrementar(5)}")
print(f"duplicar_y_sumar(5): {duplicar_y_sumar(5)}")  # incrementar(duplicar(5)) = 11
print(f"sumar_y_cuadrado(5): {sumar_y_cuadrado(5)}")  # cuadrado(incrementar(5)) = 36

# Composición generalizada
def componer(*funciones):
    """Compone múltiples funciones de derecha a izquierda."""
    def composicion(x):
        resultado = x
        for f in reversed(funciones):
            resultado = f(resultado)
        return resultado
    return composicion

# Composición de tres funciones
pipeline = componer(cuadrado, incrementar, duplicar)
print(f"pipeline(5): {pipeline(5)}")  # cuadrado(incrementar(duplicar(5))) = 121

# ------------------------------------------------------------------------------------------
# 6. Recursión
# ------------------------------------------------------------------------------------------
print("\n6. Recursión")
print("-" * 70)
print("La recursión es preferida sobre los bucles en programación funcional pura")
print("ya que evita la mutación de variables de estado.")

# Factorial con recursión
def factorial(n):
    """Calcula el factorial de n de forma recursiva."""
    return 1 if n <= 1 else n * factorial(n - 1)

# Fibonacci con recursión
def fibonacci(n):
    """Calcula el n-ésimo número de Fibonacci de forma recursiva."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("\nEjemplos de funciones recursivas:")
print(f"factorial(5): {factorial(5)}")
print(f"fibonacci(7): {fibonacci(7)}")

# ------------------------------------------------------------------------------------------
# 7. Ventajas y Desventajas
# ------------------------------------------------------------------------------------------
print("\n7. Ventajas y Desventajas")
print("-" * 70)
print("Ventajas de la programación funcional:")
print("- Código más predecible y fácil de probar")
print("- Menos errores relacionados con estado mutable")
print("- Mejor para concurrencia y paralelismo")
print("- Más fácil de razonar sobre el código")

print("\nDesventajas:")
print("- Puede ser menos eficiente en algunos casos")
print("- Curva de aprendizaje para programadores acostumbrados a estilos imperativos")
print("- No siempre es la mejor solución para todos los problemas")
print("- Python no está optimizado para recursión (límite de recursión)")

# ------------------------------------------------------------------------------------------
# 8. Ejemplo Práctico: Procesamiento de Datos
# ------------------------------------------------------------------------------------------
print("\n8. Ejemplo Práctico: Procesamiento de Datos")
print("-" * 70)

# Datos de ejemplo: lista de diccionarios con información de personas
personas = [
    {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Juan", "edad": 30, "ciudad": "Barcelona"},
    {"nombre": "María", "edad": 28, "ciudad": "Valencia"},
    {"nombre": "Carlos", "edad": 35, "ciudad": "Madrid"},
    {"nombre": "Lucía", "edad": 22, "ciudad": "Barcelona"}
]

# Enfoque funcional para filtrar, transformar y ordenar datos
def filtrar_por_ciudad(personas, ciudad):
    return list(filter(lambda p: p["ciudad"] == ciudad, personas))

def extraer_nombres(personas):
    return list(map(lambda p: p["nombre"], personas))

def ordenar_por_edad(personas):
    return sorted(personas, key=lambda p: p["edad"])

# Procesamiento de datos en un pipeline
def procesar_personas(personas, ciudad):
    return extraer_nombres(ordenar_por_edad(filtrar_por_ciudad(personas, ciudad)))

print("\nProcesamiento funcional de datos:")
print(f"Personas de Madrid ordenadas por edad: {procesar_personas(personas, 'Madrid')}")
print(f"Personas de Barcelona ordenadas por edad: {procesar_personas(personas, 'Barcelona')}")

# ------------------------------------------------------------------------------------------
# Ejercicios propuestos
# ------------------------------------------------------------------------------------------
print("\nEjercicios propuestos:")
print("-" * 70)
print("1. Implementa una función `aplicar_varias` que aplique múltiples funciones a un valor y devuelva una lista con los resultados.")
print("2. Escribe una función recursiva para calcular la suma de los dígitos de un número.")
print("3. Implementa una versión inmutable de una cola (FIFO) utilizando tuplas.")
print("4. Crea un sistema de procesamiento de texto que utilice técnicas funcionales para contar palabras, filtrar stopwords, etc.")
print("5. Desarrolla una función `agrupar_por` que agrupe elementos de una lista según el resultado de una función clave.")

"""
Soluciones a los ejercicios propuestos:

1. Función aplicar_varias:

def aplicar_varias(valor, funciones):
    """
    Aplica múltiples funciones a un valor y devuelve una lista con los resultados.
    
    Args:
        valor: El valor inicial
        funciones: Lista de funciones a aplicar
    
    Returns:
        Lista con los resultados de aplicar cada función al valor
    """
    return [funcion(valor) for funcion in funciones]

# Ejemplo de uso:
def cuadrado(x): return x ** 2
def duplicar(x): return x * 2
def invertir(x): return -x

resultados = aplicar_varias(5, [cuadrado, duplicar, invertir])
# resultados será [25, 10, -5]

2. Suma de dígitos recursiva:

def suma_digitos(numero):
    """
    Calcula la suma de los dígitos de un número de forma recursiva.
    
    Args:
        numero: El número cuyos dígitos se sumarán
    
    Returns:
        La suma de los dígitos
    """
    # Caso base
    if numero < 10:
        return numero
    
    # Caso recursivo
    return numero % 10 + suma_digitos(numero // 10)

# Ejemplo: suma_digitos(12345) = 15

3. Cola inmutable:

class ColaInmutable:
    """Implementación inmutable de una cola (FIFO)."""
    
    def __init__(self, elementos=()):
        self._elementos = tuple(elementos)
    
    def encolar(self, elemento):
        """Devuelve una nueva cola con el elemento añadido al final."""
        return ColaInmutable(self._elementos + (elemento,))
    
    def desencolar(self):
        """
        Devuelve una tupla con:
        - El primer elemento de la cola
        - Una nueva cola sin el primer elemento
        """
        if not self._elementos:
            raise ValueError("La cola está vacía")
        
        return self._elementos[0], ColaInmutable(self._elementos[1:])
    
    def esta_vacia(self):
        """Comprueba si la cola está vacía."""
        return len(self._elementos) == 0
    
    def __len__(self):
        return len(self._elementos)
    
    def __str__(self):
        return str(self._elementos)

# Ejemplo de uso:
cola = ColaInmutable()
cola = cola.encolar("A")
cola = cola.encolar("B")
elemento, cola = cola.desencolar()  # elemento = "A", cola solo contiene "B"

4. Procesamiento funcional de texto:

import re
from functools import reduce

def normalizar_texto(texto):
    """Convierte a minúsculas y elimina signos de puntuación."""
    return re.sub(r'[^\w\s]', '', texto.lower())

def tokenizar(texto):
    """Divide el texto en palabras."""
    return texto.split()

def filtrar_stopwords(tokens, stopwords):
    """Elimina las palabras vacías de la lista de tokens."""
    return filter(lambda token: token not in stopwords, tokens)

def contar_palabras(tokens):
    """Cuenta la frecuencia de cada palabra."""
    return reduce(
        lambda contador, palabra: {**contador, palabra: contador.get(palabra, 0) + 1},
        tokens,
        {}
    )

def procesar_texto(texto, stopwords=None):
    """Procesa el texto utilizando técnicas funcionales."""
    if stopwords is None:
        stopwords = set(['el', 'la', 'los', 'las', 'un', 'una', 'y', 'en', 'de', 'a'])
    
    return contar_palabras(
        list(filtrar_stopwords(
            tokenizar(
                normalizar_texto(texto)
            ),
            stopwords
        ))
    )

# Ejemplo:
texto = "El rápido zorro marrón salta sobre el perro perezoso. El perro duerme."
resultado = procesar_texto(texto)
# resultado será un diccionario con la frecuencia de cada palabra

5. Función agrupar_por:

def agrupar_por(iterable, key_func):
    """
    Agrupa elementos de un iterable según el resultado de key_func.
    
    Args:
        iterable: Iterable con los elementos a agrupar
        key_func: Función que determina la clave de agrupación
    
    Returns:
        Diccionario con elementos agrupados por clave
    """
    grupos = {}
    
    for item in iterable:
        clave = key_func(item)
        if clave not in grupos:
            grupos[clave] = []
        grupos[clave].append(item)
    
    return grupos

# Ejemplo:
personas = [
    {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Juan", "edad": 30, "ciudad": "Barcelona"},
    {"nombre": "María", "edad": 25, "ciudad": "Valencia"},
    {"nombre": "Carlos", "edad": 30, "ciudad": "Madrid"}
]

# Agrupar por edad
por_edad = agrupar_por(personas, lambda p: p["edad"])
# por_edad tendrá las claves 25 y 30, con listas de personas de esas edades

# Agrupar por ciudad
por_ciudad = agrupar_por(personas, lambda p: p["ciudad"])
# por_ciudad tendrá las claves "Madrid", "Barcelona" y "Valencia"
"""
