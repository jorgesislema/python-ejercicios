"""
Ejercicio 1: Decoradores en Python

Objetivo:
- Comprender qué son los decoradores y cómo funcionan
- Aprender a crear y utilizar decoradores
- Aplicar decoradores para extender la funcionalidad de funciones
- Implementar decoradores con parámetros

Los decoradores son una característica poderosa de Python que permite modificar o
extender el comportamiento de funciones o métodos sin cambiar su código interno.
Son funciones que toman otra función como argumento y retornan una nueva función.
"""

# 1. Fundamentos de los decoradores
print("1. Fundamentos de los decoradores")
print("-" * 50)

# Función de ejemplo que vamos a decorar
def saludar(nombre):
    """Saluda a una persona."""
    return f"Hola, {nombre}!"

# Decorador simple
def decorador_simple(funcion):
    """Decorador que añade un mensaje adicional."""
    def funcion_decorada(nombre):
        # Llamar a la función original
        mensaje_original = funcion(nombre)
        # Añadir el mensaje adicional
        mensaje_modificado = mensaje_original + " ¡Bienvenido!"
        return mensaje_modificado
    
    # Preservar los metadatos de la función original
    funcion_decorada.__name__ = funcion.__name__
    funcion_decorada.__doc__ = funcion.__doc__
    
    return funcion_decorada

# Aplicar el decorador manualmente
saludar_decorada = decorador_simple(saludar)

# Demostración
print("Función original:")
print(saludar("Ana"))

print("\nFunción decorada manualmente:")
print(saludar_decorada("Ana"))
print("-" * 50)

# 2. Sintaxis de decoradores con @
print("2. Sintaxis de decoradores con @")
print("-" * 50)

# Definir un decorador
def destacar(funcion):
    """Decorador que destaca el mensaje de una función."""
    def wrapper(nombre):
        resultado = funcion(nombre)
        return f"*** {resultado} ***"
    
    return wrapper

# Aplicar el decorador con la sintaxis @
@destacar
def bienvenida(nombre):
    """Da la bienvenida a un usuario."""
    return f"Bienvenido/a, {nombre}"

# La sintaxis @destacar es equivalente a:
# bienvenida = destacar(bienvenida)

# Demostración
print("Función decorada con @:")
print(bienvenida("Carlos"))
print("-" * 50)

# 3. Decoradores con functools.wraps
print("3. Decoradores con functools.wraps")
print("-" * 50)

import functools

def decorador_con_wraps(funcion):
    """Decorador que preserva los metadatos de la función decorada."""
    @functools.wraps(funcion)  # Preserva metadatos automáticamente
    def wrapper(*args, **kwargs):
        """Función interna del decorador."""
        print(f"Llamando a la función {funcion.__name__}")
        resultado = funcion(*args, **kwargs)
        print(f"La función {funcion.__name__} ha finalizado")
        return resultado
    
    return wrapper

@decorador_con_wraps
def sumar(a, b):
    """Suma dos números."""
    return a + b

# Demostración
print("Usando functools.wraps:")
print(f"Nombre de la función: {sumar.__name__}")
print(f"Docstring: {sumar.__doc__}")

print("\nEjecutando la función decorada:")
resultado = sumar(5, 3)
print(f"Resultado: {resultado}")
print("-" * 50)

# 4. Decoradores con argumentos
print("4. Decoradores con argumentos")
print("-" * 50)

def repetir(n=1):
    """Decorador que repite la ejecución de una función n veces.
    
    Args:
        n (int): Número de veces que se repetirá la función
    """
    def decorador(funcion):
        @functools.wraps(funcion)
        def wrapper(*args, **kwargs):
            resultados = []
            for _ in range(n):
                resultados.append(funcion(*args, **kwargs))
            return resultados
        return wrapper
    return decorador

@repetir(n=3)
def saludar_repetido(nombre):
    """Saluda a una persona."""
    return f"Hola, {nombre}!"

