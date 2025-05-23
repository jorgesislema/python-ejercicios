"""
Ejercicio 3: Funciones Generadoras

Objetivo: Aprender a utilizar funciones generadoras para crear iteradores eficientes.

Las funciones generadoras son una forma especial de crear iteradores de manera eficiente. 
A diferencia de las funciones normales, las funciones generadoras utilizan la palabra clave 
'yield' para devolver valores uno a uno, manteniendo el estado entre llamadas.

Instrucciones:
1. Explorar las funciones generadoras y sus características
2. Entender las diferencias con funciones normales
3. Implementar ejemplos prácticos de generadores
4. Comprender casos de uso y optimizaciones
"""

# ------------------------------------------------------------------------------------------
# 1. Introducción a los Generadores
# ------------------------------------------------------------------------------------------
print("\n1. Introducción a los Generadores")
print("-" * 70)
print("Un generador es una función especial que produce una secuencia de resultados")
print("en lugar de devolver un único valor. Se crean usando la palabra clave 'yield'.")

# Ejemplo básico de generador
def contador_simple(max_valor):
    """Generador que cuenta desde 1 hasta max_valor."""
    contador = 1
    while contador <= max_valor:
        yield contador
        contador += 1

print("\nEjemplo básico de generador:")
# Creamos un generador que cuenta hasta 5
mi_contador = contador_simple(5)

# Iteramos sobre el generador
for numero in mi_contador:
    print(f"Número generado: {numero}")

# ------------------------------------------------------------------------------------------
# 2. Diferencias entre Generadores y Funciones Normales
# ------------------------------------------------------------------------------------------
print("\n2. Diferencias entre Generadores y Funciones Normales")
print("-" * 70)
print("Las funciones generadoras:")
print("- Mantienen su estado entre llamadas")
print("- Suspenden su ejecución y la reanudan donde la dejaron")
print("- Son eficientes en memoria al generar valores bajo demanda")
print("- Utilizan 'yield' en lugar de 'return' para devolver valores")

# Comparación: función normal vs generador

# Función normal que devuelve una lista completa
def obtener_cuadrados(n):
    """Función que devuelve una lista con los cuadrados de 0 a n-1."""
    return [i ** 2 for i in range(n)]

# Función generadora que produce valores uno a uno
def generar_cuadrados(n):
    """Generador que produce los cuadrados de 0 a n-1 uno por uno."""
    for i in range(n):
        yield i ** 2

print("\nComparación entre función normal y generador:")
# Uso de la función normal
cuadrados_lista = obtener_cuadrados(5)
print(f"Lista de cuadrados (función normal): {cuadrados_lista}")

# Uso del generador
cuadrados_gen = generar_cuadrados(5)
print(f"Objeto generador: {cuadrados_gen}")
print("Valores del generador:", end=" ")
for cuadrado in cuadrados_gen:
    print(cuadrado, end=" ")
print()  # Salto de línea

# ------------------------------------------------------------------------------------------
# 3. Características Avanzadas de los Generadores
# ------------------------------------------------------------------------------------------
print("\n3. Características Avanzadas de los Generadores")
print("-" * 70)

# Expresiones generadoras (similar a list comprehensions)
print("\nExpresiones generadoras:")
# List comprehension (crea toda la lista en memoria)
lista_cubos = [i ** 3 for i in range(5)]
print(f"Lista de cubos: {lista_cubos}")

# Expresión generadora (genera valores bajo demanda)
gen_cubos = (i ** 3 for i in range(5))
print(f"Generador de cubos: {gen_cubos}")
print("Valores del generador de cubos:", end=" ")
for cubo in gen_cubos:
    print(cubo, end=" ")
print()  # Salto de línea

# Generadores infinitos
print("\nGeneradores infinitos:")
def numeros_impares():
    """Generador infinito de números impares."""
    n = 1
    while True:
        yield n
        n += 2

print("Primeros 5 números impares:")
impares = numeros_impares()
for _ in range(5):
    print(next(impares), end=" ")
print()  # Salto de línea

# Uso de send() para comunicarse con el generador
print("\nComunicación bidireccional con send():")
def eco_interactivo():
    """Generador que recibe y devuelve valores."""
    while True:
        # yield devuelve un valor y espera recibir otro con send()
        valor_recibido = yield "Esperando entrada..."
        if valor_recibido is not None:
            yield f"Eco: {valor_recibido}"

eco = eco_interactivo()
print(next(eco))  # Inicializar el generador
print(eco.send("Hola"))
print(next(eco))  # Avanzar al próximo yield
print(eco.send("Mundo"))

# ------------------------------------------------------------------------------------------
# 4. Casos de Uso Prácticos
# ------------------------------------------------------------------------------------------
print("\n4. Casos de Uso Prácticos")
print("-" * 70)
print("Los generadores son ideales para:")
print("- Procesar archivos grandes línea por línea")
print("- Trabajar con streams de datos")
print("- Implementar iteración perezosa (lazy evaluation)")
print("- Secuencias infinitas o muy largas")

