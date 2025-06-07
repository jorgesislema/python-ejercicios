"""
Ejercicio 34: Instrumentos Musicales ASCII

Objetivo:
- Crear diferentes instrumentos musicales en ASCII
- Incluir instrumentos de viento, cuerda y percusión
- Simular efectos sonoros con texto
- Crear una orquesta ASCII

Conceptos:
- Arte ASCII musical
- Representación de formas complejas
- Símbolos musicales
- Clasificación de instrumentos
"""

def piano_ascii():
    """Piano de cola ASCII"""
    print("🎹 PIANO DE COLA 🎹")
    print("═" * 50)
    
    piano = [
        "         ╭─────────────────────────╮",
        "        ╱                         ╲",
        "       ╱                           ╲",
        "      ╱                             ╲",
        "     ╱                               ╲",
        "    ╱                                 ╲",
        "   ╱                                   ╲",
        "  ╱_____________________________________╲",
        " ╱                                       ╲",
        "╱_________________________________________╲",
        "║▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓║",
        "║░▓░▓░░▓░▓░▓░░▓░▓░░▓░▓░▓░░▓░▓░▓░░▓░▓░░▓║",
        "║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║",
        "║_______________________________________║",
        "║                                       ║",
        "║  🎼 ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫  ║",
        "║                                       ║",
        "╚═══════════════════════════════════════╝",
        "   │     │                     │     │  ",
        "   │     │                     │     │  ",
        "  ╱│╲   ╱│╲                   ╱│╲   ╱│╲ ",
        " ╱ │ ╲ ╱ │ ╲                 ╱ │ ╲ ╱ │ ╲",
        "╱  │  ╲╱  │  ╲               ╱  │  ╲╱  │  ╲",
        "╲__│___╱╲__│__╱               ╲__│___╱╲__│__╱"
    ]
    
    for linea in piano:
        print(linea)
    
    print("\n🎵 ¡Música clásica en el aire! 🎵")

def guitarra_acustica():
    """Guitarra acústica"""
    print("🎸 GUITARRA ACÚSTICA 🎸")
    print("═" * 40)
    
    guitarra = [
        "       ╭───╮",
        "      ╱     ╲",
        "     ╱       ╲",
        "    ╱         ╲",
        "   ╱           ╲",
        "  ╱    ● ●      ╲",
        " ╱               ╲",
        "╱                 ╲",
        "╲                 ╱",
        " ╲               ╱",
        "  ╲             ╱",
        "   ╲___________╱",
        "   ║|||||||||||║",
        "   ║|||||||||||║",
        "   ║|||||||||||║",
        "   ║|||||||||||║",
        "   ║|||||||||||║",
        "   ║|||||||||||║",
        "   ║|||||||||||║",
        "   ║|||||||||||║",
        "   ║|||||||||||║",
        "   ║|||||||||||║",
        "   ║|||||||||||║",
        "   ║|||||||||||║",
        "   ║|||||||||||║",
        "   ╠═══════════╣",
        "   ╠═══════════╣",
        "   ╠═══════════╣",
        "   ╠═══════════╣",
        "   ╠═══════════╣",
        "   ╚═══════════╝",
        "   ● ● ● ● ● ●",
        "   ╲ ╲ ╲ ╲ ╲ ╲",
        "    ╲ ╲ ╲ ╲ ╲ ╲",
        "     ╲_╲_╲_╲_╲_╲"
    ]
    
    for linea in guitarra:
        print(linea)
    
    print("\n🎶 Melodías suaves 🎶")

def violin_ascii():
    """Violín ASCII"""
    print("🎻 VIOLÍN 🎻")
    print("═" * 30)
    
    violin = [
        "     ╭─╮",
        "    ╱   ╲",
        "   ╱  ●  ╲",
        "  ╱       ╲",
        " ╱         ╲",
        "╱           ╲",
        "╲           ╱",
        " ╲         ╱",
        "  ╲       ╱",
        "   ╲_____╱",
        "     ║|║",
        "     ║|║",
        "     ║|║",
        "     ║|║",
        "     ║|║",
        "     ║|║",
        "     ║|║",
        "     ║|║",
        "     ║|║",
        "     ║|║",
        "     ║|║",
        "   ╭─║|║─╮",
        "  ╱  ║|║  ╲",
        " ╱   ║|║   ╲",
        "╱    ║|║    ╲",
        "╲    ║|║    ╱",
        " ╲   ║|║   ╱",
        "  ╲  ║|║  ╱",
        "   ╲_║|║_╱",
        "     ║|║",
        "     ███",
        "",
        "   ╱─────╲  ← Arco",
        "  ╱       ╲",
        " ╱_________╲"
    ]
    
    for linea in violin:
        print(linea)
    
    print("\n🎼 Sonidos celestiales 🎼")

