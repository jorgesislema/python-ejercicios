#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 26: Mariposas ASCII
=============================

Objetivo:
- Crear diferentes tipos de mariposas con caracteres ASCII
- Implementar mariposas en vuelo y en reposo
- Mostrar el ciclo de vida (oruga -> crisálida -> mariposa)

Conceptos aplicados:
- Simetría en figuras ASCII
- Formas orgánicas complejas
- Animaciones y transformaciones
"""

import time
import random

def mariposa_simple():
    """Mariposa básica y simple"""
    print("🦋 MARIPOSA SIMPLE 🦋")
    print()
    
    mariposa = [
        "   \\   /   ",
        "    \\_/    ",
        "     |     ",
        "    / \\    ",
        "   /   \\   "
    ]
    
    for linea in mariposa:
        print(linea)

def mariposa_detallada():
    """Mariposa más detallada con patrones"""
    print("🦋 MARIPOSA DETALLADA 🦋")
    print()
    
    mariposa = [
        "  /\\_/\\  /\\_/\\  ",
        " ( o.o )( o.o ) ",
        "  > ^ <  > ^ <  ",
        "     \\_|_/     ",
        "       |       ",
        "      /|\\      ",
        "     / | \\     "
    ]
    
    for linea in mariposa:
        print(linea)

def mariposa_grande():
    """Mariposa grande con alas extendidas"""
    print("🦋 MARIPOSA GRANDE 🦋")
    print()
    
    mariposa = [
        " /\\_    _    _/\\ ",
        "/  \\\\__/|\\__//  \\",
        "\\   \\\\_/ \\_//   /",
        " \\   \\\\ O //   / ",
        "  \\   \\\\|//   /  ",
        "   \\   \\|/   /   ",
        "    \\   |   /    ",
        "     \\  |  /     ",
        "      \\ | /      ",
        "       \\|/       ",
        "        |        ",
        "       /|\\       ",
        "      / | \\      "
    ]
    
    for linea in mariposa:
        print(linea)

def mariposa_emoji():
    """Mariposa usando emojis y caracteres especiales"""
    print("🌸 MARIPOSA CON EMOJIS 🌸")
    print()
    
    mariposa = [
        "  🌸  🌸  🌸  🌸  ",
        " 🌺    🦋    🌺 ",
        "  🌸  \\   /  🌸  ",
        "       \\_/       ",
        "        |        ",
        "       /|\\       ",
        "      / | \\      ",
        "    🌼 🌼 🌼    "
    ]
    
    for linea in mariposa:
        print(linea)

def mariposa_monarca():
    """Mariposa monarca con patrones característicos"""
    print("👑 MARIPOSA MONARCA 👑")
    print()
    
    mariposa = [
        "   .-.     .-.   ",
        "  (🟠🟠)   (🟠🟠)  ",
        "   |⚫|     |⚫|   ",
        "   |🟠|     |🟠|   ",
        "    \\🟠\\   /🟠/    ",
        "     \\🟠\\_/🟠/     ",
        "      \\   /      ",
        "       \\_/       ",
        "        |        ",
        "       /|\\       ",
        "      / | \\      "
    ]
    
    for linea in mariposa:
        print(linea)

def mariposa_nocturna():
    """Polilla o mariposa nocturna"""
    print("🌙 MARIPOSA NOCTURNA 🌙")
    print()
    
    mariposa = [
        "✨ /^^^\\   /^^^\\  ✨",
        " ⭐/🌑 🌑\\ /🌑 🌑\\⭐ ",
        "  |  👁  | |  👁  |  ",
        "  |     | |     |  ",
        "   \\   / \\ /   /   ",
        "    \\ /   V   / /    ",
        "     X     X     ",
        "      \\   /      ",
        "       \\_/       ",
        "        |        ",
        "       /|\\       "
    ]
    
    for linea in mariposa:
        print(linea)

def oruga():
    """Oruga antes de convertirse en mariposa"""
    print("🐛 ORUGA 🐛")
    print()
    
    oruga_figura = [
        "  .--.  .--.  .--.  ",
        " (    )(    )(    ) ",
        "  '--'  '--'  '--'  ",
        "   🟢    🟢    🟢   "
    ]
    
    for linea in oruga_figura:
        print(linea)

def crisalida():
    """Crisálida en proceso de transformación"""
    print("🛡️ CRISÁLIDA 🛡️")
    print()
    
    crisalida_figura = [
        "    /^\\    ",
        "   |   |   ",
        "   | 🦋|   ",
        "   |   |   ",
        "   |   |   ",
        "    \\./    ",
        "     |     ",
        "   __|__   "
    ]
    
    for linea in crisalida_figura:
        print(linea)

def ciclo_vida():
    """Mostrar el ciclo completo de vida"""
    print("🔄 CICLO DE VIDA DE LA MARIPOSA 🔄")
    print("="*40)
    
    print("\n1. HUEVO 🥚")
    print("    ∘")
    
    print("\n2. ORUGA 🐛")
    oruga()
    
    print("\n3. CRISÁLIDA 🛡️")
    crisalida()
    
    print("\n4. MARIPOSA 🦋")
    mariposa_simple()

def mariposas_volando():
    """Múltiples mariposas en vuelo"""
    print("🌈 MARIPOSAS VOLANDO 🌈")
    print()
    
    cielo = [
        " 🦋      🌸       🦋    ",
        "    ✨        🦋       ",
        "        🦋    ✨      🦋",
        " ✨           🌸       ",
        "    🦋    ✨       🦋  ",
        "           🦋      ✨  ",
        " 🌸    ✨      🦋     ",
        "    🦋           🌸    "
    ]
    
    for linea in cielo:
        print(linea)

def jardin_mariposas():
    """Jardín lleno de mariposas y flores"""
    print("🌻 JARDÍN DE MARIPOSAS 🌻")
    print()
    
    jardin = [
        " 🦋  🌸  🦋  🌺  🦋  🌼 ",
        "   🌻    🦋    🌷    🦋  ",
        " 🦋    🌹    🦋    🌻   ",
        "   🌺  🦋  🌸  🦋  🌹   ",
        " 🌼    🦋    🌺    🦋    ",
        "   🦋  🌻  🦋  🌷  🦋   ",
        " 🌸    🦋    🌼    🦋    ",
        "~~~~~~~~~~~~~~~~~~~~~~~~",
        "🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱"
    ]
    
    for linea in jardin:
        print(linea)

def mariposa_animada():
    """Simulación de mariposa volando"""
    print("🎬 MARIPOSA ANIMADA 🎬")
    print("(Presiona Ctrl+C para detener)")
    print()
    
    frames = [
        [
            "   \\   /   ",
            "    \\_/    ",
            "     |     ",
            "    / \\    ",
            "   /   \\   "
        ],
        [
            "   /   \\   ",
            "    \\_/    ",
            "     |     ",
            "    \\ /    ",
            "     V     "
        ],
        [
            "   \\   /   ",
            "    \\_/    ",
            "     |     ",
            "    / \\    ",
            "   /   \\   "
        ],
        [
            "   ^   ^   ",
            "    \\_/    ",
            "     |     ",
            "    / \\    ",
            "   /   \\   "
        ]
    ]
    
    posiciones = [
        (5, 2), (10, 3), (15, 2), (10, 1), (5, 2)
    ]
    
    try:
        for _ in range(5):  # 5 ciclos de vuelo
            for i, frame in enumerate(frames):
                print("\033[H\033[J", end="")  # Limpiar pantalla
                print("🎬 MARIPOSA ANIMADA 🎬")
                print("(Presiona Ctrl+C para detener)")
                print()
                
                # Añadir espacios para simular movimiento
                x_offset = posiciones[i % len(posiciones)][0]
                y_offset = posiciones[i % len(posiciones)][1]
                
                for _ in range(y_offset):
                    print()
                
                for linea in frame:
                    print(" " * x_offset + linea)
                
                time.sleep(0.3)
    except KeyboardInterrupt:
        print("\n¡Vuelo interrumpido!")

def mariposa_matematica():
    """Mariposa generada con funciones matemáticas"""
    print("🔢 MARIPOSA MATEMÁTICA 🔢")
    print()
    
    size = 15
    centro = size // 2
    
    # Crear matriz
    matriz = [[' ' for _ in range(size)] for _ in range(size)]
    
    # Dibujar cuerpo central
    for i in range(size):
        if abs(i - centro) <= 3:
            matriz[i][centro] = '|'
    
    # Dibujar alas usando función matemática
    for i in range(size):
        for j in range(size):
            # Distancia desde el centro
            dx = j - centro
            dy = i - centro
            
            # Ecuación para forma de ala
            if abs(dy) <= 4 and abs(dx) > 1:
                # Ala superior
                if dy < 0 and abs(dx) <= 6 - abs(dy):
                    if dx > 0:
                        matriz[i][j] = '/'
                    else:
                        matriz[i][j] = '\\'
                # Ala inferior
                elif dy > 0 and abs(dx) <= 4 - abs(dy) + 2:
                    if dx > 0:
                        matriz[i][j] = '\\'
                    else:
                        matriz[i][j] = '/'
    
    # Antenas
    matriz[centro-4][centro-1] = '/'
    matriz[centro-4][centro+1] = '\\'
    
    # Imprimir matriz
    for fila in matriz:
        print(''.join(fila))

def menu_mariposas():
    """Menú interactivo para diferentes tipos de mariposas"""
    while True:
        print("\n" + "="*50)
        print("🦋 GENERADOR DE MARIPOSAS ASCII 🦋")
        print("="*50)
        print("1. Mariposa simple")
        print("2. Mariposa detallada")
        print("3. Mariposa grande")
        print("4. Mariposa con emojis")
        print("5. Mariposa monarca")
        print("6. Mariposa nocturna")
        print("7. Oruga")
        print("8. Crisálida")
        print("9. Ciclo de vida completo")
        print("10. Mariposas volando")
        print("11. Jardín de mariposas")
        print("12. Mariposa animada")
        print("13. Mariposa matemática")
        print("14. Todas las mariposas")
        print("0. Salir")
        print("-"*50)
        
        try:
            opcion = input("Selecciona una opción (0-14): ").strip()
            
            if opcion == '0':
                print("¡Que vueles alto como una mariposa! 🦋")
                break
            elif opcion == '1':
                mariposa_simple()
            elif opcion == '2':
                mariposa_detallada()
            elif opcion == '3':
                mariposa_grande()
            elif opcion == '4':
                mariposa_emoji()
            elif opcion == '5':
                mariposa_monarca()
            elif opcion == '6':
                mariposa_nocturna()
            elif opcion == '7':
                oruga()
            elif opcion == '8':
                crisalida()
            elif opcion == '9':
                ciclo_vida()
            elif opcion == '10':
                mariposas_volando()
            elif opcion == '11':
                jardin_mariposas()
            elif opcion == '12':
                mariposa_animada()
            elif opcion == '13':
                mariposa_matematica()
            elif opcion == '14':
                mariposa_simple()
                print("\n" + "-"*30 + "\n")
                mariposa_detallada()
                print("\n" + "-"*30 + "\n")
                mariposa_grande()
                print("\n" + "-"*30 + "\n")
                mariposa_emoji()
                print("\n" + "-"*30 + "\n")
                mariposa_monarca()
                print("\n" + "-"*30 + "\n")
                mariposa_nocturna()
                print("\n" + "-"*30 + "\n")
                jardin_mariposas()
            else:
                print("❌ Opción no válida. Intenta de nuevo.")
                
        except ValueError:
            print("❌ Por favor, introduce un número válido.")
        except KeyboardInterrupt:
            print("\n¡Hasta luego! 🦋")
            break
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_mariposas()
