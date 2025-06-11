"""
Ejercicio 43: Figuras de Deportes ASCII

Objetivo:
- Crear figuras deportivas en ASCII
- Incluir variantes: balón de fútbol, cancha, trofeo, raqueta, portería, medalla
- Permitir personalización y animaciones simples

Conceptos:
- Arte ASCII temático
- Menú interactivo
- Uso de cadenas multilinea
"""

def balon_futbol_ascii():
    print("⚽ BALÓN DE FÚTBOL ASCII ⚽\n" + "═"*30)
    print(r"""
      .-""""-.
    /        \
   /  .-""-.  \
  |  /  o  \  |
  |  \    /  |
   \  '-..-'  /
    \        /
      '-..-'
    """)

def cancha_ascii():
    print("🏟️ CANCHA DEPORTIVA ASCII 🏟️\n" + "═"*30)
    print(r"""
   ┌───────────────┐
   │     | |      │
   │     | |      │
   │-----   ----- │
   │     | |      │
   │     | |      │
   └───────────────┘
    """)

def trofeo_ascii():
    print("🏆 TROFEO ASCII 🏆\n" + "═"*30)
    print(r"""
      .-=========-.
     (   '---'   )
      \         /
       \       /
        |     |
        |     |
        |     |
       /       \
      /         \
     '-----------'
    """)

def raqueta_ascii():
    print("🎾 RAQUETA ASCII 🎾\n" + "═"*30)
    print(r"""
      ___
     /   \
    |     |
     \___/
       |
       |
       |
    """)

def porteria_ascii():
    print("🥅 PORTERÍA ASCII 🥅\n" + "═"*30)
    print(r"""
   ┌─────────────┐
   │  |  |  |  | │
   │  |  |  |  | │
   │  |  |  |  | │
   └─────────────┘
    """)

def medalla_ascii():
    print("🥇 MEDALLA ASCII 🥇\n" + "═"*30)
    print(r"""
      .-""-.
     / .--. \
    / /    \ \
    | |    | |
    | |    | |
    \ \    / /
     \ '--' /
      '-..-'
    """)

def menu_principal():
    while True:
        print("\n" + "═"*40)
        print("🏆 FIGURAS DE DEPORTES ASCII ⚽")
        print("═"*40)
        print("1. Balón de fútbol")
        print("2. Cancha deportiva")
        print("3. Trofeo")
        print("4. Raqueta")
        print("5. Portería")
        print("6. Medalla")
        print("0. Salir")
        print("═"*40)
        opcion = input("Selecciona una figura: ")
        if opcion == "1":
            balon_futbol_ascii()
        elif opcion == "2":
            cancha_ascii()
        elif opcion == "3":
            trofeo_ascii()
        elif opcion == "4":
            raqueta_ascii()
        elif opcion == "5":
            porteria_ascii()
        elif opcion == "6":
            medalla_ascii()
        elif opcion == "0":
            print("¡Hasta luego, deportista! 🏆")
            break
        else:
            print("Opción no válida")
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
