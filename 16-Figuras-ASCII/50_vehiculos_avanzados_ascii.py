"""
Ejercicio 50: Vehículos Avanzados ASCII

Objetivo:
- Crear representaciones ASCII de vehículos modernos y futuristas
- Incluir variantes: tren, helicóptero, submarino, nave espacial, etc.
- Permitir personalización y animaciones de movimiento

Conceptos:
- Arte ASCII vehicular avanzado
- Representación de medios de transporte
- Animaciones y efectos visuales
"""

import time
import os

def tren_ascii():
    """Tren completo ASCII"""
    print("🚂 TREN ASCII 🚂")
    print("═" * 60)
    
    tren = [
        "    ╭─────╮     ╭─────╮     ╭─────╮",
        "   ╱       ╲   ╱       ╲   ╱       ╲",
        "  ╱    🚂   ╲ ╱   📦    ╲ ╱   👥    ╲",
        " │   ┌─────┐ ││  ┌─────┐ ││  ┌─────┐ │",
        " │   │ ███ │ ││  │     │ ││  │ ▢ ▢ │ │",
        " │   └─────┘ ││  └─────┘ ││  └─────┘ │",
        "═╰═══○═════○═╯╰═══○═════○═╯╰═══○═════○═╯═",
        "    ○       ○     ○       ○     ○       ○"
    ]
    
    for linea in tren:
        print(linea)
    
    print("\n🚂 Locomotora | 📦 Vagón de carga | 👥 Vagón de pasajeros")
    print("Velocidad máxima: 320 km/h (TGV)")

def helicoptero_ascii():
    """Helicóptero ASCII"""
    print("🚁 HELICÓPTERO ASCII 🚁")
    print("═" * 50)
    
    helicoptero = [
        "      ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈",
        "            │",
        "       ╭─────────╮",
        "      ╱ 🚁       ╲",
        "     ╱  ┌─────┐   ╲",
        "    │   │ ◉ ◉ │    │",
        "    │   └─────┘    │",
        "     ╲             ╱",
        "      ╲___________╱",
        "           │ │",
        "         ╱─┴─╲",
        "        ╱     ╲",
        "       ╱_______╲",
        "            ≈≈≈"
    ]
    
    for linea in helicoptero:
        print(linea)
    
    print("\n🚁 Helicóptero de rescate")
    print("≈ Rotor principal y de cola")

def submarino_ascii():
    """Submarino ASCII"""
    print("🚢 SUBMARINO ASCII 🚢")
    print("═" * 50)
    
    submarino = [
        "                │",
        "              ╭─┴─╮",
        "             ╱     ╲",
        "────────────╱───────╲────────────",
        "  ╭─────────────────────────╮",
        " ╱  ◉  ◉  ◉  ◉  ◉  ◉  ◉   ╲",
        "│    🌊 SUBMARINO NUCLEAR 🌊  │",
        " ╲  ◦  ◦  ◦  ◦  ◦  ◦  ◦   ╱",
        "  ╰─────────────────────────╯",
        "────────────╲───────╱────────────",
        "             ╲     ╱",
        "              ╰───╯",
        "      🐟  🐠    🐟"
    ]
    
    for linea in submarino:
        print(linea)
    
    print("\n🚢 Submarino nuclear de profundidad")
    print("◉ Ventanas de observación | ──── agua")

def nave_espacial_ascii():
    """Nave espacial ASCII"""
    print("🚀 NAVE ESPACIAL ASCII 🚀")
    print("═" * 50)
    
    nave = [
        "           ╱▲╲",
        "          ╱  ╲",
        "         ╱ 🚀 ╲",
        "        ╱______╲",
        "       │ ◉    ◉ │",
        "       │  NASA  │",
        "       │ ◉    ◉ │",
        "       ╰────────╯",
        "        ╲      ╱",
        "         ╲____╱",
        "          ╲  ╱",
        "           ╲╱",
        "           🔥",
        "          🔥🔥",
        "         🔥🔥🔥"
    ]
    
    for linea in nave:
        print(linea)
    
    print("\n🚀 Nave espacial tripulada")
    print("🔥 Propulsores | ◉ Ventanas de observación")

