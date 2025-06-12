"""
Ejercicio 53: Banderas del Mundo ASCII

Objetivo:
- Crear representaciones de banderas de diferentes países en ASCII
- Incluir variantes: Estados Unidos, Reino Unido, Francia, Japón, Brasil, etc.
- Permitir visualización de símbolos patrios

Conceptos:
- Símbolos nacionales en ASCII
- Representación de colores con caracteres
- Geografia y cultura mundial
"""

def bandera_estados_unidos():
    """Bandera de Estados Unidos"""
    print("🇺🇸 BANDERA DE ESTADOS UNIDOS 🇺🇸")
    print("═" * 50)
    
    bandera = [
        "🟦⭐⭐⭐⭐⭐⭐⭐⭐⭐████████████████████████",
        "🟦⭐⭐⭐⭐⭐⭐⭐⭐⭐⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
        "🟦⭐⭐⭐⭐⭐⭐⭐⭐⭐████████████████████████",
        "🟦⭐⭐⭐⭐⭐⭐⭐⭐⭐⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
        "🟦⭐⭐⭐⭐⭐⭐⭐⭐⭐████████████████████████",
        "🟦⭐⭐⭐⭐⭐⭐⭐⭐⭐⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
        "🟦⭐⭐⭐⭐⭐⭐⭐⭐⭐████████████████████████",
        "⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
        "████████████████████████████████████████████",
        "⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
        "████████████████████████████████████████████",
        "⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
        "████████████████████████████████████████████"
    ]
    
    for linea in bandera:
        print(linea)
    
    print("\n🟦 Azul: Unión | ⭐ 50 estrellas: Estados")
    print("█ Rojo: Valor | ⚪ Blanco: Pureza")

def bandera_reino_unido():
    """Bandera del Reino Unido (Union Jack)"""
    print("🇬🇧 BANDERA DEL REINO UNIDO 🇬🇧")
    print("═" * 50)
    
    bandera = [
        "🟦🟦🟦⚪⚪⚪████⚪⚪⚪🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦",
        "🟦🟦⚪⚪⚪████████⚪⚪⚪🟦🟦🟦🟦🟦🟦🟦🟦🟦",
        "🟦⚪⚪⚪████████████⚪⚪⚪🟦🟦🟦🟦🟦🟦🟦🟦",
        "⚪⚪⚪████████████████⚪⚪⚪🟦🟦🟦🟦🟦🟦🟦",
        "⚪⚪████████████████████⚪⚪🟦🟦🟦🟦🟦🟦",
        "⚪████████████████████████⚪🟦🟦🟦🟦🟦",
        "████████████████████████████🟦🟦🟦🟦",
        "⚪████████████████████████⚪🟦🟦🟦🟦🟦",
        "⚪⚪████████████████████⚪⚪🟦🟦🟦🟦🟦🟦",
        "⚪⚪⚪████████████████⚪⚪⚪🟦🟦🟦🟦🟦🟦🟦",
        "🟦⚪⚪⚪████████████⚪⚪⚪🟦🟦🟦🟦🟦🟦🟦🟦",
        "🟦🟦⚪⚪⚪████████⚪⚪⚪🟦🟦🟦🟦🟦🟦🟦🟦🟦",
        "🟦🟦🟦⚪⚪⚪████⚪⚪⚪🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦"
    ]
    
    for linea in bandera:
        print(linea)
    
    print("\nUnión de: Inglaterra, Escocia, Gales, Irlanda del Norte")

def bandera_francia():
    """Bandera de Francia (Tricolor)"""
    print("🇫🇷 BANDERA DE FRANCIA 🇫🇷")
    print("═" * 40)
    
    bandera = [
        "🟦🟦🟦🟦🟦🟦🟦⚪⚪⚪⚪⚪⚪⚪████████████████",
        "🟦🟦🟦🟦🟦🟦🟦⚪⚪⚪⚪⚪⚪⚪████████████████",
        "🟦🟦🟦🟦🟦🟦🟦⚪⚪⚪⚪⚪⚪⚪████████████████",
        "🟦🟦🟦🟦🟦🟦🟦⚪⚪⚪⚪⚪⚪⚪████████████████",
        "🟦🟦🟦🟦🟦🟦🟦⚪⚪⚪⚪⚪⚪⚪████████████████",
        "🟦🟦🟦🟦🟦🟦🟦⚪⚪⚪⚪⚪⚪⚪████████████████",
        "🟦🟦🟦🟦🟦🟦🟦⚪⚪⚪⚪⚪⚪⚪████████████████",
        "🟦🟦🟦🟦🟦🟦🟦⚪⚪⚪⚪⚪⚪⚪████████████████",
        "🟦🟦🟦🟦🟦🟦🟦⚪⚪⚪⚪⚪⚪⚪████████████████"
    ]
    
    for linea in bandera:
        print(linea)
    
    print("\n🟦 Azul: Libertad | ⚪ Blanco: Igualdad | █ Rojo: Fraternidad")

