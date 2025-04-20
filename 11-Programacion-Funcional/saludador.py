""" 
Script Básico con Argumentos de Línea de Comandos

    Enunciado: Escribe un script de Python que acepte dos argumentos desde la línea de comandos: 
    un nombre (--nombre) y un número (--veces). El script debe imprimir un saludo personalizado 
    usando el nombre, repetido el número de veces especificado.
"""

import argparse

def main():
    # 1. Configurar el parser de argumentos
    parser = argparse.ArgumentParser(description="Saluda a alguien varias veces.")

    # 2. Añadir los argumentos esperados
    parser.add_argument(
        "--nombre",
        type=str,
        required=True,  # Hace que este argumento sea obligatorio
        help="El nombre de la persona a saludar."
    )
    parser.add_argument(
        "--veces",
        type=int,
        default=1,     # Valor por defecto si no se proporciona
        help="El número de veces que se repetirá el saludo (por defecto: 1)."
    )

    # 3. Parsear los argumentos proporcionados en la línea de comandos
    args = parser.parse_args()

    # 4. Validar el número de veces (opcional pero buena práctica)
    if args.veces < 1:
        print("Error: El número de veces debe ser al menos 1.")
        return # Salir si el valor no es válido

    # 5. Usar los argumentos parseados
    nombre_saludo = args.nombre
    num_repeticiones = args.veces

    print(f"--- Saludando a {nombre_saludo} ---")
    for i in range(num_repeticiones):
        print(f"¡Hola, {nombre_saludo}! (Saludo #{i+1})")
    print("--- Fin del saludo ---")

# Buena práctica: asegurar que main() solo se ejecute si el script es el principal
if __name__ == "__main__":
    main()