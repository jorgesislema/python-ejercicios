"""
Ejercicio 5: Entrada y Salida Básica

Objetivo: Aprender a interactuar con el usuario mediante entrada y salida de datos.

Instrucciones:
1. Utiliza la función input() para solicitar datos al usuario.
2. Convierte la entrada del usuario a diferentes tipos de datos.
3. Formatea la salida con diferentes métodos (formato f-string, .format(), etc.).
4. Crea un pequeño programa interactivo que utilice input y output.
"""

def main():
    # Solicitar datos básicos al usuario
    print("=== Recopilación de Datos Personales ===")
    nombre = input("Introduce tu nombre: ")
    
    # Solicitar y convertir un número entero
    try:
        edad = int(input("Introduce tu edad: "))
    except ValueError:
        print("Error: Debes introducir un número entero para la edad.")
        edad = 0
    
    # Solicitar y convertir un número decimal
    try:
        altura = float(input("Introduce tu altura en metros (ejemplo: 1.75): "))
    except ValueError:
        print("Error: Debes introducir un número decimal para la altura.")
        altura = 0.0
    
    # Solicitar una respuesta de tipo sí/no
    es_estudiante_str = input("¿Eres estudiante? (s/n): ").lower()
    es_estudiante = es_estudiante_str in ['s', 'si', 'sí', 'y', 'yes']
    
    # Mostrar los datos utilizando diferentes formatos de salida
    print("\n=== Datos Introducidos ===")
    
    # Formato con f-strings (Python 3.6+)
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad} años")
    
    # Formato con método .format()
    print("Altura: {:.2f} metros".format(altura))
    
    # Formato con % (estilo clásico)
    print("¿Es estudiante?: %s" % ("Sí" if es_estudiante else "No"))
    
    # Cálculos básicos con los datos introducidos
    print("\n=== Información Adicional ===")
    
    # Calcular el año de nacimiento aproximado
    import datetime
    anio_actual = datetime.datetime.now().year
    anio_nacimiento = anio_actual - edad
    print(f"Año de nacimiento aproximado: {anio_nacimiento}")
    
    # Calcular el IMC si se proporciona el peso
    try:
        peso = float(input("\nIntroduce tu peso en kg para calcular el IMC: "))
        imc = peso / (altura ** 2)
        print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")
        
        # Categoría de IMC
        if imc < 18.5:
            categoria = "Bajo peso"
        elif imc < 25:
            categoria = "Peso normal"
        elif imc < 30:
            categoria = "Sobrepeso"
        else:
            categoria = "Obesidad"
        
        print(f"Categoría de IMC: {categoria}")
    except ValueError:
        print("Error: Debes introducir un número válido para el peso.")
    except ZeroDivisionError:
        print("Error: La altura no puede ser cero.")
    
    # Generar un saludo personalizado
    print("\n=== Saludo Personalizado ===")
    hora_actual = datetime.datetime.now().hour
    
    if 5 <= hora_actual < 12:
        saludo = "Buenos días"
    elif 12 <= hora_actual < 20:
        saludo = "Buenas tardes"
    else:
        saludo = "Buenas noches"
    
    if es_estudiante:
        mensaje = f"{saludo}, {nombre}. ¡Éxito en tus estudios!"
    else:
        mensaje = f"{saludo}, {nombre}. ¡Que tengas un excelente día!"
    
    print(mensaje)
    
    # Ejercicios para el usuario
    print("\n=== EJERCICIOS PARA PRACTICAR ===")
    print("1. Modifica este programa para solicitar la ciudad de residencia y mostrarla en el saludo")
    print("2. Añade una pregunta sobre el idioma preferido y personaliza el saludo según la respuesta")
    print("3. Solicita dos números al usuario y muestra el resultado de las operaciones básicas entre ellos")
    print("4. Crea un conversor de unidades que solicite una medida en metros y la convierta a cm, mm, km, pulgadas y pies")

if __name__ == "__main__":
    main()
