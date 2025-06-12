"""
EJERCICIO 60: Elementos Arquitectónicos ASCII

Objetivo:
- Crear figuras ASCII de elementos y estilos arquitectónicos
- Practicar la representación de estructuras complejas
- Explorar diferentes períodos y estilos arquitectónicos

Conceptos a practicar:
- Representación de perspectiva y proporción
- Uso de patrones geométricos repetitivos
- Creación de texturas arquitectónicas
- Diseño de estructuras monumentales
"""

def mostrar_menu():
    print("\n" + "="*50)
    print("🏛️ ELEMENTOS ARQUITECTÓNICOS ASCII 🏛️")
    print("="*50)
    print("0. Salir")
    print("1. Columna griega 🏛️")
    print("2. Arco romano 🏟️")
    print("3. Ventanal gótico ⛪")
    print("4. Cúpula bizantina 🕌")
    print("5. Escalera helicoidal 🌀")
    print("6. Balcón barroco 🏰")
    print("7. Ventana modernista 🎨")
    print("8. Techo abovedado 🏛️")
    print("9. Puerta oriental 🏮")
    print("="*50)

def dibujar_columna_griega():
    print("\n🏛️ COLUMNA GRIEGA")
    print("-" * 30)
    columna = """
    ╔═══════════════════════╗
    ║ ◆◇◆◇◆◇◆◇◆◇◆◇◆ ║
    ╠═══════════════════════╣
    ║▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓║
    ║                       ║
    ║   ORDEN DÓRICO        ║
    ║                       ║
    ╚═══════════════════════╝
            ║ ║ ║ ║
            ║ ║ ║ ║
            ║ ║ ║ ║
            ║ ║ ║ ║
            ║ ║ ║ ║
            ║ ║ ║ ║
            ║ ║ ║ ║
            ║ ║ ║ ║
    ╔═══════════════════════╗
    ║ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ║
    ╚═══════════════════════╝
    """
    print(columna)
    print("Pilar clásico griego de proporción perfecta 📐")

def dibujar_arco_romano():
    print("\n🏟️ ARCO ROMANO")
    print("-" * 30)
    arco = """
    ║                         ║
    ║       AQUEDUCTO         ║
    ║                         ║
    ║    ╭─────────────╮      ║
    ║   ╱               ╲     ║
    ║  ╱  ╔═══════════╗  ╲    ║
    ║ ╱   ║           ║   ╲   ║
    ║╱    ║    👥👥    ║    ╲  ║
    ╱     ║           ║     ╲ ║
    ║     ║           ║     ║ ║
    ║     ║           ║     ║ ║
    ║     ╚═══════════╝     ║ ║
    ║                       ║ ║
    ╚═══════════════════════╝ ║
    ████████████████████████████
    """
    print(arco)
    print("Estructura romana de ingeniería y funcionalidad 🌉")

def dibujar_ventanal_gotico():
    print("\n⛪ VENTANAL GÓTICO")
    print("-" * 30)
    ventanal = """
        ╭─────╮   ╭─────╮
       ╱ ◆   ◆ ╲ ╱ ◆   ◆ ╲
      ╱   ◇   ◇   ◇   ◇   ╲
     ╱     ◆   ◆   ◆     ╲
    ╱  ◇     ◇   ◇     ◇  ╲
    ║ ◆   ◇   ◆ ◇ ◆   ◇   ◆ ║
    ║   ◇   ◆   ◇   ◆   ◇   ║
    ║ ◆   ◇   ◆   ◆   ◇   ◆ ║
    ║   ◇   ◆ 🌅 ◆   ◇   ║
    ║ ◆   ◇   ◆   ◆   ◇   ◆ ║
    ║   ◇   ◆   ◇   ◆   ◇   ║
    ║ ◆   ◇   ◆   ◆   ◇   ◆ ║
    ║   ◇   ◆   ◇   ◆   ◇   ║
    ║ ◆   ◇   ◆   ◆   ◇   ◆ ║
    ╚═══════════════════════╝
    """
    print(ventanal)
    print("Vidriera gótica que eleva el alma hacia la luz ✨")

def dibujar_cupula_bizantina():
    print("\n🕌 CÚPULA BIZANTINA")
    print("-" * 30)
    cupula = """
             ✦
           ╭─╫─╮
          ╱  ✦  ╲
         ╱   ║   ╲
        ╱_____║_____╲
       ╱ ◆ ◇ ◆ ◇ ◆ ╲
      ╱ ◇ ◆ ◇ ◆ ◇ ◆ ╲
     ╱ ◆ ◇ ◆ ◇ ◆ ◇ ◆ ╲
    ╱_____________________╲
    ║ ◇ ◆ ◇ ◆ ◇ ◆ ◇ ◆ ◇ ║
    ║                     ║
    ║  🕯️  ☦️  🕯️  ☦️  🕯️  ║
    ║                     ║
    ║ ◆ ◇ ◆ ◇ ◆ ◇ ◆ ◇ ◆ ║
    ╚═════════════════════╝
    """
    print(cupula)
    print("Cúpula bizantina que conecta tierra y cielo 🌌")

def dibujar_escalera_helicoidal():
    print("\n🌀 ESCALERA HELICOIDAL")
    print("-" * 30)
    escalera = """
    ║                     ║
    ║   ╔═══╗             ║
    ║   ║   ╚═══╗         ║
    ║   ║       ╚═══╗     ║
    ║   ║           ╚═══╗ ║
    ║   ║               ║ ║
    ║ ╔═╝               ║ ║
    ║ ║   ╔═══╗         ║ ║
    ║ ║   ║   ╚═══╗     ║ ║
    ║ ║   ║       ╚═══╗ ║ ║
    ║ ║   ║           ╚═╝ ║
    ║ ║   ║               ║
    ║ ╚═══╝   ╔═══╗       ║
    ║         ║   ╚═══╗   ║
    ║         ║       ╚═══╝
    ╚═════════╝
    """
    print(escalera)
    print("Escalera en espiral que desafía la perspectiva 🔄")

