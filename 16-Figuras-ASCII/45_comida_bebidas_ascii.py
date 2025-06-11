"""
Ejercicio 45: Comida y Bebidas ASCII

Objetivo:
- Crear figuras de comida y bebidas en ASCII
- Incluir variantes: hamburguesa, pizza, taco, café, cerveza, pastel
- Permitir personalización y mostrar menús gastronómicos

Conceptos:
- Arte ASCII temático gastronómico
- Menú interactivo
- Representación visual de alimentos
"""

def hamburguesa_ascii():
    """Hamburguesa ASCII"""
    print("🍔 HAMBURGUESA ASCII 🍔")
    print("═" * 40)
    
    hamburguesa = [
        "      .-\"\"\"\"\"-.",
        "     /         \\",
        "    |  ========= |  <- Pan superior",
        "    |  🍅🧀🥬🍅 |  <- Tomate, queso, lechuga",
        "    |  ████████  |  <- Carne",
        "    |  🧅🥒🧅🥒 |  <- Cebolla, pepinillo",
        "    |  ========= |  <- Pan inferior",
        "     \\         /",
        "      '-.......-'"
    ]
    
    for linea in hamburguesa:
        print(linea)
    
    print("\n🍔 ¡Deliciosa hamburguesa completa!")
    print("Ingredientes: Pan, carne, queso, lechuga, tomate, cebolla, pepinillo")

def pizza_ascii():
    """Pizza ASCII"""
    print("🍕 PIZZA ASCII 🍕")
    print("═" * 40)
    
    pizza = [
        "      ╭─────────╮",
        "     ╱           ╲",
        "    ╱   🍅   🧀   ╲",
        "   ╱  🍄   🍅   🫒  ╲",
        "  ╱    🧀   🍄   🍅  ╲",
        " ╱  🫒   🍅   🧀   🍄 ╲",
        "╱________________________╲",
        "╲________________________╱",
        " ╲  Masa crujiente      ╱",
        "  ╲____________________╱"
    ]
    
    for linea in pizza:
        print(linea)
    
    print("\n🍕 Pizza italiana con:")
    print("🍅 Tomate | 🧀 Mozzarella | 🍄 Champiñones | 🫒 Aceitunas")

def taco_ascii():
    """Taco mexicano ASCII"""
    print("🌮 TACO MEXICANO ASCII 🌮")
    print("═" * 40)
    
    taco = [
        "     ╭─────────╮",
        "    ╱           ╲",
        "   ╱   🥩🌶️🧅   ╲",
        "  ╱  🥬🍅🧀🌽   ╲",
        " ╱_______________╲",
        "╱_________________╲",
        "╲_________________╱",
        " ╲_______________╱"
    ]
    
    for linea in taco:
        print(linea)
    
    print("\n🌮 Taco mexicano auténtico con:")
    print("🥩 Carne | 🌶️ Chile | 🧅 Cebolla | 🥬 Lechuga")
    print("🍅 Tomate | 🧀 Queso | 🌽 Elote")

def cafe_ascii():
    """Café caliente ASCII"""
    print("☕ CAFÉ ASCII ☕")
    print("═" * 30)
    
    cafe = [
        "    ╭─────╮",
        "   ╱       ╲",
        "  ╱    ~    ╲  <- Vapor",
        " ╱     ~     ╲",
        "│   ████████  │ <- Café",
        "│   ████████  │",
        "│   ████████  │",
        "╰─────────────╯",
        "       │││",
        "    ╰─────╯  <- Plato"
    ]
    
    for linea in cafe:
        print(linea)
    
    print("\n☕ Café recién hecho")
    print("~ ~ ~ Aromático y caliente ~ ~ ~")

def cerveza_ascii():
    """Cerveza ASCII"""
    print("🍺 CERVEZA ASCII 🍺")
    print("═" * 30)
    
    cerveza = [
        "    ╭───╮",
        "   ╱     ╲",
        "  ╱ ░░░░░ ╲  <- Espuma",
        " │  ░░░░░░  │",
        " │  ████████ │ <- Cerveza",
        " │  ████████ │",
        " │  ████████ │",
        " │  ████████ │",
        " │  ████████ │",
        " ╰──────────╯"
    ]
    
    for linea in cerveza:
        print(linea)
    
    print("\n🍺 Cerveza fría y refrescante")
    print("░ Espuma cremosa | █ Cerveza dorada")

def pastel_ascii():
    """Pastel de cumpleaños ASCII"""
    print("🎂 PASTEL ASCII 🎂")
    print("═" * 40)
    
    pastel = [
        "   🕯️  🕯️  🕯️  🕯️  🕯️",
        "   |   |   |   |   |",
        " ╭─────────────────────╮",
        "│  🍓🍒🍓🍒🍓🍒🍓🍒  │ <- Decoración",
        "│ ████████████████████ │",
        "│ ████████████████████ │ <- Bizcocho",
        "│ 🍯🍯🍯🍯🍯🍯🍯🍯🍯 │ <- Crema",
        "│ ████████████████████ │",
        "│ ████████████████████ │ <- Bizcocho",
        "╰─────────────────────╯"
    ]
    
    for linea in pastel:
        print(linea)
    
    print("\n🎂 ¡Feliz cumpleaños!")
    print("🕯️ 5 velitas | 🍓 Fresas | 🍒 Cerezas | 🍯 Crema")

def helado_ascii():
    """Helado ASCII"""
    print("🍦 HELADO ASCII 🍦")
    print("═" * 30)
    
    helado = [
        "    ░░░░░",
        "   ░░░░░░░",
        "  ░░░░░░░░░  <- Helado",
        " ░░░░░░░░░░░",
        "░░░░░░░░░░░░░",
        " ╲░░░░░░░░░╱",
        "  ╲░░░░░░░╱",
        "   ╲░░░░░╱",
        "    ╲░░░╱",
        "     ╲░╱",
        "      V    <- Cono"
    ]
    
    for linea in helado:
        print(linea)
    
    print("\n🍦 Helado cremoso en cono")
    print("Sabores disponibles: Vainilla, Chocolate, Fresa")

def menu_principal():
    """Menú principal del programa"""
    while True:
        print("\n" + "═" * 50)
        print("🍔 COMIDA Y BEBIDAS ASCII 🍕")
        print("═" * 50)
        print("1. Hamburguesa")
        print("2. Pizza")
        print("3. Taco mexicano")
        print("4. Café")
        print("5. Cerveza")
        print("6. Pastel de cumpleaños")
        print("7. Helado")
        print("0. Salir")
        print("═" * 50)
        
        opcion = input("Selecciona un alimento: ")
        
        if opcion == "1":
            hamburguesa_ascii()
        elif opcion == "2":
            pizza_ascii()
        elif opcion == "3":
            taco_ascii()
        elif opcion == "4":
            cafe_ascii()
        elif opcion == "5":
            cerveza_ascii()
        elif opcion == "6":
            pastel_ascii()
        elif opcion == "7":
            helado_ascii()
        elif opcion == "0":
            print("¡Buen apetito! 🍽️")
            break
        else:
            print("Opción no válida")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
