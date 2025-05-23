"""
Ejercicio 2: Closures en Python

Objetivo: Comprender y utilizar closures en Python.

Un closure es una función que recuerda los valores del entorno léxico en el que fue creada,
incluso cuando se ejecuta fuera de ese entorno. En Python, los closures son funciones que
tienen acceso a variables de un ámbito externo, incluso después de que la función externa
haya terminado su ejecución.

Instrucciones:
1. Estudiar qué son los closures y cómo funcionan en Python
2. Implementar ejemplos prácticos de closures
3. Comprender sus casos de uso y ventajas
"""

# ------------------------------------------------------------------------------------------
# 1. ¿Qué son los closures?
# ------------------------------------------------------------------------------------------
print("\n1. ¿Qué son los closures?")
print("-" * 70)
print("Un closure es una función que recuerda el entorno en que fue creada.")
print("Consiste en una función interna que tiene acceso a las variables de una función externa,")
print("incluso después de que la función externa haya terminado su ejecución.")

# Ejemplo básico de closure
def crear_saludo(saludo):
    """Función que crea un closure para saludar."""
    def saludar(nombre):
        """Closure que utiliza la variable 'saludo' de la función externa."""
        return f"{saludo}, {nombre}!"
    
    return saludar  # Retornamos la función interna (closure)

# Creamos dos closures diferentes
saludo_formal = crear_saludo("Buenos días")
saludo_informal = crear_saludo("¡Hola")

# Usamos los closures
print("\nEjemplo de closures básicos:")
print(saludo_formal("Ana"))       # Output: Buenos días, Ana!
print(saludo_informal("Carlos"))  # Output: ¡Hola, Carlos!

# ------------------------------------------------------------------------------------------
# 2. Cómo funcionan los closures
# ------------------------------------------------------------------------------------------
print("\n2. Cómo funcionan los closures")
print("-" * 70)
print("Un closure 'recuerda' el entorno donde fue definido.")
print("Esto incluye las variables no locales (variables de la función externa).")

def contador():
    """Función que crea un closure para contar."""
    cuenta = 0
    
    def incrementar():
        """Closure que recuerda y modifica la variable 'cuenta'."""
        nonlocal cuenta  # Declaramos cuenta como no local para poder modificarla
        cuenta += 1
        return cuenta
    
    return incrementar

# Creamos dos contadores independientes
contador1 = contador()
contador2 = contador()

print("\nEjemplo de closures con estado:")
print(f"Contador 1: {contador1()}")  # Output: 1
print(f"Contador 1: {contador1()}")  # Output: 2
print(f"Contador 1: {contador1()}")  # Output: 3
print(f"Contador 2: {contador2()}")  # Output: 1
print(f"Contador 2: {contador2()}")  # Output: 2

# ------------------------------------------------------------------------------------------
# 3. Casos de uso prácticos
# ------------------------------------------------------------------------------------------
print("\n3. Casos de uso prácticos")
print("-" * 70)
print("Los closures son útiles para:")
print("- Crear funciones con estado")
print("- Crear funciones configurables")
print("- Implementar decoradores")
print("- Evitar el uso de variables globales")

# Ejemplo: Función multiplicadora
def crear_multiplicador(factor):
    """Crea una función que multiplica por un factor específico."""
    def multiplicar(numero):
        return numero * factor
    
    return multiplicar

# Creamos multiplicadores específicos
duplicar = crear_multiplicador(2)
triplicar = crear_multiplicador(3)
multiplicar_por_10 = crear_multiplicador(10)

print("\nEjemplo de multiplicadores:")
print(f"Duplicar 5: {duplicar(5)}")             # Output: 10
print(f"Triplicar 5: {triplicar(5)}")           # Output: 15
print(f"Multiplicar 5 por 10: {multiplicar_por_10(5)}")  # Output: 50

# Ejemplo: Función con información privada
def crear_cuenta_bancaria(saldo_inicial):
    """Crea una cuenta bancaria con un saldo inicial."""
    saldo = saldo_inicial
    
    def operacion_bancaria(cantidad, tipo="deposito"):
        """Realiza operaciones en la cuenta bancaria."""
        nonlocal saldo
        
        if tipo == "deposito":
            saldo += cantidad
            return f"Depósito de {cantidad}€ realizado. Nuevo saldo: {saldo}€"
        elif tipo == "retiro":
            if cantidad <= saldo:
                saldo -= cantidad
                return f"Retiro de {cantidad}€ realizado. Nuevo saldo: {saldo}€"
            else:
                return f"Fondos insuficientes. Saldo actual: {saldo}€"
        else:
            return "Operación no válida"
    
    return operacion_bancaria

