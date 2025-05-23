"""
Ejercicio 5: Documentación de Funciones

Objetivo:
- Aprender a documentar funciones usando docstrings
- Entender los diferentes formatos de documentación (Google, Numpy, reStructuredText)
- Utilizar anotaciones de tipos
- Conocer las herramientas para generar documentación

La documentación adecuada es esencial para crear código mantenible y 
comprensible para otros programadores (incluso para ti mismo en el futuro).
Python permite documentar funciones mediante docstrings y anotaciones de tipos.
"""

# 1. Docstrings básicos
print("1. Docstrings básicos")
print("-" * 50)

def suma(a, b):
    """Suma dos números y retorna el resultado.
    
    Esta función toma dos números como entrada y retorna su suma.
    """
    return a + b

# Acceder a la documentación
print("Documentación de la función suma:")
print(suma.__doc__)
print("-" * 50)

# 2. Formato de documentación estilo Google
print("2. Formato de documentación estilo Google")
print("-" * 50)

def calcular_promedio(numeros):
    """Calcula el promedio de una lista de números.
    
    Esta función recibe una lista de números, suma todos los valores
    y divide entre la cantidad de elementos para obtener el promedio.
    
    Args:
        numeros (list): Una lista de números (int o float)
    
    Returns:
        float: El promedio de los números en la lista
        
    Raises:
        ValueError: Si la lista está vacía
        TypeError: Si la lista contiene elementos no numéricos
    
    Examples:
        >>> calcular_promedio([1, 2, 3, 4, 5])
        3.0
        >>> calcular_promedio([10, 20])
        15.0
    """
    if not numeros:
        raise ValueError("La lista no puede estar vacía")
    
    # Verifica que todos los elementos son numéricos
    for num in numeros:
        if not isinstance(num, (int, float)):
            raise TypeError(f"Todos los elementos deben ser numéricos, encontrado: {type(num)}")
    
    return sum(numeros) / len(numeros)

# Mostrar documentación
print("Documentación de calcular_promedio:")
print(calcular_promedio.__doc__)
print("-" * 50)

# 3. Formato de documentación estilo NumPy
print("3. Formato de documentación estilo NumPy")
print("-" * 50)

def calcular_estadisticas(numeros):
    """
    Calcula estadísticas básicas de una lista de números.
    
    Calcula la suma, el promedio, el mínimo y el máximo de una lista de números.
    
    Parameters
    ----------
    numeros : list
        Una lista de números (int o float).
        
    Returns
    -------
    dict
        Un diccionario con las siguientes claves:
        - suma : float
            La suma de todos los números.
        - promedio : float
            El promedio de los números.
        - minimo : float
            El valor mínimo en la lista.
        - maximo : float
            El valor máximo en la lista.
            
    Raises
    ------
    ValueError
        Si la lista está vacía.
    
    Examples
    --------
    >>> calcular_estadisticas([1, 2, 3, 4, 5])
    {'suma': 15, 'promedio': 3.0, 'minimo': 1, 'maximo': 5}
    """
    if not numeros:
        raise ValueError("La lista no puede estar vacía")
    
    suma = sum(numeros)
    promedio = suma / len(numeros)
    minimo = min(numeros)
    maximo = max(numeros)
    
    return {
        "suma": suma,
        "promedio": promedio,
        "minimo": minimo,
        "maximo": maximo
    }

# Mostrar documentación
print("Documentación de calcular_estadisticas:")
print(calcular_estadisticas.__doc__)
print("-" * 50)

# 4. Formato de documentación estilo reStructuredText (Sphinx)
print("4. Formato de documentación estilo reStructuredText (Sphinx)")
print("-" * 50)

def filtrar_numeros(numeros, condicion):
    """
    Filtra una lista de números según una condición.
    
    :param numeros: Una lista de números a filtrar
    :type numeros: list
    :param condicion: Una función que define la condición de filtrado
    :type condicion: callable
    
    :returns: Una nueva lista con los números que cumplen la condición
    :rtype: list
    
    :raises TypeError: Si el segundo argumento no es una función
    
    :example:
    
    >>> filtrar_numeros([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
    [2, 4]
    """
    if not callable(condicion):
        raise TypeError("El segundo argumento debe ser una función")
    
    return [num for num in numeros if condicion(num)]

# Mostrar documentación
print("Documentación de filtrar_numeros:")
print(filtrar_numeros.__doc__)
print("-" * 50)

# 5. Anotaciones de tipos
print("5. Anotaciones de tipos")
print("-" * 50)

from typing import List, Dict, Union, Optional, Callable

