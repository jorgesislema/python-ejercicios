"""
Ejercicio 2: Parámetros y Argumentos en Funciones

Objetivo:
- Comprender los diferentes tipos de parámetros en Python
- Aprender a utilizar argumentos posicionales y nominales
- Entender el desempaquetado de colecciones como argumentos

En Python, existen diferentes formas de pasar argumentos a las funciones.
Los parámetros pueden ser posicionales, nominales, con valores por defecto,
o incluso un número variable de argumentos.
"""

# 1. Argumentos posicionales y nominales (keyword)
def describir_persona(nombre, edad, ciudad):
    """Describe a una persona usando los argumentos proporcionados.
    
    Args:
        nombre (str): El nombre de la persona
        edad (int): La edad de la persona
        ciudad (str): La ciudad donde vive la persona
    """
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")

print("1. Argumentos posicionales y nominales")
print("-" * 50)

# Uso de argumentos posicionales (por orden)
print("Argumentos posicionales:")
describir_persona("Carlos", 30, "Valencia")

# Uso de argumentos nominales (por nombre)
print("\nArgumentos nominales:")
describir_persona(edad=25, nombre="Laura", ciudad="Sevilla")

# Combinación de ambos (los posicionales primero)
print("\nCombinación de argumentos posicionales y nominales:")
describir_persona("Miguel", ciudad="Barcelona", edad=40)
print("-" * 50)

# 2. Parámetros con valores por defecto
def saludar(nombre, mensaje="¡Hola!", enfasis=False):
    """Saluda a una persona con un mensaje personalizable.
    
    Args:
        nombre (str): Nombre de la persona a saludar
        mensaje (str, optional): Mensaje de saludo. Por defecto "¡Hola!"
        enfasis (bool, optional): Indica si se añade énfasis. Por defecto False
    """
    if enfasis:
        print(f"{mensaje.upper()} {nombre.upper()}!!!")
    else:
        print(f"{mensaje} {nombre}.")

print("2. Parámetros con valores por defecto")
print("-" * 50)

saludar("Ana")  # Usa los valores por defecto
saludar("Pedro", "Buenos días")  # Personaliza el mensaje
saludar("María", "Bienvenida", True)  # Personaliza el mensaje y añade énfasis
saludar("Juan", enfasis=True)  # Usa valor por defecto para mensaje y personaliza énfasis
print("-" * 50)

# 3. Número variable de argumentos posicionales (*args)
def sumar(*numeros):
    """Suma un número variable de argumentos.
    
    Args:
        *numeros: Argumentos numéricos variables a sumar
        
    Returns:
        float o int: La suma de todos los números proporcionados
    """
    total = 0
    for numero in numeros:
        total += numero
    return total

print("3. Número variable de argumentos posicionales (*args)")
print("-" * 50)

print(f"Suma de 1, 2: {sumar(1, 2)}")
print(f"Suma de 1, 2, 3, 4, 5: {sumar(1, 2, 3, 4, 5)}")
print(f"Suma sin argumentos: {sumar()}")

# Desempaquetado de una lista como argumentos
numeros_lista = [10, 20, 30, 40]
print(f"Suma de {numeros_lista}: {sumar(*numeros_lista)}")
print("-" * 50)

# 4. Número variable de argumentos nominales (**kwargs)
def crear_perfil(**datos):
    """Crea un perfil de usuario con datos variables.
    
    Args:
        **datos: Pares clave-valor con los datos del perfil
        
    Returns:
        dict: Un diccionario con los datos del perfil
    """
    print("Perfil de usuario:")
    for clave, valor in datos.items():
        print(f"- {clave}: {valor}")
    return datos

print("4. Número variable de argumentos nominales (**kwargs)")
print("-" * 50)

crear_perfil(nombre="Ana", edad=28, profesion="Ingeniera", ciudad="Madrid")
print()
crear_perfil(usuario="jperez", email="jperez@ejemplo.com", activo=True)

# Desempaquetado de un diccionario como argumentos nominales
datos_usuario = {
    "nombre": "Carlos", 
    "apellido": "Gómez", 
    "rol": "Administrador",
    "departamento": "TI"
}
print()
crear_perfil(**datos_usuario)
print("-" * 50)

