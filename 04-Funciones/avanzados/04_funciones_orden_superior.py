"""
Ejercicio 4: Funciones de Orden Superior

Objetivo: Comprender y utilizar funciones de orden superior en Python.

Las funciones de orden superior son funciones que pueden recibir otras funciones como 
argumentos o que pueden devolver funciones como resultado. Este concepto es fundamental 
en la programación funcional y permite crear código más elegante, modular y reutilizable.

Instrucciones:
1. Estudiar qué son las funciones de orden superior y su importancia
2. Analizar las funciones incorporadas de Python que son de orden superior
3. Implementar ejemplos personalizados de funciones de orden superior
4. Aplicar este concepto a casos de uso prácticos
"""

# ------------------------------------------------------------------------------------------
# 1. ¿Qué son las Funciones de Orden Superior?
# ------------------------------------------------------------------------------------------
print("\n1. ¿Qué son las Funciones de Orden Superior?")
print("-" * 70)
print("Las funciones de orden superior son aquellas que pueden:")
print("- Recibir una o más funciones como argumentos")
print("- Devolver una función como resultado")
print("- O ambas cosas")

# Ejemplo sencillo: función que acepta otra función como argumento
def aplicar_funcion(f, valor):
    """Aplica la función f al valor dado y retorna el resultado."""
    return f(valor)

# Funciones para usar como argumentos
def duplicar(x):
    return x * 2

def cuadrado(x):
    return x ** 2

# Usando la función de orden superior
print("\nEjemplo de función de orden superior:")
numero = 5
print(f"Número original: {numero}")
print(f"Después de duplicar: {aplicar_funcion(duplicar, numero)}")
print(f"Después de elevar al cuadrado: {aplicar_funcion(cuadrado, numero)}")

# ------------------------------------------------------------------------------------------
# 2. Funciones de Orden Superior Incorporadas en Python
# ------------------------------------------------------------------------------------------
print("\n2. Funciones de Orden Superior Incorporadas en Python")
print("-" * 70)
print("Python incluye varias funciones de orden superior incorporadas:")
print("- map(): aplica una función a cada elemento de un iterable")
print("- filter(): filtra elementos de un iterable según una función")
print("- sorted(): ordena elementos según una función clave")
print("- reduce(): aplica una función acumulativamente a los elementos")

# Ejemplo de map()
numeros = [1, 2, 3, 4, 5]
numeros_duplicados = list(map(duplicar, numeros))
print(f"\nOriginal: {numeros}")
print(f"Después de map(duplicar): {numeros_duplicados}")

# Ejemplo de filter()
def es_par(x):
    return x % 2 == 0

numeros_pares = list(filter(es_par, numeros))
print(f"Después de filter(es_par): {numeros_pares}")

# Ejemplo de sorted() con key
personas = [
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Carlos", "edad": 25},
    {"nombre": "Berta", "edad": 35}
]

personas_ordenadas = sorted(personas, key=lambda p: p["edad"])
print("\nPersonas ordenadas por edad:")
for persona in personas_ordenadas:
    print(f"  {persona['nombre']}: {persona['edad']} años")

# Ejemplo de reduce()
from functools import reduce

def sumar(a, b):
    return a + b

suma_total = reduce(sumar, numeros)
print(f"\nSuma de {numeros} usando reduce: {suma_total}")

# ------------------------------------------------------------------------------------------
# 3. Implementando Funciones de Orden Superior Personalizadas
# ------------------------------------------------------------------------------------------
print("\n3. Implementando Funciones de Orden Superior Personalizadas")
print("-" * 70)

# Ejemplo: Función que crea funciones específicas
def crear_multiplicador(factor):
    """Crea y devuelve una función que multiplica por el factor dado."""
    def multiplicador(x):
        return x * factor
    return multiplicador

# Creamos funciones específicas
duplicador = crear_multiplicador(2)
triplicador = crear_multiplicador(3)

print("\nFunciones creadas dinámicamente:")
print(f"Duplicar 10: {duplicador(10)}")
print(f"Triplicar 10: {triplicador(10)}")

