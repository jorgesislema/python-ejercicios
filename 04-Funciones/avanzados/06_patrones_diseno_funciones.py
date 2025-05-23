"""
Ejercicio 6: Patrones de Diseño con Funciones

Objetivo: Comprender y aplicar patrones de diseño comunes utilizando funciones en Python.

Los patrones de diseño son soluciones típicas a problemas comunes en el diseño de software.
Aunque muchos patrones de diseño se implementan tradicionalmente con clases, Python permite
implementar varios de ellos de forma elegante utilizando funciones, aprovechando características
como las funciones de orden superior, los closures y los decoradores.

Instrucciones:
1. Explorar patrones de diseño que pueden implementarse con funciones
2. Comprender las ventajas de los enfoques funcionales para ciertos patrones
3. Implementar ejemplos prácticos de patrones usando funciones
4. Analizar cuándo usar un enfoque funcional vs. un enfoque orientado a objetos
"""

# ------------------------------------------------------------------------------------------
# 1. Patrón Strategy con Funciones
# ------------------------------------------------------------------------------------------
print("\n1. Patrón Strategy con Funciones")
print("-" * 70)
print("El patrón Strategy define una familia de algoritmos, encapsula cada uno")
print("y los hace intercambiables. Permite que el algoritmo varíe independientemente")
print("de los clientes que lo utilizan.")

# Implementación tradicional orientada a objetos (para comparación)
print("\nImplementación orientada a objetos (comentada):")
print("""
class EstrategiaOrdenamiento:
    def ordenar(self, datos):
        pass

class OrdenamientoAscendente(EstrategiaOrdenamiento):
    def ordenar(self, datos):
        return sorted(datos)

class OrdenamientoDescendente(EstrategiaOrdenamiento):
    def ordenar(self, datos):
        return sorted(datos, reverse=True)

class Contexto:
    def __init__(self, estrategia):
        self.estrategia = estrategia
    
    def ejecutar_estrategia(self, datos):
        return self.estrategia.ordenar(datos)
""")

# Implementación funcional del patrón Strategy
print("\nImplementación funcional:")

# Definimos las estrategias como funciones simples
def ordenar_ascendente(datos):
    """Estrategia para ordenar datos en orden ascendente."""
    return sorted(datos)

def ordenar_descendente(datos):
    """Estrategia para ordenar datos en orden descendente."""
    return sorted(datos, reverse=True)

def ordenar_por_longitud(datos):
    """Estrategia para ordenar datos por longitud."""
    return sorted(datos, key=len)

# Función que utiliza una estrategia
def aplicar_estrategia(datos, estrategia):
    """Aplica la estrategia de ordenamiento a los datos."""
    return estrategia(datos)

# Uso del patrón Strategy funcional
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5]
palabras = ["python", "es", "genial", "programación", "funcional"]

print("\nEjemplos del patrón Strategy funcional:")
print(f"Datos originales (números): {numeros}")
print(f"Ordenados ascendentemente: {aplicar_estrategia(numeros, ordenar_ascendente)}")
print(f"Ordenados descendentemente: {aplicar_estrategia(numeros, ordenar_descendente)}")

print(f"\nDatos originales (palabras): {palabras}")
print(f"Ordenadas por longitud: {aplicar_estrategia(palabras, ordenar_por_longitud)}")
print(f"Ordenadas alfabéticamente: {aplicar_estrategia(palabras, ordenar_ascendente)}")

# ------------------------------------------------------------------------------------------
# 2. Patrón Factory con Funciones
# ------------------------------------------------------------------------------------------
print("\n2. Patrón Factory con Funciones")
print("-" * 70)
print("El patrón Factory proporciona una interfaz para crear objetos en una superclase,")
print("pero permite a las subclases alterar el tipo de objetos que se crearán.")

# Implementación funcional del patrón Factory
def crear_saludo(tipo):
    """Factory function que crea diferentes tipos de funciones de saludo."""
    
    def saludo_formal(nombre):
        return f"Estimado/a {nombre}, es un placer saludarle."
    
    def saludo_casual(nombre):
        return f"¡Hola {nombre}! ¿Cómo estás?"
    
    def saludo_minimalista(nombre):
        return f"Hola {nombre}"
    
    # Diccionario que mapea tipos a funciones
    saludos = {
        'formal': saludo_formal,
        'casual': saludo_casual,
        'minimalista': saludo_minimalista
    }
    
    # Devolver la función correspondiente o una función por defecto
    return saludos.get(tipo, saludo_casual)

