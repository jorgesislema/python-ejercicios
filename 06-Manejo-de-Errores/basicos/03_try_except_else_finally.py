"""
Ejercicio 3: Try-Except-Else-Finally

Objetivo: Aprender a utilizar las cláusulas else y finally en el manejo de excepciones.

Instrucciones:
1. Crea una función que intente abrir un archivo y leer su contenido.
2. Utiliza try-except para manejar posibles errores.
3. Utiliza else para ejecutar código cuando no hay excepciones.
4. Utiliza finally para asegurar que los recursos se liberan adecuadamente.
"""

def leer_archivo(nombre_archivo):
    archivo = None
    try:
        # Intentar abrir y leer el archivo
        archivo = open(nombre_archivo, 'r', encoding='utf-8')
        contenido = archivo.read()
        return contenido
    
    except FileNotFoundError:
        # Manejar el error si el archivo no existe
        return f"Error: El archivo '{nombre_archivo}' no existe."
    
    except IOError:
        # Manejar otros errores de E/S
        return f"Error: No se pudo leer el archivo '{nombre_archivo}'."
    
    else:
        # Este bloque se ejecuta si no hay excepciones
        print(f"El archivo '{nombre_archivo}' se leyó correctamente.")
    
    finally:
        # Este bloque siempre se ejecuta, haya o no excepciones
        if archivo:
            archivo.close()
            print(f"El archivo '{nombre_archivo}' ha sido cerrado.")

# Ejemplos de uso
def main():
    # Caso 1: Archivo que existe
    print(leer_archivo("texto_ejemplo.txt"))
    print("-" * 40)
    
    # Caso 2: Archivo que no existe
    print(leer_archivo("archivo_inexistente.txt"))

# Ejecutar el programa
if __name__ == "__main__":
    main()
