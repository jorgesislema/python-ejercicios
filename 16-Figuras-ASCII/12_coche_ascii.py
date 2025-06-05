"""
Ejercicio 12: Coche ASCII
=========================

Objetivo:
Crear diferentes tipos de vehículos usando arte ASCII.

Conceptos a practicar:
- Figuras complejas
- Detalles mecánicos
- Perspectiva lateral

Instrucciones:
1. Dibujar la carrocería del coche
2. Añadir ruedas
3. Incluir detalles como ventanas y puertas
"""

def dibujar_coche_simple():
    """Dibuja un coche simple"""
    print("\n🚗 Coche simple:")
    print("=" * 25)
    
    coche = [
        "     ______     ",
        "    /|_||_\\`.__",
        "   (   _    _ _\\",
        "  =`-(_)--(_)-' ",
    ]
    
    for linea in coche:
        print(linea)

def dibujar_coche_detallado():
    """Dibuja un coche más detallado"""
    print("\n🚙 Coche detallado:")
    print("=" * 30)
    
    coche = [
        "       ___-------___     ",
        "    _-~               ~-_",
        " _-~                     ~-_",
        "~      ___-------___       ~",
        "|   _-~             ~-_   |",
        "|_-~                   ~-_|",
        "| []               []  |",
        " \\                    /",
        "  ~-_               _-~",
        "     ~-___-------___~  "
    ]
    
    for linea in coche:
        print(linea)

def dibujar_truck():
    """Dibuja un camión"""
    print("\n🚛 Camión:")
    print("=" * 30)
    
    truck = [
        "    ______________",
        "   |  ___________  |",
        "   | |           | |",
        "   | |___________| |",
        "   |_______________|",
        " _____|       |_____",
        "(     )       (     )",
        " \\___/         \\___/ "
    ]
    
    for linea in truck:
        print(linea)

def main():
    """Función principal"""
    print("🚗 GENERADOR DE VEHÍCULOS")
    print("=" * 30)
    
    dibujar_coche_simple()
    dibujar_coche_detallado()
    dibujar_truck()

if __name__ == "__main__":
    main()
