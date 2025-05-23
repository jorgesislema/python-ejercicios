"""
Ejercicio 6: Funciones como Objetos de Primera Clase

Objetivo:
- Comprender que las funciones son objetos de primera clase en Python
- Aprender a asignar funciones a variables
- Pasar funciones como argumentos a otras funciones
- Retornar funciones desde otras funciones
- Almacenar funciones en estructuras de datos

En Python, las funciones son objetos de primera clase, lo que significa que pueden
ser tratadas como cualquier otro objeto: asignadas a variables, pasadas como argumentos,
retornadas desde otras funciones y almacenadas en estructuras de datos.
"""

# 1. Asignar funciones a variables
print("1. Asignar funciones a variables")
print("-" * 50)

def saludar(nombre):
    """Saluda a una persona por su nombre."""
    return f"¡Hola, {nombre}!"

# Asignar la función a una variable
mi_funcion = saludar

# Usar la variable como una función
print("Llamando a la función original:")
print(saludar("Ana"))

print("\nLlamando a la función a través de la variable:")
print(mi_funcion("Pedro"))

# Comprobar que ambas referencias apuntan al mismo objeto
print("\nVerificar que apuntan al mismo objeto:")
print(f"saludar: {id(saludar)}")
print(f"mi_funcion: {id(mi_funcion)}")
print(f"¿Son el mismo objeto? {saludar is mi_funcion}")
print("-" * 50)

# 2. Pasar funciones como argumentos
print("2. Pasar funciones como argumentos")
print("-" * 50)

def operar(a, b, funcion):
    """Aplica una función a dos números.
    
    Args:
        a: Primer número
        b: Segundo número
        funcion: Función que toma dos argumentos y retorna un resultado
        
    Returns:
        El resultado de aplicar la función a los números
    """
    resultado = funcion(a, b)
    return resultado

# Definir algunas funciones para operaciones matemáticas
def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        raise ValueError("No se puede dividir por cero")
    return x / y

# Usar la función operar con diferentes funciones
a, b = 10, 5

print(f"Operaciones con {a} y {b}:")
print(f"Suma: {operar(a, b, sumar)}")
print(f"Resta: {operar(a, b, restar)}")
print(f"Multiplicación: {operar(a, b, multiplicar)}")
print(f"División: {operar(a, b, dividir)}")

# Usar funciones anónimas (lambda)
print("\nUsando funciones lambda:")
print(f"Potencia: {operar(a, b, lambda x, y: x ** y)}")
print(f"Módulo: {operar(a, b, lambda x, y: x % y)}")
print("-" * 50)

# 3. Retornar funciones desde otras funciones
print("3. Retornar funciones desde otras funciones")
print("-" * 50)

def crear_multiplicador(factor):
    """Crea una función que multiplica por un factor específico.
    
    Args:
        factor: Factor de multiplicación
        
    Returns:
        function: Una función que multiplica su argumento por el factor
    """
    def multiplicador(x):
        return x * factor
    
    return multiplicador

# Crear funciones especializadas
duplicar = crear_multiplicador(2)
triplicar = crear_multiplicador(3)
multiplicar_por_10 = crear_multiplicador(10)

# Usar las funciones creadas
numero = 5
print(f"Operaciones con el número {numero}:")
print(f"Duplicar: {duplicar(numero)}")
print(f"Triplicar: {triplicar(numero)}")
print(f"Multiplicar por 10: {multiplicar_por_10(numero)}")

# Ver los detalles de la función creada
print("\nDetalles de la función 'duplicar':")
print(f"Nombre: {duplicar.__name__}")
print(f"Tipo: {type(duplicar)}")
print("-" * 50)

# 4. Almacenar funciones en estructuras de datos
print("4. Almacenar funciones en estructuras de datos")
print("-" * 50)

# Lista de funciones
operaciones = [sumar, restar, multiplicar, dividir]

# Aplicar todas las operaciones a dos números
x, y = 20, 4
print(f"Aplicando todas las operaciones a {x} y {y}:")
for i, operacion in enumerate(operaciones, 1):
    print(f"Operación {i}: {operacion(x, y)}")

# Diccionario de funciones
calculadora = {
    'suma': sumar,
    'resta': restar,
    'multiplicacion': multiplicar,
    'division': dividir,
    'potencia': lambda x, y: x ** y,
    'modulo': lambda x, y: x % y
}

# Usar el diccionario de funciones
print("\nUsando el diccionario de funciones:")
for nombre, operacion in calculadora.items():
    try:
        resultado = operacion(x, y)
        print(f"{nombre}: {resultado}")
    except Exception as e:
        print(f"{nombre}: Error - {e}")
print("-" * 50)

# 5. Funciones de orden superior
print("5. Funciones de orden superior")
print("-" * 50)

def aplicar_a_lista(numeros, funcion):
    """Aplica una función a cada elemento de una lista.
    
    Args:
        numeros: Lista de números
        funcion: Función a aplicar a cada número
        
    Returns:
        list: Lista con los resultados
    """
    return [funcion(x) for x in numeros]

