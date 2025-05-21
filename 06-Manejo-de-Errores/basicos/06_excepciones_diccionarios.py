"""
Ejercicio 6: Manejo de Excepciones con Diccionarios

Objetivo: Practicar el manejo de excepciones al acceder a claves en diccionarios.

Instrucciones:
1. Crea un diccionario con información personal (nombre, edad, etc.).
2. Implementa una función que acceda de forma segura a cualquier clave del diccionario.
3. La función debe manejar el error KeyError y devolver un valor por defecto.
"""

def obtener_valor_seguro(diccionario, clave, valor_por_defecto="No disponible"):
    """
    Obtiene un valor del diccionario de forma segura.
    Si la clave no existe, devuelve un valor por defecto.
    
    Args:
        diccionario: El diccionario donde buscar
        clave: La clave a buscar
        valor_por_defecto: El valor a devolver si la clave no existe
        
    Returns:
        El valor asociado a la clave o el valor por defecto
    """
    try:
        return diccionario[clave]
    except KeyError:
        return valor_por_defecto

def main():
    # Diccionario con información personal
    persona = {
        "nombre": "Ana García",
        "edad": 28,
        "ciudad": "Madrid",
        "profesion": "Ingeniera"
    }
    
    # Lista de claves a buscar (algunas existen, otras no)
    claves_a_buscar = ["nombre", "edad", "ciudad", "telefono", "email", "profesion"]
    
    print("Información personal:")
    for clave in claves_a_buscar:
        valor = obtener_valor_seguro(persona, clave)
        print(f"  - {clave.capitalize()}: {valor}")
    
    # Probar con valor por defecto personalizado
    telefono = obtener_valor_seguro(persona, "telefono", "Número no registrado")
    print(f"\nTeléfono con mensaje personalizado: {telefono}")

if __name__ == "__main__":
    main()
