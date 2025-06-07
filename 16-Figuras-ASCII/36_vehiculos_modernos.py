"""
Ejercicio 36: Vehículos Modernos ASCII

Objetivo:
- Crear vehículos contemporáneos en ASCII
- Incluir automóviles, motos, camiones y más
- Simular tráfico y movimiento
- Crear escenas urbanas

Conceptos:
- Transporte moderno
- Diseño vehicular
- Sistemas de transporte
- Simulación de tráfico
"""

def automovil_sedan():
    """Automóvil sedán moderno"""
    print("🚗 AUTOMÓVIL SEDÁN 🚗")
    print("═" * 50)
    
    sedan = [
        "           ╭─────────────────╮",
        "          ╱                   ╲",
        "         ╱                     ╲",
        "        ╱                       ╲",
        "       ╱                         ╲",
        "╭─────╱                           ╲─────╮",
        "│                                       │",
        "│  🚗                             🚗  │",
        "│     ╔═══╗               ╔═══╗     │",
        "│     ║ ● ║               ║ ● ║     │",
        "│     ╚═══╝               ╚═══╝     │",
        "╰───────────────────────────────────╯",
        "      ●                       ●",
        "     ╱ ╲                     ╱ ╲",
        "    ╱___╲                   ╱___╲",
        "   ╱     ╲                 ╱     ╲",
        "  ╱_______╲               ╱_______╲"
    ]
    
    for linea in sedan:
        print(linea)
    
    print("\n🚗 Vehículo familiar moderno 🚗")

def motocicleta_ascii():
    """Motocicleta deportiva"""
    print("🏍️ MOTOCICLETA DEPORTIVA 🏍️")
    print("═" * 40)
    
    moto = [
        "        ╭──╮",
        "       ╱    ╲",
        "      ╱  🏍️  ╲",
        "     ╱        ╲",
        "    ╱          ╲",
        "   ╱____________╲",
        "  ╱              ╲",
        " ╱                ╲",
        "╱                  ╲",
        "╲                  ╱",
        " ╲                ╱",
        "  ╲______________╱",
        "   ╲____________╱",
        "    ╲__________╱",
        "     ╲________╱",
        "      ╲______╱",
        "       ╲____╱",
        "        ╲__╱",
        "         ██",
        "        ╱██╲",
        "       ╱____╲",
        "      ╱      ╲",
        "     ╱________╲",
        "",
        "   ●              ●",
        "  ╱╲╲            ╱╲╲",
        " ╱__╲╲          ╱__╲╲",
        "╱____╲╲        ╱____╲╲"
    ]
    
    for linea in moto:
        print(linea)
    
    print("\n🏍️ Velocidad y adrenalina 🏍️")

def camion_carga():
    """Camión de carga pesado"""
    print("🚛 CAMIÓN DE CARGA 🚛")
    print("═" * 60)
    
    camion = [
        "     ╭──╮",
        "    ╱ 🚛 ╲",
        "   ╱      ╲",
        "  ╱        ╲",
        " ╱          ╲",
        "╱____________╲═══════════════════════════════╗",
        "║            ║                               ║",
        "║     ●      ║                               ║",
        "║            ║                               ║",
        "║____________║                               ║",
        "║            ║                               ║",
        "║            ║          CARGA                ║",
        "║            ║                               ║",
        "║            ║                               ║",
        "╚════════════╩═══════════════════════════════╝",
        "      ●         ●              ●        ●",
        "     ╱╲╲       ╱╲╲            ╱╲╲      ╱╲╲",
        "    ╱__╲╲     ╱__╲╲          ╱__╲╲    ╱__╲╲",
        "   ╱____╲╲   ╱____╲╲        ╱____╲╲  ╱____╲╲"
    ]
    
    for linea in camion:
        print(linea)
    
    print("\n🚛 Transporte de mercancías 🚛")

