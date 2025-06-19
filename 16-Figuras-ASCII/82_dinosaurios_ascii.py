#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 82: Dinosaurios Prehistóricos ASCII
=============================================

Objetivo:
- Crear diferentes especies de dinosaurios usando ASCII
- Representar la era mesozoica y su fauna
- Explorar la paleontología de manera visual

Conceptos aplicados:
- Paleontología
- Evolución
- Clasificación de dinosaurios
- Historia natural
"""

import time
import random

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*60)
    print("🦕 GENERADOR DE DINOSAURIOS PREHISTÓRICOS ASCII 🦕")
    print("="*60)
    print("1. 🦕 Brontosaurus")
    print("2. 🦖 Tyrannosaurus Rex")
    print("3. 🦴 Triceratops")
    print("4. 🦅 Pterodáctilo")
    print("5. 🦏 Estegosaurus")
    print("6. 🦎 Velociraptor")
    print("7. 🦴 Diplodocus")
    print("8. 🛡️ Anquilosaurus")
    print("9. 🌋 Paisaje prehistórico")
    print("0. 🚪 Salir")
    print("-"*60)

def brontosaurus():
    """Crea un pacífico Brontosaurus"""
    print("🦕 BRONTOSAURUS 🦕")
    print("Gigante herbívoro de cuello largo del Jurásico")
    print()
    
    bronto = [
        "                      ●●",
        "                    ●●  ●●",
        "                  ●●      ●●",
        "                ●●          ●●",
        "              ●●              ●●",
        "            ●●                  ●●",
        "          ●●                      ●●",
        "        ●●                          ●●",
        "      ●●                              ●●",
        "    ●●                                  ●●",
        "  ●●____________________________________●●●●●●●●●●●",
        "●●                                               ●●●●●●",
        "●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●",
        "  |     |     |     |     |     |     |     |",
        "  |     |     |     |     |     |     |     |",
        "████   ████   ████   ████   ████   ████   ████   ████"
    ]
    
    for linea in bronto:
        print(linea)

def tyrannosaurus_rex():
    """Crea el temible Tyrannosaurus Rex"""
    print("🦖 TYRANNOSAURUS REX 🦖")
    print("El rey de los depredadores del Cretácico")
    print()
    
    trex = [
        "                    ●●●●●●●",
        "                  ●●       ●●",
        "                 ●●  ●●  ●● ●●",
        "                ●●    ●●●●   ●●",
        "               ●●  ▼▼▼▼▼▼▼  ●●",
        "              ●●   ▼▼▼▼▼▼▼   ●●",
        "             ●●     ▼▼▼▼▼     ●●",
        "            ●●                 ●●",
        "           ●●                   ●●",
        "          ●●●●●●●●●●●●●●●●●●●●●●●●●",
        "         ●●                       ●●",
        "        ●●                         ●●",
        "       ●●     ████    ████         ●●",
        "      ●●      ████    ████          ●●",
        "     ●●                              ●●",
        "    ●●          ████      ████        ●●",
        "   ●●           ████      ████         ●●",
        "████████       ████      ████      ████████"
    ]
    
    for linea in trex:
        print(linea)

def triceratops():
    """Crea un resistente Triceratops"""
    print("🦴 TRICERATOPS 🦴")
    print("Herbívoro blindado con tres cuernos")
    print()
    
    tricera = [
        "         ▲     ●●●●●●●     ▲",
        "          ▲  ●●       ●●  ▲",
        "           ▲●●  ●●  ●●  ●●▲",
        "            ●●    ●●    ●●",
        "           ●●             ●●",
        "          ●●               ●●",
        "         ●●                 ●●",
        "        ●●                   ●●",
        "       ●●                     ●●",
        "      ●●                       ●●",
        "     ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●",
        "    ●●                           ●●",
        "   ●●                             ●●",
        "  ●●      ████    ████    ████     ●●",
        " ●●       ████    ████    ████      ●●",
        "████████ ████    ████    ████ ████████",
        "  |  |     |       |       |     |  |",
        "████ ████ ████   ████   ████   ████ ████"
    ]
    
    for linea in tricera:
        print(linea)

def pterodactilo():
    """Crea un Pterodáctilo volador"""
    print("🦅 PTERODÁCTILO 🦅")
    print("Reptil volador dominante de los cielos")
    print()
    
    ptero = [
        "                 ●●●●●●●",
        "               ●●       ●●",
        "              ●●  ●●  ●● ●●",
        "             ●●    ●●●●   ●●",
        "            ●●             ●●",
        "           ●●               ●●",
        "     ████████                 ████████",
        "   ███      ●●               ●●      ███",
        " ███          ●●             ●●          ███",
        "██              ●●           ●●              ██",
        "█                ●●         ●●                █",
        "█                 ●●       ●●                 █",
        "██                 ●●     ●●                 ██",
        " ███                ●●   ●●                ███",
        "   ███               ●●●●●               ███",
        "     ████████                   ████████",
        "            ●●●●●●●●●●●●●●●●●●●●",
        "               ●●         ●●",
        "              ████       ████"
    ]
    
    for linea in ptero:
        print(linea)

def estegosaurus():
    """Crea un Estegosaurus con placas dorsales"""
    print("🦏 ESTEGOSAURUS 🦏")
    print("Herbívoro con distintivas placas en el lomo")
    print()
    
    estego = [
        "    ▲   ▲   ▲   ▲   ▲   ▲   ▲",
        "   ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲",
        "  ▲   ▲   ▲   ▲   ▲   ▲   ▲  ▲",
        " ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●",
        "●●                               ●●",
        "●●  ●●  ●●                        ●●",
        "●●    ●●                           ●●",
        " ●●                                ●●",
        "  ●●                              ●●",
        "   ●●                            ●●",
        "    ●●                          ●●",
        "     ●●●●●●●●●●●●●●●●●●●●●●●●●●●●",
        "       |     |     |     |",
        "       |     |     |     |",
        "     ████   ████   ████   ████"
    ]
    
    for linea in estego:
        print(linea)

def velociraptor():
    """Crea un ágil Velociraptor"""
    print("🦎 VELOCIRAPTOR 🦎")
    print("Cazador inteligente y veloz en manada")
    print()
    
    raptor = [
        "                 ●●●●●●",
        "               ●●      ●●",
        "              ●●  ●●  ●● ●●",
        "             ●●    ●●●●   ●●",
        "            ●●             ●●",
        "           ●●               ●●",
        "          ●●                 ●●",
        "         ●●                   ●●",
        "        ●●                     ●●",
        "       ●●                       ●●",
        "      ●●                         ●●",
        "     ●●                           ●●",
        "    ●●     ████                   ●●",
        "   ●●      ████                    ●●",
        "  ●●              ████              ●●",
        " ●●               ████               ●●",
        "●●                ████                ●●",
        "                 ▼████▼",
        "                  ████"
    ]
    
    for linea in raptor:
        print(linea)

def diplodocus():
    """Crea un largo Diplodocus"""
    print("🦴 DIPLODOCUS 🦴")
    print("El dinosaurio más largo conocido")
    print()
    
    diplo = [
        "                                                    ●●",
        "                                                  ●●  ●●",
        "                                                ●●      ●●",
        "                                              ●●          ●●",
        "                                            ●●              ●●",
        "                                          ●●                  ●●",
        "                                        ●●                      ●●",
        "                                      ●●                          ●●",
        "    ▲   ▲   ▲   ▲   ▲   ▲   ▲   ▲  ●●                              ●●",
        "   ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲●●                                  ●●",
        "●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●                                    ●●",
        "●●                                                                       ●●",
        " ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●",
        "   |     |     |     |     |     |     |     |     |     |",
        "   |     |     |     |     |     |     |     |     |     |",
        " ████   ████   ████   ████   ████   ████   ████   ████   ████   ████"
    ]
    
    for linea in diplo:
        print(linea)

def anquilosaurus():
    """Crea un blindado Anquilosaurus"""
    print("🛡️ ANQUILOSAURUS 🛡️")
    print("Tanque viviente del período Cretácico")
    print()
    
    anquilo = [
        "       ●●●●●●●●●●●●●●●●●●●●●●●●●",
        "     ●●                         ●●",
        "    ●●  ●●  ●●               ●●  ●●",
        "   ●●     ●●                  ●●  ●●",
        "  ●●                               ●●",
        " ●●  ████  ████  ████  ████  ████  ●●",
        "●●   ████  ████  ████  ████  ████   ●●",
        "●●   ████  ████  ████  ████  ████   ●●",
        "●●   ████  ████  ████  ████  ████   ●●",
        " ●●  ████  ████  ████  ████  ████  ●●",
        "  ●●                               ●●",
        "   ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●",
        "      |      |      |      |",
        "      |      |      |      |",
        "    ████    ████    ████    ████",
        "                               ●●●●●●●●",
        "                              ●●      ●●",
        "                             ●●  ████  ●●",
        "                              ●●      ●●",
        "                               ●●●●●●●●"
    ]
    
    for linea in anquilo:
        print(linea)

def paisaje_prehistorico():
    """Crea un paisaje del período mesozoico"""
    print("🌋 PAISAJE PREHISTÓRICO 🌋")
    print("La Tierra durante la era de los dinosaurios")
    print()
    
    paisaje = [
        "           ☀️                    🦅",
        "                     ☁️             ☁️",
        "    🌋     ☁️                         ",
        "   /|\\       🦕            🦖         ",
        "  / | \\        \\\\            |\\       ",
        " /  |  \\        \\\\___________| \\      ",
        "/   |   \\        ||||||||||||   \\     ",
        "    |            ||||||||||||    \\    ",
        "~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "🌴🌴🌴🌴   🦴      🌿🌿🌿     🌴🌴🌴🌴🌴",
        "🌿  🌴  🌿     🪨🪨     🌿🌿     🌿🌴🌿",
        "  🌿🌿      🦕        🪨🪨🪨       🌿  ",
        "🌴🌿🌴🌿  🌿🌿🌿🌿  🌿🌿🌿🌿🌿  🌴🌿🌴🌿",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨"
    ]
    
    for linea in paisaje:
        print(linea)

def main():
    """Función principal con menú interactivo"""
    dino_funciones = {
        '1': brontosaurus,
        '2': tyrannosaurus_rex,
        '3': triceratops,
        '4': pterodactilo,
        '5': estegosaurus,
        '6': velociraptor,
        '7': diplodocus,
        '8': anquilosaurus,
        '9': paisaje_prehistorico
    }
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("🦕 Selecciona una opción (0-9): ").strip()
            
            if opcion == '0':
                print("\n🦕 ¡Gracias por viajar al pasado con ASCII! 🦕")
                break
            elif opcion in dino_funciones:
                print("\n" + "="*60)
                dino_funciones[opcion]()
                print("="*60)
            else:
                print("❌ Opción no válida. Intenta de nuevo.")
                
        except KeyboardInterrupt:
            print("\n\n🦕 ¡Hasta luego, paleontólogo! 🦕")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        
        input("\n🦴 Presiona Enter para continuar explorando...")

if __name__ == "__main__":
    main()
