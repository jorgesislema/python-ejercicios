"""
EJERCICIO 20: Gato ASCII
========================

OBJETIVO:
Crear diferentes representaciones de gatos usando caracteres ASCII,
incluyendo caritas de gato, gatos completos y escenas con múltiples gatos.

CONCEPTOS:
- Arte ASCII para animales
- Uso de caracteres especiales para detalles
- Composición de figuras complejas
- Variaciones de expresiones faciales
"""

def cara_gato_simple():
    """Dibuja una cara de gato simple"""
    print("=== CARA DE GATO SIMPLE ===")
    print("   /\\_/\\  ")
    print("  ( o.o ) ")
    print("   > ^ <  ")
    print("")

def cara_gato_detallada():
    """Dibuja una cara de gato más detallada"""
    print("=== CARA DE GATO DETALLADA ===")
    print("    /\\_   _/\\    ")
    print("   /  o\\_/o  \\   ")
    print("  (  =  ^  =  )  ")
    print("   )         (   ")
    print("  (  (  o  )  )  ")
    print("   \\_\\_____/_/   ")
    print("")

def gato_completo():
    """Dibuja un gato completo de cuerpo entero"""
    print("=== GATO COMPLETO ===")
    print("       /\\_/\\  ")
    print("      ( o.o ) ")
    print("       > ^ <  ")
    print("      /|   |\\")
    print("     ( |   | )")
    print("      \\|___|/")
    print("       |   |")
    print("       |___|")
    print("      /     \\")
    print("     /_______\\")
    print("")

def gato_durmiendo():
    """Dibuja un gato durmiendo"""
    print("=== GATO DURMIENDO ===")
    print("   /\\_/\\  ")
    print("  ( -.- ) ")
    print("  o_(__\"_) ")
    print(" ~~~zZz~~~")
    print("")

def gato_emoji_style(tamaño=3):
    """Dibuja un gato estilo emoji"""
    print(f"=== GATO EMOJI (Tamaño {tamaño}) ===")
    
    if tamaño == 1:
        print("😸")
    elif tamaño == 2:
        print("  😸😸")
        print("  😸😸")
    else:
        # Versión ASCII del emoji de gato
        print("   🐱   ")
        print(" /\\_/\\ ")
        print("( ^.^ )")
        print(" ) ~ ( ")
        print("(___Y_)")
    print("")

def familia_gatos():
    """Dibuja una familia de gatos"""
    print("=== FAMILIA DE GATOS ===")
    print("     /\\_/\\      /\\_/\\      /\\_/\\")
    print("    ( o.o )    ( ^.^ )    ( -.-)  ")
    print("     > ^ <      > v <      > ^ <")
    print("    Papá       Mamá       Bebé")
    print("")

def gato_jugando():
    """Dibuja un gato jugando con una pelota"""
    print("=== GATO JUGANDO ===")
    print("   /\\_/\\     o")
    print("  ( >.<)    /")
    print("   > ^ <   ")
    print("  /|   |\\")
    print(" ( |   | )")
    print("  \\|___|/")
    print("   |   |")
    print("   |___|")
    print("  /     \\")
    print(" /_______\\")
    print("")

def gatos_conversando():
    """Dibuja dos gatos conversando"""
    print("=== GATOS CONVERSANDO ===")
    print("   /\\_/\\             /\\_/\\")
    print("  ( o.o )    ~~~    ( ^.^ )")
    print("   > ^ <    Miau!    > v <")
    print("¡Hola!               ¡Hola!")
    print("")

def patron_huellas_gato():
    """Dibuja un patrón de huellas de gato"""
    print("=== HUELLAS DE GATO ===")
    for i in range(5):
        if i % 2 == 0:
            print("   🐾    🐾")
        else:
            print("🐾    🐾   ")
    print("")

def gato_con_bigotes(longitud_bigotes=3):
    """Dibuja un gato con bigotes personalizables"""
    print(f"=== GATO CON BIGOTES (Longitud {longitud_bigotes}) ===")
    
    bigote = "=" * longitud_bigotes
    
    print("     /\\_/\\     ")
    print(f" {bigote}( o.o ){bigote} ")
    print("     > ^ <     ")
    print("")

