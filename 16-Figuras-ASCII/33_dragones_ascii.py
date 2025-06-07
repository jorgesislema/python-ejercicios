"""
Ejercicio 33: Dragones ASCII

Objetivo:
- Crear diferentes tipos de dragones ASCII
- Incluir dragones orientales y occidentales
- Simular vuelo y respiración de fuego
- Crear escenas épicas

Conceptos:
- Arte ASCII complejo
- Animaciones avanzadas
- Mitología y fantasía
- Diseño de criaturas
"""

def dragon_occidental():
    """Dragón occidental clásico"""
    print("🐉 DRAGÓN OCCIDENTAL 🐉")
    print("═" * 60)
    
    dragon = [
        "                    ╭─╮",
        "                   ╱   ╲",
        "                  ╱  ◉  ╲",
        "                 ╱   ∩   ╲",
        "        ╭────────╱    ╲___╱",
        "       ╱                  ╲",
        "      ╱      🔥🔥🔥         ╲",
        "     ╱                      ╲",
        "    ╱                        ╲",
        "   ╱                          ╲",
        "  ╱____________________________╲",
        " ╱                              ╲",
        "╱________________________________╲",
        "╲                                ╱",
        " ╲______________________________╱",
        "  ╲____________________________╱",
        "   ╲__________________________╱",
        "    ╲________________________╱",
        "     ╲______________________╱",
        "      ╲____________________╱",
        "       ╲__________________╱",
        "        ╲________________╱",
        "         ╲______________╱",
        "          ╲____________╱",
        "           ╲__________╱",
        "            ╲________╱",
        "             ╲______╱",
        "              ╲____╱",
        "               ╲__╱",
        "                ╲╱"
    ]
    
    for linea in dragon:
        print(linea)
    
    print("\n🐉 Dragón escupiendo fuego 🔥")

def dragon_oriental():
    """Dragón oriental (chino)"""
    print("🐲 DRAGÓN ORIENTAL 🐲")
    print("═" * 80)
    
    dragon = [
        "      ╭──╮                                                    ",
        "     ╱ ◉◉ ╲                                                   ",
        "    ╱  ∩∩  ╲       🎋🎋🎋                                     ",
        "   ╱   ╲╱   ╲     ╱     ╲                                    ",
        "  ╱_________╲    ╱       ╲                                   ",
        " ╱           ╲  ╱         ╲                                  ",
        "╱             ╲╱           ╲─────╮                           ",
        "╲                           ╲    ╲                          ",
        " ╲                           ╲    ╲                         ",
        "  ╲___________________________╲    ╲                        ",
        "   ╱                           ╲    ╲                       ",
        "  ╱                             ╲    ╲                      ",
        " ╱                               ╲    ╲─────╮               ",
        "╱                                 ╲    ╲    ╲              ",
        "╲                                  ╲    ╲    ╲             ",
        " ╲__________________________________╲    ╲    ╲            ",
        "  ╱                                  ╲    ╲    ╲           ",
        " ╱                                    ╲    ╲    ╲          ",
        "╱                                      ╲____╲____╲         ",
        "╲                                           ╲              ",
        " ╲___________________________________________╲             ",
        "  ╱                                                         ",
        " ╱                                                          ",
        "╱____________________________________________________________",
        "╲                                                           ",
        " ╲__________________________________________________________╱"
    ]
    
    for linea in dragon:
        print(linea)
    
    print("\n🐲 Dragón de la sabiduría y fortuna 🍀")

def dragon_volando():
    """Dragón en vuelo"""
    print("🐉 DRAGÓN VOLANDO 🐉")
    print("═" * 70)
    
    dragon = [
        "              ╭─╮    ╭────────────╮         ",
        "             ╱ ◉ ╲  ╱              ╲        ",
        "            ╱  ∩  ╲╱                ╲       ",
        "           ╱   ╲__╱                  ╲      ",
        "          ╱                           ╲     ",
        "         ╱                             ╲    ",
        "        ╱_______________________________╲   ",
        "       ╱                                 ╲  ",
        "      ╱___________________________________╲ ",
        "     ╱                                     ╲",
        "    ╱                                       ╲",
        "   ╱_________________________________________╲",
        "  ╱                                           ╲",
        " ╱_____________________________________________╲",
        "╱                                               ╲",
        "╲                                               ╱",
        " ╲_____________________________________________╱",
        "  ╲                                           ╱",
        "   ╲_________________________________________╱",
        "    ╲                                       ╱",
        "     ╲_____________________________________╱",
        "      ╲___________________________________╱",
        "       ╲_________________________________╱",
        "        ╲_______________________________╱",
        "         ╲_____________________________╱",
        "          ╲___________________________╱",
        "           ╲_________________________╱",
        "            ╲_______________________╱",
        "             ╲_____________________╱",
        "              ╲___________________╱"
    ]
    
    for linea in dragon:
        print(linea)
    
    print("\n🌤️ Surcando los cielos ☁️")

