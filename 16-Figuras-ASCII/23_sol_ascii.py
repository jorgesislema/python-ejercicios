#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 23: Sol ASCII
======================

Objetivo:
- Crear diferentes representaciones de soles usando caracteres ASCII
- Implementar variaciones de tamaño y estilo
- Añadir efectos de rayos y resplandor

Conceptos aplicados:
- Patrones circulares
- Rayos direccionales
- Símbolos ASCII decorativos
"""

def sol_basico():
    """Sol simple con rayos básicos"""
    print("☀️ SOL BÁSICO ☀️")
    print()
    
    sol = [
        "    \\  |  /    ",
        "     \\ | /     ",
        "   --- ☀️ ---   ",
        "     / | \\     ",
        "    /  |  \\    "
    ]
    
    for linea in sol:
        print(linea)

def sol_detallado():
    """Sol más detallado con cara sonriente"""
    print("🌞 SOL DETALLADO 🌞")
    print()
    
    sol = [
        "       \\   |   /       ",
        "     \\  \\  |  /  /     ",
        "   \\   \\  \\|/  /   /   ",
        "     --- (^o^) ---     ",
        "   /   /  /|\\  \\   \\   ",
        "     /  /  |  \\  \\     ",
        "       /   |   \\       "
    ]
    
    for linea in sol:
        print(linea)

def sol_grande():
    """Sol grande con múltiples rayos"""
    print("🌅 SOL GRANDE 🌅")
    print()
    
    sol = [
        "         \\     |     /         ",
        "       \\   \\   |   /   /       ",
        "     \\     \\   |   /     /     ",
        "   \\   \\     \\ | /     /   /   ",
        "     \\   \\     \\|/     /   /     ",
        "       --- --- ☀️ --- ---       ",
        "     /   /     /|\\     \\   \\     ",
        "   /   /     / | \\     \\   \\   ",
        "     /     /   |   \\     \\     ",
        "       /   /   |   \\   \\       ",
        "         /     |     \\         "
    ]
    
    for linea in sol:
        print(linea)

def sol_emoji():
    """Sol usando emojis y caracteres especiales"""
    print("🌟 SOL CON EMOJIS 🌟")
    print()
    
    sol = [
        "       ⭐   ☀️   ⭐       ",
        "     ⭐ \\    |    / ⭐     ",
        "   ⭐     \\   |   /     ⭐   ",
        "     ✨ --- 🌞 --- ✨     ",
        "   ⭐     /   |   \\     ⭐   ",
        "     ⭐ /    |    \\ ⭐     ",
        "       ⭐   ☀️   ⭐       "
    ]
    
    for linea in sol:
        print(linea)

def sol_amanecer():
    """Secuencia de amanecer"""
    print("🌄 AMANECER 🌄")
    print()
    
    # Sol parcialmente visible
    amanecer1 = [
        "~~~~~~~~~~~~~~~~~~~",
        "~~~~     ☀️     ~~~~",
        "~~~~~~~~~~~~~~~~~~~",
        "^^^^^^^^^^^^^^^^^^^",
        "^^^^^^^^^^^^^^^^^^^"
    ]
    
    print("Fase 1: Sol emergiendo")
    for linea in amanecer1:
        print(linea)
    
    print()
    
    # Sol más visible
    amanecer2 = [
        "    \\  ☀️  /    ",
        "~~~~~~~~~~~~~~~~~~~",
        "~~~~           ~~~~",
        "^^^^^^^^^^^^^^^^^^^",
        "^^^^^^^^^^^^^^^^^^^"
    ]
    
    print("Fase 2: Sol ascendiendo")
    for linea in amanecer2:
        print(linea)

def sol_atardecer():
    """Sol en el atardecer"""
    print("🌅 ATARDECER 🌅")
    print()
    
    atardecer = [
        "       \\   🌅   /       ",
        "         \\  |  /         ",
        "~~~~~~~~~~~\\|/~~~~~~~~~~~",
        "~~~~~~~~~~~~~~~~~~~~~~~~",
        "~~~~~~~~~~~~~~~~~~~~~~~~",
        "🏔️🏔️🏔️🏔️🏔️🏔️🏔️🏔️🏔️🏔️🏔️🏔️",
        "^^^^^^^^^^^^^^^^^^^^^^^^"
    ]
    
    for linea in atardecer:
        print(linea)

def sol_con_nubes():
    """Sol con nubes"""
    print("⛅ SOL CON NUBES ⛅")
    print()
    
    escena = [
        "    \\  ☀️  /    ",
        "     \\ | /     ",
        "   ☁️ \\|/ ☁️   ",
        "  ☁️☁️     ☁️☁️  ",
        "   ☁️       ☁️   ",
        "               "
    ]
    
    for linea in escena:
        print(linea)

def sol_matematico(radio=3):
    """Sol generado matemáticamente"""
    print(f"🔢 SOL MATEMÁTICO (Radio: {radio}) 🔢")
    print()
    
    size = radio * 2 + 5
    centro = size // 2
    
    # Crear matriz
    matriz = [[' ' for _ in range(size)] for _ in range(size)]
    
    # Dibujar rayos horizontales y verticales
    for i in range(size):
        if i == centro:
            for j in range(size):
                if j < centro - radio or j > centro + radio:
                    matriz[i][j] = '-'
        if abs(i - centro) <= radio:
            matriz[i][0] = '|'
            matriz[i][size-1] = '|'
    
    # Dibujar rayos diagonales
    for i in range(size):
        for j in range(size):
            if abs(i - centro) == abs(j - centro) and abs(i - centro) > radio:
                if i < centro and j < centro:
                    matriz[i][j] = '\\'
                elif i < centro and j > centro:
                    matriz[i][j] = '/'
                elif i > centro and j < centro:
                    matriz[i][j] = '/'
                elif i > centro and j > centro:
                    matriz[i][j] = '\\'
    
    # Dibujar círculo del sol
    for i in range(size):
        for j in range(size):
            distancia = ((i - centro) ** 2 + (j - centro) ** 2) ** 0.5
            if distancia <= radio:
                if i == centro and j == centro:
                    matriz[i][j] = '☀'
                elif distancia <= radio - 0.5:
                    matriz[i][j] = '*'
    
    # Imprimir matriz
    for fila in matriz:
        print(''.join(fila))

def menu_soles():
    """Menú interactivo para diferentes tipos de soles"""
    while True:
        print("\n" + "="*50)
        print("🌞 GENERADOR DE SOLES ASCII 🌞")
        print("="*50)
        print("1. Sol básico")
        print("2. Sol detallado")
        print("3. Sol grande")
        print("4. Sol con emojis")
        print("5. Amanecer")
        print("6. Atardecer")
        print("7. Sol con nubes")
        print("8. Sol matemático")
        print("9. Todos los soles")
        print("0. Salir")
        print("-"*50)
        
        try:
            opcion = input("Selecciona una opción (0-9): ").strip()
            
            if opcion == '0':
                print("¡Que tengas un día soleado! ☀️")
                break
            elif opcion == '1':
                sol_basico()
            elif opcion == '2':
                sol_detallado()
            elif opcion == '3':
                sol_grande()
            elif opcion == '4':
                sol_emoji()
            elif opcion == '5':
                sol_amanecer()
            elif opcion == '6':
                sol_atardecer()
            elif opcion == '7':
                sol_con_nubes()
            elif opcion == '8':
                radio = int(input("Introduce el radio del sol (1-5): ") or "3")
                sol_matematico(max(1, min(5, radio)))
            elif opcion == '9':
                sol_basico()
                print("\n" + "-"*30 + "\n")
                sol_detallado()
                print("\n" + "-"*30 + "\n")
                sol_grande()
                print("\n" + "-"*30 + "\n")
                sol_emoji()
                print("\n" + "-"*30 + "\n")
                sol_amanecer()
                print("\n" + "-"*30 + "\n")
                sol_atardecer()
                print("\n" + "-"*30 + "\n")
                sol_con_nubes()
                print("\n" + "-"*30 + "\n")
                sol_matematico()
            else:
                print("❌ Opción no válida. Intenta de nuevo.")
                
        except ValueError:
            print("❌ Por favor, introduce un número válido.")
        except KeyboardInterrupt:
            print("\n¡Hasta luego! ☀️")
            break
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_soles()