# Creamos una cuenta bancaria
mi_cuenta = crear_cuenta_bancaria(1000)

print("\nEjemplo de cuenta bancaria:")
print(mi_cuenta(500, "deposito"))    # Output: Depósito de 500€ realizado. Nuevo saldo: 1500€
print(mi_cuenta(200, "retiro"))      # Output: Retiro de 200€ realizado. Nuevo saldo: 1300€
print(mi_cuenta(2000, "retiro"))     # Output: Fondos insuficientes. Saldo actual: 1300€

# ------------------------------------------------------------------------------------------
# 4. Diferencia entre closures y clases
# ------------------------------------------------------------------------------------------
print("\n4. Diferencia entre closures y clases")
print("-" * 70)
print("Los closures son más ligeros que las clases para casos simples de encapsulamiento.")
print("Sin embargo, las clases ofrecen más funcionalidades para casos complejos.")

# Implementación de un contador usando una clase
class Contador:
    def __init__(self):
        self.cuenta = 0
    
    def incrementar(self):
        self.cuenta += 1
        return self.cuenta

# Comparación
contador_closure = contador()
contador_clase = Contador()

print("\nComparación entre closure y clase:")
print(f"Contador (closure): {contador_closure()}")  # Output: 1 (o el valor actual si ya se usó)
print(f"Contador (clase): {contador_clase.incrementar()}")  # Output: 1

# ------------------------------------------------------------------------------------------
# Ejercicios propuestos
# ------------------------------------------------------------------------------------------
print("\nEjercicios propuestos:")
print("-" * 70)
print("1. Crea un closure que genere una secuencia de números de Fibonacci.")
print("2. Implementa un closure para manejar un registro de tareas (añadir, completar, listar).")
print("3. Desarrolla un closure que simule una calculadora con memoria.")
print("4. Crea un closure para validar contraseñas según ciertos criterios configurables.")
print("5. Implementa un generador de IDs único utilizando closures.")

"""
Soluciones a los ejercicios propuestos:

1. Generador de Fibonacci:

def crear_generador_fibonacci():
    a, b = 0, 1
    
    def obtener_siguiente():
        nonlocal a, b
        resultado = a
        a, b = b, a + b
        return resultado
    
    return obtener_siguiente

2. Registro de tareas:

def crear_registro_tareas():
    tareas = []
    
    def gestor_tareas(accion, tarea=None):
        nonlocal tareas
        
        if accion == "añadir" and tarea:
            tareas.append({"tarea": tarea, "completada": False})
            return f"Tarea '{tarea}' añadida"
        elif accion == "completar" and tarea:
            for t in tareas:
                if t["tarea"] == tarea:
                    t["completada"] = True
                    return f"Tarea '{tarea}' completada"
            return f"Tarea '{tarea}' no encontrada"
        elif accion == "listar":
            return tareas
        else:
            return "Acción no válida"
    
    return gestor_tareas

3. Calculadora con memoria:

def crear_calculadora():
    memoria = 0
    
    def calcular(operacion, valor=None):
        nonlocal memoria
        
        if operacion == "suma":
            memoria += valor
        elif operacion == "resta":
            memoria -= valor
        elif operacion == "multiplicacion":
            memoria *= valor
        elif operacion == "division":
            if valor != 0:
                memoria /= valor
            else:
                return "Error: División por cero"
        elif operacion == "reset":
            memoria = 0
        elif operacion == "valor":
            return memoria
        else:
            return "Operación no válida"
        
        return memoria
    
    return calcular

4. Validador de contraseñas:

def crear_validador_contraseña(longitud_min=8, requiere_mayusculas=True, requiere_numeros=True):
    def validar(contraseña):
        if len(contraseña) < longitud_min:
            return False
        
        if requiere_mayusculas and not any(c.isupper() for c in contraseña):
            return False
        
        if requiere_numeros and not any(c.isdigit() for c in contraseña):
            return False
        
        return True
    
    return validar

5. Generador de IDs:

def crear_generador_id(prefijo="ID", inicio=1):
    contador = inicio
    
    def generar_id():
        nonlocal contador
        id_generado = f"{prefijo}-{contador:04d}"
        contador += 1
        return id_generado
    
    return generar_id
"""
