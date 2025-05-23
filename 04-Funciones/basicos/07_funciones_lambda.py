"""
Ejercicio 7: Funciones Lambda (Anónimas)

Objetivo:
- Comprender qué son las funciones lambda y cuándo usarlas
- Aprender a crear y utilizar funciones anónimas en Python
- Aplicar funciones lambda con herramientas como map, filter y sorted
- Entender las limitaciones de las funciones lambda

Las funciones lambda, también conocidas como funciones anónimas, son funciones pequeñas
y de un solo uso que se definen sin nombre usando la palabra clave 'lambda'.
Son útiles cuando necesitamos una función simple para usar de inmediato, especialmente
como argumento para funciones de orden superior como map, filter y sorted.
"""

# 1. Sintaxis básica de las funciones lambda
print("1. Sintaxis básica de las funciones lambda")
print("-" * 50)

# Función tradicional
def cuadrado(x):
    return x ** 2

# Equivalente con función lambda
lambda_cuadrado = lambda x: x ** 2

# Comparación de resultados
numero = 5
print(f"Función tradicional: {cuadrado(numero)}")
print(f"Función lambda: {lambda_cuadrado(numero)}")

# Función lambda con múltiples argumentos
sumar = lambda a, b: a + b
print(f"Suma de 3 y 4: {sumar(3, 4)}")

# Función lambda con argumentos por defecto
saludar = lambda nombre, mensaje="Hola": f"{mensaje}, {nombre}!"
print(saludar("Ana"))
print(saludar("Pedro", "Bienvenido"))
print("-" * 50)

# 2. Funciones lambda como argumentos
print("2. Funciones lambda como argumentos")
print("-" * 50)

def aplicar_operacion(a, b, operacion):
    """Aplica una operación a dos números.
    
    Args:
        a: Primer número
        b: Segundo número
        operacion: Función que define la operación a realizar
        
    Returns:
        El resultado de aplicar la operación
    """
    return operacion(a, b)

# Usar con diferentes operaciones lambda
print(f"Suma: {aplicar_operacion(5, 3, lambda x, y: x + y)}")
print(f"Resta: {aplicar_operacion(5, 3, lambda x, y: x - y)}")
print(f"Multiplicación: {aplicar_operacion(5, 3, lambda x, y: x * y)}")
print(f"División: {aplicar_operacion(5, 3, lambda x, y: x / y)}")
print(f"Potencia: {aplicar_operacion(5, 3, lambda x, y: x ** y)}")
print("-" * 50)

# 3. Uso de lambda con map()
print("3. Uso de lambda con map()")
print("-" * 50)

# map() aplica una función a cada elemento de un iterable
numeros = [1, 2, 3, 4, 5]

# Usando función tradicional
def duplicar(x):
    return x * 2

numeros_duplicados = list(map(duplicar, numeros))
print(f"Usando función tradicional: {numeros_duplicados}")

# Usando función lambda
numeros_duplicados_lambda = list(map(lambda x: x * 2, numeros))
print(f"Usando función lambda: {numeros_duplicados_lambda}")

# Aplicar operaciones más complejas
numeros_procesados = list(map(lambda x: x**2 + 2*x + 1, numeros))
print(f"Aplicando expresión x² + 2x + 1: {numeros_procesados}")

# Map con múltiples iterables
lista1 = [1, 2, 3]
lista2 = [10, 20, 30]
suma_listas = list(map(lambda x, y: x + y, lista1, lista2))
print(f"Suma de elementos correspondientes: {suma_listas}")
print("-" * 50)

# 4. Uso de lambda con filter()
print("4. Uso de lambda con filter()")
print("-" * 50)

# filter() extrae elementos de un iterable basado en una función de filtrado
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar números pares
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares: {numeros_pares}")

# Filtrar números impares mayores que 5
numeros_impares_mayores_5 = list(filter(lambda x: x % 2 != 0 and x > 5, numeros))
print(f"Números impares mayores que 5: {numeros_impares_mayores_5}")

