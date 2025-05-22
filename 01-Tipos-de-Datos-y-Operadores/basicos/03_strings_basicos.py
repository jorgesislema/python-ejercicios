"""
Ejercicio 3: Manipulación Básica de Cadenas

Objetivo: Aprender a trabajar con cadenas de texto y sus operaciones básicas.

Instrucciones:
1. Crea variables de tipo string con diferentes contenidos.
2. Realiza operaciones de concatenación, repetición y acceso a caracteres.
3. Utiliza métodos básicos como .upper(), .lower(), .strip(), etc.
4. Usa operadores de pertenencia (in, not in) con strings.
"""

def main():
    # Declaración de variables de tipo string
    nombre = "Ana"
    apellido = "Martínez"
    frase = "  Python es un lenguaje de programación poderoso  "
    
    # Concatenación de strings
    print("=== Concatenación de Strings ===")
    nombre_completo = nombre + " " + apellido
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Nombre completo: {nombre_completo}")
    
    # Concatenación con operador +=
    saludo = "Hola"
    saludo += ", " + nombre_completo
    print(f"Saludo: {saludo}")
    
    # Repetición de strings
    print("\n=== Repetición de Strings ===")
    separador = "-" * 20
    print(f"Separador: {separador}")
    repeticion = nombre * 3
    print(f"Nombre repetido 3 veces: {repeticion}")
    
    # Acceso a caracteres individuales
    print("\n=== Acceso a Caracteres ===")
    print(f"Primera letra del nombre: {nombre[0]}")
    print(f"Última letra del apellido: {apellido[-1]}")
    
    # Rebanadas (slicing)
    print("\n=== Rebanadas (Slicing) ===")
    print(f"Primeras tres letras del nombre: {nombre[:3]}")
    print(f"Últimas tres letras del apellido: {apellido[-3:]}")
    
    # Métodos básicos de strings
    print("\n=== Métodos Básicos de Strings ===")
    print(f"Frase original: '{frase}'")
    print(f"En mayúsculas: '{frase.upper()}'")
    print(f"En minúsculas: '{frase.lower()}'")
    print(f"Primera letra de cada palabra en mayúscula: '{frase.title()}'")
    print(f"Sin espacios al inicio y final: '{frase.strip()}'")
    
    # Búsqueda en strings
    print("\n=== Búsqueda en Strings ===")
    buscar = "lenguaje"
    print(f"¿'{buscar}' está en la frase? {'lenguaje' in frase}")
    print(f"¿'Java' no está en la frase? {'Java' not in frase}")
    print(f"Posición de '{buscar}' en la frase: {frase.find(buscar)}")
    
    # Reemplazo en strings
    print("\n=== Reemplazo en Strings ===")
    nuevo_texto = frase.replace("Python", "JavaScript")
    print(f"Frase con reemplazo: '{nuevo_texto}'")
    
    # División de strings
    print("\n=== División de Strings ===")
    palabras = frase.strip().split()
    print(f"Palabras en la frase: {palabras}")
    print(f"Número de palabras: {len(palabras)}")
    
    # Unión de strings
    print("\n=== Unión de Strings ===")
    nueva_frase = "-".join(palabras)
    print(f"Palabras unidas con guion: '{nueva_frase}'")
    
    # Ejercicios para el usuario
    print("\n=== EJERCICIOS PARA PRACTICAR ===")
    print("1. Crea una variable con tu nombre completo y extrae tus iniciales")
    print("2. Cuenta cuántas veces aparece la letra 'a' (mayúscula o minúscula) en tu nombre completo")
    print("3. Crea una función que reciba una frase y devuelva la misma frase pero con cada palabra invertida")
    print("4. Usa la función split() para dividir la frase 'Python,Java,C++,JavaScript' usando la coma como separador")

if __name__ == "__main__":
    main()
