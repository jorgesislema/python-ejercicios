"""
Ejercicio 16: Avión ASCII
=========================

Objetivo:
Crear diferentes tipos de aviones y aeronaves usando arte ASCII.

Conceptos a practicar:
- Figuras aerodinámicas
- Perspectiva lateral
- Detalles mecánicos

Instrucciones:
1. Crear el fuselaje del avión
2. Añadir alas y cola
3. Incluir detalles como ventanas
"""

def dibujar_avion_simple():
    """Dibuja un avión simple"""
    print("\n✈️ Avión simple:")
    print("=" * 30)
    
    avion = [
        "        __|__        ",
        "  *---oOo-----       ",
        "       \\     \\       ",
        "        \\_____\\      "
    ]
    
    for linea in avion:
        print(linea)

def dibujar_avion_comercial():
    """Dibuja un avión comercial"""
    print("\n🛫 Avión comercial:")
    print("=" * 35)
    
    avion = [
        "          ___           ",
        "       __/   \\__        ",
        "  *---(_________)---    ",
        "      o o o o o         ",
        "       \\             \\ ",
        "        \\___________    \\"
    ]
    
    for linea in avion:
        print(linea)

def dibujar_helicoptero():
    """Dibuja un helicóptero"""
    print("\n🚁 Helicóptero:")
    print("=" * 25)
    
    helicoptero = [
        "  _____________________ ",
        "    \\               /   ",
        "     \\             /    ",
        "      |  o o o o  |     ",
        "      |___________|     ",
        "           | |          ",
        "           | |          ",
        "      _____|_|_____     "
    ]
    
    for linea in helicoptero:
        print(linea)

def dibujar_cohete():
    """Dibuja un cohete espacial"""
    print("\n🚀 Cohete espacial:")
    print("=" * 25)
    
    cohete = [
        "      /\\      ",
        "     /  \\     ",
        "    /____\\    ",
        "    |    |    ",
        "    | ** |    ",
        "    |____|    ",
        "   /      \\   ",
        "  /        \\  ",
        " /__________\\ ",
        "  \\/\\/\\/\\/   "
    ]
    
    for linea in cohete:
        print(linea)

def main():
    """Función principal"""
    print("✈️ GENERADOR DE AERONAVES")
    print("=" * 30)
    
    print("\nSelecciona el tipo de aeronave:")
    print("1. Avión simple")
    print("2. Avión comercial")
    print("3. Helicóptero")
    print("4. Cohete")
    print("5. Mostrar todos")
    
    try:
        opcion = input("\nElige una opción (1-5): ")
        
        if opcion == "1":
            dibujar_avion_simple()
        elif opcion == "2":
            dibujar_avion_comercial()
        elif opcion == "3":
            dibujar_helicoptero()
        elif opcion == "4":
            dibujar_cohete()
        elif opcion == "5":
            dibujar_avion_simple()
            dibujar_avion_comercial()
            dibujar_helicoptero()
            dibujar_cohete()
        else:
            print("❌ Opción no válida")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
