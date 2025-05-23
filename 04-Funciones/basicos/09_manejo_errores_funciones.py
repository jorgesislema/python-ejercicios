"""
Ejercicio 9: Manejo de Errores en Funciones

Objetivo:
- Aprender a gestionar y manejar errores en funciones
- Utilizar try-except para capturar excepciones
- Crear excepciones personalizadas
- Utilizar cláusulas else y finally
- Implementar validación de argumentos

El manejo de errores es una parte crucial de la programación que permite
que nuestros programas sean más robustos y puedan recuperarse de situaciones inesperadas.
"""

# 1. Estructura básica de try-except
print("1. Estructura básica de try-except")
print("-" * 50)

def dividir(a, b):
    """Divide dos números con manejo de errores básico.
    
    Args:
        a (float): Dividendo
        b (float): Divisor
        
    Returns:
        float: Resultado de la división
    """
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: No es posible dividir por cero")
        return None

# Probar la función
print(f"10 / 2 = {dividir(10, 2)}")
print(f"10 / 0 = {dividir(10, 0)}")
print("-" * 50)

# 2. Capturar múltiples excepciones
print("2. Capturar múltiples excepciones")
print("-" * 50)

def calcular_promedio(lista):
    """Calcula el promedio de una lista de números.
    
    Args:
        lista (list): Lista de números
        
    Returns:
        float: Promedio de los números
    """
    try:
        return sum(lista) / len(lista)
    except TypeError:
        print("Error: La lista contiene elementos no numéricos")
        return None
    except ZeroDivisionError:
        print("Error: La lista está vacía")
        return None

# Probar con diferentes casos
print(f"Promedio de [1, 2, 3, 4, 5]: {calcular_promedio([1, 2, 3, 4, 5])}")
print(f"Promedio de [1, 2, '3', 4, 5]: {calcular_promedio([1, 2, '3', 4, 5])}")
print(f"Promedio de []: {calcular_promedio([])}")
print("-" * 50)

# 3. Usando else y finally
print("3. Usando else y finally")
print("-" * 50)

def leer_archivo(nombre_archivo):
    """Lee el contenido de un archivo y cuenta las líneas.
    
    Args:
        nombre_archivo (str): Ruta al archivo a leer
        
    Returns:
        int: Número de líneas en el archivo, o None si hay error
    """
    archivo = None
    try:
        archivo = open(nombre_archivo, 'r')
        lineas = archivo.readlines()
        num_lineas = len(lineas)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe")
        return None
    except PermissionError:
        print(f"Error: No tiene permisos para leer '{nombre_archivo}'")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None
    else:
        print(f"Archivo leído correctamente: {nombre_archivo}")
        return num_lineas
    finally:
        if archivo:
            archivo.close()
            print("Archivo cerrado correctamente")

# En lugar de un archivo real, usaremos un ejemplo simulado
print("Simulación de lectura de archivos:")
print(f"Resultado para 'archivo_existente.txt': {leer_archivo('archivo_existente.txt')}")
print(f"Resultado para 'archivo_inexistente.txt': {leer_archivo('archivo_inexistente.txt')}")
print("-" * 50)

# 4. Capturar y re-lanzar excepciones
print("4. Capturar y re-lanzar excepciones")
print("-" * 50)

def raiz_cuadrada(numero):
    """Calcula la raíz cuadrada de un número.
    
    Args:
        numero (float): Número para calcular su raíz cuadrada
        
    Returns:
        float: Raíz cuadrada del número
        
    Raises:
        ValueError: Si el número es negativo
    """
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return numero ** 0.5

def calcular_estadisticas(numeros):
    """Calcula estadísticas de una lista de números, incluyendo raíces cuadradas.
    
    Args:
        numeros (list): Lista de números
        
    Returns:
        dict: Diccionario con estadísticas
    """
    resultados = {}
    
    try:
        resultados['promedio'] = sum(numeros) / len(numeros)
        
        raices = []
        for num in numeros:
            try:
                raiz = raiz_cuadrada(num)
                raices.append(raiz)
            except ValueError as e:
                print(f"Advertencia: {e} para el número {num}")
                raices.append(None)
        
        resultados['raices'] = raices
        
    except Exception as e:
        print(f"Error en el cálculo de estadísticas: {e}")
        raise  # Re-lanzar la excepción
    
    return resultados

