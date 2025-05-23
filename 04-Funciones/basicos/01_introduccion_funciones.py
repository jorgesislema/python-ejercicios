"""
Ejercicio 1: Introducción a las Funciones en Python

Objetivo:
- Comprender qué son las funciones en Python
- Aprender a definir y llamar funciones simples
- Entender el concepto de modularización de código

En Python, las funciones son bloques de código reutilizables que realizan una tarea específica.
Una función se define usando la palabra clave 'def', seguida del nombre de la función,
paréntesis (que pueden contener parámetros) y dos puntos. El cuerpo de la función debe estar indentado.
"""

# 1. Definición de una función simple sin parámetros
def saludar():
    """Esta función muestra un saludo en la consola."""
    print("¡Hola! Bienvenido a Python.")

# Llamada a la función
print("Ejemplo 1: Función simple sin parámetros")
saludar()
print("-" * 50)

# 2. Definición de una función con un parámetro
def saludar_persona(nombre):
    """Esta función saluda a una persona específica.
    
    Args:
        nombre (str): Nombre de la persona a saludar
    """
    print(f"¡Hola, {nombre}! Bienvenido a Python.")

# Llamada a la función con un argumento
print("Ejemplo 2: Función con un parámetro")
saludar_persona("Ana")
saludar_persona("Carlos")
print("-" * 50)

# 3. Función con múltiples parámetros
def presentar(nombre, edad, ciudad):
    """Esta función presenta a una persona con su información.
    
    Args:
        nombre (str): Nombre de la persona
        edad (int): Edad de la persona
        ciudad (str): Ciudad de residencia
    """
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")

# Llamada a la función con múltiples argumentos
print("Ejemplo 3: Función con múltiples parámetros")
presentar("Laura", 28, "Madrid")
presentar("Miguel", 34, "Barcelona")
print("-" * 50)

# 4. Función con valores por defecto
def describir_mascota(nombre, tipo="perro"):
    """Esta función describe una mascota.
    
    Args:
        nombre (str): Nombre de la mascota
        tipo (str, optional): Tipo de mascota. Por defecto es "perro".
    """
    print(f"{nombre} es un {tipo}.")

# Llamadas a la función con y sin el parámetro opcional
print("Ejemplo 4: Función con valores por defecto")
describir_mascota("Toby")  # Usa el valor por defecto "perro"
describir_mascota("Luna", "gato")  # Usa el valor proporcionado "gato"
print("-" * 50)

# 5. Función que retorna un valor
def sumar(a, b):
    """Esta función suma dos números y retorna el resultado.
    
    Args:
        a (int o float): Primer número
        b (int o float): Segundo número
        
    Returns:
        int o float: Suma de los dos números
    """
    resultado = a + b
    return resultado

# Llamada a la función y uso del valor retornado
print("Ejemplo 5: Función que retorna un valor")
suma = sumar(5, 3)
print(f"La suma de 5 y 3 es: {suma}")
print(f"Podemos usar el resultado para más operaciones: {suma * 2}")
print("-" * 50)

# 6. Función con docstring y anotaciones de tipo
def multiplicar(a: int, b: int) -> int:
    """Multiplica dos números enteros y retorna el resultado.
    
    Args:
        a: Primer número entero
        b: Segundo número entero
        
    Returns:
        El producto de a y b
    """
    return a * b

# Llamada a la función con anotaciones de tipo
print("Ejemplo 6: Función con docstring y anotaciones de tipo")
producto = multiplicar(4, 6)
print(f"El producto de 4 y 6 es: {producto}")
print("-" * 50)

# 7. Importancia de la modularización
def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo.
    
    Args:
        base (float): La base del rectángulo
        altura (float): La altura del rectángulo
        
    Returns:
        float: El área del rectángulo
    """
    return base * altura

def calcular_perimetro_rectangulo(base, altura):
    """Calcula el perímetro de un rectángulo.
    
    Args:
        base (float): La base del rectángulo
        altura (float): La altura del rectángulo
        
    Returns:
        float: El perímetro del rectángulo
    """
    return 2 * (base + altura)

print("Ejemplo 7: Modularización con funciones")
base_rectangulo = 5
altura_rectangulo = 3
area = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
perimetro = calcular_perimetro_rectangulo(base_rectangulo, altura_rectangulo)
print(f"Un rectángulo de base {base_rectangulo} y altura {altura_rectangulo}:")
print(f"- Área: {area}")
print(f"- Perímetro: {perimetro}")
print("-" * 50)

"""
EJERCICIOS PROPUESTOS:

1. Escribe una función llamada 'saludar_hora' que reciba un parámetro 'hora' (un entero de 0 a 23)
   y muestre un saludo diferente según la hora del día:
   - Entre 5 y 12: "¡Buenos días!"
   - Entre 13 y 19: "¡Buenas tardes!"
   - Resto: "¡Buenas noches!"

2. Crea una función llamada 'calcular_precio_final' que reciba dos parámetros:
   - precio_base: el precio base de un producto
   - descuento: el porcentaje de descuento a aplicar (por defecto 0)
   La función debe retornar el precio final después de aplicar el descuento.

3. Escribe una función llamada 'mostrar_info_persona' que reciba parámetros para nombre,
   edad y profesión (con valor por defecto "No especificada"), y muestre un mensaje 
   con toda la información. Llama a la función con diferentes combinaciones de argumentos.
"""