# Uso del patrón Factory funcional
print("\nEjemplos del patrón Factory funcional:")
saludo1 = crear_saludo('formal')
saludo2 = crear_saludo('casual')
saludo3 = crear_saludo('minimalista')
saludo4 = crear_saludo('inexistente')  # Usará el saludo casual por defecto

print(f"Saludo formal: {saludo1('Ana')}")
print(f"Saludo casual: {saludo2('Juan')}")
print(f"Saludo minimalista: {saludo3('María')}")
print(f"Saludo tipo inexistente: {saludo4('Carlos')}")

# ------------------------------------------------------------------------------------------
# 3. Patrón Observer con Funciones
# ------------------------------------------------------------------------------------------
print("\n3. Patrón Observer con Funciones")
print("-" * 70)
print("El patrón Observer define una dependencia uno-a-muchos entre objetos,")
print("de modo que cuando un objeto cambia su estado, todos sus dependientes")
print("son notificados y actualizados automáticamente.")

# Implementación funcional del patrón Observer
class SujetoObservable:
    def __init__(self):
        self._observadores = []
    
    def agregar_observador(self, observador):
        """Agrega una función observadora."""
        if observador not in self._observadores:
            self._observadores.append(observador)
        return self  # Para permitir encadenamiento
    
    def eliminar_observador(self, observador):
        """Elimina una función observadora."""
        if observador in self._observadores:
            self._observadores.remove(observador)
        return self  # Para permitir encadenamiento
    
    def notificar(self, *args, **kwargs):
        """Notifica a todos los observadores con los argumentos dados."""
        for observador in self._observadores:
            observador(*args, **kwargs)

# Ejemplo de uso: sistema de eventos de temperatura
monitor_temperatura = SujetoObservable()

# Definimos funciones observadoras
def alerta_temperatura_alta(temperatura):
    if temperatura > 30:
        print(f"¡ALERTA! Temperatura elevada: {temperatura}°C")

def registro_temperatura(temperatura):
    print(f"Registro: Temperatura actual es {temperatura}°C")

def control_aire_acondicionado(temperatura):
    if temperatura > 25:
        print(f"Aire acondicionado: Encendido (Temperatura: {temperatura}°C)")
    else:
        print(f"Aire acondicionado: Apagado (Temperatura: {temperatura}°C)")

# Registramos los observadores
monitor_temperatura.agregar_observador(alerta_temperatura_alta)
monitor_temperatura.agregar_observador(registro_temperatura)
monitor_temperatura.agregar_observador(control_aire_acondicionado)

# Simulamos cambios de temperatura
print("\nSimulación del patrón Observer funcional:")
print("\nCambio de temperatura a 20°C:")
monitor_temperatura.notificar(20)

print("\nCambio de temperatura a 28°C:")
monitor_temperatura.notificar(28)

print("\nCambio de temperatura a 35°C:")
monitor_temperatura.notificar(35)

# ------------------------------------------------------------------------------------------
# 4. Patrón Decorator con Funciones
# ------------------------------------------------------------------------------------------
print("\n4. Patrón Decorator con Funciones")
print("-" * 70)
print("El patrón Decorator añade nuevas responsabilidades a un objeto dinámicamente.")
print("Los decoradores ofrecen una alternativa flexible a la herencia para extender funcionalidad.")
print("Python tiene soporte nativo para decoradores mediante la sintaxis @.")

# Implementación de decoradores
import time
import functools

def medir_tiempo(func):
    """Decorador que mide el tiempo de ejecución de una función."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tiempo_inicio = time.time()
        resultado = func(*args, **kwargs)
        tiempo_fin = time.time()
        print(f"La función {func.__name__} tardó {tiempo_fin - tiempo_inicio:.4f} segundos en ejecutarse.")
        return resultado
    return wrapper

def registrar_llamada(func):
    """Decorador que registra cuándo se llama a una función."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Llamada a {func.__name__} con args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