def crear_gato_personalizado():
    """Permite crear un gato personalizado"""
    print("=== CREAR GATO PERSONALIZADO ===")
    
    # Elegir ojos
    print("Elige los ojos del gato:")
    print("1. Normales (o.o)")
    print("2. Cerrados (-.-)")
    print("3. Guiñando (o.-)")
    print("4. Grandes (O.O)")
    
    ojos_opciones = {
        "1": "o.o",
        "2": "-.-",
        "3": "o.-",
        "4": "O.O"
    }
    
    opcion_ojos = input("Opción (1-4): ").strip()
    ojos = ojos_opciones.get(opcion_ojos, "o.o")
    
    # Elegir boca
    print("\nElige la boca del gato:")
    print("1. Normal (^)")
    print("2. Sonriente (v)")
    print("3. Triste (n)")
    print("4. Lengua (:P)")
    
    boca_opciones = {
        "1": "^",
        "2": "v",
        "3": "n",
        "4": ":P"
    }
    
    opcion_boca = input("Opción (1-4): ").strip()
    boca = boca_opciones.get(opcion_boca, "^")
    
    # Dibujar el gato personalizado
    print(f"\n=== TU GATO PERSONALIZADO ===")
    print("   /\\_/\\  ")
    print(f"  ( {ojos} ) ")
    print(f"   > {boca} <  ")
    print("")

def cafeteria_gatos():
    """Dibuja una escena de cafetería de gatos"""
    print("=== CAFETERÍA DE GATOS ===")
    print("┌─────────────────────────────────┐")
    print("│        🏪 CAT CAFÉ 🏪          │")
    print("├─────────────────────────────────┤")
    print("│  /\\_/\\    ☕   /\\_/\\    ☕     │")
    print("│ ( ^.^ )       ( o.o )          │")
    print("│  > v <         > ^ <           │")
    print("│                                │")
    print("│    /\\_/\\              🧶       │")
    print("│   ( -.-)    💤                 │")
    print("│    > ^ <                       │")
    print("└─────────────────────────────────┘")
    print("")

def menu_principal():
    """Menú principal con todas las opciones"""
    while True:
        print("\n" + "="*50)
        print("🐱 GENERADOR DE GATOS ASCII 🐱")
        print("="*50)
        print("1.  Cara de gato simple")
        print("2.  Cara de gato detallada")
        print("3.  Gato completo")
        print("4.  Gato durmiendo")
        print("5.  Gato emoji style")
        print("6.  Familia de gatos")
        print("7.  Gato jugando")
        print("8.  Gatos conversando")
        print("9.  Patrón de huellas")
        print("10. Gato con bigotes")
        print("11. Crear gato personalizado")
        print("12. Cafetería de gatos")
        print("0.  Salir")
        print("="*50)
        
        opcion = input("Selecciona una opción (0-12): ").strip()
        
        if opcion == "0":
            print("¡Miau! 🐱 ¡Hasta luego!")
            break
        elif opcion == "1":
            cara_gato_simple()
        elif opcion == "2":
            cara_gato_detallada()
        elif opcion == "3":
            gato_completo()
        elif opcion == "4":
            gato_durmiendo()
        elif opcion == "5":
            try:
                tamaño = int(input("Tamaño (1-3): "))
                gato_emoji_style(tamaño)
            except ValueError:
                gato_emoji_style()
        elif opcion == "6":
            familia_gatos()
        elif opcion == "7":
            gato_jugando()
        elif opcion == "8":
            gatos_conversando()
        elif opcion == "9":
            patron_huellas_gato()
        elif opcion == "10":
            try:
                longitud = int(input("Longitud de bigotes (1-5): "))
                gato_con_bigotes(longitud)
            except ValueError:
                gato_con_bigotes()
        elif opcion == "11":
            crear_gato_personalizado()
        elif opcion == "12":
            cafeteria_gatos()
        else:
            print("❌ Opción no válida. Intenta de nuevo.")
        
        input("\n📱 Presiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