# Probar la función
try:
    numeros = [16, 9, 4, -1, 25]
    print(f"Lista de números: {numeros}")
    estadisticas = calcular_estadisticas(numeros)
    print(f"Estadísticas: {estadisticas}")
except Exception as e:
    print(f"Error capturado en el programa principal: {e}")
print("-" * 50)

# 5. Excepciones personalizadas
print("5. Excepciones personalizadas")
print("-" * 50)

class EdadInvalidaError(Exception):
    """Excepción personalizada para edades inválidas."""
    pass

class SalarioInvalidoError(Exception):
    """Excepción personalizada para salarios inválidos."""
    pass

def validar_empleado(nombre, edad, salario):
    """Valida los datos de un empleado.
    
    Args:
        nombre (str): Nombre del empleado
        edad (int): Edad del empleado
        salario (float): Salario del empleado
        
    Returns:
        dict: Datos del empleado validados
        
    Raises:
        ValueError: Si el nombre está vacío
        EdadInvalidaError: Si la edad es menor de 18 o mayor de 65
        SalarioInvalidoError: Si el salario es negativo o mayor a 100000
    """
    if not nombre.strip():
        raise ValueError("El nombre no puede estar vacío")
    
    if edad < 18 or edad > 65:
        raise EdadInvalidaError(f"La edad debe estar entre 18 y 65 años, recibido: {edad}")
    
    if salario < 0 or salario > 100000:
        raise SalarioInvalidoError(f"El salario debe estar entre 0 y 100000, recibido: {salario}")
    
    return {"nombre": nombre, "edad": edad, "salario": salario}

# Probar la función con diferentes casos
empleados = [
    {"nombre": "Ana", "edad": 25, "salario": 45000},
    {"nombre": "", "edad": 30, "salario": 50000},
    {"nombre": "Carlos", "edad": 17, "salario": 30000},
    {"nombre": "Elena", "edad": 35, "salario": 120000}
]

