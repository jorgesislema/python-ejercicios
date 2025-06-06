#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 27: Peces ASCII
=========================

Objetivo:
- Crear diferentes tipos de peces usando caracteres ASCII
- Implementar acuarios y escenas marinas
- Mostrar peces en movimiento y cardúmenes

Conceptos aplicados:
- Formas orgánicas acuáticas
- Patrones de movimiento
- Ecosistemas marinos
"""

import time
import random

def pez_simple():
    """Pez básico y simple"""
    print("🐟 PEZ SIMPLE 🐟")
    print()
    
    pez = [
        "   ><>   ",
        "  ><>    ",
        " ><>     "
    ]
    
    for linea in pez:
        print(linea)

def pez_detallado():
    """Pez más detallado con aletas"""
    print("🐠 PEZ DETALLADO 🐠")
    print()
    
    pez = [
        "     /|   ",
        "    ( :>  ",
        "     \\|   "
    ]
    
    for linea in pez:
        print(linea)

def pez_grande():
    """Pez grande con escamas y detalles"""
    print("🐡 PEZ GRANDE 🐡")
    print()
    
    pez = [
        "       /|\\      ",
        "      /   \\     ",
        "     |  o  |>   ",
        "      \\   /     ",
        "       \\|/      "
    ]
    
    for linea in pez:
        print(linea)

def pez_angel():
    """Pez ángel con aletas características"""
    print("👼 PEZ ÁNGEL 👼")
    print()
    
    pez = [
        "    ^    ",
        "   /|\\   ",
        "  / | \\  ",
        " |  o  |>",
        "  \\ | /  ",
        "   \\|/   ",
        "    v    "
    ]
    
    for linea in pez:
        print(linea)

def tiburon():
    """Tiburón temible"""
    print("🦈 TIBURÓN 🦈")
    print()
    
    tiburon_figura = [
        "        ^        ",
        "       /|\\       ",
        "      / | \\      ",
        "     |  ¤  |>>>> ",
        "      \\ | /      ",
        "       \\|/       ",
        "        v        "
    ]
    
    for linea in tiburon_figura:
        print(linea)

def pez_globo():
    """Pez globo inflado"""
    print("🐡 PEZ GLOBO 🐡")
    print()
    
    pez = [
        "   /^^^\\   ",
        "  / o o \\  ",
        " |   ^   |>",
        "  \\ === /  ",
        "   \\___/   "
    ]
    
    for linea in pez:
        print(linea)

def pez_payaso():
    """Pez payaso (Nemo)"""
    print("🤡 PEZ PAYASO 🤡")
    print()
    
    pez = [
        "   🟠⚪🟠   ",
        "  🟠 o ⚪🟠>",
        "   🟠⚪🟠   "
    ]
    
    for linea in pez:
        print(linea)

def cardumen():
    """Cardúmen de peces"""
    print("🐠 CARDÚMEN 🐠")
    print()
    
    cardumen_figura = [
        " ><>    ><>    ><> ",
        "   ><>    ><>    ><",
        " ><>    ><>    ><> ",
        "   ><>    ><>      ",
        " ><>    ><>    ><> "
    ]
    
    for linea in cardumen_figura:
        print(linea)

def acuario():
    """Acuario completo con peces y decoración"""
    print("🏠 ACUARIO 🏠")
    print()
    
    acuario_figura = [
        "┌────────────────────┐",
        "│  ><>      🐠      │",
        "│      🐟     ><>   │",
        "│ 🐠      ><>       │",
        "│    ><>      🐟    │",
        "│ 🌿    🐠    🌿   │",
        "│🌿 🪨  ><>  🪨 🌿 │",
        "└────────────────────┘"
    ]
    
    for linea in acuario_figura:
        print(linea)

def fondo_marino():
    """Escena del fondo marino"""
    print("🌊 FONDO MARINO 🌊")
    print()
    
    escena = [
        "🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊",
        "   🐠    🐟    🐡   ",
        " 🐟    🦈    🐠     ",
        "    🐠    🐟    🐠  ",
        " 🌿  🐟  🌿  🐡  🌿 ",
        "🌿🪨🌿🪨🌿🪨🌿🪨🌿🪨",
        "~~~~~~~~~~~~~~~~~~~ ",
        "🏔️🏔️🏔️🏔️🏔️🏔️🏔️🏔️🏔️🏔️"
    ]
    
    for linea in escena:
        print(linea)

def pez_dorado():
    """Pez dorado de la suerte"""
    print("🥇 PEZ DORADO 🥇")
    print()
    
    pez = [
        "    ✨/|\\✨    ",
        "   ✨/   \\✨   ",
        "  ✨| 🥇 |>✨  ",
        "   ✨\\   /✨   ",
        "    ✨\\|/✨    "
    ]
    
    for linea in pez:
        print(linea)

def peces_tropicales():
    """Variedad de peces tropicales"""
    print("🏝️ PECES TROPICALES 🏝️")
    print()
    
    peces = [
        " 🐠 🐟 🐡 🐠 🐟 ",
        "   🐟 🐠 🐟 🐡   ",
        " 🐡 🐠 🐟 🐠 🐡 ",
        "   🐠 🐡 🐠 🐟   ",
        " 🐟 🐠 🐡 🐟 🐠 "
    ]
    
    for linea in peces:
        print(linea)

def pez_animado():
    """Simulación de pez nadando"""
    print("🎬 PEZ ANIMADO 🎬")
    print("(Presiona Ctrl+C para detener)")
    print()
    
    frames = [
        "><>",
        ">°>",
        "><>",
        ">°>"
    ]
    
    try:
        for ciclo in range(10):
            for i, frame in enumerate(frames):
                print("\033[H\033[J", end="")  # Limpiar pantalla
                print("🎬 PEZ ANIMADO 🎬")
                print("(Presiona Ctrl+C para detener)")
                print()
                
                # Simular movimiento horizontal
                posicion = (ciclo + i) % 20
                espacios = " " * posicion
                
                print(espacios + frame)
                print("~" * 25)
                
                time.sleep(0.3)
    except KeyboardInterrupt:
        print("\n¡Natación interrumpida!")

def pez_matematico(longitud=5):
    """Pez generado matemáticamente"""
    print(f"🔢 PEZ MATEMÁTICO (Longitud: {longitud}) 🔢")
    print()
    
    # Cuerpo del pez
    for i in range(3):
        linea = ""
        if i == 0:  # Aleta superior
            linea = " " * (longitud - 2) + "/|\\"
        elif i == 1:  # Cuerpo principal
            cuerpo = "=" * (longitud - 1)
            linea = cuerpo + " o |>"
        else:  # Aleta inferior
            linea = " " * (longitud - 2) + "\\|/"
        
        print(linea)

def ecosistema_marino():
    """Ecosistema marino completo"""
    print("🌊 ECOSISTEMA MARINO 🌊")
    print()
    
    ecosistema = [
        "☀️ ☀️ ☀️ ☀️ ☀️ ☀️",
        "🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊",
        "  🐠    🐟    🐡   ",
        "     🦈         🐠  ",
        " 🐟    🐠    🐟     ",
        "    🐡    🐠    🐟  ",
        " 🌿  🐟  🌿  🐡  🌿 ",
        "🦀🌿🪨🌿🪨🌿🪨🌿🦞🌿",
        "⭐🐚🪨🐚⭐🐚🪨🐚⭐🐚"
    ]
    
    for linea in ecosistema:
        print(linea)

def banco_peces():
    """Banco de peces en formación"""
    print("🎯 BANCO DE PECES 🎯")
    print()
    
    # Generar formación triangular
    for i in range(5):
        espacios = " " * (4 - i)
        peces = "🐟 " * (i + 1)
        print(espacios + peces)

def menu_peces():
    """Menú interactivo para diferentes tipos de peces"""
    while True:
        print("\n" + "="*50)
        print("🐟 GENERADOR DE PECES ASCII 🐟")
        print("="*50)
        print("1. Pez simple")
        print("2. Pez detallado")
        print("3. Pez grande")
        print("4. Pez ángel")
        print("5. Tiburón")
        print("6. Pez globo")
        print("7. Pez payaso")
        print("8. Cardúmen")
        print("9. Acuario")
        print("10. Fondo marino")
        print("11. Pez dorado")
        print("12. Peces tropicales")
        print("13. Pez animado")
        print("14. Pez matemático")
        print("15. Ecosistema marino")
        print("16. Banco de peces")
        print("17. Todos los peces")
        print("0. Salir")
        print("-"*50)
        
        try:
            opcion = input("Selecciona una opción (0-17): ").strip()
            
            if opcion == '0':
                print("¡Que nades en mares de felicidad! 🐟")
                break
            elif opcion == '1':
                pez_simple()
            elif opcion == '2':
                pez_detallado()
            elif opcion == '3':
                pez_grande()
            elif opcion == '4':
                pez_angel()
            elif opcion == '5':
                tiburon()
            elif opcion == '6':
                pez_globo()
            elif opcion == '7':
                pez_payaso()
            elif opcion == '8':
                cardumen()
            elif opcion == '9':
                acuario()
            elif opcion == '10':
                fondo_marino()
            elif opcion == '11':
                pez_dorado()
            elif opcion == '12':
                peces_tropicales()
            elif opcion == '13':
                pez_animado()
            elif opcion == '14':
                longitud = int(input("Introduce la longitud del pez (3-10): ") or "5")
                pez_matematico(max(3, min(10, longitud)))
            elif opcion == '15':
                ecosistema_marino()
            elif opcion == '16':
                banco_peces()
            elif opcion == '17':
                pez_simple()
                print("\n" + "-"*30 + "\n")
                pez_detallado()
                print("\n" + "-"*30 + "\n")
                pez_grande()
                print("\n" + "-"*30 + "\n")
                pez_angel()
                print("\n" + "-"*30 + "\n")
                tiburon()
                print("\n" + "-"*30 + "\n")
                pez_globo()
                print("\n" + "-"*30 + "\n")
                acuario()
                print("\n" + "-"*30 + "\n")
                fondo_marino()
            else:
                print("❌ Opción no válida. Intenta de nuevo.")
                
        except ValueError:
            print("❌ Por favor, introduce un número válido.")
        except KeyboardInterrupt:
            print("\n¡Hasta luego! 🐟")
            break
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_peces()
