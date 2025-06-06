"""
Ejercicio 22: Robot ASCII
=========================

Objetivo:
Crear diferentes tipos de robots y androides.

Conceptos a practicar:
- Formas mecánicas
- Estructura robótica
- Detalles tecnológicos

Instrucciones:
1. Crear la cabeza del robot
2. Añadir cuerpo y extremidades
3. Incluir detalles como antenas y sensores
"""

def dibujar_robot_simple():
    """Dibuja un robot simple"""
    print("\n🤖 Robot simple:")
    print("=" * 20)
    
    robot = [
        "   _____   ",
        "  |     |  ",
        "  | ● ● |  ",
        "  |  ^  |  ",
        "  |_____|  ",
        "    | |    ",
        "  __|_|__  ",
        " |       | ",
        " |   🔧   | ",
        " |_______| ",
        "    | |    ",
        "   _| |_   ",
        "  |_   _|  "
    ]
    
    for linea in robot:
        print(linea)

def dibujar_robot_avanzado():
    """Dibuja un robot más avanzado"""
    print("\n🤖 Robot avanzado:")
    print("=" * 25)
    
    robot = [
        "     📡     ",
        "   -------   ",
        "  |  ● ●  |  ",
        "  |   -   |  ",
        "  |  ___  |  ",
        "  |_______|  ",
        "      |      ",
        "   [█████]   ",
        "   |  💾  |   ",
        "   |  ⚡  |   ",
        "   |_____|   ",
        "    |   |    ",
        "   ⚪   ⚪   "
    ]
    
    for linea in robot:
        print(linea)

def dibujar_androide():
    """Dibuja un androide"""
    print("\n🤖 Androide:")
    print("=" * 20)
    
    androide = [
        "   ○   ○   ",
        "    \\_/    ",
        "   _____   ",
        "  |  ◉ ◉  | ",
        "  |   ⌒   | ",
        "  |_______|",
        "      |    ",
        "   ▓▓▓▓▓   ",
        "   ▓ ⚡ ▓   ",
        "   ▓▓▓▓▓   ",
        "   /   \\   ",
        "  /     \\  ",
        " ●       ● "
    ]
    
    for linea in androide:
        print(linea)

def main():
    """Función principal"""
    print("🤖 GENERADOR DE ROBOTS")
    print("=" * 25)
    
    dibujar_robot_simple()
    dibujar_robot_avanzado()
    dibujar_androide()

if __name__ == "__main__":
    main()
