#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 73: Alimentos y Comida ASCII
=====================================

Objetivo:
- Crear representaciones ASCII de diferentes alimentos
- Implementar platos y bebidas diversas
- Mostrar la gastronomía mundial

Conceptos aplicados:
- Representación de alimentos y gastronomía
- Arte culinario con caracteres ASCII
- Cultura alimentaria internacional
"""

def mostrar_menu():
    """Muestra el menú de opciones disponibles"""
    print("\n" + "="*50)
    print("🍽️ GENERADOR DE ALIMENTOS ASCII 🍽️")
    print("="*50)
    print("1. Pizza")
    print("2. Hamburguesa")
    print("3. Sushi")
    print("4. Tacos")
    print("5. Pastel de Cumpleaños")
    print("6. Café")
    print("7. Helado")
    print("8. Frutas")
    print("9. Paella")
    print("0. Salir")
    print("-"*50)

def pizza():
    """Pizza italiana deliciosa"""
    print("🍕 PIZZA 🍕")
    print()
    print("Especialidad italiana con ingredientes frescos")
    print()
    
    pizza_ascii = [
        "        ╭─────────────╮        ",
        "       ╱               ╲       ",
        "      ╱     🍅   🧀     ╲      ",
        "     ╱   🫒     🍅    🧀  ╲     ",
        "    ╱  🧀    🫒    🍅     ╲    ",
        "   ╱     🍅      🧀   🫒   ╲   ",
        "  ╱   🫒    🍅     🧀       ╲  ",
        " ╱  🧀      🫒   🍅    🧀    ╲ ",
        "│     🍅  🧀     🫒     🍅   │",
        " ╲  🫒     🍅   🧀    🫒    ╱ ",
        "  ╲    🧀     🍅    🫒     ╱  ",
        "   ╲     🍅  🧀     🍅   ╱   ",
        "    ╲  🫒    🧀   🍅     ╱    ",
        "     ╲    🍅     🧀   🫒 ╱     ",
        "      ╲   🧀   🍅     ╱      ",
        "       ╲_____________╱       ",
        "",
        "🇮🇹 Pizza Margherita",
        "🍅 Tomate, 🧀 Mozzarella, 🌿 Albahaca"
    ]
    
    for linea in pizza_ascii:
        print(linea)

def hamburguesa():
    """Hamburguesa americana clásica"""
    print("🍔 HAMBURGUESA 🍔")
    print()
    print("Clásico americano con todos los ingredientes")
    print()
    
    hamburguesa_ascii = [
        "      ╭─────────────╮       ",
        "     ╱ ●●●●●●●●●●●●● ╲      ",
        "    ╱  ●●●●●●●●●●●●●  ╲     ",
        "   ╱___●●●●●●●●●●●●●___╲    ",
        "  │   🥬🥬🥬🥬🥬🥬🥬🥬🥬   │   ",
        "  │  🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅  │   ",
        "  │   🧀🧀🧀🧀🧀🧀🧀🧀🧀   │   ",
        "  │ ████████████████████ │   ",
        "  │ ████████████████████ │   ",
        "  │ ████████████████████ │   ",
        "  │   🥒🥒🥒🥒🥒🥒🥒🥒🥒   │   ",
        "  │    🟡🟡🟡🟡🟡🟡🟡🟡    │   ",
        "   ╲___________________╱    ",
        "    ╲_________________╱     ",
        "     ╲_______________╱      ",
        "",
        "🇺🇸 Hamburguesa completa",
        "🥩 Carne, 🥬 Lechuga, 🍅 Tomate, 🧀 Queso"
    ]
    
    for linea in hamburguesa_ascii:
        print(linea)

def sushi():
    """Sushi japonés elegante"""
    print("🍣 SUSHI 🍣")
    print()
    print("Arte culinario japonés milenario")
    print()
    
    sushi_ascii = [
        "    🍣 NIGIRI SUSHI 🍣       ",
        "",
        "  ┌─────────┐ ┌─────────┐   ",
        "  │🐟🐟🐟🐟🐟│ │🦐🦐🦐🦐🦐│   ",
        "  │🐟🐟🐟🐟🐟│ │🦐🦐🦐🦐🦐│   ",
        "  ├─────────┤ ├─────────┤   ",
        "  │🍚🍚🍚🍚🍚│ │🍚🍚🍚🍚🍚│   ",
        "  │🍚🍚🍚🍚🍚│ │🍚🍚🍚🍚🍚│   ",
        "  │🍚🍚🍚🍚🍚│ │🍚🍚🍚🍚🍚│   ",
        "  └─────────┘ └─────────┘   ",
        "",
        "  🥢 MAKI ROLLS 🥢          ",
        "",
        "    ●●●●●   ●●●●●   ●●●●●   ",
        "   ●🥒🐟🥒● ●🥑🦐🥑● ●🥕🐟🥕●  ",
        "    ●●●●●   ●●●●●   ●●●●●   ",
        "",
        "🇯🇵 Sashimi de atún y langostino",
        "🍚 Arroz sushi, 🥢 Palillos"
    ]
    
    for linea in sushi_ascii:
        print(linea)

def tacos():
    """Tacos mexicanos auténticos"""
    print("🌮 TACOS 🌮")
    print()
    print("Sabor mexicano tradicional")
    print()
    
    tacos_ascii = [
        "   🌮 TACOS MEXICANOS 🌮     ",
        "",
        "      ╭─────────╮           ",
        "     ╱           ╲          ",
        "    ╱   🥩🌶️🧅🥬   ╲         ",
        "   ╱  🥩🌶️🧅🥬🍅🧀  ╲        ",
        "  ╱ 🥩🌶️🧅🥬🍅🧀🌶️🥩 ╲       ",
        " ╱🥩🌶️🧅🥬🍅🧀🌶️🥩🧅🥬╲      ",
        "╱ 🌶️🧅🥬🍅🧀🌶️🥩🧅🥬🍅 ╲     ",
        "╲_🥬🍅🧀🌶️🥩🧅🥬🍅🧀🌶️_╱     ",
        " ╲_🧀🌶️🥩🧅🥬🍅🧀🌶️🥩_╱      ",
        "  ╲_🥩🧅🥬🍅🧀🌶️🥩🧅_╱       ",
        "   ╲_🥬🍅🧀🌶️🥩🧅🥬_╱        ",
        "    ╲_🧀🌶️🥩🧅🥬_╱         ",
        "     ╲_🥩🌶️🧅_╱          ",
        "      ╲_____╱           ",
        "",
        "🇲🇽 Taco al pastor",
        "🥩 Carne, 🌶️ Chile, 🧅 Cebolla, 🥬 Cilantro"
    ]
    
    for linea in tacos_ascii:
        print(linea)

def pastel_cumpleanos():
    """Pastel de cumpleaños festivo"""
    print("🎂 PASTEL DE CUMPLEAÑOS 🎂")
    print()
    print("¡Celebración dulce y especial!")
    print()
    
    pastel_ascii = [
        "   🕯️  🕯️  🕯️  🕯️  🕯️    ",
        "   ┃   ┃   ┃   ┃   ┃     ",
        "  ╔═══════════════════╗   ",
        "  ║ 🍓 FELIZ 🍓 🎈 🍓  ║   ",
        "  ║ 🎈 CUMPLE 🍓 🎈 🍓 ║   ",
        "  ║ 🍓 AÑOS! 🎈 🍓 🎈  ║   ",
        "  ╠═══════════════════╣   ",
        "  ║█████████████████████║   ",
        "  ║█████████████████████║   ",
        "  ║█████████████████████║   ",
        "  ║█████████████████████║   ",
        "  ╠═══════════════════╣   ",
        "  ║🍫🍫🍫🍫🍫🍫🍫🍫🍫🍫🍫║   ",
        "  ║🍫🍫🍫🍫🍫🍫🍫🍫🍫🍫🍫║   ",
        "  ╚═══════════════════╝   ",
        "    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀     ",
        "",
        "🎉 ¡Que cumplas muchos más!",
        "🍰 Pastel de chocolate con fresas"
    ]
    
    for linea in pastel_ascii:
        print(linea)

def cafe():
    """Café aromático"""
    print("☕ CAFÉ ☕")
    print()
    print("Energía y aroma para empezar el día")
    print()
    
    cafe_ascii = [
        "    ☕ CAFÉ EXPRESSO ☕     ",
        "                           ",
        "       ╭─────────╮         ",
        "      ╱     ○     ╲        ",
        "     ╱      ○      ╲       ",
        "    ╱       ○       ╲      ",
        "   ╱    ♨️  ○  ♨️    ╲     ",
        "  ╱     ♨️  ○  ♨️     ╲    ",
        " ╱      ♨️  ○  ♨️      ╲   ",
        "│       ♨️ ███ ♨️       │  ",
        "│      ♨️ █████ ♨️      │  ",
        "│     ♨️ ███████ ♨️     │  ",
        "│    ♨️ █████████ ♨️    │  ",
        "│   ♨️ ███████████ ♨️   │  ",
        "│  ♨️ █████████████ ♨️  │  ",
        " ╲ ♨️ █████████████ ♨️ ╱   ",
        "  ╲_███████████████_╱    ",
        "   ╲_█████████████_╱     ",
        "    ╲_███████████_╱      ",
        "     ╲___________╱       ",
        "      ╰─────────╯        ",
        "",
        "☕ Café colombiano premium",
        "♨️ Recién hecho y aromático"
    ]
    
    for linea in cafe_ascii:
        print(linea)

def helado():
    """Helado refrescante"""
    print("🍦 HELADO 🍦")
    print()
    print("Dulce refrescante para el verano")
    print()
    
    helado_ascii = [
        "      🍦 HELADO 🍦         ",
        "                          ",
        "       ╭─────╮            ",
        "      ╱ 🍓🍓🍓 ╲           ",
        "     ╱ 🍓🍓🍓🍓🍓 ╲          ",
        "    ╱ 🍓🍓🍓🍓🍓🍓🍓 ╲         ",
        "   ╱🍓🍓🍓🍓🍓🍓🍓🍓🍓╲        ",
        "   │🍓🍓🍓🍓🍓🍓🍓🍓🍓│        ",
        "   │🍓🍓🍓🍓🍓🍓🍓🍓🍓│        ",
        "   │🟤🟤🟤🟤🟤🟤🟤🟤🟤│        ",
        "   │🟤🟤🟤🟤🟤🟤🟤🟤🟤│        ",
        "   │🟨🟨🟨🟨🟨🟨🟨🟨🟨│        ",
        "   │🟨🟨🟨🟨🟨🟨🟨🟨🟨│        ",
        "    ╲🟨🟨🟨🟨🟨🟨🟨╱         ",
        "     ╲🟨🟨🟨🟨🟨╱          ",
        "      ╲🟨🟨🟨╱           ",
        "       ╲🟨╱            ",
        "        ┃             ",
        "        ┃             ",
        "        ┃             ",
        "",
        "🍓 Fresa, 🟤 Chocolate, 🟨 Vainilla",
        "🧊 Triple sabor refrescante"
    ]
    
    for linea in helado_ascii:
        print(linea)

def frutas():
    """Variedad de frutas frescas"""
    print("🍎 FRUTAS FRESCAS 🍎")
    print()
    print("Vitaminas y sabor natural")
    print()
    
    frutas_ascii = [
        "  🍎 FRUTAS FRESCAS 🍎     ",
        "",
        "   🍎      🍊      🍌     ",
        "  ╱ ╲    ╱─╲    ╱───╲    ",
        " ╱●●●╲  ╱●●●╲  ╱●●●●●╲   ",
        "│●●●●●│ │●●●●│ │●●●●●●│   ",
        " ╲●●●╱   ╲●●╱   ╲●●●●╱    ",
        "  ╲_╱     ╲╱     ╲──╱     ",
        "",
        "   🍇      🍓      🥝     ",
        "  ●●●    ╱─╲    ╱───╲    ",
        "  ●●●   ╱●●●╲  ╱●●●●●╲   ",
        "  ●●●  │●●●●●│ │●○○○●│   ",
        "  ●●●   ╲●●●╱  │●○○○●│   ",
        "   ┃     ╲─╱    ╲●●●╱    ",
        "",
        "   🍑      🥭      🍍     ",
        "  ●●●    ╱─╲    ╱─────╲  ",
        "  ●●●   ╱●●●╲  ╱┬┬┬┬┬┬╲ ",
        "   ┃   │●●●●●│ │●●●●●●●│ ",
        "   ┃    ╲●●●╱  │●●●●●●●│ ",
        "        ╲─╱   ╲●●●●●●●╱ ",
        "",
        "🌈 Arcoíris de vitaminas y sabores"
    ]
    
    for linea in frutas_ascii:
        print(linea)

def paella():
    """Paella valenciana tradicional"""
    print("🥘 PAELLA 🥘")
    print()
    print("Especialidad valenciana con arroz y mariscos")
    print()
    
    paella_ascii = [
        "    🥘 PAELLA VALENCIANA 🥘   ",
        "",
        "   ╭─────────────────────╮   ",
        "  ╱                       ╲  ",
        " ╱   🦐  🍅  🦪  🟨  🟨   ╲ ",
        "╱  🟨 🦐 🟨 🍅 🦪 🟨 🦐 🟨 ╲",
        "│ 🟨🦐🟨🍅🦪🟨🦐🟨🍅🦪🟨🦐🟨│",
        "│🦐🟨🍅🦪🟨🦐🟨🍅🦪🟨🦐🟨🍅│",
        "│🟨🍅🦪🟨🦐🟨🍅🦪🟨🦐🟨🍅🦪│",
        "│🍅🦪🟨🦐🟨🍅🦪🟨🦐🟨🍅🦪🟨│",
        "│🦪🟨🦐🟨🍅🦪🟨🦐🟨🍅🦪🟨🦐│",
        "│🟨🦐🟨🍅🦪🟨🦐🟨🍅🦪🟨🦐🟨│",
        "╲🦐🟨🍅🦪🟨🦐🟨🍅🦪🟨🦐🟨╱",
        " ╲ 🟨 🍅 🦪 🟨 🦐 🟨 🍅 🦪 ╱ ",
        "  ╲_______________________╱  ",
        "    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀    ",
        "",
        "🇪🇸 Paella tradicional valenciana",
        "🍚 Arroz, 🦐 Langostinos, 🦪 Mejillones",
        "🍅 Tomate, 🧄 Ajo, 🌶️ Azafrán"
    ]
    
    for linea in paella_ascii:
        print(linea)

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Selecciona una opción (0-9): ").strip()
            
            if opcion == '0':
                print("\n¡Buen provecho! 🍽️")
                break
            elif opcion == '1':
                pizza()
            elif opcion == '2':
                hamburguesa()
            elif opcion == '3':
                sushi()
            elif opcion == '4':
                tacos()
            elif opcion == '5':
                pastel_cumpleanos()
            elif opcion == '6':
                cafe()
            elif opcion == '7':
                helado()
            elif opcion == '8':
                frutas()
            elif opcion == '9':
                paella()
            else:
                print("❌ Opción no válida. Por favor, elige una opción del 0 al 9.")
                
        except ValueError:
            print("❌ Por favor, introduce un número válido.")
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego! 🍽️")
            break
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