# Uso de decoradores
@medir_tiempo
@registrar_llamada
def fibonacci_recursivo(n):
    """Calcula el n-ésimo número de Fibonacci recursivamente."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

print("\nEjemplo del patrón Decorator con decoradores de Python:")
print(f"Fibonacci de 10: {fibonacci_recursivo(10)}")

# ------------------------------------------------------------------------------------------
# 5. Patrón Chain of Responsibility con Funciones
# ------------------------------------------------------------------------------------------
print("\n5. Patrón Chain of Responsibility con Funciones")
print("-" * 70)
print("El patrón Chain of Responsibility pasa una solicitud a lo largo de una cadena")
print("de manejadores. Cada manejador decide si procesa la solicitud o la pasa al siguiente.")

# Implementación funcional del patrón Chain of Responsibility
def crear_cadena_de_responsabilidad(*handlers):
    """Crea una cadena de manejadores de responsabilidad."""
    
    def cadena(request):
        for handler in handlers:
            response = handler(request)
            if response:
                return response
        # Si ningún manejador procesó la solicitud
        return None
    
    return cadena

# Definimos algunos manejadores
def manejador_numeros(request):
    """Maneja solicitudes que son números."""
    if isinstance(request, (int, float)):
        return f"Número procesado: {request * 2}"
    return None

def manejador_strings(request):
    """Maneja solicitudes que son cadenas de texto."""
    if isinstance(request, str):
        return f"Texto procesado: {request.upper()}"
    return None

def manejador_listas(request):
    """Maneja solicitudes que son listas."""
    if isinstance(request, list):
        return f"Lista procesada: {sorted(request)}"
    return None

# Creamos la cadena de responsabilidad
procesador = crear_cadena_de_responsabilidad(
    manejador_numeros,
    manejador_strings,
    manejador_listas
)

# Uso del patrón Chain of Responsibility
print("\nEjemplos del patrón Chain of Responsibility funcional:")
print(procesador(42))         # Procesado por manejador_numeros
print(procesador("hola"))     # Procesado por manejador_strings
print(procesador([3, 1, 2]))  # Procesado por manejador_listas
print(procesador({"a": 1}))   # No procesado por ningún manejador

# ------------------------------------------------------------------------------------------
# 6. Comparación con Enfoques Orientados a Objetos
# ------------------------------------------------------------------------------------------
print("\n6. Comparación con Enfoques Orientados a Objetos")
print("-" * 70)
print("Ventajas del enfoque funcional:")
print("- Código más conciso y con menos boilerplate")
print("- Mayor flexibilidad para composición y reutilización")
print("- Más natural en Python para casos simples")
print("- Menor sobrecarga conceptual")

print("\nVentajas del enfoque orientado a objetos:")
print("- Mejor para modelar entidades complejas con estado")
print("- Más estructurado para sistemas grandes y equipos grandes")
print("- Mejor para casos con jerarquías naturales")
print("- Más familiar para desarrolladores de otros lenguajes")

print("\n¿Cuándo usar un enfoque funcional?")
print("- Cuando las operaciones son transformaciones puras de datos")
print("- Para comportamientos que pueden ser fácilmente parametrizados")
print("- Cuando se necesita mayor flexibilidad y composición")
print("- Para patrones simples con poco estado")

# ------------------------------------------------------------------------------------------
# Ejercicios propuestos
# ------------------------------------------------------------------------------------------
print("\nEjercicios propuestos:")
print("-" * 70)
print("1. Implementa el patrón Command utilizando funciones, creando un sistema que permita ejecutar, deshacer y rehacer operaciones.")
print("2. Desarrolla un patrón Template Method con funciones de orden superior, donde se defina un algoritmo con ciertos pasos que pueden ser personalizados.")
print("3. Crea un patrón Adapter funcional para convertir la interfaz de una API a otra interfaz esperada por el cliente.")
print("4. Implementa el patrón Proxy con funciones, donde una función actúe como intermediaria controlando el acceso a otra función.")
print("5. Desarrolla un patrón Composite utilizando funciones para operar sobre estructuras de árbol de manera uniforme.")

"""
Soluciones a los ejercicios propuestos:

1. Patrón Command con funciones:

class Historial:
    def __init__(self):
        self.comandos_ejecutados = []
        self.comandos_deshechos = []
    
    def ejecutar(self, comando, *args, **kwargs):
        """Ejecuta un comando y lo añade al historial."""
        resultado = comando(*args, **kwargs)
        self.comandos_ejecutados.append((comando, args, kwargs, resultado))
        self.comandos_deshechos.clear()  # Al ejecutar un nuevo comando, se pierde la capacidad de rehacer
        return resultado
    
    def deshacer(self):
        """Deshace el último comando ejecutado."""
        if not self.comandos_ejecutados:
            return None
        
        comando, args, kwargs, resultado = self.comandos_ejecutados.pop()
        self.comandos_deshechos.append((comando, args, kwargs, resultado))
        
        # Aquí normalmente ejecutaríamos la operación inversa
        # Para este ejemplo, solo informamos
        return f"Deshechos: {comando.__name__} con resultado {resultado}"
    
    def rehacer(self):
        """Rehace el último comando deshecho."""
        if not self.comandos_deshechos:
            return None
        
        comando, args, kwargs, resultado = self.comandos_deshechos.pop()
        nuevo_resultado = comando(*args, **kwargs)
        self.comandos_ejecutados.append((comando, args, kwargs, nuevo_resultado))
        
        return nuevo_resultado

