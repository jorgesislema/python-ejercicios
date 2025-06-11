"""
Ejercicio 47: Superhéroes ASCII

Objetivo:
- Crear figuras de superhéroes famosos en ASCII
- Incluir variantes: Superman, Batman, Spider-Man, Wonder Woman, etc.
- Permitir personalización y mostrar logos/símbolos

Conceptos:
- Arte ASCII temático de superhéroes
- Representación de personajes icónicos
- Menú interactivo heroico
"""

def superman_ascii():
    """Superman ASCII con logo"""
    print("🦸‍♂️ SUPERMAN ASCII 🦸‍♂️")
    print("═" * 40)
    
    print("Logo de Superman:")
    print("""
        ╭─────────╮
       ╱           ╲
      ╱             ╲
     ╱   ╭─────╮     ╲
    │   ╱       ╲     │
    │  │    S    │    │
    │   ╲       ╱     │
     ╲   ╰─────╯     ╱
      ╲             ╱
       ╲___________╱
    """)
    
    print("Figura de Superman:")
    print("""
         ╭───╮
        ╱  ○  ╲
       ╱   │   ╲
      ╱    │    ╲
     │─────S─────│  <- Capa
     │     │     │
     │   ╱─┴─╲   │
     │  │     │  │
     ╰──┴─────┴──╯
        │     │
        │     │
       ╱│     │╲
      ╱ └─────┘ ╲
    """)
    print("¡El Hombre de Acero! 💪")

def batman_ascii():
    """Batman ASCII con logo"""
    print("🦇 BATMAN ASCII 🦇")
    print("═" * 40)
    
    print("Logo de Batman:")
    print("""
       ╭─╮   ╭─╮
      ╱   ╲ ╱   ╲
     ╱     ╲╱     ╲
    ╱               ╲
   ╱       ╭─╮       ╲
  ╱       ╱   ╲       ╲
 ╱       ╱     ╲       ╲
╱_______╱       ╲_______╲
    """)
    
    print("Figura de Batman:")
    print("""
         ╭───╮
        ╱ ◉ ◉ ╲
       ╱   │   ╲
      ╱    │    ╲
     │─────■─────│  <- Capa negra
     │     │     │
     │   ╱─┴─╲   │
     │  │     │  │
     ╰──┴─────┴──╯
        │     │
        │     │
       ╱│     │╲
      ╱ └─────┘ ╲
    """)
    print("¡El Caballero Oscuro! 🌙")

def spiderman_ascii():
    """Spider-Man ASCII"""
    print("🕷️ SPIDER-MAN ASCII 🕷️")
    print("═" * 40)
    
    print("Máscara de Spider-Man:")
    print("""
       ╭─────────╮
      ╱  ◊     ◊  ╲
     ╱     ╲ ╱     ╲
    │   ╲   ╲╱   ╱   │
    │    ╲   │   ╱    │
    │     ╲  │  ╱     │
    │      ╲ │ ╱      │
     ╲      ╲│╱      ╱
      ╲______│______╱
    """)
    
    print("Telaraña:")
    print("""
    ╱─────────────────╲
   ╱  ╱─────────────╲  ╲
  ╱  ╱               ╲  ╲
 ╱  ╱     🕷️         ╲  ╲
╱  ╱                   ╲  ╲
╲  ╲                   ╱  ╱
 ╲  ╲                 ╱  ╱
  ╲  ╲_______________╱  ╱
   ╲___________________╱
    """)
    print("¡Tu amigable vecino Spider-Man! 🕸️")

def wonder_woman_ascii():
    """Wonder Woman ASCII"""
    print("👸 WONDER WOMAN ASCII 👸")
    print("═" * 40)
    
    print("Logo de Wonder Woman:")
    print("""
         ╭─╮
        ╱   ╲
       ╱  W  ╲
      ╱   W   ╲
     ╱    W    ╲
    ╱─────W─────╲
   ╱             ╲
  ╱_______________╲
    """)
    
    print("Figura de Wonder Woman:")
    print("""
         ╭───╮
        ╱ ★ ★ ╲
       ╱   │   ╲
      ╱    │    ╲
     │─────★─────│  <- Tiara dorada
     │     │     │
     │   ╱─┴─╲   │
     │  │ ⚔️  │  │  <- Espada
     ╰──┴─────┴──╯
        │  🛡️ │     <- Escudo
        │     │
       ╱│     │╲
      ╱ └─────┘ ╲
    """)
    print("¡La Princesa Amazona! 👑")