# 5. Combinación de diferentes tipos de parámetros
def configurar_aplicacion(nombre, version, *modulos, **ajustes):
    """Configura una aplicación con sus módulos y ajustes.
    
    Args:
        nombre (str): Nombre de la aplicación
        version (str): Versión de la aplicación
        *modulos: Módulos a incluir en la aplicación
        **ajustes: Ajustes de configuración de la aplicación
    """
    print(f"Configurando {nombre} v{version}")
    
    if modulos:
        print("Módulos activados:")
        for i, modulo in enumerate(modulos, 1):
            print(f"  {i}. {modulo}")
    else:
        print("No hay módulos activados.")
    
    if ajustes:
        print("Ajustes de configuración:")
        for clave, valor in ajustes.items():
            print(f"  - {clave}: {valor}")
    else:
        print("No hay ajustes personalizados.")

print("5. Combinación de diferentes tipos de parámetros")
print("-" * 50)

configurar_aplicacion(
    "MiApp", 
    "1.0.2", 
    "Estadísticas", 
    "Usuarios", 
    "Reportes", 
    debug=True, 
    tema="oscuro", 
    idioma="es"
)
print("-" * 50)

# 6. Parámetros posicionales obligatorios con /
def dividir(a, b, /):
    """Divide a entre b. Los parámetros son exclusivamente posicionales.
    
    Args:
        a: Dividendo
        b: Divisor
        
    Returns:
        float: El resultado de a/b
    """
    return a / b

print("6. Parámetros posicionales obligatorios con /")
print("-" * 50)

print(f"10 / 2 = {dividir(10, 2)}")  # Correcto: argumentos posicionales
# Error: dividir(a=10, b=2)  # Esto daría error porque no se permiten argumentos nominales
print("-" * 50)

# 7. Parámetros exclusivamente nominales con *
def calcular_promedio(*, num1, num2, num3):
    """Calcula el promedio de tres números. Parámetros exclusivamente nominales.
    
    Args:
        num1: Primer número
        num2: Segundo número
        num3: Tercer número
        
    Returns:
        float: El promedio de los tres números
    """
    return (num1 + num2 + num3) / 3

print("7. Parámetros exclusivamente nominales con *")
print("-" * 50)

print(f"Promedio: {calcular_promedio(num1=10, num2=20, num3=30)}")  # Correcto
# Error: calcular_promedio(10, 20, 30)  # Esto daría error porque requiere argumentos nominales
print("-" * 50)

# 8. Orden correcto de parámetros
def funcion_completa(pos1, pos2, /, pos_o_kw1, pos_o_kw2, *, kw1, kw2):
    """Ejemplo de función con todos los tipos de parámetros.
    
    Args:
        pos1, pos2: Parámetros exclusivamente posicionales
        pos_o_kw1, pos_o_kw2: Parámetros posicionales o nominales
        kw1, kw2: Parámetros exclusivamente nominales
    """
    print(f"Posicionales: {pos1}, {pos2}")
    print(f"Posicionales o nominales: {pos_o_kw1}, {pos_o_kw2}")
    print(f"Nominales: {kw1}, {kw2}")

print("8. Orden correcto de parámetros")
print("-" * 50)

funcion_completa(
    1, 2,                  # Posicionales obligatorios
    3, pos_o_kw2=4,        # Posicionales o nominales
    kw1="a", kw2="b"       # Nominales obligatorios
)
print("-" * 50)

"""
EJERCICIOS PROPUESTOS:

1. Crea una función llamada 'calcular_total_compra' que acepte un número variable
   de precios y un parámetro nominal 'descuento' (por defecto 0). La función debe
   devolver el precio total después de aplicar el descuento.

2. Implementa una función 'registrar_usuario' que reciba 'nombre' y 'email' como 
   parámetros posicionales obligatorios, y acepte un número variable de datos 
   adicionales como parámetros nominales. La función debe imprimir todos los datos
   del usuario en un formato organizado.

3. Crea una función 'construir_query' que acepte 'tabla' como parámetro posicional
   obligatorio, 'campos' como número variable de argumentos posicionales (por defecto
   selecciona '*'), y condiciones como número variable de argumentos nominales.
   La función debe retornar una cadena SQL. Por ejemplo:
   construir_query('usuarios', 'id', 'nombre', edad=18, ciudad='Madrid')
   debería retornar: "SELECT id, nombre FROM usuarios WHERE edad = 18 AND ciudad = 'Madrid'"
"""
