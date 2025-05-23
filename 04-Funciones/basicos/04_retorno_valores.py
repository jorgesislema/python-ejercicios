"""
Ejercicio 4: Retorno de Valores en Funciones

Objetivo:
- Aprender los diferentes métodos para retornar valores en funciones
- Comprender el retorno de múltiples valores
- Entender cuándo y cómo utilizar valores de retorno
- Aprender a usar el valor de retorno None

En Python, las funciones pueden retornar valores utilizando la palabra clave 'return'.
Una función puede retornar cualquier tipo de dato, incluidos múltiples valores
separados por comas, o incluso no retornar nada (None).
"""

# 1. Funciones que retornan un valor simple
print("1. Funciones que retornan un valor simple")
print("-" * 50)

def calcular_area_circulo(radio):
    """Calcula el área de un círculo.
    
    Args:
        radio (float): Radio del círculo
        
    Returns:
        float: El área del círculo
    """
    pi = 3.14159
    area = pi * radio ** 2
    return area

radio = 5
area = calcular_area_circulo(radio)
print(f"El área de un círculo con radio {radio} es: {area:.2f}")

# Función que retorna un valor booleano
def es_par(numero):
    """Determina si un número es par.
    
    Args:
        numero (int): Número a evaluar
        
    Returns:
        bool: True si el número es par, False de lo contrario
    """
    return numero % 2 == 0

numero = 7
print(f"¿El número {numero} es par? {es_par(numero)}")
print("-" * 50)

# 2. Funciones que retornan múltiples valores
print("2. Funciones que retornan múltiples valores")
print("-" * 50)

def calcular_estadisticas(numeros):
    """Calcula varias estadísticas de una lista de números.
    
    Args:
        numeros (list): Lista de números
        
    Returns:
        tuple: Una tupla con (suma, promedio, mínimo, máximo)
    """
    suma = sum(numeros)
    promedio = suma / len(numeros)
    minimo = min(numeros)
    maximo = max(numeros)
    # Retorna múltiples valores separados por comas
    return suma, promedio, minimo, maximo

datos = [4, 8, 15, 16, 23, 42]
# Desempaquetado de valores retornados
suma, promedio, minimo, maximo = calcular_estadisticas(datos)

print(f"Lista de datos: {datos}")
print(f"- Suma: {suma}")
print(f"- Promedio: {promedio:.2f}")
print(f"- Mínimo: {minimo}")
print(f"- Máximo: {maximo}")

# También se puede capturar como una tupla
resultados = calcular_estadisticas(datos)
print(f"\nResultados como tupla: {resultados}")
print(f"Tipo de resultados: {type(resultados)}")
print("-" * 50)

# 3. Retorno de estructuras de datos complejas
print("3. Retorno de estructuras de datos complejas")
print("-" * 50)

def analizar_texto(texto):
    """Analiza un texto y retorna estadísticas en un diccionario.
    
    Args:
        texto (str): Texto a analizar
        
    Returns:
        dict: Diccionario con varias estadísticas del texto
    """
    palabras = texto.lower().split()
    caracteres = len(texto)
    palabras_unicas = len(set(palabras))
    frecuencia = {}
    
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    # Ordenar por frecuencia (mayor a menor)
    palabras_comunes = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)[:3]
    
    # Retorna un diccionario con los resultados
    return {
        "num_caracteres": caracteres,
        "num_palabras": len(palabras),
        "palabras_unicas": palabras_unicas,
        "palabras_mas_comunes": palabras_comunes
    }

texto_ejemplo = """
Python es un lenguaje de programación de alto nivel que se utiliza para 
desarrollar aplicaciones de todo tipo. Python es interpretado, interactivo, 
orientado a objetos y de código abierto. Python es simple pero efectivo.
"""

analisis = analizar_texto(texto_ejemplo)
print("Análisis de texto:")
print(f"- Caracteres: {analisis['num_caracteres']}")
print(f"- Palabras: {analisis['num_palabras']}")
print(f"- Palabras únicas: {analisis['palabras_unicas']}")
print("- Palabras más comunes:")
for palabra, frecuencia in analisis["palabras_mas_comunes"]:
    print(f"  * '{palabra}': {frecuencia} veces")
print("-" * 50)

# 4. Retorno condicional
print("4. Retorno condicional")
print("-" * 50)

def calcular_division(a, b):
    """Calcula la división entre dos números con manejo de error.
    
    Args:
        a (float): Dividendo
        b (float): Divisor
        
    Returns:
        float o None: Resultado de la división o None si hay división por cero
    """
    if b == 0:
        print("Error: División por cero no permitida")
        return None
    return a / b

print(f"10 / 2 = {calcular_division(10, 2)}")
print(f"10 / 0 = {calcular_division(10, 0)}")

# Verificación del valor de retorno
resultado = calcular_division(20, 5)
if resultado is not None:
    print(f"El resultado es: {resultado}")