def dragon_animado():
    """Dragón con animación de vuelo"""
    import time
    import os
    
    print("🐉 DRAGÓN ANIMADO 🐉")
    
    for frame in range(12):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🐉 DRAGÓN VOLANDO 🐉")
        print("═" * 60)
        
        # Posición del dragón
        pos_x = frame * 3
        espacios = " " * (pos_x % 40)
        
        # Aleteo de las alas
        if frame % 3 == 0:
            alas = "╱╲     ╱╲"
            cuerpo = "  🐉   "
        elif frame % 3 == 1:
            alas = "──     ──"
            cuerpo = "  🐉   "
        else:
            alas = "╲╱     ╲╱"
            cuerpo = "  🐉   "
        
        print(f"{espacios}{alas}")
        print(f"{espacios}{cuerpo}")
        print(f"{espacios}▓▓▓▓▓▓▓")
        
        # Fuego ocasional
        if frame % 4 == 0:
            print(f"{espacios}  🔥🔥🔥")
        else:
            print()
        
        print("\n☁️ ☁️ ☁️ ☁️ ☁️ ☁️ ☁️")
        time.sleep(0.4)

def dragon_respirando_fuego():
    """Dragón escupiendo fuego"""
    print("🐉 DRAGÓN RESPIRANDO FUEGO 🐉")
    print("═" * 70)
    
    dragon = [
        "           ╭─╮",
        "          ╱ ◉ ╲",
        "         ╱  ∩  ╲",
        "        ╱   O   ╲ 🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥",
        "       ╱    ╲___╱  🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥",
        "      ╱           🔥🔥🔥🔥🔥🔥🔥🔥🔥",
        "     ╱             🔥🔥🔥🔥🔥🔥🔥",
        "    ╱               🔥🔥🔥🔥🔥",
        "   ╱                 🔥🔥🔥",
        "  ╱                   🔥",
        " ╱_____________________",
        "╱                       ╲",
        "╲                       ╱",
        " ╲_____________________╱",
        "  ╲___________________╱",
        "   ╲_________________╱",
        "    ╲_______________╱",
        "     ╲_____________╱",
        "      ╲___________╱",
        "       ╲_________╱",
        "        ╲_______╱",
        "         ╲_____╱",
        "          ╲___╱",
        "           ╲_╱"
    ]
    
    for linea in dragon:
        print(linea)
    
    print("\n🔥 ¡LLAMARADA DEVASTADORA! 🔥")

def dragon_bebe():
    """Dragón bebé kawaii"""
    print("🥺 DRAGÓN BEBÉ 🥺")
    print("═" * 40)
    
    dragon = [
        "      ╭─╮",
        "     ╱ ◉◉ ╲",
        "    ╱  ∩   ╲",
        "   ╱   ○    ╲",
        "  ╱    ╲___╱ ╲",
        " ╱            ╲",
        "╱______________╲",
        "╲              ╱",
        " ╲____________╱",
        "  ╲__________╱",
        "   ╲________╱",
        "    ╲______╱",
        "     ╲____╱",
        "      ╲__╱",
        "       ╲╱"
    ]
    
    for linea in dragon:
        print(linea)
    
    print("\n🥰 ¡Pequeño y adorable! 💕")