# Ejemplo: Función que aplica múltiples operaciones
def aplicar_operaciones(valor, operaciones):
    """Aplica una serie de operaciones a un valor inicial."""
    resultado = valor
    for operacion in operaciones:
        resultado = operacion(resultado)
    return resultado

# Definimos algunas operaciones
def sumar_cinco(x):
    return x + 5

def dividir_por_dos(x):
    return x / 2

# Aplicamos las operaciones en secuencia
valor_inicial = 10
resultado_final = aplicar_operaciones(valor_inicial, [sumar_cinco, duplicar, dividir_por_dos])
print(f"\nValor inicial: {valor_inicial}")
print(f"Después de aplicar [sumar_cinco, duplicar, dividir_por_dos]: {resultado_final}")

# ------------------------------------------------------------------------------------------
# 4. Casos de Uso Prácticos
# ------------------------------------------------------------------------------------------
print("\n4. Casos de Uso Prácticos")
print("-" * 70)
print("Las funciones de orden superior son útiles para:")
print("- Estrategias de procesamiento de datos")
print("- Implementación de patrones de diseño")
print("- Personalización de comportamientos")
print("- Composición de funcionalidades")

# Ejemplo: Sistema de procesamiento de datos con diferentes estrategias
def procesar_datos(datos, estrategia):
    """Procesa datos según la estrategia proporcionada."""
    return estrategia(datos)

# Diferentes estrategias de procesamiento
def calcular_suma(datos):
    return sum(datos)

def calcular_promedio(datos):
    return sum(datos) / len(datos) if datos else 0

def encontrar_maximo(datos):
    return max(datos) if datos else None

# Datos de ejemplo
calificaciones = [85, 90, 78, 92, 88]

print("\nProcesamiento de calificaciones con diferentes estrategias:")
print(f"Calificaciones: {calificaciones}")
print(f"Suma: {procesar_datos(calificaciones, calcular_suma)}")
print(f"Promedio: {procesar_datos(calificaciones, calcular_promedio)}")
print(f"Máximo: {procesar_datos(calificaciones, encontrar_maximo)}")

# Ejemplo: Composición de funciones
def componer(*funciones):
    """Compone una serie de funciones de derecha a izquierda."""
    def funcion_compuesta(x):
        resultado = x
        for f in reversed(funciones):
            resultado = f(resultado)
        return resultado
    return funcion_compuesta

# Usamos la composición de funciones
operacion_compuesta = componer(duplicar, sumar_cinco, cuadrado)
print(f"\nValor inicial: 3")
print(f"Después de componer(duplicar, sumar_cinco, cuadrado): {operacion_compuesta(3)}")
# Esto equivale a: duplicar(sumar_cinco(cuadrado(3)))
# Es decir: duplicar(sumar_cinco(9)) = duplicar(14) = 28

# ------------------------------------------------------------------------------------------
# 5. Ventajas y Mejores Prácticas
# ------------------------------------------------------------------------------------------
print("\n5. Ventajas y Mejores Prácticas")
print("-" * 70)
print("Ventajas de las funciones de orden superior:")
print("- Promueven la reutilización de código")
print("- Aumentan la modularidad y la composición")
print("- Facilitan el mantenimiento del código")
print("- Permiten implementar estrategias intercambiables")

print("\nMejores prácticas:")
print("- Mantener las funciones pequeñas y centradas en una sola tarea")
print("- Documentar claramente el propósito y comportamiento esperado")
print("- Evitar efectos secundarios en las funciones")
print("- Preferir inmutabilidad cuando sea posible")

# ------------------------------------------------------------------------------------------
# Ejercicios propuestos
# ------------------------------------------------------------------------------------------
print("\nEjercicios propuestos:")
print("-" * 70)
print("1. Implementa una función 'filtrar_y_transformar' que aplique un filtro y luego una transformación a una lista.")
print("2. Crea un decorador personalizado que mida el tiempo de ejecución de cualquier función.")
print("3. Desarrolla un sistema de validación de datos que utilice funciones de orden superior para aplicar múltiples reglas.")
print("4. Implementa una función 'aplanar' que convierta una lista anidada en una lista plana usando funciones de orden superior.")
print("5. Crea una función 'agrupar_por' similar al 'groupby' de SQL que agrupe elementos según una función clave.")

