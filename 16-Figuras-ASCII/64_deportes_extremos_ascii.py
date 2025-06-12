"""
EJERCICIO 64: Deportes Extremos ASCII

Objetivo:
- Crear figuras ASCII de deportes extremos y aventura
- Practicar la representación de movimiento y acción
- Explorar actividades de alto riesgo y adrenalina

Conceptos a practicar:
- Representación de movimiento dinámico
- Uso de caracteres para simular velocidad
- Creación de escenas de acción
- Diseño de ambientes extremos
"""

def mostrar_menu():
    print("\n" + "="*50)
    print("🏂 DEPORTES EXTREMOS ASCII 🏂")
    print("="*50)
    print("0. Salir")
    print("1. Paracaidismo 🪂")
    print("2. Alpinismo ⛷️")
    print("3. Surf 🏄‍♂️")
    print("4. Parapente 🪁")
    print("5. Escalada en roca 🧗‍♂️")
    print("6. Snowboard 🏂")
    print("7. Bungee jumping 🤸‍♂️")
    print("8. Rafting 🚣‍♂️")
    print("9. Base jumping 🦅")
    print("="*50)

def dibujar_paracaidismo():
    print("\n🪂 PARACAIDISMO")
    print("-" * 30)
    paracaidismo = """
    ✈️ ← Avión de salto (4000m)
      ╲
       ╲ 💨 Salto libre
        ╲
         ╲ 
          👤 ← 120 km/h
          ║
          ▼
       ╱─────╲
      ╱ 🪂🪂🪂 ╲ ← Paracaídas
     ╱ ○ ○ ○ ○ ○ ╲   principal
    ╱○ ○ ○ ○ ○ ○ ○○╲
    ╲ ○ ○ ○ ○ ○ ○ ○ ╱
     ╲ ○ ○ ○ ○ ○ ╱
      ╲___________╱
           ║
           ║ ← Cuerdas
           ║
          👤 ← Paracaidista
         ╱│╲   (300m)
        ╱ │ ╲
    
    🌍🌳🏠🌳🏠🌳🌍 ← Zona aterrizaje
    """
    print(paracaidismo)
    print("Caída libre desde las alturas del cielo ☁️")

def dibujar_alpinismo():
    print("\n⛷️ ALPINISMO")
    print("-" * 30)
    alpinismo = """
    ❄️ CUMBRE 5895m ❄️
              ▲
             ╱│╲
            ╱ │ ╲
           ╱  🚩 ╲ ← Meta
          ╱___│___╲
         ╱    │    ╲
        ╱ ⛏️ 👤 ⛏️ ╲ ← Alpinista
       ╱   ╱│╲      ╲
      ╱   ╱ │ ╲     ╲
     ╱      │       ╲
    ╱ 🧗‍♂️   │   🧗‍♀️  ╲ ← Equipo
   ╱  ⛏️    │   ⛏️   ╲
  ╱─────────────────────╲
    🏔️🏔️ CAMPAMENTO 🏔️🏔️
       ⛺ ⛺ ⛺ ⛺
    
    Equipamiento: Cuerdas, piolets ⛏️
    Riesgo: Avalanchas, hipotermia ❄️
    """
    print(alpinismo)
    print("Ascensión a las cimas más altas del mundo 🏔️")

def dibujar_surf():
    print("\n🏄‍♂️ SURF")
    print("-" * 30)
    surf = """
    🌤️ Playa Perfect Break 🌤️
    
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
         ╱▀▀▀▀▀▀▀▀▀╲
        ╱ 🏄‍♂️ TUBO  ╲ ← Barrel
       ╱    ╱│╲      ╲
      ╱    ╱ │ ╲     ╲
     ╱       │       ╲
    ╱ ≈≈≈≈≈≈│≈≈≈≈≈≈ ╲
    ╲ 🌊 OLA │ 3m 🌊  ╱
     ╲ ≈≈≈≈≈│≈≈≈≈≈ ╱
      ╲     │     ╱
       ╲____│____╱
           🏄‍♂️ ← Surfista
          ╱───╲  (Take off)
    🏖️🏖️🏖️🏖️🏖️🏖️🏖️🏖️🏖️
    
    Viento: Offshore 15 knots 💨
    Ola: 3 metros, hueca 🌊
    """
    print(surf)
    print("Domando las fuerzas del océano sobre la tabla 🌊")

def dibujar_parapente():
    print("\n🪁 PARAPENTE")
    print("-" * 30)
    parapente = """
    🏔️ Despegue Monte Alto 🏔️
    
    ╭─────────────────────────╮
   ╱ 🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁 ╲
  ╱ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ╲
  ╲ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ╱
   ╲ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ╱
    ╲_________________________╱
              ║ ║ ║
              ║ ║ ║ ← Cuerdas
              ║ ║ ║
             👤🪑👤 ← Piloto
            ╱ │ ╲
           ╱  │  ╲
    
    💨 Térmica ascendente 💨
      ↗️  ↗️  ↗️  ↗️
    🌳🏞️🌳🏞️🌳🏞️🌳
    
    Vuelo: 2-6 horas ⏰
    """
    print(parapente)
    print("Volando libre como las aves en térmicas ☁️")

