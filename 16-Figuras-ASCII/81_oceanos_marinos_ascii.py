#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 81: Océanos y Vida Marina ASCII
==========================================

Objetivo:
- Crear diferentes elementos del océano y vida marina usando ASCII
- Representar ecosistemas acuáticos diversos
- Mostrar la belleza y diversidad del mundo submarino

Conceptos aplicados:
- Ecosistemas marinos
- Biodiversidad acuática
- Conservación oceánica
- Arte ASCII temático
"""

import time
import random

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*60)
    print("🌊 GENERADOR DE OCÉANOS Y VIDA MARINA ASCII 🌊")
    print("="*60)
    print("1. 🌊 Olas del océano")
    print("2. 🐟 Pez tropical")
    print("3. 🦈 Tiburón")
    print("4. 🐙 Pulpo")
    print("5. 🐠 Banco de peces")
    print("6. 🐢 Tortuga marina")
    print("7. 🦀 Cangrejo")
    print("8. 🐋 Ballena")
    print("9. 🪸 Arrecife de coral")
    print("0. 🚪 Salir")
    print("-"*60)

def olas_oceano():
    """Crea olas del océano dinámicas"""
    print("🌊 OLAS DEL OCÉANO 🌊")
    print("Un espectáculo natural de movimiento perpetuo")
    print()
    
    olas = [
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "     ~~~~~~~~     ~~~~~~~~     ~~~~~~~~     ~~~~~~",
        "~~~~~~~~~~     ~~~~~~~~     ~~~~~~~~     ~~~~~~~~~",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "  ~~~~~~~~     ~~~~~~~~     ~~~~~~~~     ~~~~~~~~~",
        "~~~~~~~~     ~~~~~~~~     ~~~~~~~~     ~~~~~~~~~~~",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    ]
    
    for linea in olas:
        print(linea)

def pez_tropical():
    """Crea un colorido pez tropical"""
    print("🐟 PEZ TROPICAL 🐟")
    print("Habitante colorido de aguas cálidas")
    print()
    
    pez = [
        "      🟡🟠🔴      ",
        "    🟡🟠🔴🟠🟡    ",
        "   🟡🟠● ○ ●🟠🟡   ",
        "    🟡🟠🔴🟠🟡    ",
        "      🟡🟠🔴      ",
        "         ><       "
    ]
    
    for linea in pez:
        print(linea)

def tiburon():
    """Crea un imponente tiburón"""
    print("🦈 TIBURÓN 🦈")
    print("Depredador perfecto de los océanos")
    print()
    
    tiburon_ascii = [
        "                  /|   ",
        "                 / |   ",
        "   /\\           /  |   ",
        "  /  \\         /   |   ",
        " /    \\       /    |   ",
        "/      \\     /     |   ",
        "\\       \\   /      |   ",
        " \\       \\_/       |   ",
        "  \\        ●       |   ",
        "   \\      /|\\_____/    ",
        "    \\____/ | \\         ",
        "           |  \\        ",
        "           |   \\       ",
        "           |____\\      "
    ]
    
    for linea in tiburon_ascii:
        print(linea)

def pulpo():
    """Crea un inteligente pulpo"""
    print("🐙 PULPO 🐙")
    print("Maestro del camuflaje y la inteligencia marina")
    print()
    
    pulpo_ascii = [
        "     ●●●●●●●     ",
        "   ●●●●●●●●●●   ",
        "  ●●● ○   ○ ●●●  ",
        "  ●●●    ∩    ●●● ",
        "   ●●●●●●●●●●   ",
        "    ●●●●●●●●    ",
        "   /  |  |  \\   ",
        "  /   |  |   \\  ",
        " ∩    |  |    ∩ ",
        "      |  |      ",
        "     ∩    ∩     "
    ]
    
    for linea in pulpo_ascii:
        print(linea)

def banco_peces():
    """Crea un banco de peces nadando"""
    print("🐠 BANCO DE PECES 🐠")
    print("La unión hace la fuerza en el océano")
    print()
    
    banco = [
        "   🐟     🐟     🐟     🐟   ",
        "      🐟     🐟     🐟      ",
        " 🐟     🐟     🐟     🐟    ",
        "    🐟     🐟     🐟     🐟 ",
        "  🐟   🐟   🐟   🐟   🐟    ",
        "     🐟     🐟     🐟       ",
        " 🐟     🐟     🐟     🐟    ",
        "   🐟     🐟     🐟     🐟  "
    ]
    
    for linea in banco:
        print(linea)

def tortuga_marina():
    """Crea una elegante tortuga marina"""
    print("🐢 TORTUGA MARINA 🐢")
    print("Navegante ancestral de los océanos")
    print()
    
    tortuga = [
        "       ____       ",
        "      /    \\      ",
        "     /  🟫  \\     ",
        "    / 🟫🟫🟫 \\    ",
        "   / 🟫🟫🟫🟫 \\   ",
        "  /  🟫🟫🟫🟫  \\  ",
        " /    🟫🟫🟫    \\ ",
        " |  ○  🟫🟫  ○  | ",
        " \\    ______    / ",
        "  \\__/      \\__/  ",
        "     \\      /     ",
        "      \\____/      "
    ]
    
    for linea in tortuga:
        print(linea)

def cangrejo():
    """Crea un cangrejo costero"""
    print("🦀 CANGREJO 🦀")
    print("Guardián de las costas rocosas")
    print()
    
    cangrejo_ascii = [
        "  \\     ●●     /  ",
        "   \\    )(    /   ",
        "    \\   ||   /    ",
        "  ❯❯ \\  ||  / ❮❮  ",
        "      \\ || /      ",
        "   ████\\||/████   ",
        "  ████████████████ ",
        "  ████ ●● ●● ████ ",
        "  ████████████████ ",
        "   \\  |  |  |  /  ",
        "    \\ |  |  | /   ",
        "     \\|  |  |/    "
    ]
    
    for linea in cangrejo_ascii:
        print(linea)

def ballena():
    """Crea una majestuosa ballena"""
    print("🐋 BALLENA 🐋")
    print("Gigante gentil de las profundidades")
    print()
    
    ballena_ascii = [
        "                    ____    ",
        "                  _/    \\_  ",
        "                 /        \\ ",
        "                /    ●     \\",
        "_______________/____________\\",
        "\\                          /",
        " \\________________________/ ",
        "  \\____________________/    ",
        "      \\              /      ",
        "        \\    💧    /        ",
        "          \\  💧  /          ",
        "            \\💧/            "
    ]
    
    for linea in ballena_ascii:
        print(linea)

def arrecife_coral():
    """Crea un vibrante arrecife de coral"""
    print("🪸 ARRECIFE DE CORAL 🪸")
    print("Oasis de biodiversidad submarina")
    print()
    
    arrecife = [
        "🪸    🐟    🪸    🐠    🪸",
        "  🌿      🌿      🌿      ",
        "🪸  🦐  🪸  🐟  🪸  🦀  🪸",
        "    🌿  🐠    🌿    🐟    ",
        "🪸      🪸  🦈  🪸      🪸",
        "  🌿🐟    🌿    🌿    🦐  ",
        "🪸    🪸      🪸    🪸    ",
        "    🌿    🐠    🌿  🐟    ",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨"
    ]
    
    for linea in arrecife:
        print(linea)

def main():
    """Función principal con menú interactivo"""
    oceano_funciones = {
        '1': olas_oceano,
        '2': pez_tropical,
        '3': tiburon,
        '4': pulpo,
        '5': banco_peces,
        '6': tortuga_marina,
        '7': cangrejo,
        '8': ballena,
        '9': arrecife_coral
    }
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("🌊 Selecciona una opción (0-9): ").strip()
            
            if opcion == '0':
                print("\n🌊 ¡Gracias por explorar los océanos con ASCII! 🌊")
                break
            elif opcion in oceano_funciones:
                print("\n" + "="*60)
                oceano_funciones[opcion]()
                print("="*60)
            else:
                print("❌ Opción no válida. Intenta de nuevo.")
                
        except KeyboardInterrupt:
            print("\n\n🌊 ¡Hasta luego, explorador marino! 🌊")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        
        input("\n💙 Presiona Enter para continuar explorando...")

if __name__ == "__main__":
    main()