def globo_aerostatico_ascii():
    """Globo aerostático ASCII"""
    print("🎈 GLOBO AEROSTÁTICO ASCII 🎈")
    print("═" * 50)
    
    globo = [
        "       ╭─────────╮",
        "      ╱           ╲",
        "     ╱             ╲",
        "    ╱  🎈 🎈 🎈 🎈  ╲",
        "   │   🎈 🎈 🎈 🎈   │",
        "   │   🎈 🎈 🎈 🎈   │",
        "    ╲  🎈 🎈 🎈 🎈  ╱",
        "     ╲             ╱",
        "      ╲___________╱",
        "           │ │",
        "           │ │",
        "       ╭───┴─┴───╮",
        "      ╱ 👥      ╲",
        "     │           │",
        "      ╲_________╱"
    ]
    
    for linea in globo:
        print(linea)
    
    print("\n🎈 Globo aerostático de pasajeros")
    print("Altura de vuelo: 500-3000 metros")

def drone_ascii():
    """Drone ASCII"""
    print("🛸 DRONE ASCII 🛸")
    print("═" * 40)
    
    drone = [
        "  ≈≈≈     ≈≈≈     ≈≈≈     ≈≈≈",
        "   │       │       │       │",
        "   ○───────┼───────┼───────○",
        "           │  🛸   │",
        "           │ ▣▣▣▣ │",
        "           │ ▣▣▣▣ │",
        "   ○───────┼───────┼───────○",
        "   │       │       │       │",
        "  ≈≈≈     ≈≈≈     ≈≈≈     ≈≈≈"
    ]
    
    for linea in drone:
        print(linea)
    
    print("\n🛸 Drone cuadricóptero")
    print("≈ Hélices | ○ Motores | ▣ Cámara")

def cohete_espacial():
    """Cohete espacial detallado"""
    print("🚀 COHETE ESPACIAL DETALLADO 🚀")
    print("═" * 60)
    
    cohete = [
        "                 ╱▲╲",
        "                ╱  ╲",
        "               ╱ 🚀 ╲",
        "              ╱______╲",
        "             │ ETAPA 3 │",
        "             │ ◉    ◉ │",
        "             ╰────────╯",
        "             │ ETAPA 2 │",
        "             │ ◦    ◦ │",
        "             │ ◦    ◦ │",
        "             ╰────────╯",
        "             │ ETAPA 1 │",
        "             │ ●    ● │",
        "             │ ●    ● │",
        "             │ ●    ● │",
        "             ╰────────╯",
        "              ╲      ╱",
        "               ╲____╱",
        "                🔥",
        "               🔥🔥🔥",
        "              🔥🔥🔥🔥🔥"
    ]
    
    for linea in cohete:
        print(linea)
    
    print("\n🚀 Cohete de múltiples etapas")
    print("Destino: Estación Espacial Internacional")

def animacion_vehiculos():
    """Animación de vehículos en movimiento"""
    print("🚗 ANIMACIÓN DE VEHÍCULOS 🚗")
    print("═" * 60)
    
    vehiculos = [
        ("🚗", "Coche"),
        ("🚌", "Autobús"),
        ("🚚", "Camión"),
        ("🏍️", "Motocicleta"),
        ("🚲", "Bicicleta")
    ]
    
    carretera = "═" * 50
    
    for vehiculo, nombre in vehiculos:
        for pos in range(0, 45, 3):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("🚗 ANIMACIÓN DE VEHÍCULOS 🚗")
            print("═" * 60)
            print(carretera)
            print(" " * pos + vehiculo + f" <- {nombre}")
            print(carretera)
            time.sleep(0.3)
    
    print("\n¡Todos los vehículos han pasado!")

def menu_principal():
    """Menú principal del programa"""
    while True:
        print("\n" + "═" * 60)
        print("🚂 VEHÍCULOS AVANZADOS ASCII 🚁")
        print("═" * 60)
        print("1. Tren completo")
        print("2. Helicóptero")
        print("3. Submarino")
        print("4. Nave espacial")
        print("5. Globo aerostático")
        print("6. Drone")
        print("7. Cohete espacial detallado")
        print("8. Animación de vehículos")
        print("0. Salir")
        print("═" * 60)
        
        opcion = input("Selecciona un vehículo: ")
        
        if opcion == "1":
            tren_ascii()
        elif opcion == "2":
            helicoptero_ascii()
        elif opcion == "3":
            submarino_ascii()
        elif opcion == "4":
            nave_espacial_ascii()
        elif opcion == "5":
            globo_aerostatico_ascii()
        elif opcion == "6":
            drone_ascii()
        elif opcion == "7":
            cohete_espacial()
        elif opcion == "8":
            animacion_vehiculos()
        elif opcion == "0":
            print("¡Buen viaje! 🚀")
            break
        else:
            print("Opción no válida")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
