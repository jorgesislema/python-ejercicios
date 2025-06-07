"""
Ejercicio 21: Barco ASCII
=========================

Objetivo:
Crear diferentes tipos de embarcaciones usando arte ASCII.

Conceptos a practicar:
- Formas marineras
- Velas y mástiles
- Elementos náuticos

Instrucciones:
1. Crear el casco del barco
2. Añadir velas y mástiles
3. Incluir detalles marineros
"""

def dibujar_barco_simple():
    """Dibuja un barco simple"""
    print("\n⛵ Barco simple:")
    print("=" * 25)
    
    barco = [
        "       |\\        ",
        "       | \\       ",
        "       |  \\      ",
        "       |   \\     ",
        "  _____|____\\    ",
        "  \\           )  ",
        "~~~\\___________/~~~"
    ]
    
    for linea in barco:
        print(linea)

def dibujar_velero():
    """Dibuja un velero completo"""
    print("\n⛵ Velero:")
    print("=" * 30)
    
    velero = [
        "        |\\           ",
        "        | \\          ",
        "        |  \\         ",
        "        |   \\        ",
        "   _____|____\\       ",
        "   |    |     |      ",
        "   |    |     |      ",
        "   |    |     |      ",
        "~~~\\____|_____/~~~~~~",
        "     ~~~~~~~         "
    ]
    
    for linea in velero:
        print(linea)

def dibujar_pirata():
    """Dibuja un barco pirata"""
    print("\n🏴‍☠️ Barco pirata:")
    print("=" * 30)
    
    pirata = [
        "      ☠️           ",
        "       |           ",
        "   ████|████       ",
        "   |   |   |       ",
        "   |   |   |       ",
        "   |___|___|       ",
        "    \\_____/        ",
        "~~~~~~~~~~~~~~~~~~~"
    ]
    
    for linea in pirata:
        print(linea)

def dibujar_submarino():
    """Dibuja un submarino"""
    print("\n🤿 Submarino:")
    print("=" * 25)
    
    submarino = [
        "        |         ",
        "   _____|_____    ",
        "  (           )   ",
        "  |  ● ● ● ●  |   ",
        "  |___________|   ",
        "~~~~~~~~~~~~~~~~~ "
    ]
    
    for linea in submarino:
        print(linea)

def main():
    """Función principal"""
    print("⛵ GENERADOR DE EMBARCACIONES")
    print("=" * 35)
    
    dibujar_barco_simple()
    dibujar_velero()
    dibujar_pirata()
    dibujar_submarino()

if __name__ == "__main__":
    main()