def dragon_epico():
    """Dragón épico detallado"""
    print("🐉 DRAGÓN ÉPICO 🐉")
    print("═" * 80)
    
    dragon = [
        "                           ╭─────╮                           ",
        "                          ╱       ╲                          ",
        "                         ╱  ◉   ◉  ╲                         ",
        "                        ╱     ^     ╲                        ",
        "                       ╱    ╲─────╱  ╲                       ",
        "              ╭───────╱      ╲___╱    ╲                      ",
        "             ╱                         ╲                     ",
        "            ╱                           ╲                    ",
        "           ╱                             ╲                   ",
        "          ╱                               ╲                  ",
        "      ╭──╱                                 ╲──╮              ",
        "     ╱                                         ╲             ",
        "    ╱                                           ╲            ",
        "   ╱                                             ╲           ",
        "  ╱                                               ╲          ",
        " ╱                                                 ╲         ",
        "╱___________________________________________________╲        ",
        "╲                                                   ╱        ",
        " ╲                                                 ╱         ",
        "  ╲                                               ╱          ",
        "   ╲                                             ╱           ",
        "    ╲                                           ╱            ",
        "     ╲                                         ╱             ",
        "      ╲───────────────────────────────────────╱              ",
        "       ╲                                     ╱               ",
        "        ╲                                   ╱                ",
        "         ╲                                 ╱                 ",
        "          ╲                               ╱                  ",
        "           ╲                             ╱                   ",
        "            ╲                           ╱                    ",
        "             ╲                         ╱                     ",
        "              ╲                       ╱                      ",
        "               ╲                     ╱                       ",
        "                ╲                   ╱                        ",
        "                 ╲                 ╱                         ",
        "                  ╲               ╱                          ",
        "                   ╲             ╱                           ",
        "                    ╲           ╱                            ",
        "                     ╲         ╱                             ",
        "                      ╲       ╱                              ",
        "                       ╲     ╱                               ",
        "                        ╲   ╱                                ",
        "                         ╲ ╱                                 ",
        "                          ╲╱                                 "
    ]
    
    for linea in dragon:
        print(linea)
    
    print("\n⚔️ REY DE LOS DRAGONES ⚔️")
    print("🔥 Guardián de tesoros ancestrales 💎")

def batalla_dragones():
    """Escena de batalla entre dragones"""
    print("⚔️ BATALLA DE DRAGONES ⚔️")
    print("═" * 80)
    
    batalla = [
        "  🐉                                                     🐲  ",
        " ╱╲ ╲           🔥🔥🔥                   🔥🔥🔥           ╱ ╱╲ ",
        "╱  ╲ ╲            🔥🔥                   🔥🔥            ╱ ╱  ╲",
        "   ╲ ╲             🔥                   🔥             ╱ ╱   ",
        "    ╲ ╲                                               ╱ ╱    ",
        "     ╲ ╲                                             ╱ ╱     ",
        "      ╲ ╲                                           ╱ ╱      ",
        "       ╲ ╲                                         ╱ ╱       ",
        "        ╲ ╲                                       ╱ ╱        ",
        "         ╲ ╲                                     ╱ ╱         ",
        "          ╲ ╲                                   ╱ ╱          ",
        "           ╲ ╲                                 ╱ ╱           ",
        "            ╲ ╲                               ╱ ╱            ",
        "             ╲ ╲                             ╱ ╱             ",
        "              ╲ ╲                           ╱ ╱              ",
        "               ╲ ╲                         ╱ ╱               ",
        "                ╲ ╲                       ╱ ╱                ",
        "                 ╲ ╲                     ╱ ╱                 ",
        "                  ╲ ╲                   ╱ ╱                  ",
        "                   ╲ ╲                 ╱ ╱                   ",
        "                    ╲ ╲               ╱ ╱                    ",
        "                     ╲ ╲             ╱ ╱                     ",
        "                      ╲ ╲           ╱ ╱                      ",
        "                       ╲ ╲         ╱ ╱                       ",
        "                        ╲ ╲       ╱ ╱                        ",
        "                         ╲ ╲     ╱ ╱                         ",
        "                          ╲ ╲   ╱ ╱                          ",
        "                           ╲ ╲ ╱ ╱                           ",
        "                            ╲ ╲╱ ╱                            ",
        "                             ╲ ▓ ╱                             ",
        "                              ╲ ╱                              ",
        "                               ╲╱                               "
    ]
    
    for linea in batalla:
        print(linea)
    
    print("\n💥 ¡CHOQUE ÉPICO DE TITANES! 💥")
    print("🏰 Defendiendo el reino 🛡️")

def menu_principal():
    """Menú principal del programa"""
    while True:
        print("\n" + "═" * 60)
        print("🐉 GENERADOR DE DRAGONES ASCII 🐉")
        print("═" * 60)
        print("1. Dragón occidental")
        print("2. Dragón oriental")
        print("3. Dragón volando")
        print("4. Dragón animado")
        print("5. Dragón respirando fuego")
        print("6. Dragón bebé")
        print("7. Dragón épico")
        print("8. Batalla de dragones")
        print("0. Salir")
        print("═" * 60)
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            dragon_occidental()
        elif opcion == "2":
            dragon_oriental()
        elif opcion == "3":
            dragon_volando()
        elif opcion == "4":
            dragon_animado()
        elif opcion == "5":
            dragon_respirando_fuego()
        elif opcion == "6":
            dragon_bebe()
        elif opcion == "7":
            dragon_epico()
        elif opcion == "8":
            batalla_dragones()
        elif opcion == "0":
            print("¡Que los dragones te protejan! 🐉")
            break
        else:
            print("Opción no válida")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
