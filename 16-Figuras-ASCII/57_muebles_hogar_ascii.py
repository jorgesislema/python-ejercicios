"""
EJERCICIO 57: Muebles y Objetos del Hogar ASCII

Objetivo:
- Crear representaciones ASCII de muebles y objetos domésticos
- Practicar el diseño de formas geométricas complejas
- Explorar la representación de espacios interiores

Conceptos a practicar:
- Representación de perspectiva y profundidad
- Uso de caracteres para texturas y materiales
- Diseño de interiores con ASCII
- Creación de objetos tridimensionales
"""

def mostrar_menu():
    print("\n" + "="*50)
    print("🏠 MUEBLES Y OBJETOS DEL HOGAR ASCII 🏠")
    print("="*50)
    print("0. Salir")
    print("1. Sofá 🛋️")
    print("2. Mesa de comedor 🍽️")
    print("3. Cama 🛏️")
    print("4. Estantería 📚")
    print("5. Televisor 📺")
    print("6. Refrigerador ❄️")
    print("7. Escritorio 💻")
    print("8. Silla de oficina 💺")
    print("9. Lámpara 💡")
    print("="*50)

def dibujar_sofa():
    print("\n🛋️ SOFÁ")
    print("-" * 30)
    sofa = """
    ╔══════════════════════════════╗
    ║                              ║
    ║  ╔════╗  ╔════╗  ╔════╗     ║
    ║  ║ 🛋️ ║  ║ 🛋️ ║  ║ 🛋️ ║     ║
    ║  ╚════╝  ╚════╝  ╚════╝     ║
    ╚══════════════════════════════╝
    ╔══╗                        ╔══╗
    ║  ║                        ║  ║
    ║  ║                        ║  ║
    ║  ║                        ║  ║
    ╚══╝                        ╚══╝
    ████  ████  ████  ████  ████
    """
    print(sofa)
    print("Mueble cómodo para relajarse en familia 👨‍👩‍👧‍👦")

def dibujar_mesa_comedor():
    print("\n🍽️ MESA DE COMEDOR")
    print("-" * 30)
    mesa = """
    🍽️       🥖       🍽️
       🥤         🥤
    ╔═════════════════════════╗
    ║                         ║
    ║    🌺      🌺      🌺   ║
    ║                         ║
    ║  🍽️               🍽️   ║
    ║                         ║
    ║    🌺      🌺      🌺   ║
    ║                         ║
    ╚═════════════════════════╝
         │               │
         │               │
         │               │
         │               │
         │               │
    ═════╧═══════════════╧═════
    """
    print(mesa)
    print("Centro de reunión familiar para compartir comidas 🍽️")

def dibujar_cama():
    print("\n🛏️ CAMA")
    print("-" * 30)
    cama = """
    ╔══╗                    ╔══╗
    ║  ║████████████████████║  ║
    ║  ║                    ║  ║
    ║  ║  ╔════════════╗    ║  ║
    ║  ║  ║ 😴 😴 😴  ║    ║  ║
    ║  ║  ║            ║    ║  ║
    ║  ║  ║ 🛏️ 🛏️ 🛏️  ║    ║  ║
    ║  ║  ║            ║    ║  ║
    ║  ║  ╚════════════╝    ║  ║
    ║  ║                    ║  ║
    ╚══╝════════════════════╚══╝
       ████              ████
    """
    print(cama)
    print("Lugar de descanso y sueños reparadores 💤")

def dibujar_estanteria():
    print("\n📚 ESTANTERÍA")
    print("-" * 30)
    estanteria = """
    ╔════════════════════════════╗
    ║ 📚📖📗📘📙📕📗📖📚 ║
    ╠════════════════════════════╣
    ║ 📓📔📒📗📘📙📕📗📓 ║
    ╠════════════════════════════╣
    ║ 📚📖📗📘📙📕📗📖📚 ║
    ╠════════════════════════════╣
    ║ 🎮 📱 ⏰ 🖼️ 🎨 📷 ⚽ ║
    ╠════════════════════════════╣
    ║ 📓📔📒📗📘📙📕📗📓 ║
    ╠════════════════════════════╣
    ║ 📚📖📗📘📙📕📗📖📚 ║
    ╚════════════════════════════╝
    """
    print(estanteria)
    print("Almacén de conocimiento y recuerdos 🧠")