# Comandos como funciones
def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

# Ejemplo de uso:
historial = Historial()
historial.ejecutar(sumar, 5, 3)       # Resultado: 8
historial.ejecutar(multiplicar, 4, 2)  # Resultado: 8
historial.deshacer()                  # Deshace: multiplicar
historial.ejecutar(restar, 10, 4)     # Resultado: 6
historial.deshacer()                  # Deshace: restar
historial.rehacer()                   # Rehace: restar, Resultado: 6

2. Patrón Template Method con funciones:

def algoritmo_template(inicializar=None, procesar=None, finalizar=None):
    """
    Implementa el patrón Template Method para un algoritmo genérico.
    
    Args:
        inicializar: Función para inicializar recursos (opcional)
        procesar: Función que realiza el procesamiento principal (requerida)
        finalizar: Función para limpiar recursos (opcional)
    
    Returns:
        Función que ejecuta el algoritmo completo
    """
    def algoritmo(datos):
        # Paso 1: Inicializar (opcional)
        contexto = {}
        if inicializar:
            contexto = inicializar(datos) or {}
        
        # Paso 2: Procesar (requerido)
        resultado = None
        if procesar:
            resultado = procesar(datos, contexto)
        
        # Paso 3: Finalizar (opcional)
        if finalizar:
            finalizar(datos, contexto, resultado)
        
        return resultado
    
    return algoritmo

# Ejemplo: Procesamiento de texto
def inicializar_procesamiento(texto):
    """Prepara el texto para su procesamiento."""
    print("Inicializando procesamiento de texto...")
    return {"palabras_originales": len(texto.split())}

def procesar_texto_mayusculas(texto, contexto):
    """Convierte el texto a mayúsculas."""
    print("Procesando texto: convirtiendo a mayúsculas...")
    return texto.upper()

def procesar_texto_minusculas(texto, contexto):
    """Convierte el texto a minúsculas."""
    print("Procesando texto: convirtiendo a minúsculas...")
    return texto.lower()

def finalizar_procesamiento(texto, contexto, resultado):
    """Muestra estadísticas del procesamiento."""
    print("Finalizando procesamiento...")
    palabras_originales = contexto.get("palabras_originales", 0)
    palabras_resultado = len(resultado.split())
    print(f"Palabras originales: {palabras_originales}")
    print(f"Palabras resultado: {palabras_resultado}")

# Creamos diferentes algoritmos con la misma estructura
procesar_mayusculas = algoritmo_template(
    inicializar_procesamiento, 
    procesar_texto_mayusculas,
    finalizar_procesamiento
)

procesar_minusculas = algoritmo_template(
    inicializar_procesamiento, 
    procesar_texto_minusculas,
    finalizar_procesamiento
)

# Uso
texto_ejemplo = "Este es un Ejemplo de TEXTO para procesar"
resultado1 = procesar_mayusculas(texto_ejemplo)
print(f"Resultado: {resultado1}")

resultado2 = procesar_minusculas(texto_ejemplo)
print(f"Resultado: {resultado2}")

3. Patrón Adapter con funciones:

# Supongamos que tenemos una API externa con una interfaz diferente
def api_externa_temperatura(ciudad):
    """API externa que devuelve temperatura en Fahrenheit."""
    # Simulamos llamada a API externa
    temperaturas = {
        "madrid": 86,
        "barcelona": 82,
        "sevilla": 95,
        "bilbao": 75
    }
    return {
        "ciudad": ciudad,
        "temp_f": temperaturas.get(ciudad.lower(), 70),
        "unidad": "F"
    }

# Nuestro sistema espera temperaturas en Celsius
def mostrar_clima(datos_clima):
    """
    Función cliente que espera datos en formato:
    {
        "ciudad": str,
        "temperatura": float,
        "unidad": "C"
    }
    """
    print(f"Clima en {datos_clima['ciudad']}: {datos_clima['temperatura']}°{datos_clima['unidad']}")

