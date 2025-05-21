"""
Ejercicio 1: Excepciones Personalizadas

Objetivo: Aprender a crear y utilizar excepciones personalizadas para representar errores específicos en tu aplicación.

Instrucciones:
1. Crea una jerarquía de excepciones personalizadas para un sistema de validación de datos.
2. Implementa al menos tres tipos diferentes de excepciones derivadas de una clase base común.
3. Usa estas excepciones en funciones de validación y captúralas adecuadamente.
"""

# Crear una jerarquía de excepciones personalizadas
class ValidacionError(Exception):
    """Clase base para excepciones de validación."""
    def __init__(self, mensaje="Error de validación", valor=None):
        self.mensaje = mensaje
        self.valor = valor
        super().__init__(f"{mensaje}: {valor}" if valor else mensaje)

class NumeroError(ValidacionError):
    """Excepción para errores en validación de números."""
    def __init__(self, mensaje="Error en validación numérica", valor=None):
        super().__init__(mensaje, valor)

class TextoError(ValidacionError):
    """Excepción para errores en validación de texto."""
    def __init__(self, mensaje="Error en validación de texto", valor=None):
        super().__init__(mensaje, valor)

class FormatoError(ValidacionError):
    """Excepción para errores en formato de datos."""
    def __init__(self, mensaje="Error en formato de datos", valor=None):
        super().__init__(mensaje, valor)


# Funciones de validación que utilizan estas excepciones
def validar_edad(edad):
    """Valida que la edad sea un número entre 0 y 120."""
    try:
        edad_num = int(edad)
    except ValueError:
        raise NumeroError("La edad debe ser un número entero", edad)
    
    if edad_num < 0:
        raise NumeroError("La edad no puede ser negativa", edad_num)
    if edad_num > 120:
        raise NumeroError("La edad parece demasiado alta", edad_num)
    
    return edad_num

def validar_nombre(nombre):
    """Valida que el nombre sea un texto no vacío con solo letras y espacios."""
    if not isinstance(nombre, str):
        raise TextoError("El nombre debe ser un texto", nombre)
    
    if not nombre.strip():
        raise TextoError("El nombre no puede estar vacío")
    
    if not all(c.isalpha() or c.isspace() for c in nombre):
        raise TextoError("El nombre debe contener solo letras y espacios", nombre)
    
    return nombre.strip()

def validar_codigo_postal(cp):
    """Valida que el código postal tenga el formato correcto (5 dígitos en España)."""
    if not isinstance(cp, str):
        raise FormatoError("El código postal debe ser una cadena de texto", cp)
    
    if len(cp) != 5 or not cp.isdigit():
        raise FormatoError("El código postal debe tener 5 dígitos", cp)
    
    return cp


def main():
    # Lista de datos para validar
    datos = [
        {"nombre": "Ana García", "edad": "28", "codigo_postal": "28001"},
        {"nombre": "Juan123", "edad": "30", "codigo_postal": "12345"},
        {"nombre": "", "edad": "-5", "codigo_postal": "1234A"},
        {"nombre": "María López", "edad": "130", "codigo_postal": "50001"},
    ]
    
    # Validar cada conjunto de datos
    for i, persona in enumerate(datos):
        print(f"\n=== Validando persona {i+1} ===")
        print(f"Datos originales: {persona}")
        
        try:
            nombre_validado = validar_nombre(persona["nombre"])
            edad_validada = validar_edad(persona["edad"])
            cp_validado = validar_codigo_postal(persona["codigo_postal"])
            
            print("✓ Todos los datos son válidos:")
            print(f"  - Nombre: {nombre_validado}")
            print(f"  - Edad: {edad_validada}")
            print(f"  - Código postal: {cp_validado}")
        
        except NumeroError as e:
            print(f"✗ Error en validación numérica: {e}")
        
        except TextoError as e:
            print(f"✗ Error en validación de texto: {e}")
        
        except FormatoError as e:
            print(f"✗ Error en formato: {e}")
        
        except ValidacionError as e:
            # Captura cualquier otro error de validación no manejado específicamente
            print(f"✗ Error de validación genérico: {e}")

if __name__ == "__main__":
    main()
