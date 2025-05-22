"""
Ejercicio 4: Expresiones Regulares

Objetivo: Aprender a utilizar expresiones regulares para buscar, validar y manipular patrones en strings.

Instrucciones:
1. Familiarizarse con la sintaxis básica de expresiones regulares.
2. Utilizar el módulo re para buscar, reemplazar y validar patrones.
3. Implementar soluciones a problemas comunes usando expresiones regulares.
4. Comprender la diferencia entre los diferentes modos de coincidencia.
"""

import re

def main():
    # Introducción a expresiones regulares
    print("=== Introducción a Expresiones Regulares ===")
    print("Las expresiones regulares son patrones que describen conjuntos de strings.")
    print("En Python, se utilizan a través del módulo 're'.")
    
    # Patrones básicos
    print("\n=== Patrones Básicos ===")
    
    # Coincidencia exacta
    texto = "Python es un lenguaje de programación potente y fácil de aprender."
    patron = "Python"
    resultado = re.search(patron, texto)
    
    print(f"Texto: '{texto}'")
    print(f"Patrón: '{patron}'")
    print(f"¿Coincidencia? {'Sí' if resultado else 'No'}")
    if resultado:
        print(f"Posición: {resultado.start()}-{resultado.end()}")
        print(f"Texto coincidente: '{resultado.group()}'")
    
    # Metacaracteres
    print("\n=== Metacaracteres ===")
    
    # . (punto) - Cualquier carácter excepto nueva línea
    patron = "P.th.n"
    print(f"Patrón '.': '{patron}' -> {bool(re.search(patron, texto))}")
    
    # ^ (acento circunflejo) - Inicio de línea
    patron = "^Python"
    print(f"Patrón '^': '{patron}' -> {bool(re.search(patron, texto))}")
    
    # $ (signo de dólar) - Fin de línea
    patron = "aprender.$"
    print(f"Patrón '$': '{patron}' -> {bool(re.search(patron, texto))}")
    
    # * (asterisco) - 0 o más repeticiones
    patron = "P.*n"
    print(f"Patrón '*': '{patron}' -> {bool(re.search(patron, texto))}")
    
    # + (signo más) - 1 o más repeticiones
    patron = "P.+n"
    print(f"Patrón '+': '{patron}' -> {bool(re.search(patron, texto))}")
    
    # ? (signo de interrogación) - 0 o 1 repetición
    patron = "Pytho?n"
    print(f"Patrón '?': '{patron}' -> {bool(re.search(patron, texto))}")
    
    # Cuantificadores
    print("\n=== Cuantificadores ===")
    
    texto_num = "Tengo 3 manzanas, 12 naranjas y 8 peras."
    
    # {n} - Exactamente n repeticiones
    patron = r"\d{2}"  # Números de 2 dígitos
    resultados = re.findall(patron, texto_num)
    print(f"Números de 2 dígitos: {resultados}")
    
    # {n,m} - Entre n y m repeticiones
    patron = r"\d{1,2}"  # Números de 1 o 2 dígitos
    resultados = re.findall(patron, texto_num)
    print(f"Números de 1 o 2 dígitos: {resultados}")
    
    # Clases de caracteres
    print("\n=== Clases de Caracteres ===")
    
    # [abc] - Cualquier carácter dentro de los corchetes
    patron = r"[aeiou]"  # Vocales
    resultados = re.findall(patron, texto)
    print(f"Vocales encontradas: {len(resultados)}")
    
    # [^abc] - Cualquier carácter excepto los que están dentro de los corchetes
    patron = r"[^aeiou\s]"  # Consonantes (excluyendo espacios)
    resultados = re.findall(patron, texto.lower())
    print(f"Consonantes encontradas: {len(resultados)}")
    
    # Secuencias especiales
    print("\n=== Secuencias Especiales ===")
    
    # \d - Dígito decimal
    patron = r"\d"  # Equivalente a [0-9]
    resultados = re.findall(patron, texto_num)
    print(f"Dígitos encontrados: {resultados}")
    
    # \D - No dígito
    patron = r"\D"
    resultados = re.findall(patron, texto_num)
    print(f"Caracteres no dígitos: {len(resultados)}")
    
    # \w - Carácter alfanumérico o guion bajo
    patron = r"\w"  # Equivalente a [a-zA-Z0-9_]
    resultados = re.findall(patron, texto)
    print(f"Caracteres alfanuméricos: {len(resultados)}")
    
    # \s - Espacio en blanco
    patron = r"\s"
    resultados = re.findall(patron, texto)
    print(f"Espacios en blanco: {len(resultados)}")
    
    # Grupos y Alternancia
    print("\n=== Grupos y Alternancia ===")
    
    # (abc) - Grupo de capturas
    texto_email = "Contacta con juan@example.com o maria@empresa.org"
    patron = r"(\w+)@(\w+)\.(\w+)"
    resultados = re.findall(patron, texto_email)
    print(f"Emails encontrados (usuario, dominio, extensión): {resultados}")
    
    # | (barra vertical) - Alternancia
    patron = r"com|org"
    resultados = re.findall(patron, texto_email)
    print(f"Extensiones 'com' u 'org': {resultados}")
    
    # Métodos del módulo re
    print("\n=== Métodos del Módulo re ===")
    
    # re.search() - Buscar la primera coincidencia
    texto_parrafos = """Primer párrafo con Python.
    Segundo párrafo sin coincidencia.
    Tercer párrafo menciona python en minúsculas."""
    
    patron = r"[Pp]ython"
    resultado = re.search(patron, texto_parrafos)
    print(f"re.search(): {resultado.group() if resultado else 'No encontrado'}")
    
    # re.match() - Coincidir desde el inicio del string
    resultado = re.match(patron, texto_parrafos)
    print(f"re.match(): {resultado.group() if resultado else 'No encontrado'}")
    
    # re.findall() - Encontrar todas las coincidencias
    resultados = re.findall(patron, texto_parrafos)
    print(f"re.findall(): {resultados}")
    
    # re.sub() - Sustituir coincidencias
    resultado = re.sub(patron, "Java", texto_parrafos)
    print(f"re.sub():\n{resultado}")
    
    # re.split() - Dividir string usando el patrón como separador
    texto_csv = "nombre,edad,email,telefono"
    resultado = re.split(r",", texto_csv)
    print(f"re.split(): {resultado}")
    
    # Banderas de expresiones regulares
    print("\n=== Banderas de Expresiones Regulares ===")
    
    # re.IGNORECASE o re.I - Ignorar mayúsculas/minúsculas
    patron = r"python"
    resultado = re.search(patron, texto_parrafos)
    print(f"Sin re.I: {resultado.group() if resultado else 'No encontrado'}")
    
    resultado = re.search(patron, texto_parrafos, re.IGNORECASE)
    print(f"Con re.I: {resultado.group() if resultado else 'No encontrado'}")
    
    # re.MULTILINE o re.M - Tratar ^ y $ como inicio y fin de cada línea
    patron = r"^Tercer"
    resultado = re.search(patron, texto_parrafos)
    print(f"Sin re.M: {resultado.group() if resultado else 'No encontrado'}")
    
    resultado = re.search(patron, texto_parrafos, re.MULTILINE)
    print(f"Con re.M: {resultado.group() if resultado else 'No encontrado'}")
    
    # Ejemplos prácticos
    print("\n=== Ejemplos Prácticos ===")
    
    # Validación de email
    def validar_email(email):
        patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(patron, email))
    
    emails = ["usuario@ejemplo.com", "usuario.nombre@subdominio.ejemplo.com", 
              "usuario@.com", "usuario@com", "@ejemplo.com"]
    
    print("Validación de emails:")
    for email in emails:
        print(f"'{email}': {'Válido' if validar_email(email) else 'Inválido'}")
    
    # Extracción de información de un texto
    texto_info = """
    Nombre: Juan Pérez
    Edad: 30 años
    Email: juan.perez@ejemplo.com
    Teléfono: +34 612 345 678
    """
    
    info = {}
    
    # Extraer nombre
    resultado = re.search(r"Nombre: ([\w\s]+)", texto_info)
    if resultado:
        info["nombre"] = resultado.group(1).strip()
    
    # Extraer edad
    resultado = re.search(r"Edad: (\d+)", texto_info)
    if resultado:
        info["edad"] = int(resultado.group(1))
    
    # Extraer email
    resultado = re.search(r"Email: ([\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,})", texto_info)
    if resultado:
        info["email"] = resultado.group(1)
    
    # Extraer teléfono
    resultado = re.search(r"Teléfono: ([+\d\s]+)", texto_info)
    if resultado:
        info["telefono"] = resultado.group(1).strip()
    
    print("\nInformación extraída:")
    for clave, valor in info.items():
        print(f"{clave.capitalize()}: {valor}")
    
    # Ejercicios para el usuario
    print("\n=== EJERCICIOS PARA PRACTICAR ===")
    print("1. Crea una función que valide si una contraseña cumple con ciertos requisitos (longitud mínima, mayúsculas, minúsculas, números, etc.)")
    print("2. Implementa un validador de números de tarjeta de crédito usando expresiones regulares")
    print("3. Desarrolla una función que extraiga todas las URLs de un texto HTML")
    print("4. Crea un programa que analice un texto y cuente la frecuencia de palabras, excluyendo palabras comunes como 'el', 'la', 'y', etc.")

if __name__ == "__main__":
    main()
