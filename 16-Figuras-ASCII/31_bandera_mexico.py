"""
Ejercicio 31: Bandera de México ASCII

Objetivo:
- Crear representaciones ASCII de la bandera de México
- Incluir escudo mexicano básico
- Mostrar proporciones correctas
- Incluir información histórica

Conceptos:
- Símbolos patrios
- Diseño con colores representados por caracteres
- Historia mexicana
- Arte ASCII avanzado
"""

def bandera_simple():
    """Bandera de México simple con proporciones correctas"""
    print("🇲🇽 BANDERA DE MÉXICO - SIMPLE 🇲🇽")
    print("═" * 50)
    
    # Verde (izquierda)
    for i in range(8):
        print("█" * 16 + "▓" * 16 + "░" * 16)
    
    print("\n🟢 Verde: Esperanza")
    print("⚪ Blanco: Unidad") 
    print("🔴 Rojo: Sangre de los héroes")

def bandera_con_escudo():
    """Bandera con escudo mexicano básico"""
    print("🇲🇽 BANDERA CON ESCUDO NACIONAL 🇲🇽")
    print("═" * 60)
    
    # Parte superior
    for i in range(3):
        print("█" * 20 + "▓" * 20 + "░" * 20)
    
    # Parte del escudo
    print("█" * 20 + "▓" * 8 + "🦅" + "🐍" + "▓" * 10 + "░" * 20)
    print("█" * 20 + "▓" * 7 + "🌵🦅🌵" + "▓" * 8 + "░" * 20)
    print("█" * 20 + "▓" * 6 + "🦅🐍🌵🦅🐍" + "▓" * 6 + "░" * 20)
    
    # Parte inferior
    for i in range(3):
        print("█" * 20 + "▓" * 20 + "░" * 20)

def bandera_detallada():
    """Bandera con escudo detallado"""
    print("🇲🇽 BANDERA DETALLADA 🇲🇽")
    print("═" * 70)
    
    escudo = [
        "       ░▓██▓░       ",
        "     ░▓█🦅█▓░     ",
        "    ░▓██🐍██▓░    ",
        "   ░▓███🌵███▓░   ",
        "  ░▓████🦅████▓░  ",
        " ░▓█████🌵█████▓░ ",
        "░▓██████🦅██████▓░",
        " ░▓█████████████▓░ ",
        "  ░▓███████████▓░  ",
        "   ░▓█████████▓░   "
    ]
    
    for i, linea in enumerate(escudo):
        if i < 3:
            print("█" * 25 + linea + "░" * 25)
        elif i < 7:
            print("█" * 25 + linea + "░" * 25)
        else:
            print("█" * 25 + linea + "░" * 25)

def bandera_animada():
    """Bandera ondeando"""
    import time
    import os
    
    print("🇲🇽 BANDERA ONDEANDO 🇲🇽")
    
    for frame in range(10):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🇲🇽 BANDERA ONDEANDO 🇲🇽")
        print("═" * 60)
        
        for i in range(8):
            if frame % 2 == 0:
                print("█" * 18 + "▓" * 18 + "░" * 18)
            else:
                print(" █" * 9 + " ▓" * 9 + " ░" * 9)
        
        print("\n🦅 ¡Viva México! 🦅")
        time.sleep(0.5)

def banderas_historicas():
    """Banderas históricas de México"""
    print("🇲🇽 BANDERAS HISTÓRICAS DE MÉXICO 🇲🇽")
    print("═" * 60)
    
    print("\n1. BANDERA DE HIDALGO (1810)")
    print("┌" + "─" * 40 + "┐")
    for i in range(6):
        print("│" + "🟤" * 40 + "│")
    print("│" + " " * 15 + "👑🎖️👑" + " " * 16 + "│")
    print("└" + "─" * 40 + "┘")
    print("Virgen de Guadalupe")
    
    print("\n2. BANDERA DE MORELOS (1813)")
    print("┌" + "─" * 40 + "┐")
    for i in range(3):
        print("│" + "⚪" * 40 + "│")
    for i in range(3):
        print("│" + "🔵" * 40 + "│")
    print("└" + "─" * 40 + "┘")
    print("Por la felicidad común")
    
    print("\n3. BANDERA ACTUAL (1968)")
    print("┌" + "─" * 60 + "┐")
    for i in range(6):
        print("│" + "🟢" * 20 + "⚪" * 20 + "🔴" * 20 + "│")
    print("└" + "─" * 60 + "┘")

def escudo_detallado():
    """Escudo nacional mexicano detallado"""
    print("🦅 ESCUDO NACIONAL MEXICANO 🦅")
    print("═" * 50)
    
    escudo = [
        "        ░▓▓▓▓▓░        ",
        "      ░▓█████▓░      ",
        "     ░▓███🦅███▓░     ",
        "    ░▓████🐍████▓░    ",
        "   ░▓█████🌵█████▓░   ",
        "  ░▓██████🦅██████▓░  ",
        " ░▓███████🌵███████▓░ ",
        "░▓████████🦅████████▓░",
        " ░▓█████████████████▓░ ",
        "  ░▓███████████████▓░  ",
        "   ░▓█████████████▓░   ",
        "    ░▓███████████▓░    ",
        "     ░▓█████████▓░     ",
        "      ░▓███████▓░      ",
        "       ░▓█████▓░       ",
        "        ░▓███▓░        ",
        "         ░▓█▓░         ",
        "          ░▓░          "
    ]
    
    for linea in escudo:
        print(linea)
    
    print("\n🦅 Águila Real")
    print("🐍 Serpiente de Cascabel")
    print("🌵 Nopal")
    print("🏝️ Islote en el lago Texcoco")

def menu_principal():
    """Menú principal del programa"""
    while True:
        print("\n" + "═" * 60)
        print("🇲🇽 BANDERAS Y SÍMBOLOS PATRIOS DE MÉXICO 🇲🇽")
        print("═" * 60)
        print("1. Bandera simple")
        print("2. Bandera con escudo")
        print("3. Bandera detallada")
        print("4. Bandera animada")
        print("5. Banderas históricas")
        print("6. Escudo nacional detallado")
        print("0. Salir")
        print("═" * 60)
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            bandera_simple()
        elif opcion == "2":
            bandera_con_escudo()
        elif opcion == "3":
            bandera_detallada()
        elif opcion == "4":
            bandera_animada()
        elif opcion == "5":
            banderas_historicas()
        elif opcion == "6":
            escudo_detallado()
        elif opcion == "0":
            print("¡Viva México! 🇲🇽")
            break
        else:
            print("Opción no válida")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
