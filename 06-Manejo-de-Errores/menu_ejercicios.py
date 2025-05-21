"""
Menú Interactivo para Ejercicios de Manejo de Errores

Este script proporciona un menú interactivo que permite ejecutar
cualquiera de los ejercicios del módulo de manejo de errores.
"""

import os
import importlib.util
import sys

def limpiar_pantalla():
    """Limpia la pantalla de la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def obtener_ejercicios(ruta):
    """Obtiene la lista de ejercicios Python en una ruta específica."""
    archivos = []
    try:
        for archivo in os.listdir(ruta):
            if archivo.endswith('.py') and not archivo.startswith('__'):
                archivos.append(archivo)
        return sorted(archivos)
    except FileNotFoundError:
        print(f"Error: No se encontró la carpeta {ruta}")
        return []

def mostrar_menu():
    """Muestra el menú principal de ejercicios."""
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("MENÚ DE EJERCICIOS DE MANEJO DE ERRORES".center(50))
        print("=" * 50)
        print("\n1. Ejercicios Básicos")
        print("2. Ejercicios Avanzados")
        print("3. Salir")
        print("-" * 50)
        
        opcion = input("\nSelecciona una opción (1-3): ")
        
        if opcion == "1":
            mostrar_submenu("basicos")
        elif opcion == "2":
            mostrar_submenu("avanzados")
        elif opcion == "3":
            print("\n¡Gracias por utilizar el menú de ejercicios!")
            break
        else:
            input("\nOpción no válida. Presiona Enter para continuar...")

def mostrar_submenu(tipo):
    """Muestra el submenú de ejercicios según el tipo seleccionado."""
    ruta = os.path.join(os.path.dirname(__file__), tipo)
    ejercicios = obtener_ejercicios(ruta)
    
    if not ejercicios:
        input(f"\nNo se encontraron ejercicios {tipo}. Presiona Enter para continuar...")
        return
    
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print(f"EJERCICIOS {tipo.upper()}".center(50))
        print("=" * 50)
        print()
        
        for i, ejercicio in enumerate(ejercicios, 1):
            nombre = ejercicio.replace('.py', '').replace('_', ' ').title()
            print(f"{i}. {nombre}")
        
        print(f"{len(ejercicios) + 1}. Volver al menú principal")
        print("-" * 50)
        
        try:
            opcion = int(input(f"\nSelecciona un ejercicio (1-{len(ejercicios) + 1}): "))
            
            if 1 <= opcion <= len(ejercicios):
                ejecutar_ejercicio(os.path.join(ruta, ejercicios[opcion - 1]))
            elif opcion == len(ejercicios) + 1:
                break
            else:
                input("\nOpción no válida. Presiona Enter para continuar...")
        except ValueError:
            input("\nDebes ingresar un número. Presiona Enter para continuar...")

def ejecutar_ejercicio(ruta_completa):
    """Ejecuta un ejercicio específico."""
    limpiar_pantalla()
    print("=" * 50)
    print(f"EJECUTANDO: {os.path.basename(ruta_completa)}")
    print("=" * 50)
    print()
    
    # Guardar el directorio actual
    directorio_actual = os.getcwd()
    
    try:
        # Cambiar al directorio del ejercicio para la ejecución
        os.chdir(os.path.dirname(ruta_completa))
        
        # Cargar y ejecutar el módulo
        spec = importlib.util.spec_from_file_location("ejercicio", ruta_completa)
        modulo = importlib.util.module_from_spec(spec)
        sys.modules["ejercicio"] = modulo
        spec.loader.exec_module(modulo)
        
        # Si existe una función main en el módulo, ejecutarla
        if hasattr(modulo, 'main'):
            modulo.main()
    except Exception as e:
        print(f"\nError al ejecutar el ejercicio: {e}")
    finally:
        # Restaurar el directorio de trabajo
        os.chdir(directorio_actual)
        
        input("\nEjecución finalizada. Presiona Enter para continuar...")

if __name__ == "__main__":
    mostrar_menu()