def dibujar_balcon_barroco():
    print("\n🏰 BALCÓN BARROCO")
    print("-" * 30)
    balcon = """
    ╔═══════════════════════════╗
    ║ ◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇ ║
    ║                           ║
    ║   🌹  🏛️  🌹  🏛️  🌹     ║
    ║                           ║
    ╚═══════════╤═══════════════╝
                │
    ╔═══════════╧═══════════════╗
    ║ ⚜️ ∞ ⚜️ ∞ ⚜️ ∞ ⚜️ ∞ ⚜️ ║
    ║                           ║
    ║  👩‍👑     🌹     👨‍🎩     ║
    ║                           ║
    ║ ⚜️ ∞ ⚜️ ∞ ⚜️ ∞ ⚜️ ∞ ⚜️ ║
    ╚═════════════════════════════╝
    ║ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ║
    ║ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ║
    """
    print(balcon)
    print("Balcón ornamentado del esplendor barroco 👑")

def dibujar_ventana_modernista():
    print("\n🎨 VENTANA MODERNISTA")
    print("-" * 30)
    ventana = """
    ╔═══════════════════════════╗
    ║ ░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░ ║
    ║ ▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓ ║
    ║                           ║
    ║ ╭─◇─╮   ╭─◆─╮   ╭─◇─╮   ║
    ║ │ 🌸 │   │ 🍃 │   │ 🦋 │   ║
    ║ ╰─◇─╯   ╰─◆─╯   ╰─◇─╯   ║
    ║                           ║
    ║ ╭─◆─╮   ╭─◇─╮   ╭─◆─╮   ║
    ║ │ 🌺 │   │ 🌿 │   │ 🐝 │   ║
    ║ ╰─◆─╯   ╰─◇─╯   ╰─◆─╯   ║
    ║                           ║
    ║ ▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓ ║
    ║ ░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░ ║
    ╚═══════════════════════════╝
    """
    print(ventana)
    print("Ventana modernista con motivos naturales 🌿")

def dibujar_techo_abovedado():
    print("\n🏛️ TECHO ABOVEDADO")
    print("-" * 30)
    techo = """
          ╭─────────────╮
         ╱ ◆ ◇ ◆ ◇ ◆ ◇ ╲
        ╱ ◇ ◆ ◇ ◆ ◇ ◆ ◇ ╲
       ╱ ◆ ◇ ◆ ◇ ◆ ◇ ◆ ◇ ╲
      ╱ ◇ ◆ ◇ ◆ ☀️ ◆ ◇ ◆ ◇ ╲
     ╱ ◆ ◇ ◆ ◇ ◆ ◇ ◆ ◇ ◆ ◇ ╲
    ╱___________________________╲
    ║ ◇ ◆ ◇ ◆ ◇ ◆ ◇ ◆ ◇ ◆ ◇ ║
    ║                           ║
    ║        👥 👥 👥          ║
    ║                           ║
    ║ ◆ ◇ ◆ ◇ ◆ ◇ ◆ ◇ ◆ ◇ ◆ ║
    ╚═══════════════════════════╝
    """
    print(techo)
    print("Bóveda que amplifica el espacio y la acústica 🎵")

def dibujar_puerta_oriental():
    print("\n🏮 PUERTA ORIENTAL")
    print("-" * 30)
    puerta = """
    ╔═══════════════════════════╗
    ║ 🏮 ◈ 🐉 ◈ 🏮 ◈ 🐉 ◈ 🏮 ║
    ║                           ║
    ║ ╔═══════════╤═══════════╗ ║
    ║ ║ 龍 🌸 龍  │  龍 🌸 龍 ║ ║
    ║ ║           │           ║ ║
    ║ ║ 🐉  ◯  🐉 │ 🐉  ◯  🐉 ║ ║
    ║ ║           │           ║ ║
    ║ ║ 龍 🌸 龍  │  龍 🌸 龍 ║ ║
    ║ ║           │           ║ ║
    ║ ║ 🐉  ◯  🐉 │ 🐉  ◯  🐉 ║ ║
    ║ ║           │           ║ ║
    ║ ║ ○         │         ○ ║ ║
    ║ ╚═══════════╧═══════════╝ ║
    ║                           ║
    ║ 🏮 ◈ 🐉 ◈ 🏮 ◈ 🐉 ◈ 🏮 ║
    ╚═══════════════════════════╝
    """
    print(puerta)
    print("Portal oriental decorado con dragones y símbolos 🐲")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (0-9): ").strip()
        
        if opcion == "0":
            print("\n¡Gracias por explorar la arquitectura ASCII! 🏛️")
            break
        elif opcion == "1":
            dibujar_columna_griega()
        elif opcion == "2":
            dibujar_arco_romano()
        elif opcion == "3":
            dibujar_ventanal_gotico()
        elif opcion == "4":
            dibujar_cupula_bizantina()
        elif opcion == "5":
            dibujar_escalera_helicoidal()
        elif opcion == "6":
            dibujar_balcon_barroco()
        elif opcion == "7":
            dibujar_ventana_modernista()
        elif opcion == "8":
            dibujar_techo_abovedado()
        elif opcion == "9":
            dibujar_puerta_oriental()
        else:
            print("\n❌ Opción no válida. Por favor, selecciona un número del 0 al 9.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