numeros = [1, 2, 3, 4, 5]

# Aplicar diferentes funciones
print(f"Lista original: {numeros}")
print(f"Duplicar cada número: {aplicar_a_lista(numeros, lambda x: x * 2)}")
print(f"Elevar al cuadrado: {aplicar_a_lista(numeros, lambda x: x ** 2)}")
print(f"Raíz cuadrada: {aplicar_a_lista(numeros, lambda x: x ** 0.5)}")

# Funciones integradas como map y filter
print("\nUsando map y filter:")
print(f"Map - duplicar: {list(map(lambda x: x * 2, numeros))}")
print(f"Filter - solo pares: {list(filter(lambda x: x % 2 == 0, numeros))}")
print("-" * 50)

# 6. Closures (clausuras)
print("6. Closures (clausuras)")
print("-" * 50)

def crear_contador():
    """Crea una función contador que recuerda su estado entre llamadas.
    
    Returns:
        function: Una función que incrementa y retorna el contador
    """
    contador = 0
    
    def incrementar():
        nonlocal contador
        contador += 1
        return contador
    
    return incrementar

# Crear dos contadores independientes
contador1 = crear_contador()
contador2 = crear_contador()

print("Usando contadores independientes:")
print(f"Contador 1 - Primera llamada: {contador1()}")
print(f"Contador 1 - Segunda llamada: {contador1()}")
print(f"Contador 1 - Tercera llamada: {contador1()}")

print(f"Contador 2 - Primera llamada: {contador2()}")
print(f"Contador 2 - Segunda llamada: {contador2()}")

print(f"Contador 1 - Cuarta llamada: {contador1()}")

# Otro ejemplo de closure
def crear_potenciador(exponente):
    """Crea una función que eleva su argumento a una potencia específica.
    
    Args:
        exponente: Exponente al que se elevará el número
        
    Returns:
        function: Una función que eleva su argumento al exponente especificado
    """
    def potencia(base):
        return base ** exponente
    
    return potencia

# Crear funciones especializadas
cuadrado = crear_potenciador(2)
cubo = crear_potenciador(3)
raiz_cuadrada = crear_potenciador(0.5)

print("\nFunciones especializadas con closures:")
print(f"Cuadrado de 4: {cuadrado(4)}")
print(f"Cubo de 3: {cubo(3)}")
print(f"Raíz cuadrada de 16: {raiz_cuadrada(16)}")
print("-" * 50)

# 7. Atributos de las funciones
print("7. Atributos de las funciones")
print("-" * 50)

def procesar_datos(datos, transformacion=lambda x: x):
    """Procesa una lista de datos aplicando una transformación.
    
    Args:
        datos: Lista de datos a procesar
        transformacion: Función para transformar los datos
    
    Returns:
        list: Lista de datos procesados
    """
    return [transformacion(x) for x in datos]

# Añadir atributos a la función
procesar_datos.autor = "Programador Python"
procesar_datos.version = "1.0"
procesar_datos.descripcion = "Función para procesar datos con transformaciones personalizadas"

# Ver atributos de la función
print("Atributos de la función procesar_datos:")
print(f"Nombre: {procesar_datos.__name__}")
print(f"Autor: {procesar_datos.autor}")
print(f"Versión: {procesar_datos.version}")
print(f"Descripción: {procesar_datos.descripcion}")

# Usar la función con sus atributos
datos = [10, 20, 30, 40, 50]
print(f"\nProcesando datos {datos} con {procesar_datos.__name__} v{procesar_datos.version}:")
print(f"Resultado: {procesar_datos(datos, lambda x: x / 10)}")
print("-" * 50)

"""
EJERCICIOS PROPUESTOS:

1. Implementa una función 'operar_lista' que reciba una lista de números y una lista
   de funciones, y retorne una lista con los resultados de aplicar cada función a la
   lista de números. Por ejemplo:
   ```
   numeros = [1, 2, 3, 4]
   funciones = [lambda x: x**2, lambda x: x*2, lambda x: x+10]
   operar_lista(numeros, funciones)
   # Debería retornar [[1, 4, 9, 16], [2, 4, 6, 8], [11, 12, 13, 14]]
   ```

2. Crea una función 'crear_validador' que reciba un tipo de dato (int, str, list, etc.)
   y retorne una función que verifique si un valor es de ese tipo. Luego, utiliza esta
   función para crear validadores específicos y aplícalos a diferentes valores.

3. Implementa un sistema de filtros encadenados. Crea una función 'aplicar_filtros'
   que reciba una lista de datos y una serie de funciones de filtro, y aplique cada
   filtro secuencialmente a los datos (cada filtro trabaja sobre el resultado del
   anterior). Luego, crea diferentes filtros como:
   - filtrar_positivos: mantiene solo números positivos
   - filtrar_pares: mantiene solo números pares
   - filtrar_mayores_que(n): retorna una función que mantiene números mayores que n
"""