def bateria_ascii():
    """Batería completa"""
    print("🥁 BATERÍA COMPLETA 🥁")
    print("═" * 60)
    
    bateria = [
        "   🥁      🥁🥁      🥁",
        "  ╱╲╲      ╱╲╱╲      ╱╱╲",
        " ╱  ╲╲    ╱  ╲  ╲    ╱╱  ╲",
        "╱____╲╲  ╱____╲__╲  ╱╱____╲",
        "║    ║╲╲ ║    ║  ║ ╱╱║    ║",
        "║    ║ ╲╲║    ║  ║╱╱ ║    ║",
        "║    ║  ╲║    ║  ║╱  ║    ║",
        "╚════╝   ╚════╝══╝   ╚════╝",
        "   │       │  │       │",
        "   │       │  │       │",
        "   │   ╭───╯  ╰───╮   │",
        "   │  ╱           ╲  │",
        "   │ ╱             ╲ │",
        "   │╱               ╲│",
        "   ╱                 ╲",
        "  ╱___________________╲",
        " ╱                     ╲",
        "╱_______________________╲",
        "║                       ║",
        "║       🥁 KICK 🥁       ║",
        "║                       ║",
        "╚═══════════════════════╝",
        "",
        "🥢 Palillos: ╱╲  ╱╲",
        "           ╱  ╲╱  ╲"
    ]
    
    for linea in bateria:
        print(linea)
    
    print("\n🎵 ¡Ritmo y percusión! 🎵")

def trompeta_ascii():
    """Trompeta"""
    print("🎺 TROMPETA 🎺")
    print("═" * 50)
    
    trompeta = [
        "                    ╭─────────╮",
        "                   ╱           ╲",
        "                  ╱             ╲",
        "                 ╱               ╲",
        "════════════════╱                 ╲",
        "███████████████╱                   ╲",
        "███████████████╲                   ╱",
        "════════════════╲                 ╱",
        "                 ╲               ╱",
        "                  ╲             ╱",
        "                   ╲___________╱",
        "      ●     ●     ●",
        "      ║     ║     ║",
        "      ╚═════╩═════╝",
        "",
        "🎵 Pistones para cambiar notas 🎵"
    ]
    
    for linea in trompeta:
        print(linea)
    
    print("\n🎺 ¡Música de viento metal! 🎺")

def flauta_ascii():
    """Flauta traversa"""
    print("🪈 FLAUTA TRAVERSA 🪈")
    print("═" * 50)
    
    flauta = [
        "●═══○═══○═══○═══○═══○═══○═══○═══○═══●",
        "║                                   ║",
        "╚═══════════════════════════════════╝",
        "    ↑   ↑   ↑   ↑   ↑   ↑   ↑   ↑",
        "   Orificios para las notas",
        "",
        "🎵 Instrumento de viento madera 🎵"
    ]
    
    for linea in flauta:
        print(linea)
    
    print("\n🪈 Melodías suaves y etéreas 🪈")

def arpa_ascii():
    """Arpa de concierto"""
    print("🪕 ARPA DE CONCIERTO 🪕")
    print("═" * 40)
    
    arpa = [
        "      ╭───╮",
        "     ╱     ╲",
        "    ╱       ╲",
        "   ╱         ╲",
        "  ╱           ╲",
        " ╱             ╲",
        "╱               ╲",
        "║               ║",
        "║ │ │ │ │ │ │ │ ║",
        "║ │ │ │ │ │ │ │ ║",
        "║ │ │ │ │ │ │ │ ║",
        "║ │ │ │ │ │ │ │ ║",
        "║ │ │ │ │ │ │ │ ║",
        "║ │ │ │ │ │ │ │ ║",
        "║ │ │ │ │ │ │ │ ║",
        "║ │ │ │ │ │ │ │ ║",
        "║ │ │ │ │ │ │ │ ║",
        "║ │ │ │ │ │ │ │ ║",
        "║ │ │ │ │ │ │ │ ║",
        "║ │ │ │ │ │ │ │ ║",
        "║ │ │ │ │ │ │ │ ║",
        "║ │ │ │ │ │ │ │ ║",
        "║ │ │ │ │ │ │ │ ║",
        "║ │ │ │ │ │ │ │ ║",
        "║ │ │ │ │ │ │ │ ║",
        "║ │ │ │ │ │ │ │ ║",
        "║ │ │ │ │ │ │ │ ║",
        "║ │ │ │ │ │ │ │ ║",
        "║ │ │ │ │ │ │ │ ║",
        "║ │ │ │ │ │ │ │ ║",
        "╚═══════════════╝"
    ]
    
    for linea in arpa:
        print(linea)
    
    print("\n🪕 Sonidos angelicales 🪕")

