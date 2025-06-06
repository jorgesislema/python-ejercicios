#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 29: Castillos ASCII
=============================

Objetivo:
- Crear diferentes tipos de castillos usando caracteres ASCII
- Implementar torres, murallas y fortificaciones
- Mostrar castillos medievales y fantásticos

Conceptos aplicados:
- Arquitectura en ASCII
- Estructuras complejas verticales
- Patrones geométricos repetitivos
"""

def castillo_simple():
    """Castillo básico con torre central"""
    print("🏰 CASTILLO SIMPLE 🏰")
    print()
    
    castillo = [
        "     🏴     ",
        "     |||     ",
        "   ┌─────┐   ",
        "   │     │   ",
        "   │ ⚔️  │   ",
        "   │     │   ",
        "   └─────┘   ",
        " ┌───────────┐ ",
        " │           │ ",
        " │     🚪    │ ",
        " └───────────┘ "
    ]
    
    for linea in castillo:
        print(linea)

def castillo_torres():
    """Castillo con múltiples torres"""
    print("🏰 CASTILLO CON TORRES 🏰")
    print()
    
    castillo = [
        " 🏴   🏴   🏴 ",
        " |||   |||   ||| ",
        "┌───┐ ┌───┐ ┌───┐",
        "│   │ │   │ │   │",
        "│ ⚔️│ │👑│ │🛡️ │",
        "│   │ │   │ │   │",
        "└─┬─┘ └─┬─┘ └─┬─┘",
        "  │     │     │  ",
        "┌─┴─────┴─────┴─┐",
        "│               │",
        "│       🚪      │",
        "│               │",
        "└───────────────┘"
    ]
    
    for linea in castillo:
        print(linea)

def castillo_medieval():
    """Castillo medieval detallado"""
    print("⚔️ CASTILLO MEDIEVAL ⚔️")
    print()
    
    castillo = [
        "       🏴           ",
        "       |||           ",
        "     ┌─────┐         ",
        "     │  👑 │         ",
        "     │     │         ",
        "   ┌─┴─────┴─┐       ",
        "   │         │       ",
        " ┌─┴─┐     ┌─┴─┐     ",
        " │🛡️ │     │⚔️ │     ",
        " │   │     │   │     ",
        " └─┬─┘     └─┬─┘     ",
        "   │         │       ",
        " ┌─┴─────────┴─┐     ",
        " │   🏰       │     ",
        " │      🚪     │     ",
        " └─────────────┘     "
    ]
    
    for linea in castillo:
        print(linea)

def fortaleza():
    """Fortaleza impenetrable"""
    print("🛡️ FORTALEZA 🛡️")
    print()
    
    fortaleza = [
        "🏴🏴🏴🏴🏴🏴🏴🏴🏴",
        "||||||||||||||||||||",
        "┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐",
        "│ ││ ││👑││ ││ ││ ││ │",
        "│⚔││🛡││ ││🗡││🏹││⚔││🛡│",
        "│ ││ ││ ││ ││ ││ ││ │",
        "└─┘└─┘└─┘└─┘└─┘└─┘└─┘",
        "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓",
        "▓                   ▓",
        "▓        🚪         ▓",
        "▓                   ▓",
        "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓"
    ]
    
    for linea in fortaleza:
        print(linea)

def castillo_fantastico():
    """Castillo fantástico con magia"""
    print("✨ CASTILLO FANTÁSTICO ✨")
    print()
    
    castillo = [
        "    ✨ 🌟 ✨    ",
        "      🔮      ",
        "     /||\\     ",
        "   ┌──────┐   ",
        "   │ 🧙‍♂️  │   ",
        "   │  ✨  │   ",
        "   └──┬───┘   ",
        "      │       ",
        "  ┌───┴───┐   ",
        "  │ 🐉   │   ",
        "  │   🗝️  │   ",
        "  │   🚪  │   ",
        "  └───────┘   ",
        "   🌟 ✨ 🌟   "
    ]
    
    for linea in castillo:
        print(linea)

def castillo_ruinas():
    """Ruinas de un castillo antiguo"""
    print("🏚️ RUINAS DEL CASTILLO 🏚️")
    print()
    
    ruinas = [
        "     🕊️      ",
        "     /|\\      ",
        "   ┌─. .─┐    ",
        "   │ 🕸️  .    ",
        "   .     │    ",
        "   └─. .─.    ",
        " ┌─.  🦇  .─┐ ",
        " .          . ",
        " │    💀    . ",
        " .    ___   │ ",
        " └─.──   ──.┘ ",
        "   🌿 🌿 🌿   "
    ]
    
    for linea in ruinas:
        print(linea)

def castillo_hielo():
    """Castillo de hielo"""
    print("❄️ CASTILLO DE HIELO ❄️")
    print()
    
    castillo = [
        "    ❄️ ❄️ ❄️    ",
        "      /|\\      ",
        "    ┌─────┐    ",
        "    │ 👸 │    ",
        "    │ ❄️  │    ",
        "    └──┬──┘    ",
        "  ❄️   │   ❄️  ",
        "  ┌────┴────┐  ",
        "  │         │  ",
        "  │   ❄️    │  ",
        "  │    🚪   │  ",
        "  └─────────┘  ",
        " ❄️❄️❄️❄️❄️❄️❄️ "
    ]
    
    for linea in castillo:
        print(linea)

def castillo_arena():
    """Castillo de arena en la playa"""
    print("🏖️ CASTILLO DE ARENA 🏖️")
    print()
    
    castillo = [
        "    🚩      ",
        "    |||      ",
        "  ░░░░░░░    ",
        " ░░     ░░   ",
        " ░░ 🏰  ░░   ",
        " ░░     ░░   ",
        " ░░░░░░░░░   ",
        "░░░       ░░░",
        "░░   🐚   ░░",
        "░░    _   ░░",
        "░░░░░░░░░░░░░",
        "🌊🌊🌊🌊🌊🌊🌊",
        "🏖️🐚⭐🐚🏖️🐚⭐"
    ]
    
    for linea in castillo:
        print(linea)

def castillo_asedio():
    """Castillo bajo asedio"""
    print("⚔️ CASTILLO BAJO ASEDIO ⚔️")
    print()
    
    asedio = [
        "  💥  🏴  💥  ",
        "  🏹  |||  🗡️  ",
        "    ┌─────┐    ",
        "🏹  │ 🛡️  │  ⚔️",
        "    │     │    ",
        "💥  └─────┘  💥",
        "  ┌───────────┐  ",
        "⚔️│           │🏹",
        "  │     🚪    │  ",
        "🗡️│           │💥",
        "  └───────────┘  ",
        "🔥🔥🔥🔥🔥🔥🔥🔥🔥"
    ]
    
    for linea in asedio:
        print(linea)

def palacio_real():
    """Palacio real lujoso"""
    print("👑 PALACIO REAL 👑")
    print()
    
    palacio = [
        "    👑   👑   👑    ",
        "    |||   |||   |||    ",
        "  ┌─────┬─────┬─────┐  ",
        "  │ 💎  │ 👑  │ 💎  │  ",
        "  │     │     │     │  ",
        "  └──┬──┴──┬──┴──┬──┘  ",
        "     │     │     │     ",
        " ┌───┴─────┴─────┴───┐ ",
        " │                   │ ",
        " │   💎   🚪   💎   │ ",
        " │                   │ ",
        " └───────────────────┘ ",
        "🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹🌹"
    ]
    
    for linea in palacio:
        print(linea)

def castillo_dragon():
    """Castillo guardado por un dragón"""
    print("🐉 CASTILLO DEL DRAGÓN 🐉")
    print()
    
    castillo = [
        "      🔥        ",
        "     🐉         ",
        "    /   \\       ",
        "   🏴     🏴    ",
        "   |||     |||   ",
        " ┌─────┐ ┌─────┐ ",
        " │ 👸  │ │ 🗝️  │ ",
        " │     │ │     │ ",
        " └──┬──┘ └──┬──┘ ",
        "    │       │    ",
        " ┌──┴───────┴──┐ ",
        " │ 💰   🚪  💰 │ ",
        " └─────────────┘ ",
        "   🔥 🔥 🔥 🔥   "
    ]
    
    for linea in castillo:
        print(linea)

def castillo_matematico(altura=5, torres=3):
    """Castillo generado matemáticamente"""
    print(f"🔢 CASTILLO MATEMÁTICO ({torres} torres, altura {altura}) 🔢")
    print()
    
    # Banderas en la parte superior
    banderas = ""
    for i in range(torres):
        banderas += "🏴   "
    print("  " + banderas)
    
    # Postes de banderas
    postes = ""
    for i in range(torres):
        postes += "|||  "
    print("  " + postes)
    
    # Torres
    for nivel in range(altura):
        linea = ""
        for torre in range(torres):
            if nivel == 0:
                linea += "┌───┐ "
            elif nivel == altura - 1:
                linea += "└─┬─┘ "
            else:
                simbolos = ["⚔️", "🛡️", "👑", "🗡️", "🏹"]
                simbolo = simbolos[torre % len(simbolos)]
                linea += f"│ {simbolo} │ "
        print(linea)
    
    # Base del castillo
    ancho_base = torres * 6 + 4
    print("┌" + "─" * (ancho_base - 2) + "┐")
    print("│" + " " * (ancho_base // 2 - 1) + "🚪" + " " * (ancho_base // 2 - 1) + "│")
    print("└" + "─" * (ancho_base - 2) + "┘")

def paisaje_castillos():
    """Paisaje con múltiples castillos"""
    print("🏞️ PAISAJE DE CASTILLOS 🏞️")
    print()
    
    paisaje = [
        "    ☀️         ☁️      ",
        "  🏰      🏰      🏰  ",
        "  |||      |||      ||| ",
        "┌─────┐  ┌─────┐  ┌─────┐",
        "│     │  │     │  │     │",
        "└─────┘  └─────┘  └─────┘",
        "🌲    🌲🌲    🌲🌲    🌲",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "^^^^^^^^^^^^^^^^^^^^^^^^^^"
    ]
    
    for linea in paisaje:
        print(linea)

def menu_castillos():
    """Menú interactivo para diferentes tipos de castillos"""
    while True:
        print("\n" + "="*50)
        print("🏰 GENERADOR DE CASTILLOS ASCII 🏰")
        print("="*50)
        print("1. Castillo simple")
        print("2. Castillo con torres")
        print("3. Castillo medieval")
        print("4. Fortaleza")
        print("5. Castillo fantástico")
        print("6. Ruinas del castillo")
        print("7. Castillo de hielo")
        print("8. Castillo de arena")
        print("9. Castillo bajo asedio")
        print("10. Palacio real")
        print("11. Castillo del dragón")
        print("12. Castillo matemático")
        print("13. Paisaje de castillos")
        print("14. Todos los castillos")
        print("0. Salir")
        print("-"*50)
        
        try:
            opcion = input("Selecciona una opción (0-14): ").strip()
            
            if opcion == '0':
                print("¡Que construyas tu propio reino! 👑")
                break
            elif opcion == '1':
                castillo_simple()
            elif opcion == '2':
                castillo_torres()
            elif opcion == '3':
                castillo_medieval()
            elif opcion == '4':
                fortaleza()
            elif opcion == '5':
                castillo_fantastico()
            elif opcion == '6':
                castillo_ruinas()
            elif opcion == '7':
                castillo_hielo()
            elif opcion == '8':
                castillo_arena()
            elif opcion == '9':
                castillo_asedio()
            elif opcion == '10':
                palacio_real()
            elif opcion == '11':
                castillo_dragon()
            elif opcion == '12':
                altura = int(input("Introduce la altura de las torres (3-8): ") or "5")
                torres = int(input("Introduce el número de torres (2-5): ") or "3")
                castillo_matematico(max(3, min(8, altura)), max(2, min(5, torres)))
            elif opcion == '13':
                paisaje_castillos()
            elif opcion == '14':
                castillo_simple()
                print("\n" + "-"*30 + "\n")
                castillo_torres()
                print("\n" + "-"*30 + "\n")
                castillo_medieval()
                print("\n" + "-"*30 + "\n")
                fortaleza()
                print("\n" + "-"*30 + "\n")
                castillo_fantastico()
                print("\n" + "-"*30 + "\n")
                castillo_hielo()
                print("\n" + "-"*30 + "\n")
                palacio_real()
                print("\n" + "-"*30 + "\n")
                paisaje_castillos()
            else:
                print("❌ Opción no válida. Intenta de nuevo.")
                
        except ValueError:
            print("❌ Por favor, introduce un número válido.")
        except KeyboardInterrupt:
            print("\n¡Hasta luego! 🏰")
            break
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_castillos()
