"""
Ejercicio 15: Montañas ASCII
============================

Objetivo:
Crear paisajes montañosos con diferentes alturas y formas.

Conceptos a practicar:
- Perfiles irregulares
- Paisajes naturales
- Capas y profundidad

Instrucciones:
1. Crear picos de diferentes alturas
2. Añadir detalles como nieve y árboles
3. Crear horizontes montañosos
"""

def dibujar_montaña_simple():
    """Dibuja una montaña simple"""
    print("\n🏔️ Montaña simple:")
    print("=" * 20)
    
    montaña = [
        "       /\\       ",
        "      /  \\      ",
        "     /    \\     ",
        "    /      \\    ",
        "   /        \\   ",
        "  /          \\  ",
        " /            \\ ",
        "/______________\\"
    ]
    
    for linea in montaña:
        print(linea)

def dibujar_cordillera():
    """Dibuja una cordillera"""
    print("\n🏔️ Cordillera:")
    print("=" * 40)
    
    cordillera = [
        "     /\\    /\\       /\\     ",
        "    /  \\  /  \\     /  \\    ",
        "   /    \\/    \\   /    \\   ",
        "  /              \\/      \\  ",
        " /                        \\ ",
        "/__________________________ \\"
    ]
    
    for linea in cordillera:
        print(linea)

def dibujar_montaña_con_nieve():
    """Dibuja montañas con nieve"""
    print("\n🏔️ Montañas nevadas:")
    print("=" * 35)
    
    montañas = [
        "       ❄️       ❄️     ",
        "      /❄️\\     /❄️\\    ",
        "     /❄️❄️\\   /❄️❄️\\   ",
        "    /      \\ /      \\  ",
        "   /        V        \\ ",
        "  /                   \\",
        " /                     \\",
        "/_______________________\\"
    ]
    
    for linea in montañas:
        print(linea)

def dibujar_paisaje_completo():
    """Dibuja un paisaje montañoso completo"""
    print("\n🌄 Paisaje completo:")
    print("=" * 45)
    
    paisaje = [
        "      ☀️                    ",
        "        ❄️    ❄️           ",
        "       /❄️\\  /❄️\\          ",
        "      /❄️❄️\\/❄️❄️\\         ",
        "     /            \\        ",
        "    /              \\   🌲  ",
        "   /                \\ 🌲🌲 ",
        "  /                  \\🌲🌲🌲",
        " /                    \\____",
        "/________________________ 🏠"
    ]
    
    for linea in paisaje:
        print(linea)

def main():
    """Función principal"""
    print("🏔️ GENERADOR DE MONTAÑAS")
    print("=" * 30)
    
    dibujar_montaña_simple()
    dibujar_cordillera()
    dibujar_montaña_con_nieve()
    dibujar_paisaje_completo()

if __name__ == "__main__":
    main()
