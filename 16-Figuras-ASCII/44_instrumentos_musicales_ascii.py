"""
Ejercicio 44: Instrumentos Musicales ASCII

Objetivo:
- Crear figuras de instrumentos musicales en ASCII
- Incluir variantes: piano, guitarra, violín, tambor, trompeta, saxofón
- Permitir personalización y mostrar notas musicales

Conceptos:
- Arte ASCII temático musical
- Menú interactivo
- Representación visual de instrumentos
"""

def piano_ascii():
    """Piano ASCII con teclas"""
    print("🎹 PIANO ASCII 🎹")
    print("═" * 50)
    
    print("Teclas blancas:")
    print("┌───┬───┬───┬───┬───┬───┬───┬───┐")
    print("│ C │ D │ E │ F │ G │ A │ B │ C │")
    print("│   │   │   │   │   │   │   │   │")
    print("│   │   │   │   │   │   │   │   │")
    print("└───┴───┴───┴───┴───┴───┴───┴───┘")
    
    print("\nTeclas negras:")
    print("  ▓▓  ▓▓    ▓▓  ▓▓  ▓▓")
    print("  ▓▓  ▓▓    ▓▓  ▓▓  ▓▓")
    print("  C#  D#    F#  G#  A#")
    
    print("\n♪ Do Re Mi Fa Sol La Si Do ♪")

def guitarra_ascii():
    """Guitarra acústica ASCII"""
    print("🎸 GUITARRA ASCII 🎸")
    print("═" * 40)
    
    guitarra = [
        "      ╭─────────────╮",
        "     ╱               ╲",
        "    ╱                 ╲",
        "   ╱   ○             ╲",
        "  ╱                   ╲",
        " ╱_____________________╲",
        "│||||||||||||||||||||||│",
        "│||||||||||||||||||||||│",
        "│||||||||||||||||||||||│",
        "│||||||||||||||||||||||│",
        "│||||||||||||||||||||||│",
        "│||||||||||||||||||||||│",
        " ╲_____________________╱",
        "  ╲                   ╱",
        "   ╲                 ╱",
        "    ╲_______________╱",
        "          │││││││",
        "          ○○○○○○○"
    ]
    
    for linea in guitarra:
        print(linea)
    
    print("\n🎵 E A D G B E (cuerdas estándar)")

def violin_ascii():
    """Violín ASCII"""
    print("🎻 VIOLÍN ASCII 🎻")
    print("═" * 30)
    
    violin = [
        "       ╭─╮",
        "      ╱   ╲",
        "     ╱     ╲",
        "    ╱   f   ╲",
        "   ╱    f    ╲",
        "  ╱           ╲",
        " ╱_____________╲",
        "│|||||||||||||||│",
        "│|||||||||||||||│",
        "│|||||||||||||||│",
        "│|||||||||||||||│",
        " ╲_____________╱",
        "  ╲           ╱",
        "   ╲         ╱",
        "    ╲_______╱",
        "       │││",
        "       ○○○"
    ]
    
    for linea in violin:
        print(linea)
    
    print("\n♫ G D A E (cuerdas del violín)")

def tambor_ascii():
    """Tambor ASCII"""
    print("🥁 TAMBOR ASCII 🥁")
    print("═" * 30)
    
    tambor = [
        "    ╭─────────╮",
        "   ╱           ╲",
        "  ╱             ╲",
        " ╱_______________╲",
        "│                 │",
        "│      BOOM!      │",
        "│                 │",
        "│                 │",
        "│                 │",
        " ╲_______________╱",
        "  ╲             ╱",
        "   ╲___________╱"
    ]
    
    for linea in tambor:
        print(linea)
    
    print("\n🥁 ¡PAM PAM PAM!")

def trompeta_ascii():
    """Trompeta ASCII"""
    print("🎺 TROMPETA ASCII 🎺")
    print("═" * 40)
    
    trompeta = [
        "        ╭─────────────╮",
        "       ╱               ╲",
        "      ╱                 ╲",
        "═════╱___________________╲═══════════",
        "     │ ○ ○ ○             │",
        "═════╲___________________╱═══════════",
        "      ╲                 ╱",
        "       ╲_______________╱",
        "        ╰─────────────╯"
    ]
    
    for linea in trompeta:
        print(linea)
    
    print("\n🎺 ¡TA TA TA TAAAAA!")

def saxofon_ascii():
    """Saxofón ASCII"""
    print("🎷 SAXOFÓN ASCII 🎷")
    print("═" * 30)
    
    saxofon = [
        "      ╭─╮",
        "     ╱   ╲",
        "    ╱     ╲",
        "   ╱       ╲",
        "  ╱         ╲",
        " ╱___________╲",
        "│             │",
        "│  ○ ○ ○ ○   │",
        "│             │",
        "│  ○ ○ ○ ○   │",
        "│             │",
        "│  ○ ○ ○ ○   │",
        " ╲___________╱",
        "  ╲         ╱",
        "   ╲_______╱",
        "    ╲     ╱",
        "     ╲___╱"
    ]
    
    for linea in saxofon:
        print(linea)
    
    print("\n🎷 ♫ Jazz smooth sounds ♫")

def notas_musicales():
    """Mostrar notas musicales ASCII"""
    print("🎵 NOTAS MUSICALES ASCII 🎵")
    print("═" * 40)
    
    print("Pentagrama con notas:")
    print("     ♪       ♫       ♪")
    print("  ───────────────────────")
    print("     ♫       ♪       ♫")
    print("  ───────────────────────")
    print("       ♪       ♫")
    print("  ───────────────────────")
    print("     ♫       ♪")
    print("  ───────────────────────")
    print("       ♪")
    print("  ───────────────────────")
    
    print("\n🎵 Do Re Mi Fa Sol La Si 🎵")
    print("♪ ♫ ♪ ♫ ♪ ♫ ♪")

def menu_principal():
    """Menú principal del programa"""
    while True:
        print("\n" + "═" * 50)
        print("🎵 INSTRUMENTOS MUSICALES ASCII 🎶")
        print("═" * 50)
        print("1. Piano")
        print("2. Guitarra")
        print("3. Violín")
        print("4. Tambor")
        print("5. Trompeta")
        print("6. Saxofón")
        print("7. Notas musicales")
        print("0. Salir")
        print("═" * 50)
        
        opcion = input("Selecciona un instrumento: ")
        
        if opcion == "1":
            piano_ascii()
        elif opcion == "2":
            guitarra_ascii()
        elif opcion == "3":
            violin_ascii()
        elif opcion == "4":
            tambor_ascii()
        elif opcion == "5":
            trompeta_ascii()
        elif opcion == "6":
            saxofon_ascii()
        elif opcion == "7":
            notas_musicales()
        elif opcion == "0":
            print("¡Hasta luego, músico! 🎵")
            break
        else:
            print("Opción no válida")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
