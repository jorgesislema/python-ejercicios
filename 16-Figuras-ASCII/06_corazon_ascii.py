"""
Ejercicio 6: Corazón ASCII
=========================

Objetivo:
Crear diferentes tipos de corazones usando caracteres ASCII y emojis.

Conceptos a practicar:
- Formas curvas con caracteres
- Patrones simétricos
- Arte ASCII romántico

Instrucciones:
1. Crear corazones de diferentes tamaños
2. Añadir efectos decorativos
3. Crear animaciones simples
"""

def dibujar_corazon_simple():
    """Dibuja un corazón simple"""
    print("\n💖 Corazón simple:")
    print("=" * 20)
    
    corazon = [
        "  ♥♥   ♥♥  ",
        " ♥♥♥♥ ♥♥♥♥ ",
        "♥♥♥♥♥♥♥♥♥♥♥",
        " ♥♥♥♥♥♥♥♥♥ ",
        "  ♥♥♥♥♥♥♥  ",
        "   ♥♥♥♥♥   ",
        "    ♥♥♥    ",
        "     ♥     "
    ]
    
    for linea in corazon:
        print(linea)

def dibujar_corazon_grande():
    """Dibuja un corazón más grande"""
    print("\n💝 Corazón grande:")
    print("=" * 30)
    
    corazon = [
        "    ♥♥♥     ♥♥♥    ",
        "  ♥♥♥♥♥♥♥ ♥♥♥♥♥♥♥  ",
        " ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ ",
        "♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥",
        "♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥",
        " ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ ",
        "  ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥  ",
        "   ♥♥♥♥♥♥♥♥♥♥♥♥♥   ",
        "    ♥♥♥♥♥♥♥♥♥♥♥    ",
        "     ♥♥♥♥♥♥♥♥♥     ",
        "      ♥♥♥♥♥♥♥      ",
        "       ♥♥♥♥♥       ",
        "        ♥♥♥        ",
        "         ♥         "
    ]
    
    for linea in corazon:
        print(linea)

def dibujar_corazon_emoji():
    """Dibuja un corazón con emojis"""
    print("\n❤️ Corazón con emojis:")
    print("=" * 25)
    
    corazon = [
        "  ❤️❤️   ❤️❤️  ",
        " ❤️💖❤️ ❤️💖❤️ ",
        "❤️💖💕💖❤️💖💕💖❤️",
        " ❤️💖💕💖💕💖💕❤️ ",
        "  ❤️💖💕💖💕💖❤️  ",
        "   ❤️💖💕💖💕❤️   ",
        "    ❤️💖💕💖❤️    ",
        "     ❤️💖💕❤️     ",
        "      ❤️💖❤️      ",
        "       ❤️❤️       ",
        "        ❤️        "
    ]
    
    for linea in corazon:
        print(linea)

def main():
    """Función principal"""
    print("💕 GENERADOR DE CORAZONES")
    print("=" * 30)
    
    dibujar_corazon_simple()
    dibujar_corazon_grande()
    dibujar_corazon_emoji()

if __name__ == "__main__":
    main()
