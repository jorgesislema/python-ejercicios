#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 72: Flores y Jardines ASCII
====================================

Objetivo:
- Crear representaciones ASCII de diferentes tipos de flores
- Implementar jardines y elementos botánicos
- Mostrar la belleza natural floral

Conceptos aplicados:
- Representación de flora y botánica
- Elementos decorativos naturales
- Jardines y paisajismo
"""

def mostrar_menu():
    """Muestra el menú de opciones disponibles"""
    print("\n" + "="*50)
    print("🌸 GENERADOR DE FLORES Y JARDINES ASCII 🌸")
    print("="*50)
    print("1. Rosa")
    print("2. Girasol")
    print("3. Tulipán")
    print("4. Margarita")
    print("5. Lirio")
    print("6. Jardín de Flores")
    print("7. Árbol Florecido")
    print("8. Maceta con Flores")
    print("9. Campo de Lavanda")
    print("0. Salir")
    print("-"*50)

def rosa():
    """Rosa romántica"""
    print("🌹 ROSA 🌹")
    print()
    print("Símbolo del amor y la pasión")
    print()
    
    rosa_ascii = [
        "           🌹          ",
        "         ╭─○─╮        ",
        "        ╱ ╭─╮ ╲       ",
        "       ╱ ╭───╮ ╲      ",
        "      │ ╱ ● ● ╲ │     ",
        "      │╱   ─   ╲│     ",
        "      ╱ ╲ ╰─╯ ╱ ╲     ",
        "     ╱   ╲___╱   ╲    ",
        "    ╱             ╲   ",
        "   ╱       ┃       ╲  ",
        "  ╱        ┃        ╲ ",
        " ╱         ┃      🍃╲ ",
        "╱       🍃 ┃         ╲",
        "        ░░░┃░░░       ",
        "        ░░░░░░░       "
    ]
    
    for linea in rosa_ascii:
        print(linea)

def girasol():
    """Girasol brillante"""
    print("🌻 GIRASOL 🌻")
    print()
    print("Siempre mirando hacia el sol")
    print()
    
    girasol_ascii = [
        "    🌻 ╲   │   ╱ 🌻    ",
        "  🌻     ╲ │ ╱     🌻  ",
        " 🌻   ╲   ╲│╱   ╱   🌻 ",
        "🌻     ╲   ●   ╱     🌻",
        " 🌻   ╱  ●●●●●  ╲   🌻 ",
        "  🌻 ╱  ●●●●●●●  ╲ 🌻  ",
        "    ╱  ●●●●●●●●●  ╲    ",
        "   │  ●●●●●●●●●●●  │   ",
        "    ╲  ●●●●●●●●●  ╱    ",
        "  🌻 ╲  ●●●●●●●  ╱ 🌻  ",
        " 🌻   ╲  ●●●●●  ╱   🌻 ",
        "🌻     ╲   ●   ╱     🌻",
        " 🌻   ╱   ╱│╲   ╲   🌻 ",
        "  🌻     ╱ │ ╲     🌻  ",
        "    🌻 ╱   │   ╲ 🌻    ",
        "         ░░┃░░         ",
        "         ░░┃░░         "
    ]
    
    for linea in girasol_ascii:
        print(linea)

def tulipan():
    """Tulipán elegante"""
    print("🌷 TULIPÁN 🌷")
    print()
    print("Elegancia primaveral holandesa")
    print()
    
    tulipan_ascii = [
        "        🌷            ",
        "       ╱─╲           ",
        "      ╱   ╲          ",
        "     ╱     ╲         ",
        "    ╱       ╲        ",
        "   ╱    ●    ╲       ",
        "  ╱           ╲      ",
        " ╱             ╲     ",
        "│               │    ",
        "│      ┃        │    ",
        " ╲     ┃       ╱     ",
        "  ╲    ┃   🍃 ╱      ",
        "   ╲   ┃     ╱       ",
        "    ╲  ┃    ╱        ",
        "     ╲ ┃   ╱         ",
        "      ░┃░░░          ",
        "      ░┃░░░          "
    ]
    
    for linea in tulipan_ascii:
        print(linea)

def margarita():
    """Margarita simple"""
    print("🌼 MARGARITA 🌼")
    print()
    print("Simplicidad y pureza natural")
    print()
    
    margarita_ascii = [
        "      🌼              ",
        "    ⬜ ╱ ╲ ⬜          ",
        "   ⬜ ╱   ╲ ⬜         ",
        "  ⬜ ╱     ╲ ⬜        ",
        " ⬜ ╱   🟡   ╲ ⬜       ",
        "⬜ ╱   🟡🟡🟡   ╲ ⬜    ",
        " ⬜╱  🟡🟡🟡🟡🟡  ╲⬜     ",
        "  ╱  🟡🟡🟡🟡🟡🟡🟡  ╲    ",
        " ⬜╲  🟡🟡🟡🟡🟡  ╱⬜     ",
        "⬜ ╲   🟡🟡🟡   ╱ ⬜    ",
        " ⬜ ╲   🟡   ╱ ⬜       ",
        "  ⬜ ╲     ╱ ⬜        ",
        "   ⬜ ╲   ╱ ⬜         ",
        "    ⬜ ╲ ╱ ⬜          ",
        "       ┃              ",
        "     ░░┃░░            ",
        "     ░░┃░░            "
    ]
    
    for linea in margarita_ascii:
        print(linea)

def lirio():
    """Lirio majestuoso"""
    print("🏵️ LIRIO 🏵️")
    print()
    print("Majestuosidad y nobleza floral")
    print()
    
    lirio_ascii = [
        "        🏵️           ",
        "       ╱──╲          ",
        "      ╱    ╲         ",
        "     ╱   ●  ╲        ",
        "    ╱        ╲       ",
        "   ╱     ●    ╲      ",
        "  ╱      ●     ╲     ",
        " ╱    ●     ●   ╲    ",
        "╱          ●     ╲   ",
        "╲       ●        ╱   ",
        " ╲          ●   ╱    ",
        "  ╲     ●      ╱     ",
        "   ╲    ●     ╱      ",
        "    ╲        ╱       ",
        "     ╲  ●  ╱         ",
        "      ╲   ╱┃         ",
        "       ╲_╱ ┃🍃       ",
        "        ░░┃░░        ",
        "        ░░┃░░        "
    ]
    
    for linea in lirio_ascii:
        print(linea)

def jardin_flores():
    """Jardín completo con múltiples flores"""
    print("🌺 JARDÍN DE FLORES 🌺")
    print()
    print("Un rincón del paraíso terrenal")
    print()
    
    jardin_ascii = [
        "🌸   🌼     🌻        🌷   🌺",
        " ╲    ╲      ●         ╱    ╱ ",
        "  ●    ●   ●●●●●      ╱    ╱  ",
        "  ┃    ┃   ●●●●●●●    ┃   ┃   ",
        "  ┃🍃  ┃    ●●●●●     ┃   ┃🍃 ",
        "░░┃░░░░┃░░░░░●░░░░░░░░░┃░░░┃░░░",
        "░░░░░░░░░░░░░░┃░░░░░░░░░░░░░░░░░",
        "🌿   🌿     ░░┃░░     🌿   🌿  ",
        "  🦋      🌿░░░░░🌿      🐝    ",
        "     🌿      🌸      🌿       ",
        "  🌿    🏵️        🌼    🌿   ",
        "     ╱      ╲      ╱           ",
        "    ╱        ╲    ╱  ●         ",
        "   ┃          ┃  ┃   ┃         ",
        "░░░┃░░░░░░░░░░░┃░░┃░░░┃░░░░░░░░░",
        "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"
    ]
    
    for linea in jardin_ascii:
        print(linea)

def arbol_florecido():
    """Árbol en plena floración"""
    print("🌸 ÁRBOL FLORECIDO 🌸")
    print()
    print("La primavera en todo su esplendor")
    print()
    
    arbol_ascii = [
        "       🌸🌸🌸🌸🌸       ",
        "     🌸🌸🌸🌸🌸🌸🌸     ",
        "   🌸🌸🌸🌸🌸🌸🌸🌸🌸   ",
        "  🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸  ",
        " 🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸 ",
        "🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸",
        " 🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸 ",
        "  🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸  ",
        "   🌸🌸🌸🌸🌸🌸🌸🌸🌸   ",
        "     🌸🌸🌸🌸🌸🌸🌸     ",
        "       🌸🌸🌸🌸🌸       ",
        "          ┃ ┃          ",
        "          ┃ ┃          ",
        "          ┃ ┃          ",
        "          ┃ ┃          ",
        "          ┃ ┃          ",
        "░░░░░░░░░░┃ ┃░░░░░░░░░░",
        "░░░░░░░░░░░░░░░░░░░░░░░░"
    ]
    
    for linea in arbol_ascii:
        print(linea)

def maceta_flores():
    """Maceta decorativa con flores"""
    print("🪴 MACETA CON FLORES 🪴")
    print()
    print("Belleza en un rincón del hogar")
    print()
    
    maceta_ascii = [
        "   🌺   🌼   🌸      ",
        "    ╲    ╲   ╱       ",
        "     ●    ●  ╱        ",
        "     ┃    ┃ ┃         ",
        "     ┃🍃  ┃ ┃🍃       ",
        "   ┌─┴────┴─┴──┐     ",
        "   │ ░░░░░░░░░░ │     ",
        "   │ ░░░░░░░░░░ │     ",
        "   │ ░░░░░░░░░░ │     ",
        "   │ ░░░░░░░░░░ │     ",
        "   │ ░░░░░░░░░░ │     ",
        "   └─┬────────┬─┘     ",
        "     │  ◊◊◊◊  │       ",
        "     │  ◊◊◊◊  │       ",
        "     └────────┘       ",
        "       ▄▄▄▄▄▄         "
    ]
    
    for linea in maceta_ascii:
        print(linea)

def campo_lavanda():
    """Campo de lavanda aromática"""
    print("💜 CAMPO DE LAVANDA 💜")
    print()
    print("Aroma relajante y color violeta")
    print()
    
    lavanda_ascii = [
        "💜 💜 💜 💜 💜 💜 💜 💜 💜",
        "🟣 🟣 🟣 🟣 🟣 🟣 🟣 🟣 🟣",
        "🟣 🟣 🟣 🟣 🟣 🟣 🟣 🟣 🟣",
        "┃  ┃  ┃  ┃  ┃  ┃  ┃  ┃  ┃ ",
        "┃  ┃  ┃  ┃  ┃  ┃  ┃  ┃  ┃ ",
        "┃  ┃  ┃  ┃  ┃  ┃  ┃  ┃  ┃ ",
        "🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩",
        "🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩",
        "",
        "💜 Lavanda francesa",
        "🌿 Perfecta para aromaterapia",
        "🦋 Atrae mariposas",
        "🐝 Amada por las abejas"
    ]
    
    for linea in lavanda_ascii:
        print(linea)

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Selecciona una opción (0-9): ").strip()
            
            if opcion == '0':
                print("\n¡Que florezca la belleza en tu día! 🌸")
                break
            elif opcion == '1':
                rosa()
            elif opcion == '2':
                girasol()
            elif opcion == '3':
                tulipan()
            elif opcion == '4':
                margarita()
            elif opcion == '5':
                lirio()
            elif opcion == '6':
                jardin_flores()
            elif opcion == '7':
                arbol_florecido()
            elif opcion == '8':
                maceta_flores()
            elif opcion == '9':
                campo_lavanda()
            else:
                print("❌ Opción no válida. Por favor, elige una opción del 0 al 9.")
                
        except ValueError:
            print("❌ Por favor, introduce un número válido.")
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego! 🌺")
            break
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