for datos in empleados:
    try:
        empleado_validado = validar_empleado(**datos)
        print(f"Empleado validado: {empleado_validado}")
    except ValueError as e:
        print(f"Error de validación: {e}")
    except EdadInvalidaError as e:
        print(f"Error de edad: {e}")
    except SalarioInvalidoError as e:
        print(f"Error de salario: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
print("-" * 50)

# 6. Validación defensiva de argumentos
print("6. Validación defensiva de argumentos")
print("-" * 50)

def crear_usuario(nombre, email, edad=None, rol="usuario"):
    """Crea un diccionario con datos de usuario, validando los argumentos.
    
    Args:
        nombre (str): Nombre de usuario (3-50 caracteres)
        email (str): Email válido (debe contener @ y .)
        edad (int, optional): Edad del usuario (mayor de 0)
        rol (str, optional): Rol del usuario (por defecto "usuario")
        
    Returns:
        dict: Datos del usuario validados
        
    Raises:
        ValueError: Si algún parámetro no cumple con las validaciones
        TypeError: Si algún parámetro no es del tipo esperado
    """
    # Validar nombre
    if not isinstance(nombre, str):
        raise TypeError("El nombre debe ser una cadena de texto")
    if len(nombre) < 3 or len(nombre) > 50:
        raise ValueError("El nombre debe tener entre 3 y 50 caracteres")
    
    # Validar email
    if not isinstance(email, str):
        raise TypeError("El email debe ser una cadena de texto")
    if "@" not in email or "." not in email:
        raise ValueError("El email debe contener @ y .")
    
    # Validar edad (si se proporciona)
    if edad is not None:
        if not isinstance(edad, int):
            raise TypeError("La edad debe ser un número entero")
        if edad <= 0:
            raise ValueError("La edad debe ser mayor que 0")
    
    # Validar rol
    if not isinstance(rol, str):
        raise TypeError("El rol debe ser una cadena de texto")
    if rol not in ["usuario", "administrador", "editor"]:
        raise ValueError("El rol debe ser 'usuario', 'administrador' o 'editor'")
    
    # Crear y retornar el diccionario de usuario
    usuario = {
        "nombre": nombre,
        "email": email,
        "rol": rol
    }
    
    if edad is not None:
        usuario["edad"] = edad
    
    return usuario

# Probar la función con diferentes casos
usuarios = [
    {"nombre": "Ana García", "email": "ana@ejemplo.com", "edad": 28},
    {"nombre": "Bo", "email": "correo_sin_formato", "edad": 25},
    {"nombre": "Carlos López", "email": "carlos@ejemplo.com", "edad": -5},
    {"nombre": "Diana Martín", "email": "diana@ejemplo.com", "rol": "superusuario"},
    {"nombre": 12345, "email": "email@ejemplo.com"}
]

for datos in usuarios:
    try:
        usuario_creado = crear_usuario(**datos)
        print(f"Usuario creado: {usuario_creado}")
    except (ValueError, TypeError) as e:
        print(f"Error al crear usuario: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
print("-" * 50)

# 7. Mensajes de error informativos
print("7. Mensajes de error informativos")
print("-" * 50)

def procesar_datos(datos, formato="json"):
    """Procesa datos en diferentes formatos.
    
    Args:
        datos: Datos a procesar
        formato (str): Formato de los datos ("json", "xml", "csv")
        
    Returns:
        dict: Datos procesados
        
    Raises:
        ValueError: Si el formato no es válido o los datos no tienen el formato correcto
    """
    formatos_validos = ["json", "xml", "csv"]
    
    if formato not in formatos_validos:
        # Mensaje de error detallado con opciones válidas
        raise ValueError(f"Formato no válido: '{formato}'. Formatos admitidos: {', '.join(formatos_validos)}")
    
    if not datos:
        raise ValueError("Los datos no pueden estar vacíos")
    
    # Simulación de procesamiento
    print(f"Procesando datos en formato {formato}...")
    
    # Simulación de errores específicos
    if formato == "json" and not isinstance(datos, dict):
        raise ValueError("Para el formato 'json', los datos deben ser un diccionario")
    
    if formato == "csv" and not isinstance(datos, list):
        raise ValueError("Para el formato 'csv', los datos deben ser una lista")
    
    # Procesamiento simulado
    return {"formato": formato, "datos_procesados": datos}

# Probar la función con diferentes casos
casos = [
    {"datos": {"nombre": "Ana", "edad": 28}, "formato": "json"},
    {"datos": "<persona><nombre>Juan</nombre></persona>", "formato": "xml"},
    {"datos": [1, 2, 3, 4, 5], "formato": "excel"},
    {"datos": "", "formato": "json"},
    {"datos": [1, 2, 3], "formato": "json"}
]

for caso in casos:
    try:
        resultado = procesar_datos(**caso)
        print(f"Resultado: {resultado}")
    except ValueError as e:
        print(f"Error de valor: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
print("-" * 50)

"""
EJERCICIOS PROPUESTOS:

1. Crea una función 'convertir_temperatura' que convierta entre diferentes unidades
   de temperatura (Celsius, Fahrenheit, Kelvin). La función debe recibir tres parámetros:
   valor, unidad_origen y unidad_destino. Implementa manejo de errores para:
   - Validar que las unidades sean válidas (C, F, K)
   - Verificar que el valor sea numérico
   - Asegurar que la temperatura no sea inferior al cero absoluto (-273.15°C)

2. Implementa una función 'dividir_lista' que divida los elementos de una lista
   por un divisor dado. La función debe manejar:
   - División por cero
   - Elementos no numéricos en la lista
   - Lista vacía
   Usa try-except-else-finally y proporciona mensajes de error informativos.

3. Crea una excepción personalizada llamada 'PasswordError' y úsala en una función
   'validar_contraseña' que verifique:
   - Longitud mínima de 8 caracteres
   - Al menos una letra mayúscula
   - Al menos un número
   - Al menos un carácter especial (!@#$%^&*)
   La función debe lanzar diferentes mensajes según el criterio que falle.
"""