def orquesta_completa():
    """Orquesta sinfónica completa"""
    print("🎼 ORQUESTA SINFÓNICA 🎼")
    print("═" * 80)
    
    orquesta = [
        "                     🎻🎻🎻🎻🎻",
        "                  🎻🎻🎻🎻🎻🎻🎻",
        "               🎻🎻🎻🎻🎻🎻🎻🎻🎻",
        "                  Violines",
        "",
        "            🎺🎺🎺      🪈🪈🪈      🎷🎷",
        "          Trompetas   Flautas   Saxofones",
        "",
        "     🥁🥁🥁              🪕              🎹",
        "   Percusión            Arpa           Piano",
        "",
        "                      🎭",
        "                   Director",
        "",
        "  👥👥👥👥👥👥👥👥👥👥👥👥👥👥👥👥👥👥👥👥",
        "              🎶 AUDIENCIA 🎶"
    ]
    
    for linea in orquesta:
        print(linea)
    
    print("\n🎼 ¡SINFONÍA MAGISTRAL! 🎼")
    print("🎵 ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ 🎵")

def instrumentos_animados():
    """Instrumentos con animación musical"""
    import time
    import os
    
    print("🎵 CONCIERTO ANIMADO 🎵")
    
    for i in range(8):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🎵 CONCIERTO EN VIVO 🎵")
        print("═" * 50)
        
        if i % 4 == 0:
            print("🎹 ♪♪♪ PIANO ♪♪♪")
            print("  ╔═══════════════╗")
            print("  ║ ♪ ♫ ♪ ♫ ♪ ♫ ║")
            print("  ╚═══════════════╝")
        elif i % 4 == 1:
            print("🎸 ♫♫♫ GUITARRA ♫♫♫")
            print("      ╭───╮")
            print("     ╱ ♪ ♫ ╲")
            print("    ╱ ♫ ♪ ♫ ╲")
            print("   ╱___♪___╲")
        elif i % 4 == 2:
            print("🥁 ♪♪♪ BATERÍA ♪♪♪")
            print("   ♫ 🥁 ♫")
            print("  ♪ ╱╲╱╲ ♪")
            print(" ♫ ╱____╲ ♫")
        else:
            print("🎺 ♫♫♫ TROMPETA ♫♫♫")
            print("♪♪♪═══════════╮")
            print("              ╲ ♫")
            print("               ╲♪")
        
        print("\n🎼 " + "♪ " * (i + 1) + "🎼")
        time.sleep(0.8)

def menu_principal():
    """Menú principal del programa"""
    while True:
        print("\n" + "═" * 60)
        print("🎼 INSTRUMENTOS MUSICALES ASCII 🎼")
        print("═" * 60)
        print("1. Piano de cola")
        print("2. Guitarra acústica")
        print("3. Violín")
        print("4. Batería completa")
        print("5. Trompeta")
        print("6. Flauta traversa")
        print("7. Arpa de concierto")
        print("8. Orquesta completa")
        print("9. Concierto animado")
        print("0. Salir")
        print("═" * 60)
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            piano_ascii()
        elif opcion == "2":
            guitarra_acustica()
        elif opcion == "3":
            violin_ascii()
        elif opcion == "4":
            bateria_ascii()
        elif opcion == "5":
            trompeta_ascii()
        elif opcion == "6":
            flauta_ascii()
        elif opcion == "7":
            arpa_ascii()
        elif opcion == "8":
            orquesta_completa()
        elif opcion == "9":
            instrumentos_animados()
        elif opcion == "0":
            print("¡Que la música te acompañe! 🎵")
            break
        else:
            print("Opción no válida")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
