"""
Ejercicio 40: Puentes y Caminos ASCII

Objetivo:
- Crear representaciones ASCII de puentes y caminos
- Incluir variantes: puentes colgantes, de arco, caminos sinuosos, carreteras
- Permitir personalización de longitud y tipo
- Añadir animaciones de vehículos cruzando

Conceptos:
- Simulación de trayectorias
- Arte ASCII estructural
- Interactividad y animación básica
"""

def puente_colgante(longitud=20):
    """Dibuja un puente colgante ASCII"""
    print("🌉 PUENTE COLGANTE 🌉")
    print("═" * (longitud + 8))
    print("  " + "/" + "~" * longitud + "\\")
    for i in range(3):
        print(" |" + " " * longitud + "|")
    print("/=" + "=" * longitud + "=\\")
    print("".join([" " for _ in range(longitud + 8)]))

def puente_arco(longitud=20):
    """Dibuja un puente de arco ASCII"""
    print("🌉 PUENTE DE ARCO 🌉")
    print("═" * (longitud + 8))
    print("  " + "_" * longitud)
    print(" /" + " " * longitud + "\\")
    print("| " + "_" * longitud + " |")
    print("|_|" + "_" * longitud + "|_|")

def camino_sinuoso(longitud=20):
    """Dibuja un camino sinuoso ASCII"""
    print("🛣️ CAMINO SINUOSO 🛣️")
    print("═" * (longitud + 8))
    for i in range(longitud):
        if i % 4 == 0:
            print(" " * (i % 8) + "/\\")
        elif i % 4 == 2:
            print(" " * (8 - (i % 8)) + "\\/")
        else:
            print(" " * 4 + "||")

def carretera_vehiculo(longitud=30):
    """Animación de un vehículo cruzando un puente/carretera"""
    import time
    import os
    print("🚗 ANIMACIÓN DE CARRETERA 🚗")
    print("═" * (longitud + 8))
    carretera = "=" * longitud
    for pos in range(longitud):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(" " * 4 + carretera)
        print(" " * (4 + pos) + "🚗")
        time.sleep(0.08)
    print("¡Vehículo ha cruzado!")

def menu_principal():
    """Menú principal del programa"""
    while True:
        print("\n" + "═" * 50)
        print("🌉 PUENTES Y CAMINOS ASCII 🌉")
        print("═" * 50)
        print("1. Puente colgante")
        print("2. Puente de arco")
        print("3. Camino sinuoso")
        print("4. Animación de carretera con vehículo")
        print("0. Salir")
        print("═" * 50)
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            l = int(input("Longitud del puente (10-40): ") or 20)
            puente_colgante(l)
        elif opcion == "2":
            l = int(input("Longitud del puente (10-40): ") or 20)
            puente_arco(l)
        elif opcion == "3":
            l = int(input("Longitud del camino (10-40): ") or 20)
            camino_sinuoso(l)
        elif opcion == "4":
            l = int(input("Longitud de la carretera (10-60): ") or 30)
            carretera_vehiculo(l)
        elif opcion == "0":
            print("¡Hasta luego! 🌉")
            break
        else:
            print("Opción no válida")
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
