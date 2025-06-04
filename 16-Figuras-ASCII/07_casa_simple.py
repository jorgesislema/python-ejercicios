"""
Ejercicio 7: Casa Simple
========================

Objetivo:
Crear una casa usando caracteres ASCII con techo, paredes, puerta y ventanas.

Conceptos a practicar:
- Combinación de formas geométricas
- Estructuras con detalles
- Proporciones arquitectónicas básicas

Instrucciones:
1. Crear el techo triangular
2. Añadir paredes rectangulares
3. Incluir puerta y ventanas
4. Decorar con elementos adicionales
"""

def dibujar_casa_simple():
    """Dibuja una casa simple"""
    print("\n🏠 Casa simple:")
    print("=" * 25)
    
    casa = [
        "      /\\      ",
        "     /  \\     ",
        "    /    \\    ",
        "   /______\\   ",
        "   |  __  |   ",
        "   | |  | |   ",
        "   | |  | |   ",
        "   | |__| |   ",
        "   |______|   "
    ]
    
    for linea in casa:
        print(linea)

def dibujar_casa_con_ventanas():
    """Dibuja una casa con ventanas"""
    print("\n🏡 Casa con ventanas:")
    print("=" * 30)
    
    casa = [
        "        /\\        ",
        "       /  \\       ",
        "      /    \\      ",
        "     /______\\     ",
        "     |  []  |     ",
        "     | ---- |     ",
        "     |[]  []|     ",
        "     | ---- |     ",
        "     | |__| |     ",
        "     |______|     "
    ]
    
    for linea in casa:
        print(linea)

def dibujar_casa_completa():
    """Dibuja una casa completa con detalles"""
    print("\n🏘️ Casa completa:")
    print("=" * 35)
    
    casa = [
        "         /\\         ",
        "        /  \\        ",
        "       /    \\       ",
        "      /______\\      ",
        "      |  🔥  |      ",  # Chimenea
        "      |[🪟][🪟]|      ",  # Ventanas
        "      | ---- |      ",
        "      |[🪟][🪟]|      ",
        "      | ---- |      ",
        "      |  🚪  |      ",  # Puerta
        "      |______|      ",
        "     🌸🌸🌸🌸🌸     "   # Jardín
    ]
    
    for linea in casa:
        print(linea)

def main():
    """Función principal"""
    print("🏠 GENERADOR DE CASAS")
    print("=" * 25)
    
    dibujar_casa_simple()
    dibujar_casa_con_ventanas()
    dibujar_casa_completa()

if __name__ == "__main__":
    main()
