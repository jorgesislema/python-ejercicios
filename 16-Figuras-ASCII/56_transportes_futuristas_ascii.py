"""
EJERCICIO 56: Medios de Transporte Futuristas ASCII

Objetivo:
- Crear figuras ASCII de vehículos y transportes futuristas
- Practicar el diseño de formas tecnológicas avanzadas
- Explorar conceptos de ciencia ficción y tecnología

Conceptos a practicar:
- Representación de diseños futuristas
- Uso de caracteres para simular tecnología avanzada
- Creación de efectos de movimiento y energía
- Diseño de interfaces de ciencia ficción
"""

def mostrar_menu():
    print("\n" + "="*50)
    print("🚀 TRANSPORTES FUTURISTAS ASCII 🚀")
    print("="*50)
    print("0. Salir")
    print("1. Nave espacial 🛸")
    print("2. Auto volador 🚗")
    print("3. Teletransportador ⚡")
    print("4. Hoverboard 🛹")
    print("5. Tubo de transporte 🚇")
    print("6. Moto flotante 🏍️")
    print("7. Portal dimensional 🌀")
    print("8. Drone personal 🚁")
    print("9. Estación espacial 🛰️")
    print("="*50)

def dibujar_nave_espacial():
    print("\n🛸 NAVE ESPACIAL")
    print("-" * 30)
    nave = """
         ✨ ⭐ ✨ ⭐ ✨
           ╭─────────╮
          ╱ ◉ ◉ ◉ ◉ ╲
         ╱ ◈ ╔═════╗ ◈ ╲
        ╱  ◉ ║ ⚡⚡⚡ ║ ◉  ╲
       ╱ ◈ ◉ ║ ███ ║ ◉ ◈ ╲
      ╱_____╚═══════╝_____╲
     ╔═══════════════════════╗
     ║ ⚡ ○ ● ◐ ◑ ◒ ◓ ◔ ⚡ ║
     ╚═══════════════════════╝
       ╲ ~~~ ~~~ ~~~ ~~~ ╱
        ╲ 💫 💫 💫 💫 ╱
         ╲ ~~~ ~~~ ~~~ ╱
          ╲___________╱
            ⚡ ⚡ ⚡
    """
    print(nave)
    print("Vehículo intergaláctico para explorar el cosmos 🌌")

def dibujar_auto_volador():
    print("\n🚗 AUTO VOLADOR")
    print("-" * 30)
    auto = """
      ~~~> 💨 ~~~> 💨 ~~~>
    
    ╔═══════════════════════╗
    ║ ◉ ◉           ◉ ◉    ║
    ║                      ║
    ║  👤     🎛️     👤   ║
    ╠══════════════════════╣
    ║ ⚡ ▲ ▲ ▲ ▲ ▲ ▲ ⚡   ║
    ╚═══════════════════════╝
       ╲               ╱
        ╲ ○ ○ ○ ○ ○ ╱
         ╲___________╱
            💨 💨 💨
         ┊ ┊ ┊ ┊ ┊ ┊
         ▽ ▽ ▽ ▽ ▽ ▽
    """
    print(auto)
    print("Automóvil con capacidad de vuelo antigravitatorio 🌅")

def dibujar_teletransportador():
    print("\n⚡ TELETRANSPORTADOR")
    print("-" * 30)
    teletransportador = """
    ╔═══════════╗     ╔═══════════╗
    ║ ⚡⚡⚡⚡⚡ ║     ║ ⚡⚡⚡⚡⚡ ║
    ║ ○ ○ ○ ○ ○ ║     ║ ○ ○ ○ ○ ○ ║
    ║           ║     ║           ║
    ║     👤    ║ ~~> ║           ║
    ║           ║     ║     👤    ║
    ║ ● ● ● ● ● ║     ║ ● ● ● ● ● ║
    ║ ▲▲▲▲▲▲▲▲▲ ║     ║ ▲▲▲▲▲▲▲▲▲ ║
    ╚═══════════╝     ╚═══════════╝
     ✨✨✨✨✨        ✨✨✨✨✨
       ORIGEN          DESTINO
       
    [ACTIVANDO...] ⚡⚡⚡ [COMPLETO!]
    """
    print(teletransportador)
    print("Transporte instantáneo a través del espacio-tiempo ⏰")

def dibujar_hoverboard():
    print("\n🛹 HOVERBOARD")
    print("-" * 30)
    hoverboard = """
                 👤
                ╱│╲
               ╱ │ ╲
              ╱  │  ╲
    ╔════════════════════════╗
    ║ ⚡ ◉ ◉ ◉ ◉ ◉ ◉ ◉ ⚡ ║
    ║ ○ ● ○ ● ○ ● ○ ● ○ ● ○ ║
    ╚════════════════════════╝
           ┊ ┊ ┊ ┊ ┊
           ▽ ▽ ▽ ▽ ▽
           💨💨💨💨💨
        
    ~~~> ~~~> ~~~> ~~~> ~~~>
    
    [ALTITUD: 1.5m] [VELOCIDAD: 45 km/h]
    """
    print(hoverboard)
    print("Tabla flotante para transporte personal ágil 🏄")

