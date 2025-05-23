"""
Ejercicio 3: Alcance (Scope) y Tiempo de Vida de Variables

Objetivo:
- Comprender el alcance de las variables en Python
- Entender la diferencia entre variables locales y globales
- Aprender a modificar variables globales desde funciones
- Conocer el concepto del alcance nonlocal en funciones anidadas

El alcance de una variable en Python define dónde es accesible la variable
dentro del código. Python sigue la regla LEGB (Local, Enclosing, Global, Built-in)
para buscar variables.
"""

# 1. Variables locales y globales
print("1. Variables locales y globales")
print("-" * 50)

# Variable global
contador = 0

def incrementar_contador():
    """Intenta incrementar un contador global pero crea una variable local."""
    contador = 0  # Esta es una variable local, no modifica la global
    contador += 1
    print(f"Valor del contador local dentro de la función: {contador}")

print(f"Valor del contador global antes: {contador}")
incrementar_contador()
print(f"Valor del contador global después: {contador}")  # No cambió porque la función usó una variable local
print("-" * 50)

# 2. Modificar variables globales con la palabra clave 'global'
print("2. Modificar variables globales con la palabra clave 'global'")
print("-" * 50)

total = 0

def agregar_al_total(valor):
    """Agrega un valor al total global usando la palabra clave global.
    
    Args:
        valor: Cantidad a agregar al total
    """
    global total
    total += valor
    print(f"Total dentro de la función: {total}")

print(f"Total global antes: {total}")
agregar_al_total(10)
agregar_al_total(5)
print(f"Total global después: {total}")  # Ahora sí se modificó la variable global
print("-" * 50)

# 3. Variables locales en diferentes llamadas a funciones
print("3. Variables locales en diferentes llamadas a funciones")
print("-" * 50)

def generar_contador():
    """Genera un contador que incrementa en cada llamada."""
    contador = 0
    contador += 1
    return contador

print(f"Primera llamada: {generar_contador()}")
print(f"Segunda llamada: {generar_contador()}")
print(f"Tercera llamada: {generar_contador()}")
print("Cada llamada reinicia el contador porque la variable 'contador' es local")
print("-" * 50)

# 4. Parámetros como variables locales
print("4. Parámetros como variables locales")
print("-" * 50)

def duplicar(x):
    """Duplica el valor de x y muestra la dirección de memoria.
    
    Args:
        x: Valor a duplicar
        
    Returns:
        El valor duplicado
    """
    print(f"Dentro de la función: x = {x}, id(x) = {id(x)}")
    x = x * 2
    print(f"Después de modificar: x = {x}, id(x) = {id(x)}")
    return x

valor = 5
print(f"Antes de llamar a la función: valor = {valor}, id(valor) = {id(valor)}")
resultado = duplicar(valor)
print(f"Después de llamar a la función: valor = {valor}, id(valor) = {id(valor)}")
print(f"Resultado: {resultado}")
print("-" * 50)

# 5. Alcance nonlocal (variables en funciones anidadas)
print("5. Alcance nonlocal (variables en funciones anidadas)")
print("-" * 50)

def crear_contador():
    """Crea una función contador que recuerda su estado entre llamadas.
    
    Returns:
        function: Una función que incrementa y devuelve el contador
    """
    # Esta variable es local a crear_contador
    # pero es "nonlocal" para la función incrementar
    cuenta = 0
    
    def incrementar():
        """Incrementa y devuelve el contador."""
        nonlocal cuenta
        cuenta += 1
        return cuenta
    
    # Devuelve la función interna (closure)
    return incrementar

# Creamos dos contadores independientes
contador1 = crear_contador()
contador2 = crear_contador()

print(f"Contador 1 - Primera llamada: {contador1()}")
print(f"Contador 1 - Segunda llamada: {contador1()}")
print(f"Contador 1 - Tercera llamada: {contador1()}")

print(f"Contador 2 - Primera llamada: {contador2()}")
print(f"Contador 2 - Segunda llamada: {contador2()}")

print(f"Contador 1 - Cuarta llamada: {contador1()}")
print("Cada contador mantiene su propio estado gracias al uso de nonlocal")
print("-" * 50)

# 6. Efecto de mutabilidad en el alcance
print("6. Efecto de mutabilidad en el alcance")
print("-" * 50)

# Con objetos inmutables (int, float, str, tuple)
def modificar_inmutable(x):
    """Intenta modificar un objeto inmutable.
    
    Args:
        x: Objeto inmutable (int, str, etc.)
    """
    x = x + 1  # Crea un nuevo objeto, no modifica el original
    print(f"Dentro de la función: x = {x}")

numero = 10
print(f"Antes de la función: numero = {numero}")
modificar_inmutable(numero)
print(f"Después de la función: numero = {numero}")  # No cambió

# Con objetos mutables (list, dict, set)
def modificar_mutable(lista):
    """Modifica un objeto mutable.
    
    Args:
        lista: Objeto mutable (list, dict, etc.)
    """
    lista.append(4)  # Modifica el objeto original
    print(f"Dentro de la función: lista = {lista}")

numeros = [1, 2, 3]
print(f"\nAntes de la función: numeros = {numeros}")
modificar_mutable(numeros)
print(f"Después de la función: numeros = {numeros}")  # La lista cambió
print("-" * 50)

# 7. Variables globales y buenas prácticas
print("7. Variables globales y buenas prácticas")
print("-" * 50)

# Variables globales para configuración
DEBUG = True
MAX_INTENTOS = 3
NOMBRE_APP = "MiAplicación"

def imprimir_configuracion():
    """Imprime la configuración actual usando variables globales."""
    # En este caso, solo leemos las variables globales, no las modificamos
    print(f"Configuración actual:")
    print(f"- Modo debug: {DEBUG}")
    print(f"- Máximo de intentos: {MAX_INTENTOS}")
    print(f"- Nombre de la aplicación: {NOMBRE_APP}")

imprimir_configuracion()

# Mejor alternativa: pasar valores como parámetros
def procesar_datos(datos, debug=False, max_intentos=3):
    """Procesa datos con configuración personalizable.
    
    Args:
        datos: Datos a procesar
        debug: Activa el modo debug
        max_intentos: Número máximo de intentos
    """
    print(f"\nProcesando {len(datos)} elementos:")
    print(f"- Modo debug: {debug}")
    print(f"- Máximo de intentos: {max_intentos}")
    # Procesamiento real aquí...

datos_ejemplo = [1, 2, 3, 4, 5]
procesar_datos(datos_ejemplo, debug=True)
print("-" * 50)

"""
EJERCICIOS PROPUESTOS:

1. Escribe una función llamada 'actualizar_configuracion' que tome un diccionario
   como parámetro y actualice una variable global llamada 'configuracion' con esos
   valores. Asegúrate de usar la palabra clave 'global' correctamente.

2. Crea una función 'crear_generador_id' que devuelva otra función. La función
   interna debe generar IDs secuenciales que comiencen en un valor dado y tengan
   un prefijo específico. Por ejemplo:
   generador = crear_generador_id(prefijo="USER-", inicio=100)
   print(generador())  # Debería imprimir "USER-100"
   print(generador())  # Debería imprimir "USER-101"

3. Implementa una función 'calcular_estadisticas' que reciba una lista de números
   y devuelva una función para acceder a diferentes estadísticas (suma, promedio,
   máximo, mínimo). La función devuelta debe aceptar un parámetro 'tipo' que 
   indique qué estadística se desea calcular. Usa nonlocal para almacenar los
   resultados ya calculados y evitar recalcularlos.
"""