# Filtrar cadenas vacías
cadenas = ["", "Hola", "", "Mundo", "Python", ""]
cadenas_no_vacias = list(filter(lambda s: s, cadenas))  # Las cadenas vacías son False
print(f"Cadenas no vacías: {cadenas_no_vacias}")

# Filtrar elementos None
lista_con_none = [1, None, 3, None, 5, None]
lista_sin_none = list(filter(lambda x: x is not None, lista_con_none))
print(f"Lista sin elementos None: {lista_sin_none}")
print("-" * 50)

# 5. Uso de lambda con sorted()
print("5. Uso de lambda con sorted()")
print("-" * 50)

# sorted() ordena los elementos de un iterable
numeros = [5, 2, 8, 1, 9, 3]

# Ordenar de forma ascendente (por defecto)
numeros_ordenados = sorted(numeros)
print(f"Ordenados ascendente: {numeros_ordenados}")

# Ordenar de forma descendente
numeros_ordenados_desc = sorted(numeros, reverse=True)
print(f"Ordenados descendente: {numeros_ordenados_desc}")

# Ordenar lista de tuplas por el segundo elemento
pares = [(1, 5), (3, 2), (2, 8), (4, 1)]
pares_ordenados = sorted(pares, key=lambda par: par[1])
print(f"Pares ordenados por segundo elemento: {pares_ordenados}")

# Ordenar palabras por longitud
palabras = ["Python", "es", "un", "lenguaje", "de", "programación"]
palabras_por_longitud = sorted(palabras, key=lambda palabra: len(palabra))
print(f"Palabras ordenadas por longitud: {palabras_por_longitud}")

# Ordenar diccionarios por valor
estudiantes = [
    {"nombre": "Ana", "edad": 22},
    {"nombre": "Carlos", "edad": 19},
    {"nombre": "Berta", "edad": 25},
    {"nombre": "Daniel", "edad": 20}
]
estudiantes_por_edad = sorted(estudiantes, key=lambda e: e["edad"])
print("Estudiantes ordenados por edad:")
for e in estudiantes_por_edad:
    print(f"  {e['nombre']}: {e['edad']} años")
print("-" * 50)

# 6. Funciones lambda con operadores lógicos
print("6. Funciones lambda con operadores lógicos")
print("-" * 50)

# Operador AND
es_adulto_estudiante = lambda persona: persona["edad"] >= 18 and persona["es_estudiante"]

# Operador OR
necesita_atencion = lambda paciente: paciente["temperatura"] > 38 or paciente["presion"] > 140

# Operador NOT
no_disponible = lambda producto: not producto["en_stock"]

# Ejemplos de uso
persona1 = {"nombre": "Juan", "edad": 22, "es_estudiante": True}
persona2 = {"nombre": "María", "edad": 17, "es_estudiante": True}
persona3 = {"nombre": "Pedro", "edad": 25, "es_estudiante": False}

print(f"¿{persona1['nombre']} es adulto y estudiante? {es_adulto_estudiante(persona1)}")
print(f"¿{persona2['nombre']} es adulto y estudiante? {es_adulto_estudiante(persona2)}")
print(f"¿{persona3['nombre']} es adulto y estudiante? {es_adulto_estudiante(persona3)}")

paciente1 = {"nombre": "Lucía", "temperatura": 39, "presion": 120}
paciente2 = {"nombre": "Miguel", "temperatura": 37, "presion": 145}
print(f"¿{paciente1['nombre']} necesita atención? {necesita_atencion(paciente1)}")
print(f"¿{paciente2['nombre']} necesita atención? {necesita_atencion(paciente2)}")
print("-" * 50)

# 7. Funciones lambda con expresiones condicionales
print("7. Funciones lambda con expresiones condicionales")
print("-" * 50)

# Expresión condicional en lambda
estado = lambda temp: "Caliente" if temp > 25 else "Frío"
print(f"Temperatura 30°C: {estado(30)}")
print(f"Temperatura 15°C: {estado(15)}")

