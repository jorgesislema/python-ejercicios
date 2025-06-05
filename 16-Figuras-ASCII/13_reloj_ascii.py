"""
Ejercicio 13: Reloj ASCII
=========================

Objetivo:
Crear diferentes tipos de relojes con manecillas y números.

Conceptos a practicar:
- Círculos con marcadores
- Posicionamiento de elementos
- Representación de tiempo

Instrucciones:
1. Crear la cara del reloj
2. Añadir números de horas
3. Dibujar manecillas
"""

def dibujar_reloj_simple():
    """Dibuja un reloj simple"""
    print("\n🕐 Reloj simple:")
    print("=" * 20)
    
    reloj = [
        "    12    ",
        "  9  |  3 ",
        "     |    ",
        "-----+----",
        "     |    ",
        "     6    "
    ]
    
    for linea in reloj:
        print(linea)

def dibujar_reloj_completo():
    """Dibuja un reloj completo con todos los números"""
    print("\n🕓 Reloj completo:")
    print("=" * 25)
    
    reloj = [
        "      12      ",
        "  11      1   ",
        "10          2 ",
        "9     +     3 ",
        "8           4 ",
        "  7       5   ",
        "      6       "
    ]
    
    for linea in reloj:
        print(linea)

def dibujar_reloj_digital():
    """Dibuja un reloj digital"""
    print("\n📱 Reloj digital:")
    print("=" * 25)
    
    import datetime
    hora_actual = datetime.datetime.now()
    
    reloj = [
        "┌─────────────┐",
        "│             │",
        f"│   {hora_actual.strftime('%H:%M:%S')}   │",
        "│             │",
        "└─────────────┘"
    ]
    
    for linea in reloj:
        print(linea)

def main():
    """Función principal"""
    print("🕐 GENERADOR DE RELOJES")
    print("=" * 25)
    
    dibujar_reloj_simple()
    dibujar_reloj_completo()
    dibujar_reloj_digital()

if __name__ == "__main__":
    main()
