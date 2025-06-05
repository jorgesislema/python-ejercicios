"""
Ejercicio 19: Laberinto ASCII
============================

Objetivo:
Crear laberintos usando caracteres ASCII con entrada, salida y caminos.

Conceptos a practicar:
- Algoritmos de generación de laberintos
- Representación de espacios y obstáculos
- Pathfinding visual

Instrucciones:
1. Crear paredes y caminos
2. Añadir entrada y salida
3. Generar laberintos aleatorios
"""

import random

def dibujar_laberinto_simple():
    """Dibuja un laberinto simple predefinido"""
    print("\n🧩 Laberinto simple:")
    print("=" * 25)
    
    laberinto = [
        "███████████████",
        "█S    █       █",
        "█ ███ █ █████ █",
        "█   █   █     █",
        "███ █████ ███ █",
        "█           █ █",
        "█ ███████ ███ █",
        "█   █     █   █",
        "███ █ █████ ███",
        "█     █      E█",
        "███████████████"
    ]
    
    for linea in laberinto:
        print(linea)

def dibujar_laberinto_con_solucion():
    """Dibuja un laberinto con la solución marcada"""
    print("\n🎯 Laberinto con solución:")
    print("=" * 30)
    
    laberinto = [
        "███████████████",
        "█S····█       █",
        "█·███·█ █████ █",
        "█···█···█     █",
        "███·█████ ███ █",
        "█  ·········█ █",
        "█ ███████·███ █",
        "█   █    ·█   █",
        "███ █ ███·█·███",
        "█     █  ··· E█",
        "███████████████"
    ]
    
    print("Leyenda:")
    print("S = Entrada (Start)")
    print("E = Salida (Exit)")
    print("· = Camino de solución")
    print("█ = Pared")
    print("  = Camino libre")
    print()
    
    for linea in laberinto:
        print(linea)

def generar_laberinto_aleatorio(ancho, alto):
    """Genera un laberinto aleatorio simple"""
    print(f"\n🎲 Laberinto aleatorio ({ancho}x{alto}):")
    print("=" * (ancho + 10))
    
    # Crear laberinto lleno de paredes
    laberinto = [['█' for _ in range(ancho)] for _ in range(alto)]
    
    # Crear algunos caminos aleatorios
    for _ in range((ancho * alto) // 4):
        x = random.randint(1, ancho - 2)
        y = random.randint(1, alto - 2)
        laberinto[y][x] = ' '
    
    # Asegurar que hay un camino desde la entrada
    laberinto[1][1] = 'S'  # Entrada
    laberinto[alto-2][ancho-2] = 'E'  # Salida
    
    # Crear camino básico
    x, y = 1, 1
    while x < ancho - 2 or y < alto - 2:
        laberinto[y][x] = ' '
        if x < ancho - 2 and random.choice([True, False]):
            x += 1
        elif y < alto - 2:
            y += 1
    
    laberinto[1][1] = 'S'
    laberinto[alto-2][ancho-2] = 'E'
    
    # Dibujar el laberinto
    for fila in laberinto:
        print(''.join(fila))

def dibujar_laberinto_hexagonal():
    """Dibuja un laberinto con patrón hexagonal"""
    print("\n⬡ Laberinto hexagonal:")
    print("=" * 25)
    
    laberinto = [
        "   ⬡ ⬡ ⬡ ⬡ ⬡   ",
        "  ⬡ S   ⬡   ⬡  ",
        " ⬡   ⬡ ⬡   ⬡ ⬡ ",
        "⬡   ⬡     ⬡   ⬡",
        " ⬡   ⬡ ⬡ ⬡   ⬡ ",
        "  ⬡     ⬡ E ⬡  ",
        "   ⬡ ⬡ ⬡ ⬡ ⬡   "
    ]
    
    for linea in laberinto:
        print(linea)

def main():
    """Función principal"""
    print("🧩 GENERADOR DE LABERINTOS")
    print("=" * 35)
    
    print("\nSelecciona el tipo de laberinto:")
    print("1. Laberinto simple")
    print("2. Laberinto con solución")
    print("3. Laberinto aleatorio")
    print("4. Laberinto hexagonal")
    print("5. Mostrar todos")
    
    try:
        opcion = input("\nElige una opción (1-5): ")
        
        if opcion == "1":
            dibujar_laberinto_simple()
        elif opcion == "2":
            dibujar_laberinto_con_solucion()
        elif opcion == "3":
            ancho = int(input("Ancho del laberinto (10-20): "))
            alto = int(input("Alto del laberinto (8-15): "))
            if 10 <= ancho <= 20 and 8 <= alto <= 15:
                generar_laberinto_aleatorio(ancho, alto)
            else:
                print("❌ Dimensiones fuera de rango")
        elif opcion == "4":
            dibujar_laberinto_hexagonal()
        elif opcion == "5":
            dibujar_laberinto_simple()
            dibujar_laberinto_con_solucion()
            generar_laberinto_aleatorio(15, 10)
            dibujar_laberinto_hexagonal()
        else:
            print("❌ Opción no válida")
            
    except ValueError:
        print("❌ Por favor ingresa números válidos")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