def procesar_datos(
    datos: List[int],
    factor: float = 1.0,
    aplicar_funcion: Optional[Callable[[int], int]] = None
) -> Dict[str, Union[List[int], float]]:
    """
    Procesa una lista de datos aplicando un factor y opcionalmente una función.
    
    Args:
        datos: Lista de enteros a procesar
        factor: Factor de multiplicación (por defecto 1.0)
        aplicar_funcion: Función opcional para aplicar a cada elemento
        
    Returns:
        Diccionario con los resultados procesados y estadísticas
    """
    if aplicar_funcion:
        datos_procesados = [aplicar_funcion(item) for item in datos]
    else:
        datos_procesados = datos.copy()
    
    # Aplicar factor
    datos_con_factor = [item * factor for item in datos_procesados]
    promedio = sum(datos_con_factor) / len(datos_con_factor) if datos_con_factor else 0
    
    return {
        "datos_originales": datos,
        "datos_procesados": datos_procesados,
        "datos_con_factor": datos_con_factor,
        "promedio": promedio
    }

# Usar la función
numeros = [1, 2, 3, 4, 5]
resultado = procesar_datos(numeros, 2.0, lambda x: x * x)

print("Resultado de procesar_datos:")
for clave, valor in resultado.items():
    print(f"- {clave}: {valor}")

# Mostrar anotaciones de tipos
print("\nAnotaciones de tipos:")
for param, tipo in procesar_datos.__annotations__.items():
    if param == 'return':
        print(f"- Retorno: {tipo}")
    else:
        print(f"- {param}: {tipo}")
print("-" * 50)

# 6. Documentación en módulos y paquetes
print("6. Documentación en módulos y paquetes")
print("-" * 50)

# Ejemplo de docstring a nivel de módulo:
"""
Módulo de utilidades matemáticas

Este módulo contiene funciones para realizar operaciones matemáticas comunes
y procesamiento de datos numéricos.

Contiene las siguientes funciones:
- suma: Suma dos números
- calcular_promedio: Calcula el promedio de una lista de números
- calcular_estadisticas: Calcula estadísticas básicas de una lista de números
- filtrar_numeros: Filtra números según una condición
- procesar_datos: Procesa datos aplicando factores y funciones

Ejemplos:
    >>> from mi_modulo_matematicas import suma
    >>> suma(5, 3)
    8
"""

print("Docstring a nivel de módulo se colocaría al principio del archivo.")
print("Estos docstrings describen el propósito general del módulo/paquete.")
print("Se accede mediante la propiedad __doc__ del módulo importado.")
print("-" * 50)

# 7. Herramientas para generar documentación
print("7. Herramientas para generar documentación")
print("-" * 50)

print("Python ofrece varias herramientas para generar documentación a partir de docstrings:")
print("- help(): Función integrada para ver documentación en la consola")
print("- pydoc: Módulo para generar documentación en formato texto o HTML")
print("- Sphinx: Sistema de documentación que genera HTML, PDF, etc.")
print("- MkDocs: Generador de sitios de documentación a partir de Markdown")
print("- pdoc: Generador de documentación simple y moderno")

print("\nEjemplo de uso de help():")
help(calcular_promedio)
print("-" * 50)

# 8. Mejores prácticas para documentar funciones
print("8. Mejores prácticas para documentar funciones")
print("-" * 50)

print("Recomendaciones para documentar funciones en Python:")
print("1. Mantén un estilo consistente en todo el proyecto")
print("2. Documenta todas las funciones públicas")
print("3. Describe qué hace la función, no cómo lo hace")
print("4. Incluye ejemplos de uso cuando sea posible")
print("5. Documenta los parámetros, valores de retorno y excepciones")
print("6. Usa anotaciones de tipos para mejorar la claridad")
print("7. Mantén la documentación actualizada cuando cambies el código")
print("8. No repitas información obvia (evita redundancia)")
print("-" * 50)

"""
EJERCICIOS PROPUESTOS:

1. Crea una función llamada 'validar_email' que verifique si un email es válido. 
   La función debe tener un docstring completo en formato Google que incluya:
   - Descripción de la función
   - Parámetros
   - Valor de retorno
   - Excepciones que puede lanzar
   - Al menos un ejemplo de uso
   Además, añade anotaciones de tipos.

2. Escribe una función 'generar_tabla_multiplicar' que genere la tabla de 
   multiplicar de un número hasta cierto límite. Usa el formato de documentación 
   NumPy y añade anotaciones de tipos. Incluye ejemplos en la documentación.

3. Documenta las tres funciones que implementaste en los ejercicios anteriores
   usando el formato reStructuredText. Asegúrate de incluir toda la información
   necesaria: parámetros, valores de retorno, excepciones y ejemplos.
"""