else:
    print("No se pudo calcular el resultado.")
print("-" * 50)

# 5. Uso del valor de retorno None
print("5. Uso del valor de retorno None")
print("-" * 50)

def saludar_usuario(nombre):
    """Imprime un saludo al usuario.
    
    Args:
        nombre (str): Nombre del usuario
    
    Returns:
        None: Esta función no retorna ningún valor explícitamente
    """
    print(f"¡Hola, {nombre}!")
    # Sin return, implícitamente retorna None

valor_retorno = saludar_usuario("Elena")
print(f"Valor retornado por la función: {valor_retorno}")
print(f"Tipo del valor retornado: {type(valor_retorno)}")

# Función que explícitamente retorna None
def validar_edad(edad):
    """Valida que la edad sea apropiada.
    
    Args:
        edad (int): Edad a validar
        
    Returns:
        None: Si la edad es válida
        str: Mensaje de error si la edad no es válida
    """
    if edad < 0:
        return "La edad no puede ser negativa"
    if edad > 150:
        return "La edad parece demasiado alta"
    # Si la edad es válida, no retorna ningún mensaje de error
    return None

edad = 25
error = validar_edad(edad)
if error is None:
    print(f"La edad {edad} es válida.")
else:
    print(f"Error: {error}")

edad_invalida = -5
error = validar_edad(edad_invalida)
if error is None:
    print(f"La edad {edad_invalida} es válida.")
else:
    print(f"Error: {error}")
print("-" * 50)

# 6. Retorno temprano en funciones
print("6. Retorno temprano en funciones")
print("-" * 50)

def verificar_acceso(usuario, nivel_acceso):
    """Verifica si un usuario tiene acceso a cierto nivel.
    
    Args:
        usuario (dict): Datos del usuario
        nivel_acceso (int): Nivel de acceso requerido
        
    Returns:
        bool: True si tiene acceso, False si no
    """
    # Verificación de usuario activo
    if not usuario.get("activo", False):
        print(f"Usuario {usuario['nombre']} no está activo")
        return False
    
    # Verificación de nivel de acceso
    if usuario.get("nivel", 0) < nivel_acceso:
        print(f"Usuario {usuario['nombre']} no tiene suficiente nivel de acceso")
        return False
    
    # Si pasa todas las verificaciones
    print(f"Usuario {usuario['nombre']} tiene acceso autorizado")
    return True

usuario1 = {"nombre": "Ana", "activo": True, "nivel": 5}
usuario2 = {"nombre": "Juan", "activo": False, "nivel": 3}
usuario3 = {"nombre": "Pedro", "activo": True, "nivel": 2}

print("Verificando acceso nivel 3:")
verificar_acceso(usuario1, 3)  # Debería tener acceso
verificar_acceso(usuario2, 3)  # No está activo
verificar_acceso(usuario3, 3)  # Nivel insuficiente
print("-" * 50)

# 7. Uso de retorno para generar secuencias
print("7. Uso de retorno para generar secuencias")
print("-" * 50)

def fibonacci(n):
    """Genera los primeros n números de la secuencia de Fibonacci.
    
    Args:
        n (int): Cantidad de números a generar
        
    Returns:
        list: Lista con los primeros n números de Fibonacci
    """
    if n <= 0:
        return []
    
    if n == 1:
        return [0]
    
    # Inicializa con los dos primeros números
    secuencia = [0, 1]
    
    # Genera el resto de la secuencia
    while len(secuencia) < n:
        siguiente = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente)
    
    return secuencia

print("Secuencia de Fibonacci:")
for n in range(1, 11):
    print(f"Fibonacci({n}): {fibonacci(n)}")
print("-" * 50)

"""
EJERCICIOS PROPUESTOS:

1. Crea una función 'calcular_precio_final' que reciba el precio base de un producto 
   y el código de descuento (opcional). La función debe retornar una tupla con 
   (precio_final, descuento_aplicado, mensaje). Si el código es 'PROMO10', aplicar 10% 
   de descuento; si es 'PROMO20', aplicar 20%; si no es válido, no aplicar descuento
   y devolver un mensaje adecuado.

2. Escribe una función 'analizar_calificaciones' que reciba una lista de calificaciones
   y retorne un diccionario con las siguientes estadísticas: promedio, calificación más
   alta, calificación más baja, cantidad de aprobados (>=60) y cantidad de reprobados.

3. Implementa una función 'validar_usuario' que reciba un diccionario con datos de 
   usuario (nombre, email, contraseña) y verifique que todos los campos sean válidos.
   Si hay errores, debe retornar una lista con mensajes de error. Si todo es correcto,
   debe retornar None. Validaciones:
   - El nombre debe tener al menos 3 caracteres
   - El email debe contener '@' y '.'
   - La contraseña debe tener al menos 8 caracteres y un número
"""