def dibujar_escalada_roca():
    print("\n🧗‍♂️ ESCALADA EN ROCA")
    print("-" * 30)
    escalada = """
    🏔️ PARED VERTICAL 🏔️
    
    ████████████████████
    ██ 🧗‍♂️ LEAD ██ ← Líder
    ██  ╱│╲   ██   
    ██ ○ │ ○  ██ ← Seguros
    ██   │    ██
    ██ ○ │ ○  ██
    ██   │    ██   
    ██ ○ │ ○  ██
    ██   │ 🧗‍♀️ ██ ← Segundo
    ██ ○ │╱│╲ ██
    ██   │ ○  ██
    ██ ○ │    ██
    ██   │    ██
    ██████████████████
    ⚓ REUNIÓN ⚓
       👥 ← Asegurador
    
    Grado: 7a+ / 5.11d 📊
    Equipamiento: 12 cintas 🔗
    """
    print(escalada)
    print("Ascendiendo paredes verticales con fuerza y técnica 💪")

def dibujar_snowboard():
    print("\n🏂 SNOWBOARD")
    print("-" * 30)
    snowboard = """
    🏔️ PISTA EXTREME 🏔️
    
    ❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️
    ╲                   ╱
     ╲ 🏂 HALFPIPE    ╱
      ╲     ╱│╲     ╱ ← Rider
       ╲   ╱ │ ╲   ╱   aerial
        ╲ ╱  │  ╲ ╱
         ╲   │   ╱
          ╲  │  ╱ 🏂 ← Trick
           ╲ │ ╱     360°
            ╲│╱
             │
    ❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️
    
    Velocidad: 80 km/h 💨
    Pendiente: 35° ⛷️
    Nieve: Polvo fresco ❄️
    """
    print(snowboard)
    print("Deslizándose sobre nieve fresca en montañas nevadas ⛷️")

def dibujar_bungee_jumping():
    print("\n🤸‍♂️ BUNGEE JUMPING")
    print("-" * 30)
    bungee = """
    🌉 PUENTE 120m 🌉
    ════════════════════
    ║                  ║
    ║     🤸‍♂️ SALTO    ║ ← Saltador
    ║      ╱│╲        ║
    ║     ╱ │ ╲       ║
    ║       │         ║
    ║ ~~~~~ │ ~~~~~   ║ ← Cuerda
    ║       │         ║   elástica
    ║ ~~~~~ │ ~~~~~   ║
    ║       │         ║
    ║ ~~~~~ │ ~~~~~   ║
    ║       │         ║
    ║ ~~~~~ 👤 ~~~~~  ║ ← Rebote
    ║                  ║
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    ≈≈≈ RÍO ABAJO ≈≈≈
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    
    Caída libre: 3 segundos ⏱️
    """
    print(bungee)
    print("Salto al vacío con cuerda elástica como único apoyo 🎢")

def dibujar_rafting():
    print("\n🚣‍♂️ RAFTING")
    print("-" * 30)
    rafting = """
    🏔️ RÍO CLASE V 🏔️
    
    ████████████████████
    ╲ RAPID EXTREMO   ╱
     ╲ ≈≈≈≈≈≈≈≈≈≈≈ ╱
      ╲ 🚣‍♂️🚣‍♀️🚣‍♂️🚣‍♀️ ╱ ← Equipo
       ╲ ══════════ ╱    rafting
        ╲ ≈≈≈≈≈≈≈≈ ╱
         ╲ 🌊🌊🌊🌊 ╱ ← Rápidos
          ╲ ≈≈≈≈≈≈ ╱   Clase V
           ╲ 🌊🌊🌊 ╱
            ╲ ≈≈≈≈ ╱
             ╲ 🌊🌊 ╱
              ╲ ≈≈ ╱
               ╲ 🌊 ╱
                ╲__╱
    
    Caudal: 500 m³/s 🌊
    Dificultad: Experto 🏆
    """
    print(rafting)
    print("Navegando rápidos torrenciales en equipo 🌊")

def dibujar_base_jumping():
    print("\n🦅 BASE JUMPING")
    print("-" * 30)
    base_jumping = """
    🏔️ ACANTILADO 800m 🏔️
    ████████████████████
    ██                ██
    ██  🦅 BASE       ██ ← Saltador
    ██   ╱│╲         ██   saliendo
    ██  ╱ │ ╲        ██
    ██    │          ██
    ██    │ ⏱️ 3s     ██ ← Cuenta
    ██    │          ██   regresiva
    ██    │          ██
    ██    🪂         ██ ← Paracaídas
    ██   ╱│╲         ██   abierto
    ██  ╱ │ ╲        ██
    ██    │          ██
    ██████████████████
    
    B.A.S.E: Building, Antenna 🏢
            Span, Earth 🌍
    
    Tiempo de caída: 15 segundos ⚡
    """
    print(base_jumping)
    print("Salto desde acantilados con paracaídas extremo 🪂")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (0-9): ").strip()
        
        if opcion == "0":
            print("\n¡Gracias por explorar los deportes extremos! 🏂")
            break
        elif opcion == "1":
            dibujar_paracaidismo()
        elif opcion == "2":
            dibujar_alpinismo()
        elif opcion == "3":
            dibujar_surf()
        elif opcion == "4":
            dibujar_parapente()
        elif opcion == "5":
            dibujar_escalada_roca()
        elif opcion == "6":
            dibujar_snowboard()
        elif opcion == "7":
            dibujar_bungee_jumping()
        elif opcion == "8":
            dibujar_rafting()
        elif opcion == "9":
            dibujar_base_jumping()
        else:
            print("\n❌ Opción no válida. Por favor, selecciona un número del 0 al 9.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
