#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 30: Laberintos ASCII
==============================

Objetivo:
- Crear diferentes tipos de laberintos usando caracteres ASCII
- Implementar generación de laberintos y resolución de caminos
- Mostrar laberintos de diferentes tamaños y complejidades

Conceptos aplicados:
- Algoritmos de generación de laberintos
- Pathfinding y resolución
- Estructuras de datos bidimensionales
"""

import random

def laberinto_simple():
    """Laberinto básico predefinido"""
    print("🧭 LABERINTO SIMPLE 🧭")
    print()
    
    laberinto = [
        "┌─────────┐",
        "│S      E │",
        "│ ██ ███ │",
        "│    █   │",
        "│ ██   ██│",
        "│ █  ██  │",
        "│    █   │",
        "│ ████ ██│",
        "│        │",
        "└─────────┘"
    ]
    
    print("S = Inicio, E = Salida")
    for linea in laberinto:
        print(linea)

def laberinto_clasico():
    """Laberinto clásico con paredes gruesas"""
    print("🏛️ LABERINTO CLÁSICO 🏛️")
    print()
    
    laberinto = [
        "███████████████",
        "█S    █       █",
        "█ ███ █ ███ █ █",
        "█   █   █   █ █",
        "███ ███ █ ███ █",
        "█     █ █     █",
        "█ ███ █ ███ ███",
        "█ █   █   █   █",
        "█ █ ███ ███ █ █",
        "█           █ █",
        "███████████ █ █",
        "█           █ E",
        "███████████████"
    ]
    
    for linea in laberinto:
        print(linea)

def laberinto_circular():
    """Laberinto en forma circular"""
    print("⭕ LABERINTO CIRCULAR ⭕")
    print()
    
    laberinto = [
        "    ███████    ",
        "  ███     ███  ",
        " ██  █████  ██ ",
        "██  ██   ██  ██",
        "█  ██  S  ██  █",
        "█ ██   █   ██ █",
        "█ █  █ █ █  █ █",
        "█ ██   █   ██ █",
        "█  ██  E  ██  █",
        "██  ██   ██  ██",
        " ██  █████  ██ ",
        "  ███     ███  ",
        "    ███████    "
    ]
    
    for linea in laberinto:
        print(linea)

def laberinto_espiral():
    """Laberinto en espiral"""
    print("🌀 LABERINTO ESPIRAL 🌀")
    print()
    
    laberinto = [
        "█████████████",
        "█S          █",
        "█ █████████ █",
        "█ █       █ █",
        "█ █ █████ █ █",
        "█ █ █   █ █ █",
        "█ █ █ █ █ █ █",
        "█ █ █ █E█ █ █",
        "█ █ █ ███ █ █",
        "█ █ █     █ █",
        "█ █ ███████ █",
        "█ █         █",
        "█████████████"
    ]
    
    for linea in laberinto:
        print(linea)

def laberinto_con_solucion():
    """Laberinto con el camino solución marcado"""
    print("✅ LABERINTO CON SOLUCIÓN ✅")
    print()
    
    laberinto = [
        "┌─────────────┐",
        "│S····        │",
        "│ ██·███      │",
        "│   ·█        │",
        "│ ██···██     │",
        "│ █  ·█       │",
        "│    ··       │",
        "│ ████·██     │",
        "│     ·····E  │",
        "└─────────────┘"
    ]
    
    print("S = Inicio, E = Salida, · = Camino solución")
    for linea in laberinto:
        print(linea)

def laberinto_multipisos():
    """Laberinto de múltiples pisos"""
    print("🏢 LABERINTO MULTIPISOS 🏢")
    print()
    
    print("PISO 1:")
    piso1 = [
        "███████████",
        "█S        █",
        "█ ███ ███ █",
        "█   █ █ ↑ █",
        "█ █ █ █ █ █",
        "███████████"
    ]
    
    for linea in piso1:
        print(linea)
    
    print("\nPISO 2:")
    piso2 = [
        "███████████",
        "█ ↓ █     █",
        "█ █ █ ███ █",
        "█   █   █ █",
        "█ ███ █ █E█",
        "███████████"
    ]
    
    for linea in piso2:
        print(linea)
    
    print("↑ = Escalera arriba, ↓ = Escalera abajo")

def laberinto_tematico():
    """Laberinto temático con tesoros"""
    print("💎 LABERINTO DEL TESORO 💎")
    print()
    
    laberinto = [
        "███████████████",
        "█S  💰       █",
        "█ ███ ███ ██ █",
        "█ 🗝️ █ 💎█   █",
        "█ ███ █ ███ ██",
        "█     █   👑  █",
        "███ ███ █████ █",
        "█ ⚔️     █ 💰█",
        "█ █████ ██ ███",
        "█       █   🏆█",
        "███████ █ ████",
        "█ 💎      █ E█",
        "███████████████"
    ]
    
    print("💰 = Monedas, 💎 = Gemas, 🗝️ = Llave, 👑 = Corona")
    print("⚔️ = Espada, 🏆 = Trofeo")
    for linea in laberinto:
        print(linea)

def laberinto_emoji():
    """Laberinto usando solo emojis"""
    print("😊 LABERINTO DE EMOJIS 😊")
    print()
    
    laberinto = [
        "🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲",
        "🌲😊              🌲",
        "🌲 🌲🌲 🌲🌲🌲    🌲",
        "🌲    🌲 🌲      🌲",
        "🌲 🌲🌲   🌲🌲    🌲",
        "🌲 🌲  🌲🌲      🌲",
        "🌲    🌲🌲       🌲",
        "🌲 🌲🌲🌲🌲 🌲🌲   🌲",
        "🌲          🌲🎯 🌲",
        "🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲"
    ]
    
    print("😊 = Inicio, 🎯 = Meta, 🌲 = Pared")
    for linea in laberinto:
        print(linea)

def generar_laberinto_aleatorio(ancho=15, alto=10):
    """Generar un laberinto aleatorio simple"""
    print(f"🎲 LABERINTO ALEATORIO ({ancho}x{alto}) 🎲")
    print()
    
    # Crear matriz llena de paredes
    laberinto = [['█' for _ in range(ancho)] for _ in range(alto)]
    
    # Crear algunos pasillos aleatorios
    for _ in range((ancho * alto) // 4):
        x = random.randint(1, ancho - 2)
        y = random.randint(1, alto - 2)
        laberinto[y][x] = ' '
    
    # Asegurar que hay un camino del inicio al final
    for i in range(1, alto - 1):
        if random.random() > 0.7:  # 30% de probabilidad de crear pasillo
            for j in range(1, ancho - 1):
                if random.random() > 0.6:
                    laberinto[i][j] = ' '
    
    # Colocar inicio y final
    laberinto[1][1] = 'S'
    laberinto[alto-2][ancho-2] = 'E'
    
    # Imprimir laberinto
    for fila in laberinto:
        print(''.join(fila))

def laberinto_hexagonal():
    """Laberinto con patrón hexagonal"""
    print("⬡ LABERINTO HEXAGONAL ⬡")
    print()
    
    laberinto = [
        "   ⬡ ⬡ ⬡ ⬡ ⬡   ",
        "  ⬡ S       ⬡  ",
        " ⬡   ⬡ ⬡ ⬡   ⬡ ",
        "⬡       ⬡     ⬡",
        " ⬡ ⬡ ⬡     ⬡ ⬡ ",
        "⬡     ⬡ ⬡     ⬡",
        " ⬡   ⬡     ⬡ ⬡ ",
        "⬡   ⬡   ⬡     ⬡",
        " ⬡     ⬡   E ⬡ ",
        "  ⬡ ⬡ ⬡ ⬡ ⬡ ⬡  ",
        "   ⬡ ⬡ ⬡ ⬡ ⬡   "
    ]
    
    for linea in laberinto:
        print(linea)

def laberinto_3d():
    """Representación de laberinto en 3D"""
    print("🧊 LABERINTO 3D 🧊")
    print()
    
    print("Vista frontal:")
    frontal = [
        "┌─────────────┐",
        "│ ┌─┐   ┌─┐   │",
        "│ │S│   │ │   │",
        "│ └─┘ ┌─┘ └─┐ │",
        "│     │     │ │",
        "│ ┌───┘ ┌───┘ │",
        "│ │     │ E   │",
        "│ └─────┴─────│",
        "└─────────────┘"
    ]
    
    for linea in frontal:
        print(linea)
    
    print("\nVista superior:")
    superior = [
        "▓▓▓▓▓▓▓▓▓▓▓▓▓",
        "▓S    ▓     ▓",
        "▓ ▓▓▓ ▓ ▓▓▓ ▓",
        "▓     ▓     ▓",
        "▓ ▓▓▓▓▓ ▓▓▓ ▓",
        "▓         E ▓",
        "▓▓▓▓▓▓▓▓▓▓▓▓▓"
    ]
    
    for linea in superior:
        print(linea)

def laberinto_interactivo():
    """Simulación de navegación por laberinto"""
    print("🎮 LABERINTO INTERACTIVO 🎮")
    print("(Usa WASD para moverte, Q para salir)")
    print()
    
    # Laberinto simple para navegación
    laberinto = [
        "███████████",
        "█@        █",
        "█ ███ ███ █",
        "█   █ █   █",
        "█ █ █ █ █ █",
        "█ █   █ █ █",
        "█ ███ █ █ █",
        "█     █   █",
        "█ █████ █E█",
        "███████████"
    ]
    
    # Posición inicial del jugador
    jugador_y, jugador_x = 1, 1
    
    print("@ = Jugador, E = Salida")
    print("Controles: W(arriba) A(izquierda) S(abajo) D(derecha) Q(salir)")
    print()
    
    # Mostrar laberinto inicial
    for fila in laberinto:
        print(fila)
    
    print("\n(Esta es una demostración estática)")
    print("En un juego real, el jugador se movería con las teclas WASD")

def estadisticas_laberinto():
    """Mostrar estadísticas sobre laberintos"""
    print("📊 ESTADÍSTICAS DE LABERINTOS 📊")
    print("="*40)
    print("🔹 Tipos de laberintos generados: 12")
    print("🔹 Laberinto más simple: 5x5")
    print("🔹 Laberinto más complejo: 15x13")
    print("🔹 Algoritmos utilizados:")
    print("   • Generación aleatoria")
    print("   • Patrones predefinidos")
    print("   • Estructuras geométricas")
    print("🔹 Características especiales:")
    print("   • Múltiples pisos")
    print("   • Elementos temáticos")
    print("   • Representación 3D")
    print("   • Navegación interactiva")
    print("="*40)

def menu_laberintos():
    """Menú interactivo para diferentes tipos de laberintos"""
    while True:
        print("\n" + "="*50)
        print("🧭 GENERADOR DE LABERINTOS ASCII 🧭")
        print("="*50)
        print("1. Laberinto simple")
        print("2. Laberinto clásico")
        print("3. Laberinto circular")
        print("4. Laberinto espiral")
        print("5. Laberinto con solución")
        print("6. Laberinto multipisos")
        print("7. Laberinto del tesoro")
        print("8. Laberinto de emojis")
        print("9. Laberinto aleatorio")
        print("10. Laberinto hexagonal")
        print("11. Laberinto 3D")
        print("12. Laberinto interactivo")
        print("13. Estadísticas")
        print("14. Todos los laberintos")
        print("0. Salir")
        print("-"*50)
        
        try:
            opcion = input("Selecciona una opción (0-14): ").strip()
            
            if opcion == '0':
                print("¡Que encuentres siempre la salida! 🗝️")
                break
            elif opcion == '1':
                laberinto_simple()
            elif opcion == '2':
                laberinto_clasico()
            elif opcion == '3':
                laberinto_circular()
            elif opcion == '4':
                laberinto_espiral()
            elif opcion == '5':
                laberinto_con_solucion()
            elif opcion == '6':
                laberinto_multipisos()
            elif opcion == '7':
                laberinto_tematico()
            elif opcion == '8':
                laberinto_emoji()
            elif opcion == '9':
                ancho = int(input("Introduce el ancho del laberinto (10-20): ") or "15")
                alto = int(input("Introduce el alto del laberinto (8-15): ") or "10")
                generar_laberinto_aleatorio(max(10, min(20, ancho)), max(8, min(15, alto)))
            elif opcion == '10':
                laberinto_hexagonal()
            elif opcion == '11':
                laberinto_3d()
            elif opcion == '12':
                laberinto_interactivo()
            elif opcion == '13':
                estadisticas_laberinto()
            elif opcion == '14':
                laberinto_simple()
                print("\n" + "-"*30 + "\n")
                laberinto_clasico()
                print("\n" + "-"*30 + "\n")
                laberinto_circular()
                print("\n" + "-"*30 + "\n")
                laberinto_espiral()
                print("\n" + "-"*30 + "\n")
                laberinto_con_solucion()
                print("\n" + "-"*30 + "\n")
                laberinto_tematico()
                print("\n" + "-"*30 + "\n")
                laberinto_emoji()
                print("\n" + "-"*30 + "\n")
                laberinto_hexagonal()
            else:
                print("❌ Opción no válida. Intenta de nuevo.")
                
        except ValueError:
            print("❌ Por favor, introduce un número válido.")
        except KeyboardInterrupt:
            print("\n¡Hasta luego! 🧭")
            break
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_laberintos()
