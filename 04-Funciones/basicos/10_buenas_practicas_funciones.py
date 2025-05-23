"""
Ejercicio 10: Buenas Prácticas y Guías de Estilo para Funciones

Objetivo:
- Aprender las mejores prácticas para definir y utilizar funciones
- Conocer las convenciones de estilo de Python (PEP 8) para funciones
- Entender los principios de diseño de funciones
- Aplicar técnicas para mejorar la legibilidad y mantenibilidad del código

Las buenas prácticas en la definición y uso de funciones son fundamentales para
crear código legible, mantenible y libre de errores. Seguir las convenciones de
estilo de Python (PEP 8) ayuda a que tu código sea más consistente y profesional.
"""

# 1. Convenciones de nomenclatura (PEP 8)
print("1. Convenciones de nomenclatura (PEP 8)")
print("-" * 50)

# MAL: Nombre con camelCase
def calcularArea(radio):
    return 3.14159 * radio ** 2

# BIEN: Nombre con snake_case
def calcular_area(radio):
    return 3.14159 * radio ** 2

# MAL: Nombre poco descriptivo
def calc(a, b):
    return a * b

# BIEN: Nombre descriptivo
def calcular_producto(multiplicando, multiplicador):
    return multiplicando * multiplicador

# Demostración
radio = 5
print(f"Área de un círculo con radio {radio}: {calcular_area(radio):.2f}")
print(f"Producto de 4 y 7: {calcular_producto(4, 7)}")
print("-" * 50)

# 2. Responsabilidad única
print("2. Responsabilidad única")
print("-" * 50)

# MAL: Función con múltiples responsabilidades
def procesar_usuario(nombre, edad, email):
    # Validar datos
    if not nombre or not email or edad < 0:
        return None
    
    # Crear estructura de usuario
    usuario = {
        "nombre": nombre,
        "edad": edad,
        "email": email
    }
    
    # Mostrar información
    print(f"Usuario creado: {usuario}")
    
    return usuario

# BIEN: Funciones con responsabilidad única
def validar_datos_usuario(nombre, edad, email):
    """Valida los datos de un usuario.
    
    Args:
        nombre (str): Nombre del usuario
        edad (int): Edad del usuario
        email (str): Email del usuario
        
    Returns:
        bool: True si los datos son válidos, False en caso contrario
    """
    return bool(nombre) and bool(email) and edad >= 0

def crear_usuario(nombre, edad, email):
    """Crea un diccionario con los datos del usuario.
    
    Args:
        nombre (str): Nombre del usuario
        edad (int): Edad del usuario
        email (str): Email del usuario
        
    Returns:
        dict: Datos del usuario
    """
    return {
        "nombre": nombre,
        "edad": edad,
        "email": email
    }

def mostrar_usuario(usuario):
    """Muestra la información de un usuario.
    
    Args:
        usuario (dict): Datos del usuario
    """
    print(f"Usuario: {usuario['nombre']}, {usuario['edad']} años, {usuario['email']}")

# Demostración del enfoque mejorado
print("Enfoque con responsabilidad única:")
nombre = "Ana García"
edad = 28
email = "ana@ejemplo.com"

if validar_datos_usuario(nombre, edad, email):
    usuario = crear_usuario(nombre, edad, email)
    mostrar_usuario(usuario)
else:
    print("Datos de usuario inválidos")
print("-" * 50)

# 3. Longitud y complejidad adecuadas
print("3. Longitud y complejidad adecuadas")
print("-" * 50)

# MAL: Función demasiado larga y compleja
def analizar_texto_complejo(texto):
    """Analiza un texto y calcula diversas estadísticas."""
    # Esta función sería muy larga con toda la lógica aquí
    # Por brevedad, solo se muestra un esquema
    palabras = texto.lower().split()
    num_palabras = len(palabras)
    caracteres = len(texto)
    frases = texto.count('.') + texto.count('!') + texto.count('?')
    
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    palabras_unicas = len(frecuencia)
    
    # Calcular complejidad léxica
    complejidad = palabras_unicas / num_palabras if num_palabras > 0 else 0
    
    # Longitud promedio de palabras
    total_letras = sum(len(palabra) for palabra in palabras)
    longitud_promedio = total_letras / num_palabras if num_palabras > 0 else 0
    
    # Más cálculos...
    
    return {
        "num_palabras": num_palabras,
        "caracteres": caracteres,
        "frases": frases,
        "palabras_unicas": palabras_unicas,
        "complejidad": complejidad,
        "longitud_promedio": longitud_promedio
    }