def autobus_urbano():
    """Autobús urbano de pasajeros"""
    print("🚌 AUTOBÚS URBANO 🚌")
    print("═" * 60)
    
    autobus = [
        "╭────────────────────────────────────────────────╮",
        "│ 🚌                                       🚌 │",
        "│   ╔══╗  ╔══╗  ╔══╗  ╔══╗  ╔══╗  ╔══╗   │",
        "│   ║👤║  ║👤║  ║👤║  ║👤║  ║👤║  ║👤║   │",
        "│   ╚══╝  ╚══╝  ╚══╝  ╚══╝  ╚══╝  ╚══╝   │",
        "│                                              │",
        "│   ╔══╗  ╔══╗  ╔══╗  ╔══╗  ╔══╗  ╔══╗   │",
        "│   ║👤║  ║👤║  ║👤║  ║👤║  ║👤║  ║👤║   │",
        "│   ╚══╝  ╚══╝  ╚══╝  ╚══╝  ╚══╝  ╚══╝   │",
        "│                                              │",
        "╰──────────────────────────────────────────────╯",
        "    ●        ●                    ●        ●",
        "   ╱╲╲      ╱╲╲                  ╱╲╲      ╱╲╲",
        "  ╱__╲╲    ╱__╲╲                ╱__╲╲    ╱__╲╲",
        " ╱____╲╲  ╱____╲╲              ╱____╲╲  ╱____╲╲"
    ]
    
    for linea in autobus:
        print(linea)
    
    print("\n🚌 Transporte público eficiente 🚌")

def ambulancia_ascii():
    """Ambulancia de emergencias"""
    print("🚑 AMBULANCIA 🚑")
    print("═" * 50)
    
    ambulancia = [
        "          ╭─────────────╮",
        "         ╱               ╲",
        "        ╱                 ╲",
        "       ╱                   ╲",
        "╭─────╱                     ╲─────╮",
        "│  🚑                         🚑  │",
        "│      ╔═══╗           ╔═══╗      │",
        "│      ║ + ║           ║ + ║      │",
        "│      ╚═══╝           ╚═══╝      │",
        "│                                 │",
        "│         AMBULANCIA               │",
        "│           🏥 + 🏥               │",
        "╰─────────────────────────────────╯",
        "      ●                     ●",
        "     ╱╲╲                   ╱╲╲",
        "    ╱__╲╲                 ╱__╲╲",
        "   ╱____╲╲               ╱____╲╲",
        "",
        "🚨 EMERGENCIA MÉDICA 🚨"
    ]
    
    for linea in ambulancia:
        print(linea)
    
    print("\n🚑 Salvando vidas 24/7 🚑")

def coche_deportivo():
    """Coche deportivo de lujo"""
    print("🏎️ COCHE DEPORTIVO 🏎️")
    print("═" * 50)
    
    deportivo = [
        "              ╭───╮",
        "             ╱     ╲",
        "            ╱       ╲",
        "           ╱         ╲",
        "╭─────────╱           ╲─────────╮",
        "│                               │",
        "│  🏎️                     🏎️  │",
        "│     ╔═══╗         ╔═══╗     │",
        "│     ║ ◐ ║         ║ ◐ ║     │",
        "│     ╚═══╝         ╚═══╝     │",
        "╰───────────────────────────────╯",
        "        ●               ●",
        "       ╱●╲             ╱●╲",
        "      ╱_●_╲           ╱_●_╲",
        "     ╱_____╲         ╱_____╲",
        "",
        "💨 VELOCIDAD MÁXIMA 💨"
    ]
    
    for linea in deportivo:
        print(linea)
    
    print("\n🏎️ Lujo y velocidad extrema 🏎️")

def trafico_animado():
    """Simulación de tráfico animado"""
    import time
    import os
    
    print("🚦 TRÁFICO URBANO 🚦")
    
    for frame in range(12):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🚦 SIMULACIÓN DE TRÁFICO 🚦")
        print("═" * 60)
        
        # Semáforo
        if frame % 6 < 2:
            semaforo = "🟢"
            estado = "VERDE - AVANZAR"
        elif frame % 6 < 4:
            semaforo = "🟡"
            estado = "AMARILLO - PRECAUCIÓN"
        else:
            semaforo = "🔴"
            estado = "ROJO - DETENERSE"
        
        print(f"Semáforo: {semaforo} {estado}")
        print("─" * 60)
        
        # Vehículos en movimiento
        pos1 = (frame * 2) % 40
        pos2 = (frame * 3) % 40
        pos3 = (frame * 1) % 40
        
        calle1 = [' '] * 50
        calle2 = [' '] * 50
        calle3 = [' '] * 50
        
        if semaforo == "🟢":
            if pos1 < 47: calle1[pos1:pos1+3] = ['🚗', '─', '─']
            if pos2 < 47: calle2[pos2:pos2+3] = ['🚌', '═', '═']
            if pos3 < 47: calle3[pos3:pos3+3] = ['🏍️', '─', '─']
        
        print("Carril 1: " + "".join(calle1))
        print("Carril 2: " + "".join(calle2))
        print("Carril 3: " + "".join(calle3))
        
        print("\n🏙️ Ciudad en movimiento 🏙️")
        time.sleep(0.4)

