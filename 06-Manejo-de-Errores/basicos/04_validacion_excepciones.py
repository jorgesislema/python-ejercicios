"""
Ejercicio 4: Validación con Excepciones

Objetivo: Practicar la validación de datos usando excepciones.

Instrucciones:
1. Crea una función para validar la edad de una persona.
2. La edad debe ser un entero entre 0 y 120.
3. Lanza una excepción ValueError con un mensaje adecuado si la validación falla.
4. Usa bloques try-except para manejar estas excepciones en el programa principal.
"""

def validar_edad(edad):
    """
    Valida que una edad sea un número entero entre 0 y 120.
    Lanza ValueError si la validación falla.
    """
    # Convertir a entero (podría lanzar ValueError si no es convertible)
    edad = int(edad)
    
    # Validar el rango
    if edad < 0 or edad > 120:
        raise ValueError(f"La edad debe estar entre 0 y 120 años, pero se recibió {edad}.")
    
    return edad

def solicitar_edad():
    """Solicita y valida la edad del usuario."""
    try:
        edad_str = input("Por favor, introduce tu edad: ")
        edad_validada = validar_edad(edad_str)
        print(f"Tu edad ({edad_validada} años) ha sido registrada correctamente.")
        return edad_validada
    
    except ValueError as e:
        # Capturar errores de conversión y validación
        print(f"Error de validación: {e}")
        return None

# Ejecutar el programa
if __name__ == "__main__":
    edad = solicitar_edad()
    
    if edad is not None:
        # Continuar con el programa...
        if edad < 18:
            print("Eres menor de edad.")
        else:
            print("Eres mayor de edad.")
