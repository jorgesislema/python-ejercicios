"""
Ejercicio 9: Errores de Sintaxis vs Excepciones

Objetivo: Comprender la diferencia entre errores de sintaxis y excepciones en tiempo de ejecución.

Instrucciones:
1. Explora diferentes tipos de errores de sintaxis y comenta por qué ocurren.
2. Crea ejemplos de excepciones en tiempo de ejecución.
3. Aprende a identificar y corregir ambos tipos de errores.
"""

# Este archivo contiene ejemplos comentados de errores de sintaxis
# y ejemplos ejecutables de excepciones en tiempo de ejecución.

def mostrar_ejemplos_errores_sintaxis():
    """
    Muestra ejemplos de errores de sintaxis (comentados para que el script pueda ejecutarse).
    Los errores de sintaxis ocurren durante la fase de análisis del código y evitan que el programa se ejecute.
    """
    print("=== Ejemplos de errores de sintaxis (comentados) ===")
    
    # Ejemplo 1: Paréntesis sin cerrar
    # print("Hola mundo"
    print("1. Paréntesis sin cerrar: Python espera un ')' al final")
    
    # Ejemplo 2: Uso incorrecto de palabras clave
    # if = 42:
    #     print("Esto nunca se ejecutará")
    print("2. Uso incorrecto de palabras clave: 'if' no puede ser usado como variable")
    
    # Ejemplo 3: Indentación incorrecta
    # def funcion():
    # print("Indentación incorrecta")
    print("3. Indentación incorrecta: el cuerpo de la función debe estar indentado")
    
    # Ejemplo 4: Comillas sin cerrar
    # mensaje = "Hola mundo
    print("4. Comillas sin cerrar: Python espera que se cierren las comillas")
    
    # Ejemplo 5: Dos puntos faltantes
    # if True
    #     print("Falta algo...")
    print("5. Dos puntos faltantes: después de 'if True' debe ir ':'")

def demostrar_excepciones_tiempo_ejecucion():
    """
    Demuestra excepciones que ocurren durante la ejecución del programa.
    Estas excepciones pueden ser manejadas con try-except.
    """
    print("\n=== Excepciones en tiempo de ejecución (ejecutables) ===")
    
    # Ejemplo 1: División por cero
    try:
        resultado = 10 / 0
    except ZeroDivisionError as e:
        print(f"1. ZeroDivisionError: {e}")
    
    # Ejemplo 2: Índice fuera de rango
    try:
        lista = [1, 2, 3]
        elemento = lista[10]
    except IndexError as e:
        print(f"2. IndexError: {e}")
    
    # Ejemplo 3: Clave no existe en diccionario
    try:
        diccionario = {"a": 1, "b": 2}
        valor = diccionario["z"]
    except KeyError as e:
        print(f"3. KeyError: {e}")
    
    # Ejemplo 4: Error de tipo
    try:
        texto = "123"
        resultado = texto + 456
    except TypeError as e:
        print(f"4. TypeError: {e}")
    
    # Ejemplo 5: Error de valor
    try:
        numero = int("abc")
    except ValueError as e:
        print(f"5. ValueError: {e}")

def practicar_correccion_errores():
    """
    Ejercicio práctico: Corregir errores en el siguiente código.
    El código original tiene errores que debes identificar y corregir.
    """
    print("\n=== Ejercicio: Corregir errores ===")
    
    # Código con errores (ahora corregido):
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
            
        # Calcular año de nacimiento aproximado
        import datetime
        anio_actual = datetime.datetime.now().year
        anio_nacimiento = anio_actual - edad
        
        print(f"Naciste aproximadamente en el año {anio_nacimiento}")
        
        # Comprobar si es mayor de edad
        if edad >= 18:
            print("Eres mayor de edad")
        else:
            print("Eres menor de edad")
            
    except ValueError as e:
        print(f"Error: {e}")

def main():
    mostrar_ejemplos_errores_sintaxis()
    demostrar_excepciones_tiempo_ejecucion()
    practicar_correccion_errores()

if __name__ == "__main__":
    main()
