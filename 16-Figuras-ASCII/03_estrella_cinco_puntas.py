"""
Ejercicio 3: Estrella de Cinco Puntas
====================================

Objetivo:
Crear diferentes tipos de estrellas usando caracteres ASCII.

Conceptos a practicar:
- Patrones complejos con bucles
- Cálculos matemáticos para coordenadas
- Arte ASCII avanzado

Instrucciones:
1. Crear estrellas de diferentes tamaños
2. Implementar variaciones de estrellas
3. Usar caracteres especiales para efectos visuales
"""

def dibujar_estrella_simple():
    """Dibuja una estrella simple pequeña"""
    print("\n⭐ Estrella simple:")
    print("=" * 20)
    
    estrella = [
        "    *    ",
        "   ***   ",
        "  *****  ",
        " ******* ",
        "*********",
        " ******* ",
        "  *****  ",
        "   ***   ",
        "    *    "
    ]
    
    for linea in estrella:
        print(linea)

def dibujar_estrella_grande():
    """Dibuja una estrella más grande"""
    print("\n🌟 Estrella grande:")
    print("=" * 30)
    
    estrella = [
        "        *        ",
        "       ***       ",
        "      *****      ",
        "     *******     ",
        "    *********    ",
        "   ***********   ",
        "  *************  ",
        " *************** ",
        "*****************",
        " *************** ",
        "  *************  ",
        "   ***********   ",
        "    *********    ",
        "     *******     ",
        "      *****      ",
        "       ***       ",
        "        *        "
    ]
    
    for linea in estrella:
        print(linea)

def dibujar_estrella_hueca(tamaño):
    """Dibuja una estrella hueca parametrizable"""
    print(f"\n✨ Estrella hueca (tamaño {tamaño}):")
    print("=" * (tamaño * 2 + 10))
    
    centro = tamaño
    
    for i in range(tamaño * 2 + 1):
        linea = ""
        for j in range(tamaño * 2 + 1):
            # Calcular distancia del centro
            dx = abs(j - centro)
            dy = abs(i - centro)
            
            # Patrones para formar estrella
            if (dx == 0 and dy <= tamaño) or \
               (dy == 0 and dx <= tamaño) or \
               (dx == dy and dx <= tamaño) or \
               (dx + dy == tamaño):
                linea += "*"
            else:
                linea += " "
        print(linea)

def dibujar_estrella_navideña():
    """Dibuja una estrella navideña decorativa"""
    print("\n🎄 Estrella navideña:")
    print("=" * 25)
    
    estrella = [
        "       ⭐       ",
        "      /|\\      ",
        "     / | \\     ",
        "    /  |  \\    ",
        "   ⭐⭐⭐⭐⭐   ",
        "    \\  |  /    ",
        "     \\ | /     ",
        "      \\|/      ",
        "       |       ",
        "      ⭐⭐      ",
        "     ⭐⭐⭐     ",
        "    ⭐⭐⭐⭐    ",
        "   ⭐⭐⭐⭐⭐   ",
        "  ⭐⭐⭐⭐⭐⭐  ",
        " ⭐⭐⭐⭐⭐⭐⭐ ",
        "⭐⭐⭐⭐⭐⭐⭐⭐"
    ]
    
    for linea in estrella:
        print(linea)

def dibujar_constelacion():
    """Dibuja una constelación de estrellas"""
    print("\n🌌 Constelación:")
    print("=" * 40)
    
    constelacion = [
        "      *           *        ",
        "        *     *           ",
        "  *         *       *     ",
        "      *   ⭐    *        ",
        "*           *             ",
        "    *     *       ⭐      ",
        "        *           *     ",
        "  ⭐       *              ",
        "      *         *    *    ",
        "            ⭐            ",
        "  *       *       *       ",
        "        *     *     ⭐    ",
        "    *                 *   ",
        "          *       *       ",
        "      ⭐      *          ",
    ]
    
    for linea in constelacion:
        print(linea)

def dibujar_estrella_ascii_art():
    """Dibuja estrella con ASCII art avanzado"""
    print("\n💫 Estrella ASCII Art:")
    print("=" * 35)
    
    estrella = [
        "           /\\           ",
        "          /  \\          ",
        "         /    \\         ",
        "        /      \\        ",
        "       /        \\       ",
        "      /    /\\    \\      ",
        "     /    /  \\    \\     ",
        "    /    /    \\    \\    ",
        "   /____/      \\____\\   ",
        "   \\              /    ",
        "    \\            /     ",
        "     \\          /      ",
        "      \\        /       ",
        "       \\      /        ",
        "        \\    /         ",
        "         \\  /          ",
        "          \\/           "
    ]
    
    for linea in estrella:
        print(linea)

def main():
    """Función principal"""
    print("🌟 GENERADOR DE ESTRELLAS ASCII")
    print("=" * 40)
    
    print("\nSelecciona el tipo de estrella:")
    print("1. Estrella simple")
    print("2. Estrella grande")
    print("3. Estrella hueca (personalizable)")
    print("4. Estrella navideña")
    print("5. Constelación")
    print("6. Estrella ASCII Art")
    print("7. Mostrar todas")
    
    try:
        opcion = input("\nElige una opción (1-7): ")
        
        if opcion == "1":
            dibujar_estrella_simple()
        elif opcion == "2":
            dibujar_estrella_grande()
        elif opcion == "3":
            tamaño = int(input("Ingresa el tamaño (3-8): "))
            if 3 <= tamaño <= 8:
                dibujar_estrella_hueca(tamaño)
            else:
                print("❌ Tamaño debe estar entre 3 y 8")
        elif opcion == "4":
            dibujar_estrella_navideña()
        elif opcion == "5":
            dibujar_constelacion()
        elif opcion == "6":
            dibujar_estrella_ascii_art()
        elif opcion == "7":
            dibujar_estrella_simple()
            dibujar_estrella_grande()
            dibujar_estrella_hueca(5)
            dibujar_estrella_navideña()
            dibujar_constelacion()
            dibujar_estrella_ascii_art()
        else:
            print("❌ Opción no válida")
            
    except ValueError:
        print("❌ Por favor ingresa un número válido")

if __name__ == "__main__":
    main()