def flash_ascii():
    """Flash ASCII"""
    print("⚡ FLASH ASCII ⚡")
    print("═" * 40)
    
    print("Logo de Flash:")
    print("""
       ╭─────────╮
      ╱           ╲
     ╱    ⚡⚡⚡    ╲
    │   ⚡⚡⚡⚡⚡   │
    │  ⚡⚡⚡⚡⚡⚡  │
    │   ⚡⚡⚡⚡⚡   │
     ╲    ⚡⚡⚡    ╱
      ╲___________╱
    """)
    
    print("Flash corriendo:")
    print("""
         ╭───╮
        ╱ ◉ ◉ ╲
       ╱   │   ╲
      ╱    │    ╲
     │─────⚡─────│  <- Rayo
     │     │     │ ≡≡≡  <- Velocidad
     │   ╱─┴─╲   │ ≡≡≡
     │  │     │  │ ≡≡≡
     ╰──┴─────┴──╯
        │     │
        │     │ ≡≡≡
       ╱│     │╲≡≡≡
      ╱ └─────┘ ╲
    """)
    print("¡El Hombre Más Rápido del Mundo! 💨")

def iron_man_ascii():
    """Iron Man ASCII"""
    print("🤖 IRON MAN ASCII 🤖")
    print("═" * 40)
    
    print("Casco de Iron Man:")
    print("""
       ╭─────────╮
      ╱ ◉ ╱─╲ ◉ ╲
     ╱    ╱   ╲    ╲
    │    ╱  ▲  ╲    │
    │   │   │   │   │
    │   │   ▼   │   │
    │    ╲     ╱    │
     ╲    ╲___╱    ╱
      ╲___________╱
    """)
    
    print("Armadura de Iron Man:")
    print("""
         ╭───╮
        ╱ ◆ ◆ ╲
       ╱   ╲╱   ╲
      ╱    ◆    ╲  <- Reactor Arc
     │─────◆─────│
     │     ◆     │
     │   ╱─┴─╲   │
     │  │ 🔥  │  │  <- Propulsores
     ╰──┴─────┴──╯
        │ 🔥  │
        │     │
       ╱│ 🔥  │╲
      ╱ └─────┘ ╲
    """)
    print("¡El Hombre de Hierro! 🔥")

def capitan_america_ascii():
    """Capitán América ASCII"""
    print("🇺🇸 CAPITÁN AMÉRICA ASCII 🇺🇸")
    print("═" * 40)
    
    print("Escudo del Capitán América:")
    print("""
       ╭─────────╮
      ╱ ░░░░░░░░░ ╲
     ╱ ░▓▓▓▓▓▓▓▓░ ╲
    │ ░▓░░░░░░░▓░ │
    │ ░▓░ ★ ★ ░▓░ │
    │ ░▓░ ★★★ ░▓░ │
    │ ░▓░ ★ ★ ░▓░ │
    │ ░▓░░░░░░░▓░ │
     ╲ ░▓▓▓▓▓▓▓▓░ ╱
      ╲ ░░░░░░░░░ ╱
       ╰─────────╯
    """)
    
    print("Capitán América:")
    print("""
         ╭───╮
        ╱ ◉ ◉ ╲
       ╱   │   ╲
      ╱    │    ╲
     │─────A─────│  <- Uniforme
     │     │     │
     │   ╱─┴─╲   │
     │  │ 🛡️  │  │  <- Escudo
     ╰──┴─────┴──╯
        │     │
        │     │
       ╱│     │╲
      ╱ └─────┘ ╲
    """)
    print("¡El Primer Vengador! 🛡️")

def menu_principal():
    """Menú principal del programa"""
    while True:
        print("\n" + "═" * 50)
        print("🦸‍♂️ SUPERHÉROES ASCII 🦸‍♀️")
        print("═" * 50)
        print("1. Superman")
        print("2. Batman")
        print("3. Spider-Man")
        print("4. Wonder Woman")
        print("5. Flash")
        print("6. Iron Man")
        print("7. Capitán América")
        print("0. Salir")
        print("═" * 50)
        
        opcion = input("Selecciona un superhéroe: ")
        
        if opcion == "1":
            superman_ascii()
        elif opcion == "2":
            batman_ascii()
        elif opcion == "3":
            spiderman_ascii()
        elif opcion == "4":
            wonder_woman_ascii()
        elif opcion == "5":
            flash_ascii()
        elif opcion == "6":
            iron_man_ascii()
        elif opcion == "7":
            capitan_america_ascii()
        elif opcion == "0":
            print("¡Hasta luego, héroe! 🦸‍♂️")
            break
        else:
            print("Opción no válida")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