"""
Soluciones a los ejercicios propuestos:

1. Función filtrar_y_transformar:

def filtrar_y_transformar(datos, filtro, transformacion):
    """
    Aplica un filtro y luego una transformación a los datos.
    
    Args:
        datos: Iterable con los datos originales
        filtro: Función que devuelve True para los elementos a conservar
        transformacion: Función que transforma los elementos filtrados
    
    Returns:
        Lista con los elementos filtrados y transformados
    """
    return list(map(transformacion, filter(filtro, datos)))

# Ejemplo de uso:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = filtrar_y_transformar(
    numeros,
    lambda x: x % 2 == 0,  # Filtrar solo pares
    lambda x: x ** 2       # Elevar al cuadrado
)
# resultado será [4, 16, 36, 64, 100]

2. Decorador para medir tiempo:

import time

def medir_tiempo(funcion):
    """
    Decorador que mide el tiempo de ejecución de una función.
    """
    def wrapper(*args, **kwargs):
        tiempo_inicio = time.time()
        resultado = funcion(*args, **kwargs)
        tiempo_fin = time.time()
        print(f"La función {funcion.__name__} tardó {tiempo_fin - tiempo_inicio:.5f} segundos en ejecutarse.")
        return resultado
    return wrapper

# Ejemplo de uso:
@medir_tiempo
def operacion_lenta():
    time.sleep(1)  # Simulamos una operación que tarda 1 segundo
    return "Operación completada"

3. Sistema de validación:

def validar(datos, reglas):
    """
    Valida datos contra múltiples reglas.
    
    Args:
        datos: Los datos a validar
        reglas: Lista de funciones de validación
    
    Returns:
        True si todas las reglas se cumplen, False en caso contrario
    """
    for regla in reglas:
        if not regla(datos):
            return False
    return True

# Ejemplo de reglas para validación de contraseñas
def longitud_minima(password, min_longitud=8):
    return len(password) >= min_longitud

def contiene_mayusculas(password):
    return any(c.isupper() for c in password)

def contiene_numeros(password):
    return any(c.isdigit() for c in password)

# Uso del sistema de validación
reglas_password = [
    lambda p: longitud_minima(p, 10),
    contiene_mayusculas,
    contiene_numeros
]

es_valida = validar("Abc123456", reglas_password)

4. Función aplanar:

def aplanar(lista_anidada):
    """
    Convierte una lista anidada en una lista plana.
    
    Args:
        lista_anidada: Lista que puede contener otras listas
    
    Returns:
        Lista plana con todos los elementos
    """
    resultado = []
    
    def _aplanar(item):
        if isinstance(item, list):
            for subitem in item:
                _aplanar(subitem)
        else:
            resultado.append(item)
    
    for elemento in lista_anidada:
        _aplanar(elemento)
        
    return resultado

# Ejemplo de uso:
lista_anidada = [1, [2, 3], [4, [5, 6]], 7, [8, 9]]
# aplanar(lista_anidada) devolverá [1, 2, 3, 4, 5, 6, 7, 8, 9]

5. Función agrupar_por:

def agrupar_por(iterable, key_func):
    """
    Agrupa elementos según el resultado de la función clave.
    
    Args:
        iterable: Iterable con los elementos a agrupar
        key_func: Función que determina la clave de agrupación
    
    Returns:
        Diccionario con elementos agrupados por clave
    """
    grupos = {}
    for item in iterable:
        key = key_func(item)
        if key not in grupos:
            grupos[key] = []
        grupos[key].append(item)
    return grupos

# Ejemplo de uso:
personas = [
    {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"},
    {"nombre": "Carlos", "edad": 25, "ciudad": "Barcelona"},
    {"nombre": "Berta", "edad": 30, "ciudad": "Valencia"},
    {"nombre": "David", "edad": 25, "ciudad": "Madrid"}
]

# Agrupamos por edad
grupos_por_edad = agrupar_por(personas, lambda p: p["edad"])
# grupos_por_edad será un diccionario con claves 25 y 30,
# cada una con una lista de las personas de esa edad
"""