def bandera_japon():
    """Bandera de Japón (Sol Naciente)"""
    print("🇯🇵 BANDERA DE JAPÓN 🇯🇵")
    print("═" * 40)
    
    bandera = [
        "⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
        "⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
        "⚪⚪⚪⚪⚪⚪⚪🔴🔴🔴🔴⚪⚪⚪⚪⚪⚪⚪⚪⚪",
        "⚪⚪⚪⚪⚪🔴🔴🔴🔴🔴🔴🔴🔴⚪⚪⚪⚪⚪⚪⚪",
        "⚪⚪⚪⚪🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴⚪⚪⚪⚪⚪⚪",
        "⚪⚪⚪🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴⚪⚪⚪⚪⚪",
        "⚪⚪⚪🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴⚪⚪⚪⚪⚪",
        "⚪⚪⚪⚪🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴⚪⚪⚪⚪⚪⚪",
        "⚪⚪⚪⚪⚪🔴🔴🔴🔴🔴🔴🔴🔴⚪⚪⚪⚪⚪⚪⚪",
        "⚪⚪⚪⚪⚪⚪⚪🔴🔴🔴🔴⚪⚪⚪⚪⚪⚪⚪⚪⚪",
        "⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
        "⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪"
    ]
    
    for linea in bandera:
        print(linea)
    
    print("\n⚪ Blanco: Pureza y honestidad")
    print("🔴 Rojo: Sol naciente")

def bandera_brasil():
    """Bandera de Brasil"""
    print("🇧🇷 BANDERA DE BRASIL 🇧🇷")
    print("═" * 50)
    
    bandera = [
        "🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩",
        "🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩",
        "🟩🟩🟩🟩🟩🟩🟩🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩🟩🟩🟩",
        "🟩🟩🟩🟩🟩🟨🟨🟨🟨🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩🟩",
        "🟩🟩🟩🟨🟨🟨🟨🔵🔵🔵🔵🟨🟨🟨🟨🟩🟩🟩🟩🟩",
        "🟩🟩🟨🟨🟨🟨🔵🔵🔵🔵🔵🔵🟨🟨🟨🟨🟩🟩🟩🟩",
        "🟩🟩🟨🟨🟨🟨🔵🔵⭐🔵🔵🔵🟨🟨🟨🟨🟩🟩🟩🟩",
        "🟩🟩🟩🟨🟨🟨🟨🔵🔵🔵🔵🟨🟨🟨🟨🟩🟩🟩🟩🟩",
        "🟩🟩🟩🟩🟩🟨🟨🟨🟨🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩🟩",
        "🟩🟩🟩🟩🟩🟩🟩🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩🟩🟩🟩",
        "🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩",
        "🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩"
    ]
    
    for linea in bandera:
        print(linea)
    
    print("\n🟩 Verde: Bosques | 🟨 Amarillo: Riquezas minerales")
    print("🔵 Azul: Cielo | ⭐ Constelaciones")

def bandera_canada():
    """Bandera de Canadá"""
    print("🇨🇦 BANDERA DE CANADÁ 🇨🇦")
    print("═" * 40)
    
    bandera = [
        "████████⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪████████",
        "████████⚪⚪⚪⚪⚪🍁⚪⚪⚪⚪⚪⚪⚪⚪████████",
        "████████⚪⚪⚪⚪🍁🍁🍁⚪⚪⚪⚪⚪⚪████████",
        "████████⚪⚪⚪🍁🍁🍁🍁🍁⚪⚪⚪⚪⚪████████",
        "████████⚪⚪🍁🍁🍁🍁🍁🍁🍁⚪⚪⚪⚪████████",
        "████████⚪⚪🍁🍁🍁🍁🍁🍁🍁⚪⚪⚪⚪████████",
        "████████⚪⚪⚪🍁🍁🍁🍁🍁⚪⚪⚪⚪⚪████████",
        "████████⚪⚪⚪⚪🍁🍁🍁⚪⚪⚪⚪⚪⚪████████",
        "████████⚪⚪⚪⚪⚪🍁⚪⚪⚪⚪⚪⚪⚪⚪████████"
    ]
    
    for linea in bandera:
        print(linea)
    
    print("\n█ Rojo: Sacrificio | ⚪ Blanco: Paz | 🍁 Hoja de arce")

