"""
Ejercicio 14: Flores ASCII
==========================

Objetivo:
Crear diferentes tipos de flores usando caracteres ASCII y emojis.

Conceptos a practicar:
- Formas orgánicas
- Patrones radiales
- Elementos decorativos naturales

Instrucciones:
1. Crear pétalos simétricos
2. Añadir tallo y hojas
3. Crear jardines con múltiples flores
"""

def dibujar_flor_simple():
    """Dibuja una flor simple"""
    print("\n🌸 Flor simple:")
    print("=" * 20)
    
    flor = [
        "   \\|/   ",
        "  -- --  ",
        "   /|\\   ",
        "    |    ",
        "    |    ",
        "    |    "
    ]
    
    for linea in flor:
        print(linea)

def dibujar_rosa():
    """Dibuja una rosa"""
    print("\n🌹 Rosa:")
    print("=" * 15)
    
    rosa = [
        "  @@@@@  ",
        " @@@@@@@ ",
        "@@@@@@@@@",
        " @@@@@@@ ",
        "  @@@@@  ",
        "    |    ",
        "    |    ",
        "   /|\\   ",
        "    |    "
    ]
    
    for linea in rosa:
        print(linea)

def dibujar_girasol():
    """Dibuja un girasol"""
    print("\n🌻 Girasol:")
    print("=" * 20)
    
    girasol = [
        "   \\ | /   ",
        "  \\ \\|/ /  ",
        " -- ● ● -- ",
        "  / /|\\ \\  ",
        "   / | \\   ",
        "     |     ",
        "     |     ",
        "     |     "
    ]
    
    for linea in girasol:
        print(linea)

def dibujar_jardin():
    """Dibuja un jardín con múltiples flores"""
    print("\n🌺 Jardín:")
    print("=" * 35)
    
    jardin = [
        "  🌸   🌻   🌺   🌼  ",
        "   |     |     |     | ",
        "   |     |     |     | ",
        "🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿"
    ]
    
    for linea in jardin:
        print(linea)

def main():
    """Función principal"""
    print("🌸 GENERADOR DE FLORES")
    print("=" * 25)
    
    dibujar_flor_simple()
    dibujar_rosa()
    dibujar_girasol()
    dibujar_jardin()

if __name__ == "__main__":
    main()