def dibujar_televisor():
    print("\n📺 TELEVISOR")
    print("-" * 30)
    televisor = """
    ╔══════════════════════════════╗
    ║ ○ ○ ○                   ⚡  ║
    ║                              ║
    ║  ┌────────────────────────┐  ║
    ║  │ 📺 CANAL 1 - NOTICIAS │  ║
    ║  │                        │  ║
    ║  │  🎬 PROGRAMA EN VIVO   │  ║
    ║  │                        │  ║
    ║  │    👨‍💼 → 📰 ← 👩‍💼     │  ║
    ║  │                        │  ║
    ║  │ VOL: ████████▒▒ 80%    │  ║
    ║  └────────────────────────┘  ║
    ║                              ║
    ║ 🔴 ⏹️ ⏸️ ▶️ ⏩ ⏪ 🔊 📶 ║
    ╚══════════════════════════════╝
         ╲                  ╱
          ╲________________╱
    """
    print(televisor)
    print("Ventana al mundo del entretenimiento 🎭")

def dibujar_refrigerador():
    print("\n❄️ REFRIGERADOR")
    print("-" * 30)
    refrigerador = """
    ╔════════════════════════╗
    ║ ⚡ ❄️ FRÍO ❄️ ⚡      ║
    ║ ○                  🌡️ ║
    ╠════════════════════════╣
    ║                        ║
    ║  🥛 🧀 🥚 🍎 🥕      ║
    ║                        ║
    ║  🥩 🐟 🍗 🥓 🌭      ║
    ║                        ║
    ╠════════════════════════╣
    ║                        ║
    ║  🥤 🍺 🍷 🧃 💧      ║
    ║                        ║
    ║  🍰 🧊 🍦 🍓 🍇      ║
    ║                        ║
    ╚═══════════╤════════════╝
                │
    ████████████████████████
    """
    print(refrigerador)
    print("Guardián de la frescura y conservación de alimentos 🥗")

def dibujar_escritorio():
    print("\n💻 ESCRITORIO")
    print("-" * 30)
    escritorio = """
         💻                📱
       ╔═════╗           ╔═══╗
       ║ ○ ○ ║           ║ ○ ║
       ║     ║           ╚═══╝
       ╚═════╝     
    ╔═══════════════════════════════╗
    ║ 📝 ✏️ 📎 📌 📏 📐 ✂️ 🖇️ ║
    ║                               ║
    ║  ╔═══╗   ╔═══╗   ╔═══╗      ║
    ║  ║   ║   ║   ║   ║   ║      ║
    ║  ╚═══╝   ╚═══╝   ╚═══╝      ║
    ╚═══════════════════════════════╝
         │                   │
         │                   │
         │                   │
         │                   │
    ═════╧═══════════════════╧═════
    """
    print(escritorio)
    print("Espacio de trabajo y creatividad 🎨")

def dibujar_silla_oficina():
    print("\n💺 SILLA DE OFICINA")
    print("-" * 30)
    silla = """
         ╔═════════════╗
         ║ ◉ ◉ ◉ ◉ ◉ ║
         ║             ║
         ║      👤     ║
         ║             ║
         ╚══════╤══════╝
    ╔══════════╧══════════╗
    ║ ◉ ◉ ◉ ◉ ◉ ◉ ◉ ◉ ◉ ║
    ║                     ║
    ║   █████████████     ║
    ║                     ║
    ╚══════════╤══════════╝
               │
               │ ⚙️
               │
        ○─────╱│╲─────○
       ╱       │       ╲
      ○         │         ○
               ○○○
    """
    print(silla)
    print("Asiento ergonómico para largas jornadas laborales 💼")

def dibujar_lampara():
    print("\n💡 LÁMPARA")
    print("-" * 30)
    lampara = """
                💡
              ╱   ╲
             ╱  ☀️  ╲
            ╱ ░░░░░░░ ╲
           ╱_____∩_____╲
                 │
                 │ ╔═╗
                 │ ║ ║
                 │ ║ ║
                 │ ║ ║
                 │ ╚═╝
           ╔═════╧═════╗
           ║ ◯ ⚡ ON ◯ ║
           ║           ║
           ║    ███    ║
           ║           ║
           ╚═══════════╝
    
    [ENCENDIDA] ✨ [LUZ CÁLIDA] 💛
    """
    print(lampara)
    print("Fuente de iluminación acogedora 🕯️")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (0-9): ").strip()
        
        if opcion == "0":
            print("\n¡Gracias por decorar tu hogar ASCII! 🏠")
            break
        elif opcion == "1":
            dibujar_sofa()
        elif opcion == "2":
            dibujar_mesa_comedor()
        elif opcion == "3":
            dibujar_cama()
        elif opcion == "4":
            dibujar_estanteria()
        elif opcion == "5":
            dibujar_televisor()
        elif opcion == "6":
            dibujar_refrigerador()
        elif opcion == "7":
            dibujar_escritorio()
        elif opcion == "8":
            dibujar_silla_oficina()
        elif opcion == "9":
            dibujar_lampara()
        else:
            print("\n❌ Opción no válida. Por favor, selecciona un número del 0 al 9.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
