"""
Ejercicio 17: Calavera ASCII
============================

Objetivo:
Crear calaveras y elementos de Halloween usando caracteres ASCII.

Conceptos a practicar:
- Formas simétricas
- Detalles anatómicos
- Arte gótico

Instrucciones:
1. Crear la forma básica del cráneo
2. Añadir cuencas de ojos
3. Incluir nariz y boca con dientes
"""

def dibujar_calavera_simple():
    """Dibuja una calavera simple"""
    print("\n💀 Calavera simple:")
    print("=" * 25)
    
    calavera = [
        "     _____     ",
        "   /       \\   ",
        "  |  O   O  |  ",
        "  |    v    |  ",
        "  |  \\___/  |  ",
        "   \\_______/   "
    ]
    
    for linea in calavera:
        print(linea)

def dibujar_calavera_detallada():
    """Dibuja una calavera más detallada"""
    print("\n☠️ Calavera detallada:")
    print("=" * 30)
    
    calavera = [
        "      .-..--.     ",
        "     (  o    )    ",
        "      '-'  '-'    ",
        "       \\    /     ",
        "        \\  /      ",
        "         \\/       ",
        "      .------.    ",
        "     ( || || )    ",
        "      '------'    "
    ]
    
    for linea in calavera:
        print(linea)

def dibujar_calavera_emoji():
    """Dibuja una calavera con emojis"""
    print("\n💀 Calavera emoji:")
    print("=" * 25)
    
    calavera = [
        "     🤍🤍🤍     ",
        "   🤍🖤 🖤🤍   ",
        "  🤍  🖤🖤  🤍  ",
        "  🤍    🔸    🤍  ",
        "  🤍  ⬛⬛⬛  🤍  ",
        "   🤍🤍🤍🤍🤍   "
    ]
    
    for linea in calavera:
        print(linea)

def dibujar_esqueleto():
    """Dibuja un esqueleto simple"""
    print("\n🦴 Esqueleto:")
    print("=" * 25)
    
    esqueleto = [
        "     💀     ",
        "     ||     ",
        "   --||--   ",
        "     ||     ",
        "     ||     ",
        "    /  \\    ",
        "   /    \\   ",
        "  🦴      🦴  "
    ]
    
    for linea in esqueleto:
        print(linea)

def main():
    """Función principal"""
    print("💀 GENERADOR DE CALAVERAS")
    print("=" * 30)
    
    print("\nSelecciona el tipo:")
    print("1. Calavera simple")
    print("2. Calavera detallada")
    print("3. Calavera emoji")
    print("4. Esqueleto")
    print("5. Mostrar todos")
    
    try:
        opcion = input("\nElige una opción (1-5): ")
        
        if opcion == "1":
            dibujar_calavera_simple()
        elif opcion == "2":
            dibujar_calavera_detallada()
        elif opcion == "3":
            dibujar_calavera_emoji()
        elif opcion == "4":
            dibujar_esqueleto()
        elif opcion == "5":
            dibujar_calavera_simple()
            dibujar_calavera_detallada()
            dibujar_calavera_emoji()
            dibujar_esqueleto()
        else:
            print("❌ Opción no válida")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