# Demostración
print("Decorador con argumentos:")
print(saludar_repetido("Pedro"))
print("-" * 50)

# 5. Múltiples decoradores
print("5. Múltiples decoradores")
print("-" * 50)

def convertir_a_mayusculas(funcion):
    """Decorador que convierte el resultado a mayúsculas."""
    @functools.wraps(funcion)
    def wrapper(*args, **kwargs):
        resultado = funcion(*args, **kwargs)
        return resultado.upper()
    return wrapper

def agregar_prefijo(prefijo):
    """Decorador que agrega un prefijo al resultado."""
    def decorador(funcion):
        @functools.wraps(funcion)
        def wrapper(*args, **kwargs):
            resultado = funcion(*args, **kwargs)
            return f"{prefijo}: {resultado}"
        return wrapper
    return decorador

# Aplicar múltiples decoradores (se aplican de abajo hacia arriba)
@convertir_a_mayusculas
@agregar_prefijo("Mensaje")
def mensaje_personal(nombre):
    """Crea un mensaje personalizado."""
    return f"Este mensaje es para {nombre}"

# Demostración
print("Múltiples decoradores:")
print(mensaje_personal("Laura"))
print("-" * 50)

# 6. Decoradores para temporización
print("6. Decoradores para temporización")
print("-" * 50)

import time

def medir_tiempo(funcion):
    """Decorador que mide el tiempo de ejecución de una función."""
    @functools.wraps(funcion)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"La función {funcion.__name__} tardó {fin - inicio:.6f} segundos en ejecutarse")
        return resultado
    return wrapper

@medir_tiempo
def esperar(segundos):
    """Función que espera un número de segundos."""
    time.sleep(segundos)
    return f"Esperé {segundos} segundos"

# Demostración
print("Decorador para medir tiempo:")
print(esperar(1))
print("-" * 50)

# 7. Decoradores para registro (logging)
print("7. Decoradores para registro (logging)")
print("-" * 50)

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def registrar(funcion):
    """Decorador que registra llamadas a funciones."""
    @functools.wraps(funcion)
    def wrapper(*args, **kwargs):
        args_str = ', '.join(map(str, args))
        kwargs_str = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        all_args = f"{args_str}{', ' if args and kwargs else ''}{kwargs_str}"
        
        logging.info(f"Llamando a {funcion.__name__}({all_args})")
        try:
            resultado = funcion(*args, **kwargs)
            logging.info(f"{funcion.__name__} retornó: {resultado}")
            return resultado
        except Exception as e:
            logging.error(f"Error en {funcion.__name__}: {e}")
            raise
    return wrapper

@registrar
def dividir(a, b):
    """Divide dos números."""
    return a / b

# Demostración
print("Decorador para registro:")
try:
    print(f"10 / 2 = {dividir(10, 2)}")
    print(f"10 / 0 = {dividir(10, 0)}")
except Exception as e:
    print(f"Se capturó una excepción: {e}")
print("-" * 50)

# 8. Decoradores de clase
print("8. Decoradores de clase")
print("-" * 50)

def agregar_metodos(cls):
    """Decorador que agrega métodos a una clase."""
    def saludar(self):
        return f"Hola, soy {self.nombre}"
    
    def describir(self):
        return f"{self.nombre} es una instancia de {cls.__name__}"
    
    # Agregar los métodos a la clase
    cls.saludar = saludar
    cls.describir = describir
    
    return cls

@agregar_metodos
class Persona:
    """Clase que representa a una persona."""
    def __init__(self, nombre):
        self.nombre = nombre

# Demostración
print("Decorador de clase:")
persona = Persona("Elena")
print(persona.saludar())
print(persona.describir())
print("-" * 50)

# 9. Decoradores con estado
print("9. Decoradores con estado")
print("-" * 50)