def estacionamiento():
    """Vista de estacionamiento"""
    print("🅿️ ESTACIONAMIENTO 🅿️")
    print("═" * 60)
    
    parking = [
        "╔══════════════════════════════════════════════════╗",
        "║                ESTACIONAMIENTO                   ║",
        "╠══════════════════════════════════════════════════╣",
        "║                                                  ║",
        "║  🚗     🚙     🚐     ⬜     🚌     🏎️    ║",
        "║  ───    ───    ───    ───    ───    ───   ║",
        "║   A1     A2     A3     A4     A5     A6    ║",
        "║                                                  ║",
        "║════════════════════════════════════════════════  ║",
        "║                                                  ║",
        "║  🚑     ⬜     🚛     🚕     ⬜     🚓    ║",
        "║  ───    ───    ───    ───    ───    ───   ║",
        "║   B1     B2     B3     B4     B5     B6    ║",
        "║                                                  ║",
        "║════════════════════════════════════════════════  ║",
        "║                                                  ║",
        "║  🏍️     🛺     ⬜     🚜     🚒     ⬜    ║",
        "║  ───    ───    ───    ───    ───    ───   ║",
        "║   C1     C2     C3     C4     C5     C6    ║",
        "║                                                  ║",
        "╚══════════════════════════════════════════════════╝",
        "",
        "⬜ = Plaza disponible",
        "🅿️ Espacios ocupados: 14/18",
        "💳 Tarifa: $5/hora"
    ]
    
    for linea in parking:
        print(linea)
    
    print("\n🅿️ Sistema de estacionamiento inteligente 🅿️")

def vehiculos_especiales():
    """Vehículos de servicios especiales"""
    print("🚒 VEHÍCULOS ESPECIALES 🚒")
    print("═" * 60)
    
    especiales = [
        "BOMBEROS 🚒",
        "╭─────────────────────╮",
        "│ 🚒               🚒 │",
        "│   ╔═══╗     ╔═══╗   │",
        "│   ║🔥 ║     ║🔥 ║   │",
        "│   ╚═══╝     ╚═══╝   │",
        "│      BOMBEROS       │",
        "╰─────────────────────╯",
        "",
        "POLICÍA 🚓",
        "╭─────────────────────╮",
        "│ 🚓               🚓 │",
        "│   ╔═══╗     ╔═══╗   │",
        "│   ║👮 ║     ║👮 ║   │",
        "│   ╚═══╝     ╚═══╝   │",
        "│      POLICÍA        │",
        "╰─────────────────────╯",
        "",
        "TAXI 🚕",
        "╭─────────────────────╮",
        "│ 🚕               🚕 │",
        "│   ╔═══╗     ╔═══╗   │",
        "│   ║💰 ║     ║💰 ║   │",
        "│   ╚═══╝     ╚═══╝   │",
        "│       TAXI          │",
        "╰─────────────────────╯"
    ]
    
    for linea in especiales:
        print(linea)
    
    print("\n🚨 Servicios públicos esenciales 🚨")

def menu_principal():
    """Menú principal del programa"""
    while True:
        print("\n" + "═" * 60)
        print("🚗 CONCESIONARIO VIRTUAL ASCII 🚗")
        print("═" * 60)
        print("1. Automóvil sedán")
        print("2. Motocicleta deportiva")
        print("3. Camión de carga")
        print("4. Autobús urbano")
        print("5. Ambulancia")
        print("6. Coche deportivo")
        print("7. Tráfico animado")
        print("8. Estacionamiento")
        print("9. Vehículos especiales")
        print("0. Salir")
        print("═" * 60)
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            automovil_sedan()
        elif opcion == "2":
            motocicleta_ascii()
        elif opcion == "3":
            camion_carga()
        elif opcion == "4":
            autobus_urbano()
        elif opcion == "5":
            ambulancia_ascii()
        elif opcion == "6":
            coche_deportivo()
        elif opcion == "7":
            trafico_animado()
        elif opcion == "8":
            estacionamiento()
        elif opcion == "9":
            vehiculos_especiales()
        elif opcion == "0":
            print("¡Buen viaje! 🚗")
            break
        else:
            print("Opción no válida")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