def dibujar_tubo_transporte():
    print("\n🚇 TUBO DE TRANSPORTE")
    print("-" * 30)
    tubo = """
    ╔═════════════════════════════════╗
    ║ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ║
    ║                                 ║
    ║   👤👤👤   ~~~>   ○○○○○○○     ║
    ║                                 ║
    ║ ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ║
    ╚═════════════════════════════════╝
       ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊
       ▽ ▽ ▽ ▽ ▽ ▽ ▽ ▽ ▽ ▽ ▽ ▽ ▽
       
    ╔═════════════════════════════════╗
    ║ ESTACIÓN A ←→ ESTACIÓN B        ║
    ║ VELOCIDAD: 800 km/h             ║
    ║ TIEMPO: 3.5 minutos             ║
    ╚═════════════════════════════════╝
    """
    print(tubo)
    print("Sistema de transporte neumático ultrarrápido 💨")

def dibujar_moto_flotante():
    print("\n🏍️ MOTO FLOTANTE")
    print("-" * 30)
    moto = """
         👤
        ╱│╲
       ╱ │ ╲
    ╔═══════════════╗
    ║ ◉     ○ ○ ○   ║
    ║  ╰─╮ ╔═════╗  ║
    ║    │ ║ ⚡⚡⚡ ║  ║
    ║  ╭─╯ ╚═════╝  ║
    ║ ◉     ○ ○ ○   ║
    ╚═══════════════╝
        ┊ ┊ ┊ ┊
        ▽ ▽ ▽ ▽
        💨💨💨💨
    
    ~~~> ~~~> ~~~> ~~~>
    
    [MODO: FLOTACIÓN] [ENERGÍA: 87%]
    """
    print(moto)
    print("Motocicleta con tecnología de levitación magnética 🧲")

def dibujar_portal_dimensional():
    print("\n🌀 PORTAL DIMENSIONAL")
    print("-" * 30)
    portal = """
    ╔═══════════════════╗
    ║ ⚡⚡⚡⚡⚡⚡⚡⚡⚡ ║
    ║ ○ ◉ ◉ ◉ ◉ ◉ ○ ║
    ║ ◉ ░ ▓ ▓ ▓ ░ ◉ ║
    ║ ◉ ▓ 🌀🌌🌀 ▓ ◉ ║
    ║ ◉ ▓ 🌌⭐🌌 ▓ ◉ ║
    ║ ◉ ▓ 🌀🌌🌀 ▓ ◉ ║
    ║ ◉ ░ ▓ ▓ ▓ ░ ◉ ║
    ║ ○ ◉ ◉ ◉ ◉ ◉ ○ ║
    ║ ⚡⚡⚡⚡⚡⚡⚡⚡⚡ ║
    ╚═══════════════════╝
    
    ✨ DIMENSIÓN A ←→ DIMENSIÓN B ✨
     [CONEXIÓN ESTABLE] ⚡ [ACTIVO]
    """
    print(portal)
    print("Puerta entre realidades paralelas y universos alternos 🌌")

def dibujar_drone_personal():
    print("\n🚁 DRONE PERSONAL")
    print("-" * 30)
    drone = """
    ○──○           ○──○
     ╲ │           │ ╱
      ╲│           │╱
    ┌───┴───────────┴───┐
    │ ◉ ○ ○ ○ ○ ○ ○ ◉ │
    │                   │
    │       👤          │
    │                   │
    │ ● ● ● ● ● ● ● ● ● │
    └───┬───────────┬───┘
      ╱│           │╲
     ╱ │           │ ╲
    ○──○           ○──○
    
    ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊ ┊
    ▽ ▽ ▽ ▽ ▽ ▽ ▽ ▽ ▽
    """
    print(drone)
    print("Vehículo aéreo personal automatizado 🤖")

def dibujar_estacion_espacial():
    print("\n🛰️ ESTACIÓN ESPACIAL")
    print("-" * 30)
    estacion = """
      ✨ ⭐ ✨ ⭐ ✨ ⭐ ✨
    
    ═══○═══     ═══○═══
       │           │
    ╔══╧═══════════╧══╗
    ║ ◉ ○ ● ○ ● ○ ◉ ║
    ║                 ║
    ║  🚪  👤 👤  🚪  ║
    ║                 ║
    ║ ⚡ ○ ● ○ ● ○ ⚡ ║
    ╠═════════════════╣
    ║ 🛸   🛸   🛸   ║
    ╚══╤═══════════╤══╝
       │           │
    ═══○═══     ═══○═══
    
     [ROTACIÓN: 2.3 RPM]
     [GRAVEDAD: 0.8g]
    """
    print(estacion)
    print("Habitat orbital para viajes espaciales de larga distancia 🌍")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (0-9): ").strip()
        
        if opcion == "0":
            print("\n¡Gracias por explorar el futuro del transporte! 🚀")
            break
        elif opcion == "1":
            dibujar_nave_espacial()
        elif opcion == "2":
            dibujar_auto_volador()
        elif opcion == "3":
            dibujar_teletransportador()
        elif opcion == "4":
            dibujar_hoverboard()
        elif opcion == "5":
            dibujar_tubo_transporte()
        elif opcion == "6":
            dibujar_moto_flotante()
        elif opcion == "7":
            dibujar_portal_dimensional()
        elif opcion == "8":
            dibujar_drone_personal()
        elif opcion == "9":
            dibujar_estacion_espacial()
        else:
            print("\n❌ Opción no válida. Por favor, selecciona un número del 0 al 9.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
