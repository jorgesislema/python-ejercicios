#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 78: Vehículos del Futuro ASCII
=======================================

Objetivo:
- Crear representaciones ASCII de vehículos futuristas
- Implementar tecnologías de transporte avanzadas
- Mostrar la visión del futuro del transporte

Conceptos aplicados:
- Representación de tecnología futurista
- Vehículos autónomos y eléctricos
- Innovación en transporte
"""

def mostrar_menu():
    """Muestra el menú de opciones disponibles"""
    print("\n" + "="*50)
    print("🚗 GENERADOR DE VEHÍCULOS DEL FUTURO ASCII 🚗")
    print("="*50)
    print("1. Auto Eléctrico")
    print("2. Drone de Pasajeros")
    print("3. Hyperloop")
    print("4. Moto Voladora")
    print("5. Submarino Personal")
    print("6. Robot de Entrega")
    print("7. Tren Magnético")
    print("8. Coche Autónomo")
    print("9. Taxi Aéreo")
    print("0. Salir")
    print("-"*50)

def auto_electrico():
    """Auto eléctrico futurista"""
    print("⚡ AUTO ELÉCTRICO ⚡")
    print()
    print("Movilidad sostenible sin emisiones")
    print()
    
    auto_ascii = [
        "     ⚡ AUTO ELÉCTRICO ⚡     ",
        "",
        "          ╭─────────────╮     ",
        "         ╱               ╲    ",
        "        ╱    TESLA MODEL  ╲   ",
        "       ╱      X PLAID      ╲  ",
        "      ╱                     ╲ ",
        "     │  ◊◊   ◊◊◊◊◊◊◊   ◊◊  │",
        "     │      ╭─────────╮      │",
        "     │     ╱  ● AUTO ●  ╲     │",
        "     │    ╱   PILOT     ╲    │",
        "     │   ╱      ⚡       ╲   │",
        "     │  ╱_________________╲  │",
        "     ╲                     ╱ ",
        "      ╲___________________╱  ",
        "        ●               ●   ",
        "       ╱ ╲             ╱ ╲  ",
        "      ╱   ╲           ╱   ╲ ",
        "     ╱_____╲_________╱_____╲",
        "",
        "⚡ Batería: 100 kWh",
        "🔋 Autonomía: 600 km",
        "🚗 Autopilot nivel 5",
        "🌱 0% emisiones CO₂",
        "⚡ Carga rápida: 15 min"
    ]
    
    for linea in auto_ascii:
        print(linea)

def drone_pasajeros():
    """Drone para transporte de personas"""
    print("🚁 DRONE DE PASAJEROS 🚁")
    print()
    print("Taxi aéreo del futuro")
    print()
    
    drone_ascii = [
        "    🚁 DRONE DE PASAJEROS 🚁  ",
        "",
        "  ●─────●           ●─────●   ",
        "  │  ↻  │           │  ↻  │   ",
        "  │ ╭─╮ │           │ ╭─╮ │   ",
        "  │ │ │ │           │ │ │ │   ",
        "  │ ╰─╯ │           │ ╰─╯ │   ",
        "  └─┬─┬─┘           └─┬─┬─┘   ",
        "    │ │               │ │     ",
        "    │ ╰─┬─────────┬─╯ │     ",
        "    │   │ ■ ■ ■ ■ │   │     ",
        "    │   │ ▲ TAXI ▲ │   │     ",
        "    │   │  AÉREO   │   │     ",
        "    │   │ 👤 👤 👤 │   │     ",
        "    │   │ ▼ ▼ ▼ ▼ │   │     ",
        "    │ ╭─┴─────────┴─╮ │     ",
        "    │ │             │ │     ",
        "  ┌─┴─┴─┐         ┌─┴─┴─┐   ",
        "  │  ↻  │         │  ↻  │   ",
        "  │ ╭─╮ │         │ ╭─╮ │   ",
        "  │ │ │ │         │ │ │ │   ",
        "  │ ╰─╯ │         │ ╰─╯ │   ",
        "  ●─────●         ●─────●   ",
        "",
        "🚁 4 hélices eléctricas",
        "👥 Capacidad: 4 pasajeros",
        "🔋 Autonomía: 100 km",
        "📱 Control por app",
        "🌆 Vuelos urbanos"
    ]
    
    for linea in drone_ascii:
        print(linea)

def hyperloop():
    """Sistema Hyperloop de alta velocidad"""
    print("🚅 HYPERLOOP 🚅")
    print()
    print("Transporte supersónico en tubo de vacío")
    print()
    
    hyperloop_ascii = [
        "      🚅 HYPERLOOP 🚅       ",
        "",
        "  ════════════════════════════",
        " ╱                           ╲",
        "│    ┌─────────────────────┐  │",
        "│    │  ╭─────────────╮   │  │",
        "│    │ ╱  HYPERLOOP   ╲  │  │",
        "│    ││    1200 KM/H   │ │  │",
        "│    ││  ●●●●●●●●●●●●  │ │  │",
        "│    ││  👤👤👤👤👤👤  │ │  │",
        "│    │ ╲_______________╱  │  │",
        "│    └─────────────────────┘  │",
        " ╲           ≋≋≋≋≋≋≋≋≋≋      ╱",
        "  ════════════════════════════",
        "",
        "    ╭─────────────────────╮   ",
        "   ╱  ESTACIÓN HYPERLOOP  ╲  ",
        "  ╱                       ╲ ",
        " │  🚪 ← → ← → ← → ← → 🚪 │",
        " │   👤👤👤    👤👤👤   │",
        " │                         │",
        "  ╲_______________________╱ ",
        "",
        "🚅 Velocidad: 1200 km/h",
        "⚡ Levitación magnética",
        "🌌 Vacío parcial",
        "🌍 Madrid-París: 50 min"
    ]
    
    for linea in hyperloop_ascii:
        print(linea)

def moto_voladora():
    """Motocicleta voladora futurista"""
    print("🏍️ MOTO VOLADORA 🏍️")
    print()
    print("Libertad en tres dimensiones")
    print()
    
    moto_ascii = [
        "    🏍️ MOTO VOLADORA 🏍️     ",
        "",
        "         ↻     ↻            ",
        "        ╱ ╲   ╱ ╲           ",
        "       ╱   ╲ ╱   ╲          ",
        "      ╱  ●  ╲╱  ●  ╲         ",
        "     ╱       ●       ╲       ",
        "    ╱                 ╲      ",
        "   ●───┬─────────────┬───●   ",
        "       │    👤       │       ",
        "       │   ╱│╲       │       ",
        "       │  ╱ │ ╲      │       ",
        "  ●────┴─╱  │  ╲─────┴────●  ",
        " ╱      ╱   │   ╲         ╲ ",
        "╱  ●───╱    │    ╲───●    ╲",
        "│     ╱     │     ╲       │",
        "╲    ╱      │      ╲      ╱",
        " ╲  ╱       │       ╲    ╱ ",
        "  ╲╱        │        ╲  ╱  ",
        "   ●         │         ●   ",
        "            ↻ ↻            ",
        "",
        "🏍️ Turbinas de plasma",
        "⚡ Propulsión eléctrica",
        "🎮 Control neural",
        "🌆 Vuelo urbano seguro"
    ]
    
    for linea in moto_ascii:
        print(linea)

def submarino_personal():
    """Submarino personal compacto"""
    print("🚤 SUBMARINO PERSONAL 🚤")
    print()
    print("Exploración submarina individual")
    print()
    
    submarino_ascii = [
        "   🚤 SUBMARINO PERSONAL 🚤  ",
        "",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "~~   ╭─────────────────╮   ~~",
        "~~  ╱  ◐ PERISCOPE ◑   ╲  ~~",
        "~~ ╱                     ╲ ~~",
        "~~│    ◊◊◊◊◊◊◊◊◊◊◊◊    │~~",
        "~~│   ╭───────────────╮   │~~",
        "~~│  ╱  👤 EXPLORER   ╲  │~~",
        "~~│ ╱                  ╲ │~~",
        "~~│╱      🌊 SUB 🌊     ╲│~~",
        "~~│     ●●●●●●●●●●●     │~~",
        "~~│ ╲    BALLAST TANK   ╱ │~~",
        "~~│  ╲                ╱  │~~",
        "~~│   ╲______________╱   │~~",
        "~~│       ● ● ● ●       │~~",
        "~~ ╲     PROPELLERS     ╱ ~~",
        "~~  ╲___________________╱  ~~",
        "~~     )))        (((      ~~",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "🐠  🐠  🐠  🐠  🐠  🐠  🐠 ",
        "",
        "🚤 Profundidad máx: 200m",
        "🔋 Autonomía: 8 horas",
        "🌊 Exploración marina",
        "🐠 Observación fauna"
    ]
    
    for linea in submarino_ascii:
        print(linea)

def robot_entrega():
    """Robot autónomo de entrega"""
    print("🤖 ROBOT DE ENTREGA 🤖")
    print()
    print("Logística automatizada del futuro")
    print()
    
    robot_ascii = [
        "   🤖 ROBOT DE ENTREGA 🤖   ",
        "",
        "       ┌─────────────┐      ",
        "       │ ● DELIVERY ● │      ",
        "       │      BOT     │      ",
        "       └─┬─────────┬─┘      ",
        "         │    📦   │        ",
        "    ┌────┴─────────┴────┐   ",
        "    │  📦 📦 📦 📦 📦  │   ",
        "    │                   │   ",
        "    │ ┌─┐  STATUS: ✅  │   ",
        "    │ │●│  ROUTE: 15KM  │   ",
        "    │ └─┘  ETA: 12 MIN  │   ",
        "    │                   │   ",
        "    │  📦 📦 📦 📦 📦  │   ",
        "    └─┬─────────────┬─┘   ",
        "      │ ● ● ● ● ● ● │      ",
        "     ╱│             │╲     ",
        "    ╱ │  LIDAR 360° │ ╲    ",
        "   ╱  └─────────────┘  ╲   ",
        "  ●     ●         ●     ●  ",
        " ╱ ╲   ╱ ╲       ╱ ╲   ╱ ╲ ",
        "╱___╲ ╱___╲     ╱___╲ ╱___╲",
        "",
        "🤖 IA navegación autónoma",
        "📦 Capacidad: 50 kg",
        "🔋 Autonomía: 100 km",
        "📍 GPS + LIDAR precisión"
    ]
    
    for linea in robot_ascii:
        print(linea)

def tren_magnetico():
    """Tren de levitación magnética"""
    print("🚄 TREN MAGNÉTICO 🚄")
    print()
    print("Levitación sin fricción")
    print()
    
    tren_ascii = [
        "     🚄 TREN MAGNÉTICO 🚄    ",
        "",
        "   ╭─────────────────────────╮",
        "  ╱    MAGLEV EXPRESS        ╲",
        " ╱       500 KM/H             ╲",
        "│  ◊◊◊ ◊◊◊ ◊◊◊ ◊◊◊ ◊◊◊     │",
        "│                             │",
        "│ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐  │",
        "│ │👤│ │👤│ │👤│ │👤│ │👤│ │🍴│  │",
        "│ └─┘ └─┘ └─┘ └─┘ └─┘ └─┘  │",
        "│                             │",
        "│  ◊◊◊ ◊◊◊ ◊◊◊ ◊◊◊ ◊◊◊     │",
        " ╲_____________________________╱",
        "  ╲___________________________╱ ",
        "         ≋≋≋≋≋≋≋≋≋≋≋        ",
        "    ●●●●●●●●●●●●●●●●●●●      ",
        "   ╱                     ╲    ",
        "  ╱  ELECTROMAGNETIC RAIL ╲   ",
        " ╱_________________________╲  ",
        "●●●●●●●●●●●●●●●●●●●●●●●●●●●",
        "",
        "🚄 Levitación electromagnética",
        "⚡ Sin fricción, sin ruido",
        "🌍 Japón, China, Alemania",
        "⚡ Velocidad récord: 603 km/h"
    ]
    
    for linea in tren_ascii:
        print(linea)

def coche_autonomo():
    """Vehículo totalmente autónomo"""
    print("🚙 COCHE AUTÓNOMO 🚙")
    print()
    print("Conducción sin piloto humano")
    print()
    
    coche_ascii = [
        "    🚙 COCHE AUTÓNOMO 🚙     ",
        "",
        "    ┌─────────────────────┐   ",
        "   ╱  ● AUTONOMOUS DRIVE  ╲  ",
        "  ╱                       ╲ ",
        " ╱     ┌─────────────┐     ╲",
        "│      │ ┌─────────┐ │      │",
        "│      │ │ READING │ │      │",
        "│  🔍  │ │  📱📰💻  │ │  🔍  │",
        "│      │ │         │ │      │",
        "│      │ │ NO      │ │      │",
        "│      │ │ DRIVER  │ │      │",
        "│      │ └─────────┘ │      │",
        "│      └─────────────┘      │",
        " ╲                         ╱",
        "  ╲_______________________╱ ",
        "    ●                   ●   ",
        "   ╱ ╲                 ╱ ╲  ",
        "  ╱   ╲_______________╱   ╲ ",
        " ╱_______________________╲",
        "",
        "    ◦◦◦ SENSORES ◦◦◦       ",
        "  📷 8 cámaras 360°        ",
        "  📡 12 sensores ultrasónicos",
        "  🔍 1 radar frontal        ",
        "  ⚡ 1 LIDAR láser          ",
        "",
        "🤖 IA nivel 5 autonomía",
        "📡 5G conectividad",
        "⚡ 100% eléctrico"
    ]
    
    for linea in coche_ascii:
        print(linea)

def taxi_aereo():
    """Taxi volador urbano"""
    print("🚁 TAXI AÉREO 🚁")
    print()
    print("Movilidad aérea urbana")
    print()
    
    taxi_ascii = [
        "      🚁 TAXI AÉREO 🚁      ",
        "",
        "   ↻───↻         ↻───↻     ",
        "  ╱ ● ● ╲       ╱ ● ● ╲    ",
        " ╱   ●   ╲     ╱   ●   ╲   ",
        "●    ●    ●   ●    ●    ●  ",
        " ╲   ●   ╱     ╲   ●   ╱   ",
        "  ╲ ● ● ╱       ╲ ● ● ╱    ",
        "   ●───●         ●───●     ",
        "     │             │       ",
        "  ┌──┴─────────────┴──┐    ",
        "  │  🚖 SKYBER TAXI  │    ",
        "  │                   │    ",
        "  │ ┌─┐ ┌─┐ ┌─┐ ┌─┐ │    ",
        "  │ │👤│ │👤│ │👤│ │👤│ │    ",
        "  │ └─┘ └─┘ └─┘ └─┘ │    ",
        "  │                   │    ",
        "  │  📱 APP CONTROL   │    ",
        "  └───────────────────┘    ",
        "     │             │       ",
        "   ●───●         ●───●     ",
        "  ╱ ● ● ╲       ╱ ● ● ╲    ",
        " ╱   ●   ╲     ╱   ●   ╲   ",
        "●    ●    ●   ●    ●    ●  ",
        " ╲   ●   ╱     ╲   ●   ╱   ",
        "  ╲ ● ● ╱       ╲ ● ● ╱    ",
        "   ↻───↻         ↻───↻     ",
        "",
        "🚁 8 rotores eléctricos",
        "👥 Capacidad: 4 pasajeros",
        "📱 Reserva por app",
        "🌆 Rutas aéreas urbanas"
    ]
    
    for linea in taxi_ascii:
        print(linea)

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Selecciona una opción (0-9): ").strip()
            
            if opcion == '0':
                print("\n¡Bienvenido al futuro del transporte! 🚀")
                break
            elif opcion == '1':
                auto_electrico()
            elif opcion == '2':
                drone_pasajeros()
            elif opcion == '3':
                hyperloop()
            elif opcion == '4':
                moto_voladora()
            elif opcion == '5':
                submarino_personal()
            elif opcion == '6':
                robot_entrega()
            elif opcion == '7':
                tren_magnetico()
            elif opcion == '8':
                coche_autonomo()
            elif opcion == '9':
                taxi_aereo()
            else:
                print("❌ Opción no válida. Por favor, elige una opción del 0 al 9.")
                
        except ValueError:
            print("❌ Por favor, introduce un número válido.")
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego! 🚗")
            break
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