# Adapter para convertir la interfaz
def adapter_temperatura(api_func):
    """
    Adapter que convierte el formato de la API externa al formato esperado.
    También convierte Fahrenheit a Celsius.
    """
    def wrapper(ciudad):
        datos_api = api_func(ciudad)
        # Convertir Fahrenheit a Celsius: (F - 32) * 5/9
        temp_c = round((datos_api["temp_f"] - 32) * 5/9, 1)
        return {
            "ciudad": datos_api["ciudad"],
            "temperatura": temp_c,
            "unidad": "C"
        }
    return wrapper

# Creamos la versión adaptada de la API
api_temperatura_adaptada = adapter_temperatura(api_externa_temperatura)

# Uso del adapter
datos_madrid = api_temperatura_adaptada("Madrid")
mostrar_clima(datos_madrid)

4. Patrón Proxy con funciones:

def crear_proxy(funcion, verificador_acceso=None, cache=False):
    """
    Crea un proxy para controlar el acceso a una función.
    
    Args:
        funcion: La función objetivo a la que se controla el acceso
        verificador_acceso: Función que determina si se permite el acceso
        cache: Si es True, se cachean los resultados
    
    Returns:
        Función proxy que controla el acceso a la función objetivo
    """
    # Caché para resultados
    resultados_cache = {}
    
    def proxy(*args, **kwargs):
        # Verificar acceso si hay verificador
        if verificador_acceso and not verificador_acceso(*args, **kwargs):
            return "Acceso denegado"
        
        # Usar caché si está habilitada
        if cache:
            # Creamos una clave para la caché basada en los argumentos
            key = str(args) + str(sorted(kwargs.items()))
            if key in resultados_cache:
                print(f"Resultado obtenido de caché para {funcion.__name__}")
                return resultados_cache[key]
        
        # Ejecutar la función objetivo
        resultado = funcion(*args, **kwargs)
        
        # Guardar en caché si está habilitada
        if cache:
            key = str(args) + str(sorted(kwargs.items()))
            resultados_cache[key] = resultado
            
        return resultado
    
    return proxy

# Ejemplo: Función costosa que queremos proteger y cachear
def operacion_costosa(n):
    """Una operación que toma tiempo o recursos."""
    print(f"Ejecutando operación costosa para n={n}...")
    import time
    time.sleep(1)  # Simulamos operación costosa
    return n ** 2

# Función para verificar acceso
def verificar_acceso(n, **kwargs):
    """Verifica si se permite el acceso basado en el valor de n."""
    return n < 100  # Solo permitimos valores menores a 100

# Creamos el proxy
operacion_proxy = crear_proxy(operacion_costosa, verificador_acceso=verificar_acceso, cache=True)

# Uso del proxy
print(operacion_proxy(5))        # Acceso permitido, ejecución normal
print(operacion_proxy(5))        # Acceso permitido, resultado de caché
print(operacion_proxy(200))      # Acceso denegado

5. Patrón Composite con funciones:

def crear_operacion_compuesta(operaciones):
    """
    Crea una función compuesta que ejecuta múltiples operaciones sobre datos.
    Implementa el patrón Composite para tratar operaciones individuales y compuestas uniformemente.
    
    Args:
        operaciones: Lista de funciones a aplicar
    
    Returns:
        Función compuesta que aplica todas las operaciones
    """
    def operacion_compuesta(datos):
        resultado = datos
        for op in operaciones:
            resultado = op(resultado)
        return resultado
    
    return operacion_compuesta

# Operaciones individuales (equivalentes a "hojas" en el patrón Composite)
def duplicar_numeros(datos):
    """Duplica todos los números en una lista."""
    return [x * 2 for x in datos]

def filtrar_positivos(datos):
    """Filtra solo los números positivos."""
    return [x for x in datos if x > 0]

def sumar_uno(datos):
    """Suma 1 a cada número."""
    return [x + 1 for x in datos]

# Crear operaciones compuestas (equivalentes a "composites")
operacion1 = crear_operacion_compuesta([filtrar_positivos, duplicar_numeros])
operacion2 = crear_operacion_compuesta([sumar_uno, filtrar_positivos])

# Operación más compleja que usa las anteriores
operacion_compleja = crear_operacion_compuesta([
    operacion1,
    sumar_uno,
    operacion2
])

# Uso del patrón Composite
datos = [-2, -1, 0, 1, 2, 3]
print(f"Datos originales: {datos}")
print(f"Operación 1 (filtrar positivos y duplicar): {operacion1(datos)}")
print(f"Operación 2 (sumar uno y filtrar positivos): {operacion2(datos)}")
print(f"Operación compleja: {operacion_compleja(datos)}")
"""