def bandera_china():
    """Bandera de China"""
    print("🇨🇳 BANDERA DE CHINA 🇨🇳")
    print("═" * 40)
    
    bandera = [
        "████⭐⚪⭐████████████████████████████████",
        "████⭐⭐⭐████████████████████████████████",
        "████⭐⚪⭐████████████████████████████████",
        "████████████████████████████████████████",
        "████████████████████████████████████████",
        "████████████████████████████████████████",
        "████████████████████████████████████████",
        "████████████████████████████████████████",
        "████████████████████████████████████████"
    ]
    
    for linea in bandera:
        print(linea)
    
    print("\n█ Rojo: Revolución | ⭐ Estrella grande: Partido")
    print("⭐ Estrellas pequeñas: Clases sociales")

def bandera_india():
    """Bandera de India"""
    print("🇮🇳 BANDERA DE INDIA 🇮🇳")
    print("═" * 40)
    
    bandera = [
        "🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧",
        "⚪⚪⚪⚪⚪⚪⚪⚪⚪☸️⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
        "⚪⚪⚪⚪⚪⚪⚪⚪⚪☸️⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
        "⚪⚪⚪⚪⚪⚪⚪⚪⚪☸️⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪",
        "🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩",
        "🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩",
        "🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩"
    ]
    
    for linea in bandera:
        print(linea)
    
    print("\n🟧 Azafrán: Valor | ⚪ Blanco: Paz | 🟩 Verde: Fe")
    print("☸️ Chakra: Rueda del dharma")

def banderas_olimpicas():
    """Anillos olímpicos"""
    print("🏅 ANILLOS OLÍMPICOS 🏅")
    print("═" * 50)
    
    anillos = [
        "    🔵🔵🔵       🟡🟡🟡       ⚫⚫⚫    ",
        "  🔵     🔵   🟡     🟡   ⚫     ⚫  ",
        "  🔵     🔵   🟡  🟢🟢🟡🟢⚫     ⚫  ",
        "    🔵🔵🔵    🟡🟢     🟢🟡 ⚫⚫⚫    ",
        "            🟡🟢       🟢🟡        ",
        "            🟡🟢  🔴🔴🔴🟢🟡        ",
        "            🟡🟢🔴     🔴🟢🟡        ",
        "              🟢🔴     🔴🟢          ",
        "                🔴🔴🔴              "
    ]
    
    for linea in anillos:
        print(linea)
    
    print("\n🔵 Azul: Europa | 🟡 Amarillo: Asia | ⚫ Negro: África")
    print("🟢 Verde: Oceanía | 🔴 Rojo: América")

def menu_principal():
    """Menú principal del programa"""
    while True:
        print("\n" + "═" * 60)
        print("🏴 BANDERAS DEL MUNDO ASCII 🏳️")
        print("═" * 60)
        print("1. Estados Unidos")
        print("2. Reino Unido")
        print("3. Francia")
        print("4. Japón")
        print("5. Brasil")
        print("6. Canadá")
        print("7. China")
        print("8. India")
        print("9. Anillos Olímpicos")
        print("0. Salir")
        print("═" * 60)
        
        opcion = input("Selecciona una bandera: ")
        
        if opcion == "1":
            bandera_estados_unidos()
        elif opcion == "2":
            bandera_reino_unido()
        elif opcion == "3":
            bandera_francia()
        elif opcion == "4":
            bandera_japon()
        elif opcion == "5":
            bandera_brasil()
        elif opcion == "6":
            bandera_canada()
        elif opcion == "7":
            bandera_china()
        elif opcion == "8":
            bandera_india()
        elif opcion == "9":
            banderas_olimpicas()
        elif opcion == "0":
            print("¡Hasta luego, ciudadano del mundo! 🌍")
            break
        else:
            print("Opción no válida")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
