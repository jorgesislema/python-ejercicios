"""
Ejercicio 32: Serpientes ASCII

Objetivo:
- Crear diferentes tipos de serpientes ASCII
- Simular movimiento serpenteante
- Incluir diferentes especies
- Crear juegos simples

Conceptos:
- Patrones curvos
- Animación secuencial
- Caracteres de serpiente
- Movimiento ondulante
"""

def serpiente_basica():
    """Serpiente básica recta"""
    print("🐍 SERPIENTE BÁSICA 🐍")
    print("═" * 40)
    
    cabeza = "🐍"
    cuerpo = "▓"
    cola = "░"
    
    print(f"{cabeza}{cuerpo * 15}{cola}")
    print("Serpiente recta básica")

def serpiente_ondulante():
    """Serpiente con movimiento ondulante"""
    print("🐍 SERPIENTE ONDULANTE 🐍")
    print("═" * 50)
    
    patron = [
        "🐍▓▓▓░",
        "  ▓▓▓▓░",
        "    ▓▓▓▓░",
        "      ▓▓▓▓░",
        "        ▓▓▓▓░",
        "      ▓▓▓▓░",
        "    ▓▓▓▓░",
        "  ▓▓▓▓░",
        "▓▓▓▓░"
    ]
    
    for linea in patron:
        print(linea)

def serpiente_animada():
    """Serpiente con animación de movimiento"""
    import time
    import os
    
    print("🐍 SERPIENTE ANIMADA 🐍")
    
    for i in range(15):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🐍 SERPIENTE ANIMADA 🐍")
        print("═" * 50)
        
        # Crear espacio antes de la serpiente
        espacios = " " * (i % 30)
        print(f"{espacios}🐍▓▓▓▓▓▓▓░")
        
        # Simular ondulación
        if i % 4 == 0:
            print(f"{espacios}  ▓▓▓▓▓▓░")
            print(f"{espacios}    ▓▓▓▓░")
        elif i % 4 == 1:
            print(f"{espacios}▓▓▓▓▓▓░")
            print(f"{espacios}  ▓▓▓▓░")
        elif i % 4 == 2:
            print(f"{espacios}  ▓▓▓▓▓▓░")
            print(f"{espacios}    ▓▓▓▓░")
        else:
            print(f"{espacios}▓▓▓▓▓▓░")
            print(f"{espacios}▓▓▓▓░")
        
        time.sleep(0.3)

def serpientes_especies():
    """Diferentes especies de serpientes"""
    print("🐍 ESPECIES DE SERPIENTES 🐍")
    print("═" * 60)
    
    print("\n1. BOA CONSTRICTOR")
    print("🐍████████████████████████████░")
    print("  ██████████████████████████░")
    print("    ████████████████████████░")
    print("Boa constrictora - No venenosa")
    
    print("\n2. VÍBORA DE CASCABEL")
    print("🐍▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓🔔")
    print("  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░🔔")
    print("Crotalus - Venenosa")
    
    print("\n3. COBRA")
    print("    🐍")
    print("   ╱═╲")
    print("  ╱═══╲")
    print(" ╱═════╲")
    print("▓▓▓▓▓▓▓▓▓░")
    print("Naja - Venenosa mortal")
    
    print("\n4. ANACONDA")
    print("🐍██████████████████████████████████████░")
    print("  ████████████████████████████████████░")
    print("    ██████████████████████████████████░")
    print("      ████████████████████████████████░")
    print("Eunectes murinus - La más grande")
    
    print("\n5. SERPIENTE CORAL")
    print("🐍🔴⚫🟡⚫🔴⚫🟡⚫🔴⚫🟡⚫🔴░")
    print("Micrurus - Muy venenosa")

def serpiente_espiral():
    """Serpiente en forma de espiral"""
    print("🐍 SERPIENTE ESPIRAL 🐍")
    print("═" * 50)
    
    # Crear espiral
    espiral = [
        "        🐍▓▓▓▓▓▓▓▓▓▓▓▓▓",
        "        ▓                ▓",
        "        ▓  ▓▓▓▓▓▓▓▓▓▓   ▓",
        "        ▓  ▓        ▓   ▓",
        "        ▓  ▓  ▓▓▓▓  ▓   ▓",
        "        ▓  ▓  ▓  ▓  ▓   ▓",
        "        ▓  ▓  ▓▓▓▓  ▓   ▓",
        "        ▓  ▓        ▓   ▓",
        "        ▓  ▓▓▓▓▓▓▓▓▓▓   ▓",
        "        ▓                ▓",
        "        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░"
    ]
    
    for linea in espiral:
        print(linea)

