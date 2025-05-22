"""
Ejercicio 4: Operadores Booleanos y de Comparación

Objetivo: Entender el funcionamiento de los operadores booleanos y de comparación.

Instrucciones:
1. Utiliza operadores de comparación (==, !=, >, <, >=, <=) con diferentes tipos de datos.
2. Trabaja con operadores lógicos (and, or, not).
3. Combina operadores de comparación y lógicos en expresiones complejas.
4. Evalúa la precedencia de operadores en expresiones booleanas.
"""

def main():
    # Variables para los ejemplos
    a = 10
    b = 5
    c = 10
    nombre1 = "Ana"
    nombre2 = "Carlos"
    es_estudiante = True
    tiene_descuento = False
    
    # Operadores de comparación
    print("=== Operadores de Comparación ===")
    print(f"{a} == {c}: {a == c}")  # Igualdad
    print(f"{a} == {b}: {a == b}")
    print(f"{a} != {b}: {a != b}")  # Desigualdad
    print(f"{a} > {b}: {a > b}")    # Mayor que
    print(f"{a} < {b}: {a < b}")    # Menor que
    print(f"{a} >= {c}: {a >= c}")  # Mayor o igual que
    print(f"{a} <= {b}: {a <= b}")  # Menor o igual que
    
    # Comparaciones con strings
    print("\n=== Comparaciones con Strings ===")
    print(f"'{nombre1}' == '{nombre2}': {nombre1 == nombre2}")
    print(f"'{nombre1}' != '{nombre2}': {nombre1 != nombre2}")
    print(f"'{nombre1}' < '{nombre2}': {nombre1 < nombre2}")  # Comparación alfabética
    print(f"len('{nombre1}') < len('{nombre2}'): {len(nombre1) < len(nombre2)}")  # Comparación de longitudes
    
    # Operadores lógicos
    print("\n=== Operadores Lógicos ===")
    print(f"True and True: {True and True}")
    print(f"True and False: {True and False}")
    print(f"False and False: {False and False}")
    print(f"True or False: {True or False}")
    print(f"False or False: {False or False}")
    print(f"not True: {not True}")
    print(f"not False: {not False}")
    
    # Operadores lógicos con variables
    print("\n=== Operadores Lógicos con Variables ===")
    print(f"es_estudiante: {es_estudiante}")
    print(f"tiene_descuento: {tiene_descuento}")
    print(f"es_estudiante and tiene_descuento: {es_estudiante and tiene_descuento}")
    print(f"es_estudiante or tiene_descuento: {es_estudiante or tiene_descuento}")
    print(f"not es_estudiante: {not es_estudiante}")
    
    # Combinaciones de operadores
    print("\n=== Combinaciones de Operadores ===")
    expresion1 = (a > b) and (nombre1 < nombre2)
    print(f"(a > b) and (nombre1 < nombre2): {expresion1}")
    
    expresion2 = (a == b) or (c == a)
    print(f"(a == b) or (c == a): {expresion2}")
    
    expresion3 = not ((a < b) or (nombre1 == nombre2))
    print(f"not ((a < b) or (nombre1 == nombre2)): {expresion3}")
    
    # Cortocircuito en operadores lógicos
    print("\n=== Cortocircuito en Operadores Lógicos ===")
    print("En 'and', si el primer operando es False, el segundo no se evalúa.")
    print("En 'or', si el primer operando es True, el segundo no se evalúa.")
    
    # Ejemplo práctico
    print("\n=== Ejemplo Práctico ===")
    edad = 20
    tiene_carnet = True
    puede_conducir = edad >= 18 and tiene_carnet
    print(f"Edad: {edad}, Tiene carnet: {tiene_carnet}")
    print(f"¿Puede conducir?: {puede_conducir}")
    
    # Precedencia de operadores
    print("\n=== Precedencia de Operadores ===")
    # La precedencia de mayor a menor es: not, and, or
    resultado1 = True or False and False  # Equivale a: True or (False and False)
    resultado2 = (True or False) and False
    print(f"True or False and False: {resultado1}")
    print(f"(True or False) and False: {resultado2}")
    
    # Ejercicios para el usuario
    print("\n=== EJERCICIOS PARA PRACTICAR ===")
    print("1. Crea una expresión que determine si un número está en el rango de 10 a 20 (inclusive)")
    print("2. Escribe una condición que evalúe si una persona puede jubilarse (edad >= 65 o años_trabajados >= 40)")
    print("3. Crea una expresión que compruebe si una cadena empieza por 'A' y termina por '.'")
    print("4. Evalúa si un año es bisiesto (divisible por 4 y no por 100, o divisible por 400)")

if __name__ == "__main__":
    main()
