"""
Ejercicio 46: Emojis y Caritas ASCII

Objetivo:
- Crear diferentes emojis y caritas expresivas en ASCII
- Incluir variantes: feliz, triste, enojado, sorprendido, guiño, etc.
- Permitir personalización y animaciones de expresiones

Conceptos:
- Arte ASCII expresivo
- Representación de emociones
- Menú interactivo con estados de ánimo
"""

def carita_feliz():
    """Carita feliz ASCII"""
    print("😊 CARITA FELIZ ASCII 😊")
    print("═" * 30)
    
    print("""
       ╭─────────╮
      ╱           ╲
     ╱   ◉     ◉   ╲
    │               │
    │       ω       │
    │   ╲         ╱ │
    │    ╲_______╱  │
     ╲             ╱
      ╲___________╱
    """)
    print("¡Muy feliz! 😊")

def carita_triste():
    """Carita triste ASCII"""
    print("😢 CARITA TRISTE ASCII 😢")
    print("═" * 30)
    
    print("""
       ╭─────────╮
      ╱           ╲
     ╱   ◉     ◉   ╲
    │               │
    │       ω       │
    │   ╱         ╲ │
    │  ╱___________╲│
     ╲             ╱
      ╲___________╱
    """)
    print("Muy triste... 😢")

def carita_enojada():
    """Carita enojada ASCII"""
    print("😠 CARITA ENOJADA ASCII 😠")
    print("═" * 30)
    
    print("""
       ╭─────────╮
      ╱           ╲
     ╱  ╲◉     ◉╱  ╲
    │     ╲     ╱   │
    │       ω       │
    │   ╱─────────╲ │
    │  ╱___________╲│
     ╲             ╱
      ╲___________╱
    """)
    print("¡Muy enojado! 😠")

def carita_sorprendida():
    """Carita sorprendida ASCII"""
    print("😲 CARITA SORPRENDIDA ASCII 😲")
    print("═" * 30)
    
    print("""
       ╭─────────╮
      ╱           ╲
     ╱   ○     ○   ╲
    │               │
    │       ω       │
    │       ○       │
    │               │
     ╲             ╱
      ╲___________╱
    """)
    print("¡Qué sorpresa! 😲")

def carita_guino():
    """Carita con guiño ASCII"""
    print("😉 CARITA GUIÑO ASCII 😉")
    print("═" * 30)
    
    print("""
       ╭─────────╮
      ╱           ╲
     ╱   ─     ◉   ╲
    │               │
    │       ω       │
    │   ╲         ╱ │
    │    ╲_______╱  │
     ╲             ╱
      ╲___________╱
    """)
    print("Guiño coqueto 😉")

def carita_dormida():
    """Carita dormida ASCII"""
    print("😴 CARITA DORMIDA ASCII 😴")
    print("═" * 30)
    
    print("""
       ╭─────────╮
      ╱           ╲
     ╱   ─     ─   ╲
    │               │
    │       ω       │
    │       ∩       │
    │    Z z z      │
     ╲             ╱
      ╲___________╱
    """)
    print("Durmiendo profundamente... 😴")

def carita_corazon():
    """Carita enamorada ASCII"""
    print("😍 CARITA ENAMORADA ASCII 😍")
    print("═" * 30)
    
    print("""
       ╭─────────╮
      ╱           ╲
     ╱   ♥     ♥   ╲
    │               │
    │       ω       │
    │   ╲         ╱ │
    │    ╲_______╱  │
     ╲             ╱
      ╲___________╱
    """)
    print("Enamorado total! 😍")

def animacion_caritas():
    """Animación de cambio de expresiones"""
    import time
    import os
    
    expresiones = [
        ("😊", "¡Feliz!"),
        ("😢", "Triste..."),
        ("😠", "¡Enojado!"),
        ("😲", "¡Sorpresa!"),
        ("😉", "Guiño"),
        ("😴", "Dormido..."),
        ("😍", "Enamorado")
    ]
    
    print("🎭 ANIMACIÓN DE EXPRESIONES 🎭")
    print("═" * 40)
    
    for i in range(3):  # 3 ciclos
        for emoji, descripcion in expresiones:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("🎭 ANIMACIÓN DE EXPRESIONES 🎭")
            print("═" * 40)
            print(f"""
           ╭─────────╮
          ╱           ╲
         ╱   ◉     ◉   ╲
        │               │
        │   {emoji}  {descripcion}  │
        │               │
         ╲             ╱
          ╲___________╱
            """)
            time.sleep(0.8)
    
    print("\n¡Ciclo de emociones completado! 🎭")

def menu_principal():
    """Menú principal del programa"""
    while True:
        print("\n" + "═" * 50)
        print("😊 EMOJIS Y CARITAS ASCII 😊")
        print("═" * 50)
        print("1. Carita feliz")
        print("2. Carita triste")
        print("3. Carita enojada")
        print("4. Carita sorprendida")
        print("5. Carita con guiño")
        print("6. Carita dormida")
        print("7. Carita enamorada")
        print("8. Animación de expresiones")
        print("0. Salir")
        print("═" * 50)
        
        opcion = input("Selecciona una expresión: ")
        
        if opcion == "1":
            carita_feliz()
        elif opcion == "2":
            carita_triste()
        elif opcion == "3":
            carita_enojada()
        elif opcion == "4":
            carita_sorprendida()
        elif opcion == "5":
            carita_guino()
        elif opcion == "6":
            carita_dormida()
        elif opcion == "7":
            carita_corazon()
        elif opcion == "8":
            animacion_caritas()
        elif opcion == "0":
            print("¡Hasta luego! 😊")
            break
        else:
            print("Opción no válida")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