def contador_llamadas(funcion):
    """Decorador que cuenta las veces que se llama a una función."""
    # Variable para almacenar el estado (contador)
    contador = 0
    
    @functools.wraps(funcion)
    def wrapper(*args, **kwargs):
        # Usar la variable definida en el ámbito externo
        nonlocal contador
        contador += 1
        print(f"La función {funcion.__name__} ha sido llamada {contador} veces")
        return funcion(*args, **kwargs)
    
    # Añadir el contador como atributo de la función decorada
    wrapper.contador = lambda: contador
    
    return wrapper

@contador_llamadas
def decir_hola():
    """Dice hola."""
    return "¡Hola!"

# Demostración
print("Decorador con estado:")
print(decir_hola())
print(decir_hola())
print(decir_hola())
print(f"Contador desde el atributo: {decir_hola.contador()}")
print("-" * 50)

# 10. Aplicaciones prácticas de los decoradores
print("10. Aplicaciones prácticas de los decoradores")
print("-" * 50)

# Decorador para caché (memoización)
def memoizar(funcion):
    """Decorador que implementa memoización para funciones."""
    cache = {}
    
    @functools.wraps(funcion)
    def wrapper(*args):
        # Solo funciona con argumentos inmutables
        if args not in cache:
            cache[args] = funcion(*args)
        return cache[args]
    
    # Agregar función para ver el estado del caché
    wrapper.ver_cache = lambda: cache
    
    return wrapper

@memoizar
def fibonacci(n):
    """Calcula el n-ésimo número de Fibonacci."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Demostración
print("Decorador para memoización:")
print(f"fibonacci(10) = {fibonacci(10)}")
print(f"fibonacci(20) = {fibonacci(20)}")
print(f"Estado del caché: {fibonacci.ver_cache()}")
print("-" * 50)

# Decorador para control de acceso
def requiere_autenticacion(nivel_acceso=1):
    """Decorador que verifica el nivel de acceso antes de ejecutar la función."""
    def decorador(funcion):
        @functools.wraps(funcion)
        def wrapper(usuario, *args, **kwargs):
            if not usuario.get("autenticado", False):
                return "Acceso denegado: Usuario no autenticado"
            
            if usuario.get("nivel", 0) < nivel_acceso:
                return f"Acceso denegado: Se requiere nivel de acceso {nivel_acceso}"
            
            return funcion(usuario, *args, **kwargs)
        return wrapper
    return decorador

@requiere_autenticacion(nivel_acceso=2)
def acceder_area_admin(usuario):
    """Accede al área de administración."""
    return f"Bienvenido al área de administración, {usuario['nombre']}"

# Demostración
usuarios = [
    {"nombre": "Invitado", "autenticado": False, "nivel": 0},
    {"nombre": "Usuario", "autenticado": True, "nivel": 1},
    {"nombre": "Admin", "autenticado": True, "nivel": 3}
]

print("Decorador para control de acceso:")
for usuario in usuarios:
    print(f"{usuario['nombre']}: {acceder_area_admin(usuario)}")
print("-" * 50)

"""
EJERCICIOS PROPUESTOS:

1. Crea un decorador 'validar_tipos' que verifique que los argumentos pasados a una 
   función sean del tipo esperado. El decorador debe recibir como parámetros los tipos
   esperados para cada argumento. Si algún argumento no coincide con el tipo esperado,
   debe lanzar una excepción TypeError con un mensaje informativo.

2. Implementa un decorador 'reintentar' que permita ejecutar una función varias veces
   en caso de que lance una excepción. El decorador debe aceptar los siguientes parámetros:
   - max_intentos: número máximo de intentos (por defecto 3)
   - excepciones: tupla de excepciones a capturar (por defecto Exception)
   - delay: tiempo de espera entre intentos en segundos (por defecto 0)

3. Crea un sistema de decoradores para un framework web simple que incluya:
   - Un decorador 'ruta' que asocie una función a una URL
   - Un decorador 'metodo' que restrinja la función a ciertos métodos HTTP (GET, POST, etc.)
   - Un decorador 'json_response' que convierta el retorno de la función a formato JSON
   Luego, demuestra cómo se usarían estos decoradores juntos para definir endpoints de API.
"""
