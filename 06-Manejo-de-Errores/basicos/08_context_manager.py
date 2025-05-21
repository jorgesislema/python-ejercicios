"""
Ejercicio 8: Manejo de Recursos con Context Manager

Objetivo: Aprender a usar context managers (with) para el manejo seguro de recursos.

Instrucciones:
1. Crea una función que lea un archivo usando el context manager 'with'.
2. Compara este enfoque con el manejo tradicional usando try-finally.
3. Implementa una función adicional que escriba en un archivo con manejo de excepciones.
"""

def leer_archivo_tradicional(nombre_archivo):
    """Lee un archivo usando el método tradicional con try-finally."""
    archivo = None
    try:
        archivo = open(nombre_archivo, 'r', encoding='utf-8')
        contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
        return None
    except IOError as e:
        print(f"Error al leer el archivo: {e}")
        return None
    finally:
        # Este bloque se ejecuta siempre, haya o no excepciones
        if archivo:
            archivo.close()
            print(f"Archivo cerrado (método tradicional): {nombre_archivo}")

def leer_archivo_with(nombre_archivo):
    """Lee un archivo usando context manager 'with'."""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
        return None
    except IOError as e:
        print(f"Error al leer el archivo: {e}")
        return None
    # No es necesario cerrar el archivo: lo hace automáticamente al salir del bloque 'with'
    finally:
        print(f"Bloque with finalizado para: {nombre_archivo}")

def escribir_archivo_seguro(nombre_archivo, contenido):
    """Escribe contenido en un archivo usando context manager y manejo de excepciones."""
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido)
        print(f"Archivo '{nombre_archivo}' escrito correctamente.")
        return True
    except IOError as e:
        print(f"Error al escribir en '{nombre_archivo}': {e}")
        return False

def main():
    archivo_prueba = "ejemplo_context_manager.txt"
    
    # 1. Escribir un archivo de prueba
    print("=== Escribiendo archivo de prueba ===")
    escribir_archivo_seguro(archivo_prueba, "¡Hola mundo!\nEste es un archivo de prueba.\nPrueba de manejo de archivos.")
    
    # 2. Leer usando método tradicional
    print("\n=== Leyendo con método tradicional ===")
    contenido1 = leer_archivo_tradicional(archivo_prueba)
    if contenido1:
        print(f"Contenido leído:\n{contenido1}")
    
    # 3. Leer usando context manager
    print("\n=== Leyendo con context manager ===")
    contenido2 = leer_archivo_with(archivo_prueba)
    if contenido2:
        print(f"Contenido leído:\n{contenido2}")
    
    # 4. Probar con un archivo que no existe
    print("\n=== Probando con archivo inexistente ===")
    leer_archivo_with("archivo_que_no_existe.txt")

if __name__ == "__main__":
    main()