# BIEN: Dividir en funciones más pequeñas y especializadas
def contar_palabras(texto):
    """Cuenta el número de palabras en un texto."""
    return len(texto.split())

def contar_caracteres(texto):
    """Cuenta el número de caracteres en un texto."""
    return len(texto)

def contar_frases(texto):
    """Cuenta el número de frases en un texto."""
    return texto.count('.') + texto.count('!') + texto.count('?')

def calcular_frecuencia_palabras(texto):
    """Calcula la frecuencia de cada palabra en un texto."""
    palabras = texto.lower().split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

def calcular_complejidad_lexica(texto):
    """Calcula la complejidad léxica de un texto."""
    palabras = texto.lower().split()
    num_palabras = len(palabras)
    palabras_unicas = len(set(palabras))
    return palabras_unicas / num_palabras if num_palabras > 0 else 0

def analizar_texto(texto):
    """Analiza un texto y calcula diversas estadísticas.
    
    Divide el proceso en funciones más pequeñas y especializadas.
    """
    return {
        "num_palabras": contar_palabras(texto),
        "caracteres": contar_caracteres(texto),
        "frases": contar_frases(texto),
        "frecuencia": calcular_frecuencia_palabras(texto),
        "complejidad": calcular_complejidad_lexica(texto)
    }

# Demostración
texto_ejemplo = "Python es un lenguaje de programación de alto nivel. Es fácil de aprender y muy versátil."
print("Análisis de texto:")
analisis = analizar_texto(texto_ejemplo)
print(f"- Número de palabras: {analisis['num_palabras']}")
print(f"- Número de caracteres: {analisis['caracteres']}")
print(f"- Número de frases: {analisis['frases']}")
print(f"- Complejidad léxica: {analisis['complejidad']:.2f}")
print("-" * 50)

# 4. Valores por defecto inmutables
print("4. Valores por defecto inmutables")
print("-" * 50)

# MAL: Usar un objeto mutable como valor por defecto
def agregar_item_mal(item, lista=[]):
    lista.append(item)
    return lista

