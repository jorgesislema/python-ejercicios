#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 25: Nubes ASCII
=========================

Objetivo:
- Crear diferentes tipos de nubes con caracteres ASCII
- Implementar efectos climáticos (lluvia, nieve, rayos)
- Generar paisajes atmosféricos

Conceptos aplicados:
- Formas orgánicas con ASCII
- Patrones meteorológicos
- Efectos visuales dinámicos
"""

import random
import time

def nube_simple():
    """Nube básica y simple"""
    print("☁️ NUBE SIMPLE ☁️")
    print()
    
    nube = [
        "    ☁️☁️☁️    ",
        "  ☁️☁️☁️☁️☁️  ",
        " ☁️☁️☁️☁️☁️☁️ ",
        "☁️☁️☁️☁️☁️☁️☁️"
    ]
    
    for linea in nube:
        print(linea)

def nube_detallada():
    """Nube más detallada con contornos"""
    print("🌤️ NUBE DETALLADA 🌤️")
    print()
    
    nube = [
        "      .-.     ",
        "     (   )    ",
        "   (___(__)   ",
        "              "
    ]
    
    for linea in nube:
        print(linea)

def nube_grande():
    """Nube grande y esponjosa"""
    print("☁️ NUBE GRANDE ☁️")
    print()
    
    nube = [
        "        ☁️☁️☁️☁️☁️        ",
        "      ☁️☁️☁️☁️☁️☁️☁️      ",
        "    ☁️☁️☁️☁️☁️☁️☁️☁️☁️    ",
        "  ☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️  ",
        " ☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️ ",
        "☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️"
    ]
    
    for linea in nube:
        print(linea)

def nube_con_lluvia():
    """Nube con lluvia"""
    print("🌧️ NUBE CON LLUVIA 🌧️")
    print()
    
    escena = [
        "    ☁️☁️☁️☁️    ",
        "  ☁️☁️☁️☁️☁️☁️  ",
        " ☁️☁️☁️☁️☁️☁️☁️ ",
        "☁️☁️☁️☁️☁️☁️☁️☁️",
        "  |  |  |  |  ",
        " |  |  |  |  |",
        "  |  |  |  |  ",
        " |  |  |  |  |",
        "  💧 💧 💧 💧  "
    ]
    
    for linea in escena:
        print(linea)

def nube_con_nieve():
    """Nube con nieve"""
    print("🌨️ NUBE CON NIEVE 🌨️")
    print()
    
    escena = [
        "    ☁️☁️☁️☁️    ",
        "  ☁️☁️☁️☁️☁️☁️  ",
        " ☁️☁️☁️☁️☁️☁️☁️ ",
        "☁️☁️☁️☁️☁️☁️☁️☁️",
        "  *  ❄️  *  ❄️  ",
        " ❄️  *  ❄️  *  ",
        "  *  ❄️  *  ❄️  ",
        " ❄️  *  ❄️  *  ",
        "  ❄️ ❄️ ❄️ ❄️  "
    ]
    
    for linea in escena:
        print(linea)

def nube_tormenta():
    """Nube de tormenta con rayos"""
    print("⛈️ NUBE DE TORMENTA ⛈️")
    print()
    
    escena = [
        "  ⚡ ☁️☁️☁️☁️☁️ ⚡ ",
        " ☁️☁️☁️☁️☁️☁️☁️☁️ ",
        "☁️☁️☁️☁️☁️☁️☁️☁️☁️",
        "☁️☁️☁️☁️☁️☁️☁️☁️☁️",
        "  ⚡   |   ⚡   ",
        "   \\   |   /   ",
        "    \\  |  /    ",
        "     \\ | /     ",
        "      \\|/      ",
        "   💧 ⚡ 💧    "
    ]
    
    for linea in escena:
        print(linea)

def cielo_nublado():
    """Cielo con múltiples nubes"""
    print("🌥️ CIELO NUBLADO 🌥️")
    print()
    
    cielo = [
        "☁️☁️☁️    ☁️☁️      ☁️☁️☁️",
        "☁️☁️☁️☁️  ☁️☁️☁️    ☁️☁️☁️☁️",
        "  ☁️☁️    ☁️☁️☁️☁️  ☁️☁️  ",
        "           ☁️☁️☁️          ",
        "                          ",
        "    ☁️☁️☁️        ☁️☁️    ",
        "  ☁️☁️☁️☁️☁️    ☁️☁️☁️☁️  ",
        " ☁️☁️☁️☁️☁️☁️  ☁️☁️☁️☁️☁️ "
    ]
    
    for linea in cielo:
        print(linea)

def nube_arcoiris():
    """Nube con arcoíris"""
    print("🌈 NUBE CON ARCOÍRIS 🌈")
    print()
    
    escena = [
        "    ☁️☁️☁️☁️☁️    ",
        "  ☁️☁️☁️☁️☁️☁️☁️  ",
        " ☁️☁️☁️☁️☁️☁️☁️☁️ ",
        "☁️☁️☁️☁️☁️☁️☁️☁️☁️",
        "  🟥🟧🟨🟩🟦🟪  ",
        " 🟥🟧🟨🟩🟦🟪🟣 ",
        "🟥🟧🟨🟩🟦🟪🟣  ",
        "               ",
        "   🌈 ¡Arcoíris! 🌈   "
    ]
    
    for linea in escena:
        print(linea)

def nube_animada():
    """Simulación de nube animada"""
    print("🎬 NUBE ANIMADA 🎬")
    print("(Presiona Ctrl+C para detener)")
    print()
    
    frames = [
        [
            "    ☁️☁️☁️    ",
            "  ☁️☁️☁️☁️☁️  ",
            " ☁️☁️☁️☁️☁️☁️ ",
            "☁️☁️☁️☁️☁️☁️☁️"
        ],
        [
            "     ☁️☁️☁️     ",
            "   ☁️☁️☁️☁️☁️   ",
            "  ☁️☁️☁️☁️☁️☁️  ",
            " ☁️☁️☁️☁️☁️☁️☁️ "
        ],
        [
            "      ☁️☁️☁️      ",
            "    ☁️☁️☁️☁️☁️    ",
            "   ☁️☁️☁️☁️☁️☁️   ",
            "  ☁️☁️☁️☁️☁️☁️☁️  "
        ]
    ]
    
    try:
        for _ in range(10):  # 10 ciclos de animación
            for frame in frames:
                print("\033[H\033[J", end="")  # Limpiar pantalla
                print("🎬 NUBE ANIMADA 🎬")
                print("(Presiona Ctrl+C para detener)")
                print()
                for linea in frame:
                    print(linea)
                time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n¡Animación detenida!")

def nube_matematica(ancho=15, alto=4):
    """Nube generada matemáticamente"""
    print(f"🔢 NUBE MATEMÁTICA ({ancho}x{alto}) 🔢")
    print()
    
    # Generar forma de nube usando algoritmo simple
    for i in range(alto):
        linea = ""
        for j in range(ancho):
            # Crear forma redondeada de nube
            centro_x = ancho // 2
            centro_y = alto // 2
            
            # Distancia desde el centro
            distancia = ((j - centro_x) ** 2 + (i - centro_y) ** 2) ** 0.5
            max_radio = min(ancho, alto) // 2
            
            # Añadir variación aleatoria para forma orgánica
            variacion = random.uniform(0.7, 1.3)
            
            if distancia <= max_radio * variacion:
                linea += "☁️"
            else:
                linea += "  "
        
        print(linea)

def lluvia_aleatoria():
    """Generar lluvia con patrones aleatorios"""
    print("🌧️ LLUVIA ALEATORIA 🌧️")
    print()
    
    # Nube fija
    nube = [
        "    ☁️☁️☁️☁️☁️    ",
        "  ☁️☁️☁️☁️☁️☁️☁️  ",
        " ☁️☁️☁️☁️☁️☁️☁️☁️ ",
        "☁️☁️☁️☁️☁️☁️☁️☁️☁️"
    ]
    
    for linea in nube:
        print(linea)
    
    # Lluvia aleatoria
    for i in range(8):
        linea = ""
        for j in range(20):
            if random.random() < 0.3:  # 30% probabilidad de gota
                linea += "|"
            else:
                linea += " "
        print(linea)

def menu_nubes():
    """Menú interactivo para diferentes tipos de nubes"""
    while True:
        print("\n" + "="*50)
        print("☁️ GENERADOR DE NUBES ASCII ☁️")
        print("="*50)
        print("1. Nube simple")
        print("2. Nube detallada")
        print("3. Nube grande")
        print("4. Nube con lluvia")
        print("5. Nube con nieve")
        print("6. Nube de tormenta")
        print("7. Cielo nublado")
        print("8. Nube con arcoíris")
        print("9. Nube animada")
        print("10. Nube matemática")
        print("11. Lluvia aleatoria")
        print("12. Todas las nubes")
        print("0. Salir")
        print("-"*50)
        
        try:
            opcion = input("Selecciona una opción (0-12): ").strip()
            
            if opcion == '0':
                print("¡Que tengas un día despejado! ☀️")
                break
            elif opcion == '1':
                nube_simple()
            elif opcion == '2':
                nube_detallada()
            elif opcion == '3':
                nube_grande()
            elif opcion == '4':
                nube_con_lluvia()
            elif opcion == '5':
                nube_con_nieve()
            elif opcion == '6':
                nube_tormenta()
            elif opcion == '7':
                cielo_nublado()
            elif opcion == '8':
                nube_arcoiris()
            elif opcion == '9':
                nube_animada()
            elif opcion == '10':
                ancho = int(input("Introduce el ancho de la nube (10-30): ") or "15")
                alto = int(input("Introduce el alto de la nube (3-8): ") or "4")
                nube_matematica(max(10, min(30, ancho)), max(3, min(8, alto)))
            elif opcion == '11':
                lluvia_aleatoria()
            elif opcion == '12':
                nube_simple()
                print("\n" + "-"*30 + "\n")
                nube_detallada()
                print("\n" + "-"*30 + "\n")
                nube_grande()
                print("\n" + "-"*30 + "\n")
                nube_con_lluvia()
                print("\n" + "-"*30 + "\n")
                nube_con_nieve()
                print("\n" + "-"*30 + "\n")
                nube_tormenta()
                print("\n" + "-"*30 + "\n")
                cielo_nublado()
                print("\n" + "-"*30 + "\n")
                nube_arcoiris()
            else:
                print("❌ Opción no válida. Intenta de nuevo.")
                
        except ValueError:
            print("❌ Por favor, introduce un número válido.")
        except KeyboardInterrupt:
            print("\n¡Hasta luego! ☁️")
            break
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_nubes()
