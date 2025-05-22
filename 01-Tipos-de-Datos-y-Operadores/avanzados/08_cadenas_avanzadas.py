"""
Ejercicio 8: Operaciones Avanzadas con Cadenas

Objetivo: Explorar técnicas avanzadas de manipulación y procesamiento de cadenas de texto.

Instrucciones:
1. Utilizar métodos avanzados de string y técnicas de procesamiento de texto.
2. Implementar algoritmos de búsqueda y comparación de cadenas.
3. Explorar la manipulación de texto multilinea y Unicode.
4. Aplicar expresiones regulares para tareas complejas de procesamiento de texto.
"""

import re
import unicodedata
import difflib
import textwrap
import string
from collections import Counter

def main():
    # Técnicas avanzadas de manipulación de strings
    print("=== Técnicas Avanzadas de Manipulación de Strings ===")
    
    # String multilinea con triple comilla
    texto_largo = """Este es un texto
    que ocupa múltiples líneas
    y conserva el formato.
    """
    
    print("Texto multilinea original:")
    print(texto_largo)
    
    # Método dedent para quitar sangría común
    import textwrap
    texto_dedent = textwrap.dedent("""
        Este es un texto
        que ocupa múltiples líneas
        pero sin sangría común.
    """)
    
    print("\nTexto con dedent aplicado:")
    print(texto_dedent)
    
    # Justificación y formato de párrafos
    texto = "Este es un texto largo que se utilizará para mostrar cómo funcionan las operaciones de justificación y formato de párrafos en Python. Veremos diferentes ejemplos."
    
    # Envolver texto a un ancho específico
    print("\nTexto envuelto a 40 caracteres:")
    texto_envuelto = textwrap.fill(texto, width=40)
    print(texto_envuelto)
    
    # Justificación
    palabras = ["Python", "es", "poderoso"]
    
    print("\nJustificación:")
    print(f"Izquierda  : '{' '.join(palabras):<30}'")
    print(f"Centro     : '{' '.join(palabras):^30}'")
    print(f"Derecha    : '{' '.join(palabras):>30}'")
    
    # Partición y unión de strings
    print("\n=== Partición y Unión de Strings ===")
    
    frase = "Python es un lenguaje de programación potente y versátil"
    
    # Partir por espacio
    palabras = frase.split()
    print(f"Split por espacio: {palabras}")
    
    # Partir por un carácter específico
    csv_data = "nombre,edad,ciudad,profesión"
    campos = csv_data.split(',')
    print(f"Split por coma: {campos}")
    
    # Partir con límite
    resultado = frase.split(' ', 3)
    print(f"Split con límite 3: {resultado}")
    
    # Partir por múltiples caracteres (requiere regex)
    resultado = re.split(r'[ ,]+', "Python, es, un lenguaje  de programación")
    print(f"Split por espacio o coma: {resultado}")
    
    # Unir elementos
    print(f"Join con espacio: '{' '.join(palabras)}'")
    print(f"Join con guion: '{'-'.join(palabras)}'")
    
    # Alineación, relleno y truncamiento
    print("\n=== Alineación, Relleno y Truncamiento ===")
    
    texto = "Python"
    
    # Alineación con relleno
    print(f"Centrado con asteriscos: '{texto:*^20}'")
    print(f"Alineado a la izquierda con guiones: '{texto:-<20}'")
    print(f"Alineado a la derecha con puntos: '{texto:.>20}'")
    
    # Truncamiento
    texto_largo = "Esto es una cadena muy larga que será truncada"
    print(f"Truncado a 20 caracteres: '{texto_largo:.20}'")
    
    # Strings Unicode y normalización
    print("\n=== Strings Unicode y Normalización ===")
    
    # Caracteres Unicode
    unicode_string = "Café résumé で 漢字"
    print(f"String Unicode: {unicode_string}")
    
    # Longitud en caracteres vs bytes
    print(f"Longitud en caracteres: {len(unicode_string)}")
    print(f"Longitud en bytes (UTF-8): {len(unicode_string.encode('utf-8'))}")
    
    # Normalización Unicode
    s1 = "café"  # 'e' con acento agudo como un solo carácter
    s2 = "cafe\u0301"  # 'e' normal seguido del carácter combinante acento agudo
    
    print(f"s1: {s1}, longitud: {len(s1)}")
    print(f"s2: {s2}, longitud: {len(s2)}")
    print(f"¿s1 == s2? {s1 == s2}")
    
    # Normalizar a la forma NFC (forma compuesta canónica)
    s1_nfc = unicodedata.normalize('NFC', s1)
    s2_nfc = unicodedata.normalize('NFC', s2)
    
    print(f"s1 normalizado (NFC): {s1_nfc}, longitud: {len(s1_nfc)}")
    print(f"s2 normalizado (NFC): {s2_nfc}, longitud: {len(s2_nfc)}")
    print(f"¿s1_nfc == s2_nfc? {s1_nfc == s2_nfc}")
    
    # Quitar acentos
    def quitar_acentos(s):
        return ''.join(c for c in unicodedata.normalize('NFD', s)
                       if unicodedata.category(c) != 'Mn')
    
    texto_con_acentos = "Café résumé"
    texto_sin_acentos = quitar_acentos(texto_con_acentos)
    
    print(f"Texto con acentos: {texto_con_acentos}")
    print(f"Texto sin acentos: {texto_sin_acentos}")
    
    # Algoritmos de búsqueda y comparación de strings
    print("\n=== Algoritmos de Búsqueda y Comparación de Strings ===")
    
    # Métodos básicos de búsqueda
    texto = "Python es un lenguaje de programación Python muy popular"
    
    print(f"Posición de 'Python': {texto.find('Python')}")
    print(f"Posición de 'Python' desde la posición 10: {texto.find('Python', 10)}")
    print(f"Última posición de 'Python': {texto.rfind('Python')}")
    
    # Buscar todas las ocurrencias
    def buscar_todas(texto, subcadena):
        posiciones = []
        pos = -1
        while True:
            pos = texto.find(subcadena, pos + 1)
            if pos == -1:
                break
            posiciones.append(pos)
        return posiciones
    
    print(f"Todas las posiciones de 'Python': {buscar_todas(texto, 'Python')}")
    
    # Coincidencia aproximada de strings
    print("\n=== Coincidencia Aproximada de Strings ===")
    
    s1 = "Python es un lenguaje de programación"
    s2 = "Python es lenguaje de programación"
    s3 = "Python es un lenguaje para programar"
    
    # Ratio de coincidencia
    ratio12 = difflib.SequenceMatcher(None, s1, s2).ratio()
    ratio13 = difflib.SequenceMatcher(None, s1, s3).ratio()
    
    print(f"Ratio de coincidencia entre s1 y s2: {ratio12:.4f}")
    print(f"Ratio de coincidencia entre s1 y s3: {ratio13:.4f}")
    
    # Obtener la subcadena más larga común
    matcher = difflib.SequenceMatcher(None, s1, s3)
    match = matcher.find_longest_match(0, len(s1), 0, len(s3))
    
    print(f"Subcadena más larga común: '{s1[match.a:match.a+match.size]}'")
    
    # Sugerencias para corrección ortográfica
    palabras = ["python", "javascript", "java", "csharp", "ruby", "golang"]
    palabra_buscada = "pitón"
    
    sugerencias = difflib.get_close_matches(palabra_buscada, palabras, n=3, cutoff=0.6)
    print(f"Sugerencias para '{palabra_buscada}': {sugerencias}")
    
    # Procesamiento de texto
    print("\n=== Procesamiento de Texto ===")
    
    texto = """Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código.
    Es un lenguaje multiparadigma, ya que soporta orientación a objetos, programación imperativa y programación funcional.
    Python es administrado por la Python Software Foundation. Posee una licencia de código abierto."""
    
    # Tokenización simple
    palabras = re.findall(r'\b\w+\b', texto.lower())
    print(f"Número de palabras: {len(palabras)}")
    
    # Contar frecuencia de palabras
    contador = Counter(palabras)
    palabras_mas_comunes = contador.most_common(5)
    
    print("Palabras más comunes:")
    for palabra, frecuencia in palabras_mas_comunes:
        print(f"  {palabra}: {frecuencia}")
    
    # Eliminar palabras vacías (stopwords)
    stopwords = {"es", "un", "la", "de", "en", "y", "a", "que", "su", "por"}
    palabras_filtradas = [palabra for palabra in palabras if palabra not in stopwords]
    
    contador_filtrado = Counter(palabras_filtradas)
    palabras_mas_comunes_filtradas = contador_filtrado.most_common(5)
    
    print("\nPalabras más comunes (sin stopwords):")
    for palabra, frecuencia in palabras_mas_comunes_filtradas:
        print(f"  {palabra}: {frecuencia}")
    
    # Estadísticas de texto
    lineas = texto.split('\n')
    num_lineas = len(lineas)
    num_caracteres = len(texto)
    num_caracteres_sin_espacios = len(texto.replace(" ", ""))
    
    print(f"\nEstadísticas del texto:")
    print(f"  Líneas: {num_lineas}")
    print(f"  Caracteres (con espacios): {num_caracteres}")
    print(f"  Caracteres (sin espacios): {num_caracteres_sin_espacios}")
    print(f"  Palabras: {len(palabras)}")
    
    # Transformaciones de texto
    print("\n=== Transformaciones de Texto ===")
    
    texto_ejemplo = "Python es genial!"
    
    # Mapeo de caracteres
    tabla_mapeo = str.maketrans({
        'a': '4',
        'e': '3',
        'i': '1',
        'o': '0',
        ' ': '_'
    })
    
    texto_transformado = texto_ejemplo.translate(tabla_mapeo)
    print(f"Texto original: {texto_ejemplo}")
    print(f"Texto transformado: {texto_transformado}")
    
    # Reemplazo múltiple con expresiones regulares
    def reemplazo_multiple(texto, reemplazos):
        """Realiza múltiples reemplazos en un solo paso."""
        patrones = '|'.join(map(re.escape, reemplazos.keys()))
        return re.sub(patrones, lambda m: reemplazos[m.group(0)], texto)
    
    reemplazos = {
        'Python': 'Java',
        'genial': 'increíble',
        'es': 'era'
    }
    
    texto_reemplazado = reemplazo_multiple(texto_ejemplo, reemplazos)
    print(f"Texto con reemplazos múltiples: {texto_reemplazado}")
    
    # Transformación de casos
    print("\n=== Transformación de Casos ===")
    
    texto_caso = "Python es un Lenguaje de Programación"
    
    print(f"Original: {texto_caso}")
    print(f"Mayúsculas: {texto_caso.upper()}")
    print(f"Minúsculas: {texto_caso.lower()}")
    print(f"Título: {texto_caso.title()}")
    print(f"Capitalizado: {texto_caso.capitalize()}")
    print(f"Intercambio: {texto_caso.swapcase()}")
    
    # Ejemplos prácticos
    print("\n=== Ejemplos Prácticos ===")
    
    # Generador de slugs
    def generar_slug(texto):
        """Genera un slug a partir de un texto."""
        # Normalizar Unicode y convertir a ASCII
        texto = unicodedata.normalize('NFKD', texto)
        texto = ''.join([c for c in texto if not unicodedata.combining(c)])
        
        # Convertir a minúsculas y reemplazar espacios por guiones
        texto = texto.lower()
        texto = re.sub(r'[^\w\s-]', '', texto)  # Eliminar caracteres especiales
        texto = re.sub(r'[\s_-]+', '-', texto)  # Reemplazar espacios y guiones bajos por guiones
        texto = texto.strip('-')  # Eliminar guiones al inicio y final
        
        return texto
    
    titulo = "¡Python es el mejor lenguaje de programación! (Opinión)"
    slug = generar_slug(titulo)
    print(f"Título: {titulo}")
    print(f"Slug: {slug}")
    
    # Extracción de información con regex
    def extraer_emails(texto):
        """Extrae direcciones de correo electrónico de un texto."""
        patron = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.findall(patron, texto)
    
    texto_con_emails = """
    Contactos:
    - Juan Pérez: juan.perez@example.com
    - María García: maria@empresa.org
    - Soporte: help@python.org
    """
    
    emails = extraer_emails(texto_con_emails)
    print(f"Emails extraídos: {emails}")
    
    # Ejercicios para el usuario
    print("\n=== EJERCICIOS PARA PRACTICAR ===")
    print("1. Implementa un verificador de palíndromos que ignore espacios, signos de puntuación y diferencias entre mayúsculas y minúsculas")
    print("2. Crea una función que genere un acrónimo a partir de una frase (ej. 'Lenguaje de Marcado de Hipertexto' -> 'LMH')")
    print("3. Desarrolla un algoritmo para detectar anagramas entre dos palabras o frases")
    print("4. Implementa un generador de contraseñas seguras basadas en frases mnemotécnicas")

if __name__ == "__main__":
    main()