# BIEN: Usar None y asignar el objeto mutable dentro de la función
def agregar_item_bien(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista

# Demostración del problema
print("Usando valor por defecto mutable:")
print(agregar_item_mal(1))  # [1]
print(agregar_item_mal(2))  # [1, 2] - ¡La lista persiste entre llamadas!

print("\nUsando enfoque correcto:")
print(agregar_item_bien(1))  # [1]
print(agregar_item_bien(2))  # [2] - Cada llamada tiene una lista nueva
print("-" * 50)

# 5. Documentación adecuada
print("5. Documentación adecuada")
print("-" * 50)

# MAL: Sin documentación
def calcular_impuesto(precio, tasa):
    return precio * tasa / 100

# BIEN: Con documentación completa
def calcular_impuesto_bien(precio, tasa):
    """Calcula el impuesto para un precio dado.
    
    Multiplica el precio por la tasa de impuesto proporcionada.
    
    Args:
        precio (float): El precio antes de impuestos
        tasa (float): La tasa de impuesto en porcentaje (ej. 21 para 21%)
        
    Returns:
        float: El importe del impuesto
        
    Examples:
        >>> calcular_impuesto_bien(100, 21)
        21.0
    """
    return precio * tasa / 100

# Demostración
precio = 100
tasa = 21
print(f"Impuesto para {precio}€ con tasa {tasa}%: {calcular_impuesto_bien(precio, tasa)}€")
print("-" * 50)

# 6. Uso adecuado de return
print("6. Uso adecuado de return")
print("-" * 50)

# MAL: Múltiples puntos de salida sin clara justificación
def validar_nombre_mal(nombre):
    if not isinstance(nombre, str):
        return False
    if len(nombre) < 2:
        return False
    if not all(c.isalpha() or c.isspace() for c in nombre):
        return False
    return True

# BIEN: Puntos de salida tempranos para casos de error
def validar_nombre_bien(nombre):
    """Valida que un nombre cumpla los requisitos.
    
    Args:
        nombre: El nombre a validar
        
    Returns:
        bool: True si el nombre es válido, False en caso contrario
    """
    # Retornos tempranos para casos de error (patrón de guarda)
    if not isinstance(nombre, str):
        return False
    
    if len(nombre) < 2:
        return False
    
    if not all(c.isalpha() or c.isspace() for c in nombre):
        return False
    
    # Si pasa todas las validaciones
    return True

# Demostración
nombres = ["Ana García", "J", "Juan123", 12345]
for nombre in nombres:
    print(f"¿'{nombre}' es un nombre válido? {validar_nombre_bien(nombre)}")
print("-" * 50)

# 7. Evitar efectos secundarios inesperados
print("7. Evitar efectos secundarios inesperados")
print("-" * 50)

# MAL: Función con efectos secundarios inesperados
def agregar_usuario_mal(usuarios, nombre, edad):
    """Agrega un usuario a la lista."""
    # Modificación inesperada: ordena la lista
    usuarios.sort()
    # Agrega el usuario
    usuarios.append({"nombre": nombre, "edad": edad})
    return usuarios

# BIEN: Función sin efectos secundarios inesperados
def agregar_usuario_bien(usuarios, nombre, edad):
    """Agrega un usuario a la lista sin modificar el orden original.
    
    Args:
        usuarios (list): Lista de usuarios
        nombre (str): Nombre del nuevo usuario
        edad (int): Edad del nuevo usuario
        
    Returns:
        list: Lista con el nuevo usuario agregado
    """
    # Crea una copia para no modificar la original
    resultado = usuarios.copy()
    # Agrega el usuario
    resultado.append({"nombre": nombre, "edad": edad})
    return resultado

# Demostración
usuarios = [
    {"nombre": "Carlos", "edad": 30},
    {"nombre": "Ana", "edad": 25}
]
print(f"Lista original: {usuarios}")

# Con efectos secundarios
usuarios_mal = agregar_usuario_mal(usuarios.copy(), "Luis", 40)
print(f"Después de agregar_usuario_mal: {usuarios_mal}")

# Sin efectos secundarios
usuarios_bien = agregar_usuario_bien(usuarios, "Luis", 40)
print(f"Después de agregar_usuario_bien: {usuarios_bien}")
print(f"Lista original sigue igual: {usuarios}")
print("-" * 50)

# 8. Principio DRY (Don't Repeat Yourself)
print("8. Principio DRY (Don't Repeat Yourself)")
print("-" * 50)

# MAL: Código repetido
def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_cuadrado(lado):
    return lado * lado

# BIEN: Reutilizar código
def calcular_area_rectangulo_bien(base, altura):
    """Calcula el área de un rectángulo."""
    return base * altura

def calcular_area_cuadrado_bien(lado):
    """Calcula el área de un cuadrado usando la función de rectángulo."""
    return calcular_area_rectangulo_bien(lado, lado)

# Demostración
print(f"Área de un rectángulo de 5×3: {calcular_area_rectangulo_bien(5, 3)}")
print(f"Área de un cuadrado de lado 4: {calcular_area_cuadrado_bien(4)}")
print("-" * 50)

# 9. Funciones puras vs. impuras
print("9. Funciones puras vs. impuras")
print("-" * 50)

# Variables globales para el ejemplo
contador_global = 0

# Función impura (usa/modifica estado global)
def incrementar_contador():
    """Incrementa un contador global."""
    global contador_global
    contador_global += 1
    return contador_global

# Función pura (sin efectos secundarios)
def sumar(a, b):
    """Suma dos números."""
    return a + b

# Demostración
print("Función impura (con estado):")
print(f"Primera llamada: {incrementar_contador()}")
print(f"Segunda llamada: {incrementar_contador()}")
print(f"Tercera llamada: {incrementar_contador()}")

print("\nFunción pura (sin estado):")
print(f"sumar(2, 3): {sumar(2, 3)}")
print(f"sumar(2, 3) de nuevo: {sumar(2, 3)}")  # Siempre el mismo resultado
print("-" * 50)

# 10. Optimización de parámetros
print("10. Optimización de parámetros")
print("-" * 50)

# MAL: Demasiados parámetros
def crear_reporte_mal(titulo, autor, fecha, contenido, formato, resumen, palabras_clave, version, departamento, confidencial):
    # Crea un reporte con demasiados parámetros
    return {
        "titulo": titulo,
        "autor": autor,
        "fecha": fecha,
        "contenido": contenido,
        "formato": formato,
        "resumen": resumen,
        "palabras_clave": palabras_clave,
        "version": version,
        "departamento": departamento,
        "confidencial": confidencial
    }

# BIEN: Usar diccionarios o clases para agrupar parámetros relacionados
def crear_reporte_bien(titulo, autor, contenido, **opciones):
    """Crea un reporte con parámetros opcionales usando kwargs.
    
    Args:
        titulo (str): Título del reporte
        autor (str): Autor del reporte
        contenido (str): Contenido principal del reporte
        **opciones: Opciones adicionales (formato, resumen, etc.)
        
    Returns:
        dict: Datos del reporte
    """
    # Valores por defecto
    valores_por_defecto = {
        "fecha": "2023-01-01",
        "formato": "PDF",
        "version": "1.0",
        "confidencial": False
    }
    
    # Crear el reporte con valores básicos
    reporte = {
        "titulo": titulo,
        "autor": autor,
        "contenido": contenido
    }
    
    # Agregar valores por defecto (si no están en opciones)
    for clave, valor in valores_por_defecto.items():
        if clave not in opciones:
            reporte[clave] = valor
    
    # Agregar opciones proporcionadas
    for clave, valor in opciones.items():
        reporte[clave] = valor
    
    return reporte

# Demostración
print("Creando reporte con parámetros optimizados:")
reporte = crear_reporte_bien(
    "Informe Anual",
    "Juan Pérez",
    "Contenido del informe...",
    fecha="2023-05-15",
    resumen="Resumen ejecutivo...",
    departamento="Finanzas"
)
print(f"Reporte creado: {reporte}")
print("-" * 50)

"""
EJERCICIOS PROPUESTOS:

1. Refactoriza el siguiente código para seguir las buenas prácticas de funciones:

```python
def Procesar(data, type="suma", filter=None):
    results = []
    if filter != None:
        filtered_data = []
        for item in data:
            if filter(item):
                filtered_data.append(item)
        data = filtered_data
    
    if type == "suma":
        return sum(data)
    elif type == "promedio":
        return sum(data) / len(data)
    elif type == "maximo":
        return max(data)
    else:
        return "Tipo no válido"
```

2. Identifica y corrige los problemas en estas funciones:

```python
# Función 1
def get_user_data(id, db=[]):
    for user in db:
        if user["id"] == id:
            return user
    new_user = {"id": id, "visits": 1}
    db.append(new_user)
    return new_user

# Función 2
def Process_Text(t):
    words = len(t.split())
    chars = len(t)
    lines = t.count("\n") + 1
    print(f"Words: {words}")
    print(f"Chars: {chars}")
    print(f"Lines: {lines}")
    return {"w": words, "c": chars, "l": lines}
```

3. Implementa una función `crear_calculadora` que siga las buenas prácticas
   aprendidas. La función debe recibir parámetros para configurar el número de
   decimales a mostrar y las operaciones permitidas. Debe retornar un diccionario
   de funciones que realicen operaciones matemáticas (suma, resta, multiplicación,
   división) respetando la configuración proporcionada.
"""