# Expresión condicional múltiple
calificacion = lambda puntos: "Excelente" if puntos >= 90 else "Bueno" if puntos >= 70 else "Regular" if puntos >= 60 else "Insuficiente"
print(f"95 puntos: {calificacion(95)}")
print(f"75 puntos: {calificacion(75)}")
print(f"65 puntos: {calificacion(65)}")
print(f"55 puntos: {calificacion(55)}")

# Función más compleja con condicionales
ajustar_precio = lambda precio, es_temporada_alta, tiene_descuento: \
    precio * 1.2 if es_temporada_alta and not tiene_descuento else \
    precio * 0.9 if tiene_descuento and not es_temporada_alta else \
    precio * 1.1 if es_temporada_alta and tiene_descuento else \
    precio

print(f"Precio normal (100): {ajustar_precio(100, False, False)}")
print(f"Temporada alta (100): {ajustar_precio(100, True, False)}")
print(f"Con descuento (100): {ajustar_precio(100, False, True)}")
print(f"Temporada alta con descuento (100): {ajustar_precio(100, True, True)}")
print("-" * 50)

# 8. Limitaciones de las funciones lambda
print("8. Limitaciones de las funciones lambda")
print("-" * 50)

print("Las funciones lambda tienen varias limitaciones:")
print("1. Solo pueden contener una expresión (no múltiples líneas de código)")
print("2. No pueden contener sentencias (como if, for, while, etc.)")
print("3. No tienen un nombre, lo que dificulta la depuración")
print("4. No se pueden documentar con docstrings")
print("5. Pueden hacer el código menos legible si son complejas")

print("\nCuando una lambda se vuelve compleja, es mejor usar una función tradicional:")

# Lambda compleja (difícil de leer)
compleja = lambda x, y, z: x**2 + y**2 + z**2 + 2*x*y + 2*y*z + 2*x*z

# Mejor como función tradicional
def suma_cuadrados_completa(x, y, z):
    """Calcula la suma de los cuadrados de tres números y sus productos cruzados."""
    return x**2 + y**2 + z**2 + 2*x*y + 2*y*z + 2*x*z

print(f"Resultado con lambda: {compleja(2, 3, 4)}")
print(f"Resultado con función tradicional: {suma_cuadrados_completa(2, 3, 4)}")
print("-" * 50)

"""
EJERCICIOS PROPUESTOS:

1. Escribe una función lambda que reciba una cadena de texto y retorne True si
   la cadena es un palíndromo (se lee igual de izquierda a derecha que de derecha
   a izquierda, ignorando espacios y mayúsculas/minúsculas), o False en caso
   contrario. Prueba la función con varias cadenas.

2. Crea una lista de diccionarios que representen productos con las claves
   'nombre', 'precio' y 'categoria'. Luego:
   a) Utiliza filter y lambda para obtener solo los productos de una categoría específica
   b) Utiliza map y lambda para aplicar un descuento del 10% a todos los productos
   c) Utiliza sorted y lambda para ordenar los productos por precio, de menor a mayor

3. Implementa una función llamada 'aplicar_operaciones' que reciba una lista de
   números y una lista de funciones lambda, y retorne un diccionario donde las
   claves sean los nombres descriptivos de las operaciones y los valores sean
   listas con los resultados de aplicar cada función a los números. Por ejemplo:
   ```
   numeros = [1, 2, 3, 4, 5]
   operaciones = {
       "cuadrados": lambda x: x**2,
       "cubos": lambda x: x**3,
       "raices": lambda x: x**0.5
   }
   resultado = aplicar_operaciones(numeros, operaciones)
   # Debería retornar:
   # {
   #     "cuadrados": [1, 4, 9, 16, 25],
   #     "cubos": [1, 8, 27, 64, 125],
   #     "raices": [1.0, 1.4142..., 1.7320..., 2.0, 2.2360...]
   # }
   ```
"""