def juego_serpiente_ascii():
    """Juego simple de serpiente ASCII"""
    print("🐍 JUEGO SERPIENTE ASCII 🐍")
    print("═" * 40)
    
    # Tablero 10x10
    tablero = [['·' for _ in range(20)] for _ in range(10)]
    
    # Posición inicial de la serpiente
    serpiente = [(5, 5), (5, 4), (5, 3)]
    comida = (3, 10)
    
    # Colocar serpiente
    for i, (y, x) in enumerate(serpiente):
        if i == 0:
            tablero[y][x] = '🐍'
        else:
            tablero[y][x] = '▓'
    
    # Colocar comida
    tablero[comida[0]][comida[1]] = '🍎'
    
    # Mostrar tablero
    print("┌" + "─" * 40 + "┐")
    for fila in tablero:
        print("│" + "".join(str(celda) for celda in fila) + "│")
    print("└" + "─" * 40 + "┘")
    
    print("\nControles: W(arriba) S(abajo) A(izquierda) D(derecha)")
    print("Objetivo: Come las manzanas 🍎")

def serpiente_arte():
    """Arte ASCII avanzado de serpientes"""
    print("🐍 ARTE SERPIENTE AVANZADO 🐍")
    print("═" * 60)
    
    arte = [
        "                    ╭─────╮",
        "                   ╱       ╲",
        "                  ╱  ◉   ◉  ╲",
        "                 ╱     ^     ╲",
        "                ╱    ╲___╱    ╲",
        "               ╱               ╲",
        "              ╱_________________╲",
        "             ╱                   ╲",
        "    ╭───────╱                     ╲",
        "   ╱                               ╲",
        "  ╱                                 ╲",
        " ╱                                   ╲──╮",
        "╱                                       ╲",
        "╲                                       ╱",
        " ╲                                   ╱──╯",
        "  ╲                                 ╱",
        "   ╲                               ╱",
        "    ╲───────╲                     ╱",
        "             ╲                   ╱",
        "              ╲_________________╱",
        "               ╲               ╱",
        "                ╲             ╱",
        "                 ╲___________╱",
        "",
        "        🐍 SERPIENTE PITÓN 🐍"
    ]
    
    for linea in arte:
        print(linea)

def serpientes_mitologicas():
    """Serpientes de la mitología"""
    print("🐍 SERPIENTES MITOLÓGICAS 🐍")
    print("═" * 60)
    
    print("\n1. QUETZALCÓATL (Serpiente Emplumada)")
    print("      🪶🪶🪶🪶🪶")
    print("     🪶🐍▓▓▓▓▓🪶")
    print("    🪶▓▓▓▓▓▓▓▓▓🪶")
    print("   🪶▓▓▓▓▓▓▓▓▓▓▓🪶")
    print("  🪶▓▓▓▓▓▓▓▓▓▓▓▓▓🪶")
    print(" 🪶▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓🪶")
    print("🪶▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓🪶")
    print("Dios azteca del viento y la sabiduría")
    
    print("\n2. OUROBOROS (Serpiente que se muerde la cola)")
    print("       ╭─────────────╮")
    print("      ╱               ╲")
    print("     ╱                 ╲")
    print("    ╱          🐍      ╲")
    print("   ╱         ╱█╲        ╲")
    print("  ╱         ╱███╲        ╲")
    print(" ╱          █████         ╲")
    print("╱           ╲███╱          ╲")
    print("╲            ╲█╱           ╱")
    print(" ╲                        ╱")
    print("  ╲                      ╱")
    print("   ╲                    ╱")
    print("    ╲                  ╱")
    print("     ╲________________╱")
    print("Símbolo del ciclo eterno")

def menu_principal():
    """Menú principal del programa"""
    while True:
        print("\n" + "═" * 50)
        print("🐍 GENERADOR DE SERPIENTES ASCII 🐍")
        print("═" * 50)
        print("1. Serpiente básica")
        print("2. Serpiente ondulante")
        print("3. Serpiente animada")
        print("4. Especies de serpientes")
        print("5. Serpiente espiral")
        print("6. Juego serpiente ASCII")
        print("7. Arte serpiente avanzado")
        print("8. Serpientes mitológicas")
        print("0. Salir")
        print("═" * 50)
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            serpiente_basica()
        elif opcion == "2":
            serpiente_ondulante()
        elif opcion == "3":
            serpiente_animada()
        elif opcion == "4":
            serpientes_especies()
        elif opcion == "5":
            serpiente_espiral()
        elif opcion == "6":
            juego_serpiente_ascii()
        elif opcion == "7":
            serpiente_arte()
        elif opcion == "8":
            serpientes_mitologicas()
        elif opcion == "0":
            print("¡Adiós! 🐍")
            break
        else:
            print("Opción no válida")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
