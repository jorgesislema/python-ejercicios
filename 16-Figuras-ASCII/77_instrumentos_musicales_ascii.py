#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 77: Instrumentos Musicales ASCII
=========================================

Objetivo:
- Crear representaciones ASCII de diferentes instrumentos musicales
- Implementar instrumentos de diversas culturas
- Mostrar la riqueza musical mundial

Conceptos aplicados:
- Representación de instrumentos musicales
- Cultura musical global
- Arte sonoro y visual
"""

def mostrar_menu():
    """Muestra el menú de opciones disponibles"""
    print("\n" + "="*50)
    print("🎵 GENERADOR DE INSTRUMENTOS MUSICALES ASCII 🎵")
    print("="*50)
    print("1. Guitarra")
    print("2. Piano")
    print("3. Violín")
    print("4. Batería")
    print("5. Saxofón")
    print("6. Flauta")
    print("7. Trompeta")
    print("8. Arpa")
    print("9. Maracas")
    print("0. Salir")
    print("-"*50)

def guitarra():
    """Guitarra acústica clásica"""
    print("🎸 GUITARRA 🎸")
    print()
    print("Instrumento de cuerdas versátil")
    print()
    
    guitarra_ascii = [
        "       🎸 GUITARRA 🎸        ",
        "",
        "          ┌─┬─┬─┬─┬─┬─┐     ",
        "          │○│○│○│○│○│○│     ",
        "          ├─┼─┼─┼─┼─┼─┤     ",
        "          ┃ ┃ ┃ ┃ ┃ ┃ ┃     ",
        "       ┌──┨ ┃ ┃ ┃ ┃ ┃ ┃     ",
        "       │  ┃ ┃ ┃ ┃ ┃ ┃ ┃     ",
        "       │  ┃ ┃ ┃ ┃ ┃ ┃ ┃     ",
        "       │  ┃ ┃ ┃ ┃ ┃ ┃ ┃     ",
        "       │  ┃ ┃ ┃ ┃ ┃ ┃ ┃  ●  ",
        "       │  ┃ ┃ ┃ ┃ ┃ ┃ ┃     ",
        "       │  ┃ ┃ ┃ ┃ ┃ ┃ ┃     ",
        "       │  ┃ ┃ ┃ ┃ ┃ ┃ ┃  ●  ",
        "       │  ┃ ┃ ┃ ┃ ┃ ┃ ┃     ",
        "    ╭──┴──┨ ┃ ┃ ┃ ┃ ┃ ┃     ",
        "   ╱      ┃ ┃ ┃ ┃ ┃ ┃ ┃  ●  ",
        "  ╱       ┃ ┃ ┃ ┃ ┃ ┃ ┃     ",
        " ╱        ┃ ┃ ┃ ┃ ┃ ┃ ┃     ",
        "│    ●    ┃ ┃ ┃ ┃ ┃ ┃ ┃  ●  ",
        "│         ┃ ┃ ┃ ┃ ┃ ┃ ┃     ",
        " ╲        ┃ ┃ ┃ ┃ ┃ ┃ ┃     ",
        "  ╲       ┗━┷━┷━┷━┷━┷━┛     ",
        "   ╲_____________________    ",
        "",
        "🎸 6 cuerdas afinadas",
        "🎵 Do, Re, Mi, Fa, Sol, La",
        "🎶 Rock, flamenco, clásica"
    ]
    
    for linea in guitarra_ascii:
        print(linea)

def piano():
    """Piano de cola elegante"""
    print("🎹 PIANO 🎹")
    print()
    print("Rey de los instrumentos")
    print()
    
    piano_ascii = [
        "         🎹 PIANO 🎹         ",
        "",
        "    ┌─────────────────────┐  ",
        "    │ ♫   S T E I N W A Y │  ",
        "    └─┬─────────────────┬─┘  ",
        "      │                 │    ",
        "      │ ┌─────────────┐ │    ",
        "      │ │  ♪ MÚSICA ♪ │ │    ",
        "      │ └─────────────┘ │    ",
        "      └─┬─────────────┬─┘    ",
        "        │             │      ",
        "  ┌─────┴─────────────┴─────┐",
        "  │⬜⬛⬜⬛⬜⬜⬛⬜⬛⬜⬛⬜│",
        "  │⬜⬛⬜⬛⬜⬜⬛⬜⬛⬜⬛⬜│",
        "  │⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜│",
        "  │⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜│",
        "  │⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜│",
        "  └───┬─────────────┬─────┘  ",
        "      │ ●         ● │        ",
        "      │             │        ",
        "      └─────────────┘        ",
        "",
        "🎹 88 teclas (52 blancas + 36 negras)",
        "🎵 Rango completo de 7 octavas",
        "🎼 Mozart, Beethoven, Chopin"
    ]
    
    for linea in piano_ascii:
        print(linea)

def violin():
    """Violín clásico elegante"""
    print("🎻 VIOLÍN 🎻")
    print()
    print("Alma de la orquesta")
    print()
    
    violin_ascii = [
        "        🎻 VIOLÍN 🎻         ",
        "",
        "          ● ● ● ●            ",
        "          ┃ ┃ ┃ ┃            ",
        "          ┃ ┃ ┃ ┃            ",
        "       ┌──┨ ┃ ┃ ┃            ",
        "       │  ┃ ┃ ┃ ┃            ",
        "       │  ┃ ┃ ┃ ┃            ",
        "       │  ┃ ┃ ┃ ┃            ",
        "       │  ┃ ┃ ┃ ┃  ♫         ",
        "       │  ┃ ┃ ┃ ┃            ",
        "       │  ┃ ┃ ┃ ┃            ",
        "       │  ┃ ┃ ┃ ┃            ",
        "    ╭──┴──┨ ┃ ┃ ┃            ",
        "   ╱      ┃ ┃ ┃ ┃            ",
        "  ╱    ƒ  ┃ ┃ ┃ ┃            ",
        " ╱        ┃ ┃ ┃ ┃  ♪         ",
        "│     ●   ┃ ┃ ┃ ┃            ",
        "│         ┃ ┃ ┃ ┃            ",
        " ╲    ƒ   ┃ ┃ ┃ ┃            ",
        "  ╲       ┗━┷━┷━┛            ",
        "   ╲____________________     ",
        "                         \\   ",
        "                          \\  ",
        "                       🏹 \\ ",
        "                           \\",
        "",
        "🎻 4 cuerdas: Sol, Re, La, Mi",
        "🏹 Arco de crin de caballo",
        "🎼 Vivaldi, Bach, Paganini"
    ]
    
    for linea in violin_ascii:
        print(linea)

def bateria():
    """Set de batería completo"""
    print("🥁 BATERÍA 🥁")
    print()
    print("El corazón rítmico de la música")
    print()
    
    bateria_ascii = [
        "        🥁 BATERÍA 🥁        ",
        "",
        "      ●           ●          ",
        "     ╱│╲         ╱│╲         ",
        "    ╱ │ ╲       ╱ │ ╲        ",
        "   ╱  │  ╲     ╱  │  ╲       ",
        "  ●───●───●   ●───●───●      ",
        "  │ CRASH │   │ RIDE  │      ",
        "  └───┬───┘   └───┬───┘      ",
        "      │           │          ",
        "  ┌───●───┐   ┌───●───┐      ",
        "  │ TOM 1 │   │ TOM 2 │      ",
        "  └───────┘   └───────┘      ",
        "                             ",
        "  ┌─────────┐ ┌───────────┐  ",
        "  │ SNARE   │ │ FLOOR TOM │  ",
        "  │  DRUM   │ │           │  ",
        "  └─────────┘ └───────────┘  ",
        "                             ",
        "    ┌─────────────────┐      ",
        "    │   KICK  DRUM    │      ",
        "    │       🦶        │      ",
        "    └─────────────────┘      ",
        "",
        "🥁 Kick, snare, hi-hat, toms",
        "🥢 Baquetas de madera",
        "🎵 Rock, jazz, latino"
    ]
    
    for linea in bateria_ascii:
        print(linea)

def saxofon():
    """Saxofón dorado"""
    print("🎷 SAXOFÓN 🎷")
    print()
    print("El alma del jazz")
    print()
    
    saxofon_ascii = [
        "       🎷 SAXOFÓN 🎷        ",
        "",
        "          ●                 ",
        "          │                 ",
        "      ┌───●───┐             ",
        "      │ MOUTH │             ",
        "      │ PIECE │             ",
        "      └───┬───┘             ",
        "          ┃                 ",
        "          ┃ ●               ",
        "          ┃                 ",
        "          ┃ ●               ",
        "          ┃                 ",
        "          ┃ ●               ",
        "       ╭──┃──╮              ",
        "      ╱   ┃ ● ╲             ",
        "     ╱    ┃    ╲            ",
        "    ╱     ┃ ●   ╲           ",
        "   ╱      ┃      ╲  ♪       ",
        "  ╱       ┃ ●     ╲         ",
        " ╱        ┃        ╲        ",
        "│         ┃ ●       │       ",
        "│         ┃         │  ♫    ",
        " ╲        ┃ ●      ╱        ",
        "  ╲       ┗━━━━━━━╱         ",
        "   ╲               ╱        ",
        "    ╲_____________╱         ",
        "           🔔               ",
        "",
        "🎷 Saxofón alto en Mi♭",
        "🎵 Jazz, blues, clásica",
        "🎼 Charlie Parker, Coltrane"
    ]
    
    for linea in saxofon_ascii:
        print(linea)

def flauta():
    """Flauta traversa plateada"""
    print("🪈 FLAUTA 🪈")
    print()
    print("Viento mágico y melodioso")
    print()
    
    flauta_ascii = [
        "         🪈 FLAUTA 🪈        ",
        "",
        "                            ",
        "  ♪ ═══●═══●═══●═══●═══●═══●",
        "        │   │   │   │   │   │",
        "        ●   ●   ●   ●   ●   ●",
        "                            ",
        "  ♫ ═══●═══●═══●═══●═══●═══●",
        "        │   │   │   │   │   │",
        "        ●   ●   ●   ●   ●   ●",
        "                            ",
        "     ┌─┐                    ",
        "     │●│← EMBOCADURA        ",
        "     └─┘                    ",
        "",
        "    DIGITACIÓN PARA DO:     ",
        "                            ",
        "    ●●○●●●○                 ",
        "    ││││││└─ Fa#            ",
        "    │││││└─── Sol           ",
        "    ││││└──── La            ",
        "    │││└───── Si            ",
        "    ││└────── Do            ",
        "    │└─────── Re            ",
        "    └──────── Mi            ",
        "",
        "🪈 Flauta traversa en Do",
        "🎵 Escala cromática completa",
        "🎼 Mozart, Bach, Debussy"
    ]
    
    for linea in flauta_ascii:
        print(linea)

def trompeta():
    """Trompeta dorada"""
    print("🎺 TROMPETA 🎺")
    print()
    print("Majestuosidad en metal")
    print()
    
    trompeta_ascii = [
        "        🎺 TROMPETA 🎺       ",
        "",
        "      ●                     ",
        "      │                     ",
        "  ┌───●───┐                 ",
        "  │ MOUTH │                 ",
        "  │ PIECE │                 ",
        "  └───┬───┘                 ",
        "      ┃                     ",
        "   ┌──┃──┐ ●               ",
        "   │  ┃  │ │ VALVE 1       ",
        "   │  ┃  │ ●               ",
        "   └──┃──┘                 ",
        "   ┌──┃──┐ ●               ",
        "   │  ┃  │ │ VALVE 2       ",
        "   │  ┃  │ ●               ",
        "   └──┃──┘                 ",
        "   ┌──┃──┐ ●               ",
        "   │  ┃  │ │ VALVE 3       ",
        "   │  ┃  │ ●               ",
        "   └──┃──┘                 ",
        "      ┃                     ",
        "   ╭──┃╮   ♪               ",
        "  ╱   ┃ ╲                  ",
        " ╱    ┗━━╲═══════════════╗  ",
        "│                        ║  ",
        " ╲                      ╱   ",
        "  ╲____________________╱    ",
        "           🔔               ",
        "",
        "🎺 Trompeta en Si♭",
        "🎵 Jazz, clásica, militar",
        "🎼 Miles Davis, Louis Armstrong"
    ]
    
    for linea in trompeta_ascii:
        print(linea)

def arpa():
    """Arpa clásica elegante"""
    print("🪕 ARPA 🪕")
    print()
    print("Instrumento celestial de cuerdas")
    print()
    
    arpa_ascii = [
        "         🪕 ARPA 🪕         ",
        "",
        "            ╭─●             ",
        "           ╱  ┃             ",
        "          ╱   ┃             ",
        "         ╱    ┃             ",
        "        ╱     ┃             ",
        "       ╱      ┃             ",
        "      ╱       ┃ ♪           ",
        "     ╱        ┃             ",
        "    ╱         ┃             ",
        "   ╱          ┃             ",
        "  ╱           ┃             ",
        " ╱            ┃             ",
        "╱             ┃ ♫           ",
        "│             ┃             ",
        "│             ┃             ",
        "│             ┃             ",
        "│             ┃             ",
        "│             ┃ ♪           ",
        "│    ♫        ┃             ",
        "│             ┃             ",
        "│             ┃             ",
        "╲             ┃             ",
        " ╲____________┃_____________╱",
        "  ╲___________●___________╱ ",
        "",
        "🪕 47 cuerdas cromáticas",
        "🎵 Rango de 6½ octavas",
        "🎼 Música clásica y celta"
    ]
    
    for linea in arpa_ascii:
        print(linea)

def maracas():
    """Maracas latinoamericanas"""
    print("🪇 MARACAS 🪇")
    print()
    print("Ritmo tropical latino")
    print()
    
    maracas_ascii = [
        "       🪇 MARACAS 🪇        ",
        "",
        "       ●         ●          ",
        "      ╱ ╲       ╱ ╲         ",
        "     ╱   ╲     ╱   ╲        ",
        "    ╱ ● ● ╲   ╱ ● ● ╲       ",
        "   ╱ ● ● ● ╲ ╱ ● ● ● ╲      ",
        "  │ ● ● ● ● │ │ ● ● ● ●│     ",
        "  │ ● ● ● ● │ │ ● ● ● ●│     ",
        "   ╲ ● ● ● ╱ ╲ ● ● ● ╱      ",
        "    ╲ ● ● ╱   ╲ ● ● ╱       ",
        "     ╲___╱     ╲___╱        ",
        "       ┃         ┃          ",
        "       ┃  SHAKE  ┃          ",
        "       ┃    ♪    ┃          ",
        "       ┃  SHAKE  ┃          ",
        "       ┃    ♫    ┃          ",
        "       ┃  SHAKE  ┃          ",
        "      ═╪═       ═╪═         ",
        "      ═╪═       ═╪═         ",
        "      ═╪═       ═╪═         ",
        "",
        "    🎵 ¡Cha-cha-cha! 🎵     ",
        "",
        "🪇 Maracas de calabaza",
        "🎵 Salsa, merengue, cumbia",
        "🌶️ Ritmo caribeño ardiente"
    ]
    
    for linea in maracas_ascii:
        print(linea)

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Selecciona una opción (0-9): ").strip()
            
            if opcion == '0':
                print("\n¡Que la música llene tu vida! 🎵")
                break
            elif opcion == '1':
                guitarra()
            elif opcion == '2':
                piano()
            elif opcion == '3':
                violin()
            elif opcion == '4':
                bateria()
            elif opcion == '5':
                saxofon()
            elif opcion == '6':
                flauta()
            elif opcion == '7':
                trompeta()
            elif opcion == '8':
                arpa()
            elif opcion == '9':
                maracas()
            else:
                print("❌ Opción no válida. Por favor, elige una opción del 0 al 9.")
                
        except ValueError:
            print("❌ Por favor, introduce un número válido.")
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego! 🎵")
            break
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