# Ejemplo: Leer un archivo línea por línea
print("\nEjemplo conceptual de lectura de archivo:")
def leer_archivo_grande(nombre_archivo):
    """Generador que lee un archivo grande línea por línea."""
    print(f"[Simulando apertura de {nombre_archivo}]")
    # En un caso real: with open(nombre_archivo, 'r') as archivo:
    lineas = ["Línea 1: Datos importantes", 
              "Línea 2: Más información", 
              "Línea 3: Datos finales"]
    
    for linea in lineas:
        yield linea
    
    print(f"[Simulando cierre de {nombre_archivo}]")

# Usar el generador para procesar el archivo
for linea in leer_archivo_grande("datos_enormes.txt"):
    print(f"Procesando: {linea}")

# Implementación de la secuencia de Fibonacci con generadores
print("\nSecuencia de Fibonacci con generadores:")
def fibonacci(limite):
    """Generador que produce números de Fibonacci hasta el límite especificado."""
    a, b = 0, 1
    while a <= limite:
        yield a
        a, b = b, a + b

print("Secuencia de Fibonacci hasta 100:")
for num in fibonacci(100):
    print(num, end=" ")
print()  # Salto de línea

# ------------------------------------------------------------------------------------------
# 5. Optimización de Memoria
# ------------------------------------------------------------------------------------------
print("\n5. Optimización de Memoria")
print("-" * 70)
print("Los generadores son mucho más eficientes en memoria que las listas")
print("para secuencias grandes, ya que solo mantienen un valor a la vez.")

# Ejemplo conceptual de ahorro de memoria
import sys

# Creación de una lista de 1000 números
numeros_lista = [i for i in range(1000)]
# Creación de un generador de 1000 números
numeros_gen = (i for i in range(1000))

# Comparación de tamaño en memoria (aproximado)
print(f"\nTamaño de lista en memoria: {sys.getsizeof(numeros_lista)} bytes")
print(f"Tamaño de generador en memoria: {sys.getsizeof(numeros_gen)} bytes")

# ------------------------------------------------------------------------------------------
# Ejercicios propuestos
# ------------------------------------------------------------------------------------------
print("\nEjercicios propuestos:")
print("-" * 70)
print("1. Crea un generador que produzca los primeros n números primos.")
print("2. Implementa un generador que simule la lectura de un archivo de log línea por línea.")
print("3. Desarrolla un generador que permita paginar resultados (similar a un paginador).")
print("4. Crea un generador de permutaciones de una lista de elementos.")
print("5. Implementa un generador que produzca números aleatorios dentro de un rango.")

"""
Soluciones a los ejercicios propuestos:

1. Generador de números primos:

def es_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generar_primos(n):
    """Genera los primeros n números primos."""
    contador = 0
    numero = 2
    while contador < n:
        if es_primo(numero):
            yield numero
            contador += 1
        numero += 1

2. Simulador de lectura de log:

def lector_log(archivo_simulado):
    """Simula la lectura de un archivo de log."""
    logs = [
        "[INFO] 2023-05-01 10:15:32 - Aplicación iniciada",
        "[WARNING] 2023-05-01 10:16:45 - Conexión lenta detectada",
        "[ERROR] 2023-05-01 10:17:22 - Fallo al conectar con la base de datos",
        "[INFO] 2023-05-01 10:18:10 - Reintentando conexión",
        "[INFO] 2023-05-01 10:18:43 - Conexión establecida"
    ]
    
    for log in logs:
        yield log

3. Paginador de resultados:

def paginador(items, items_por_pagina):
    """Genera páginas de resultados con el número especificado de ítems por página."""
    total_items = len(items)
    for i in range(0, total_items, items_por_pagina):
        yield items[i:i + items_por_pagina]

4. Generador de permutaciones:

def generar_permutaciones(elementos):
    """Genera todas las permutaciones posibles de una lista de elementos."""
    if len(elementos) <= 1:
        yield elementos
    else:
        for i in range(len(elementos)):
            # Elemento actual
            elemento_actual = elementos[i]
            # Elementos restantes
            elementos_restantes = elementos[:i] + elementos[i+1:]
            
            # Para cada permutación de los elementos restantes
            for permutacion in generar_permutaciones(elementos_restantes):
                # Yield la permutación con el elemento actual al principio
                yield [elemento_actual] + permutacion

5. Generador de números aleatorios:

import random

def generador_aleatorio(min_valor, max_valor, cantidad):
    """Genera 'cantidad' números aleatorios entre min_valor y max_valor."""
    for _ in range(cantidad):
        yield random.randint(min_valor, max_valor)
"""
