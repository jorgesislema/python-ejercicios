#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 80: Jardines Zen ASCII
===============================

Objetivo:
- Crear representaciones ASCII de jardines zen japoneses
- Implementar elementos de meditación y tranquilidad
- Mostrar la filosofía oriental en arte ASCII

Conceptos aplicados:
- Representación de espacios meditativos
- Filosofía zen y minimalismo
- Jardines paisajísticos japoneses
"""

def mostrar_menu():
    """Muestra el menú de opciones disponibles"""
    print("\n" + "="*50)
    print("🧘 GENERADOR DE JARDINES ZEN ASCII 🧘")
    print("="*50)
    print("1. Jardín de Rocas")
    print("2. Estanque Koi")
    print("3. Bambú")
    print("4. Puente de Madera")
    print("5. Pagoda")
    print("6. Círculo Zen")
    print("7. Sendero de Piedras")
    print("8. Cascada")
    print("9. Jardín Completo")
    print("0. Salir")
    print("-"*50)

def jardin_rocas():
    """Jardín seco de rocas (karesansui)"""
    print("🪨 JARDÍN DE ROCAS 🪨")
    print()
    print("Karesansui - El arte de la contemplación")
    print()
    
    jardin_ascii = [
        "    🪨 JARDÍN DE ROCAS 🪨   ",
        "",
        "┌─────────────────────────────┐",
        "│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░ │",
        "│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░ │",
        "│ ░░░░●●●░░░░░░░░░●●░░░░░░░░░ │",
        "│ ░░░●●●●●░░░░░░░●●●●░░░░░░░░ │",
        "│ ░░░░●●●░░░░░░░░●●●░░░░░░░░░ │",
        "│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░ │",
        "│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░ │",
        "│ ░░░░░░░░●●●●●░░░░░░░░░░░░░░ │",
        "│ ░░░░░░●●●●●●●●░░░░░░░░░░░░░ │",
        "│ ░░░░░░░●●●●●●░░░░░░░░░░░░░░ │",
        "│ ░░░░░░░░●●●░░░░░░░░░░░░░░░░ │",
        "│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░ │",
        "│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░ │",
        "└─────────────────────────────┘",
        "",
        "🪨 Rocas representan montañas",
        "🌊 Arena rastrillada simboliza agua",
        "🧘 Espacio para meditación"
    ]
    
    for linea in jardin_ascii:
        print(linea)

def estanque_koi():
    """Estanque con peces koi"""
    print("🐟 ESTANQUE KOI 🐟")
    print()
    print("Armonía acuática y movimiento sereno")
    print()
    
    estanque_ascii = [
        "     🐟 ESTANQUE KOI 🐟     ",
        "",
        "       🌸           🌸     ",
        "         ╲         ╱       ",
        "    ╭─────╲───────╱─────╮  ",
        "   ╱       ╲     ╱       ╲ ",
        "  ╱         ╲   ╱         ╲",
        " ╱           ╲ ╱           ╲",
        "│    🐠        ●        🐟 │",
        "│  ~~   ~~  ~~   ~~  ~~   │",
        "│ ~  🐟   ~    ~   🐠  ~  │",
        "│~     ~  ~  ●  ~  ~     ~│",
        "│  ~  ~    🐟    ~  ~  ~  │",
        "│ ~    ~  ~    ~  ~    ~  │",
        "│~  🐠  ~  ~  ~  ~  🐟  ~│",
        " ╲  ~    ~  ●  ~    ~   ╱ ",
        "  ╲  ~  ~    ~  ~  ~   ╱  ",
        "   ╲_________________╱   ",
        "      🪨   🪨   🪨       ",
        "",
        "🐟 Koi dorados y rojos",
        "🪨 Piedras naturales",
        "🌸 Flores de loto",
        "💧 Agua cristalina"
    ]
    
    for linea in estanque_ascii:
        print(linea)

def bambu():
    """Bosquecillo de bambú"""
    print("🎋 BAMBÚ 🎋")
    print()
    print("Flexibilidad y resistencia natural")
    print()
    
    bambu_ascii = [
        "       🎋 BAMBÚ 🎋         ",
        "",
        "  ┃   ┃     ┃    ┃   ┃    ",
        "  ┃   ┃  🍃 ┃    ┃   ┃    ",
        "  ┃   ┃     ┃ 🍃 ┃   ┃    ",
        "  ┃🍃 ┃     ┃    ┃   ┃ 🍃 ",
        "  ┃   ┃     ┃    ┃🍃 ┃    ",
        "  ┃   ┃  🍃 ┃    ┃   ┃    ",
        "  ┃   ┃     ┃    ┃   ┃    ",
        "  ╬   ╬     ╬    ╬   ╬    ",
        "  ┃   ┃  🍃 ┃    ┃   ┃    ",
        "  ┃   ┃     ┃ 🍃 ┃   ┃    ",
        "  ┃🍃 ┃     ┃    ┃   ┃ 🍃 ",
        "  ┃   ┃     ┃    ┃🍃 ┃    ",
        "  ┃   ┃  🍃 ┃    ┃   ┃    ",
        "  ┃   ┃     ┃    ┃   ┃    ",
        "  ╬   ╬     ╬    ╬   ╬    ",
        "  ┃   ┃     ┃    ┃   ┃    ",
        "  ┃   ┃  🍃 ┃ 🍃 ┃   ┃    ",
        "  ┃🍃 ┃     ┃    ┃   ┃ 🍃 ",
        "░░░░░░░░░░░░░░░░░░░░░░░░░░  ",
        "",
        "🎋 Bambusa japonica",
        "🍃 Hojas que susurran",
        "🌬️ Sonido meditativo del viento"
    ]
    
    for linea in bambu_ascii:
        print(linea)

def puente_madera():
    """Puente tradicional japonés"""
    print("🌉 PUENTE DE MADERA 🌉")
    print()
    print("Conexión entre mundos espirituales")
    print()
    
    puente_ascii = [
        "    🌉 PUENTE DE MADERA 🌉  ",
        "",
        "  🌸                   🌸  ",
        "    ╲                 ╱    ",
        "     ╲               ╱     ",
        "      ╲             ╱      ",
        "       ╲___________╱       ",
        "       ┃┃┃┃┃┃┃┃┃┃┃       ",
        "      ╱ ┃┃┃┃┃┃┃┃┃ ╲      ",
        "     ╱  ┃┃┃┃┃┃┃┃┃  ╲     ",
        "    ╱   ┃┃┃┃┃┃┃┃┃   ╲    ",
        "   ╱    ┃┃┃┃┃┃┃┃┃    ╲   ",
        "  ╱     ┃┃┃┃┃┃┃┃┃     ╲  ",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~ ",
        "~  🐟  ~    ~    ~  🐠  ~ ",
        "~    ~   🐟   🐟   ~    ~ ",
        "~  ~    ~    ~    ~    ~  ~",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "",
        "🌉 Puente arqueado tradicional",
        "🌸 Cerezos en flor (sakura)",
        "🐟 Peces koi nadando debajo"
    ]
    
    for linea in puente_ascii:
        print(linea)

def pagoda():
    """Pagoda de cinco pisos"""
    print("🏯 PAGODA 🏯")
    print()
    print("Torre espiritual de múltiples niveles")
    print()
    
    pagoda_ascii = [
        "        🏯 PAGODA 🏯        ",
        "",
        "            ╱╲             ",
        "           ╱  ╲            ",
        "          ╱____╲           ",
        "         ╱      ╲          ",
        "        ╱________╲         ",
        "       ╱          ╲        ",
        "      ╱____________╲       ",
        "     ╱              ╲      ",
        "    ╱________________╲     ",
        "   ╱                  ╲    ",
        "  ╱____________________╲   ",
        "  │                    │   ",
        "  │        🔔          │   ",
        "  │      ╱────╲        │   ",
        "  │     ╱      ╲       │   ",
        "  │    ╱________╲      │   ",
        "  │   ╱          ╲     │   ",
        "  │  ╱____________╲    │   ",
        "  │ ╱              ╲   │   ",
        "  │╱________________╲  │   ",
        "  └────────────────────┘   ",
        "",
        "🏯 5 pisos representan elementos",
        "🔔 Campana del viento",
        "🧘 Centro de meditación"
    ]
    
    for linea in pagoda_ascii:
        print(linea)

def circulo_zen():
    """Ensō - círculo zen de la iluminación"""
    print("⚪ CÍRCULO ZEN ⚪")
    print()
    print("Ensō - Símbolo de la iluminación")
    print()
    
    circulo_ascii = [
        "      ⚪ CÍRCULO ZEN ⚪      ",
        "",
        "                           ",
        "         ╭─────╮           ",
        "       ╱         ╲         ",
        "      ╱           ╲        ",
        "     ╱             ╲       ",
        "    ╱               ╲      ",
        "   ╱                 ╲     ",
        "  │                   │    ",
        "  │        🧘          │    ",
        "  │                   │    ",
        "   ╲                 ╱     ",
        "    ╲               ╱      ",
        "     ╲             ╱       ",
        "      ╲           ╱        ",
        "       ╲         ╱         ",
        "         ╲     ╱           ",
        "           ╲ ╱             ",
        "                           ",
        "",
        "⚪ Ensō - círculo de la iluminación",
        "🧘 Meditación zen",
        "∞ Infinito y vacuidad",
        "🎨 Pincelada única e irrepetible"
    ]
    
    for linea in circulo_ascii:
        print(linea)

def sendero_piedras():
    """Sendero de piedras de paso"""
    print("🪨 SENDERO DE PIEDRAS 🪨")
    print()
    print("Camino hacia la contemplación")
    print()
    
    sendero_ascii = [
        "   🪨 SENDERO DE PIEDRAS 🪨 ",
        "",
        "🌿                       🌿",
        "  🌿     ●             🌿  ",
        "    🌿     ╲         🌿    ",
        "      🌿     ●     🌿      ",
        "        🌿     ╲ 🌿        ",
        "          🌿     ●         ",
        "            🌿 ╱ 🌿        ",
        "              ●           ",
        "            ╱   ╲         ",
        "          ●       ●       ",
        "        ╱           ╲     ",
        "      ●               ●   ",
        "    ╱                   ╲ ",
        "  ●                       ●",
        " ╱                         ╲",
        "●                           ●",
        "🌿                       🌿",
        "  🌿                   🌿  ",
        "    🌿               🌿    ",
        "      🌿           🌿      ",
        "        🌿       🌿        ",
        "          🌿   🌿          ",
        "            🌿🌿           ",
        "",
        "🪨 Piedras de río pulidas",
        "🌿 Musgo entre las piedras",
        "🚶 Caminata meditativa"
    ]
    
    for linea in sendero_ascii:
        print(linea)

def cascada():
    """Cascada serena con rocas"""
    print("💧 CASCADA 💧")
    print()
    print("Flujo eterno de la naturaleza")
    print()
    
    cascada_ascii = [
        "       💧 CASCADA 💧       ",
        "",
        "      🌸           🌸      ",
        "        ╲         ╱        ",
        "         ╲  💧  ╱         ",
        "          ╲ ┃ ╱          ",
        "           ╲┃╱           ",
        "            ┃            ",
        "            ┃💧          ",
        "            ┃            ",
        "            ┃            ",
        "          💧┃            ",
        "            ┃💧          ",
        "       🪨   ┃   🪨       ",
        "         ╲  ┃  ╱         ",
        "          ╲ ┃ ╱          ",
        "           ╲┃╱           ",
        "      🪨    ●    🪨      ",
        "         ╲  ~  ╱         ",
        "          ╲~~~╱          ",
        "       ~~~~●●●~~~~       ",
        "     ~~~~~~~~~~~~~~~     ",
        "   ~~~~~~~~~~~~~~~~~   ",
        "",
        "💧 Agua pura de montaña",
        "🪨 Rocas naturales",
        "🌸 Flores silvestres",
        "🎵 Sonido relajante"
    ]
    
    for linea in cascada_ascii:
        print(linea)

def jardin_completo():
    """Jardín zen completo con todos los elementos"""
    print("🏮 JARDÍN ZEN COMPLETO 🏮")
    print()
    print("Santuario de paz y armonía")
    print()
    
    jardin_ascii = [
        "    🏮 JARDÍN ZEN COMPLETO 🏮",
        "",
        "🌸    🏯         🎋  🎋    🌸",
        "  ╲  ╱│╲       ┃  ┃ ┃  ╱  ",
        "   ╲╱ │ ╲      ┃🍃┃ ┃ ╱   ",
        "    ●  │  ╲     ┃  ┃ ┃╱    ",
        "   ╱ ╲ │   ╲    ┃  ┃ ┃     ",
        "  ╱   ╲│    ╲   ┃  ┃ ┃     ",
        " ╱     ●     ╲  ┃  ┃ ┃     ",
        "~~~~~~~~~~~~~~~~~┃~~┃~┃~~~~~",
        "~  🐟  ~    ~    ┃  ┃ ┃   ~",
        "~    ~   🐟   🐟 ┃  ┃ ┃ ~  ",
        "~  ~    ~    ~   ┃  ┃ ┃  ~ ",
        "~~~~~~~~~~~~~~~~~~┃~┃~┃~~~~~",
        "░░░░●●●░░░░░░░░░░░┃░┃░┃░░░░░",
        "░░●●●●●░░░░░░░░░░░┃░┃░┃░░░░░",
        "░░░●●●░░░░●●●●●░░░┃░┃░┃░░░░░",
        "░░░░░░░░●●●●●●●●░░┃░┃░┃░░░░░",
        "░░░░░░░░░●●●●●░░░░┃░┃░┃░░░░░",
        "░░░░░░░░░░●●●░░░░░░░░░░░░░░░",
        "                            ",
        "    🧘    ⚪    🪨    🔔   ",
        "",
        "🏯 Pagoda central",
        "🎋 Bosque de bambú",
        "🐟 Estanque koi",
        "🪨 Jardín de rocas",
        "🧘 Área de meditación"
    ]
    
    for linea in jardin_ascii:
        print(linea)

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Selecciona una opción (0-9): ").strip()
            
            if opcion == '0':
                print("\n🧘 Que encuentres paz interior y armonía 🧘")
                break
            elif opcion == '1':
                jardin_rocas()
            elif opcion == '2':
                estanque_koi()
            elif opcion == '3':
                bambu()
            elif opcion == '4':
                puente_madera()
            elif opcion == '5':
                pagoda()
            elif opcion == '6':
                circulo_zen()
            elif opcion == '7':
                sendero_piedras()
            elif opcion == '8':
                cascada()
            elif opcion == '9':
                jardin_completo()
            else:
                print("❌ Opción no válida. Por favor, elige una opción del 0 al 9.")
                
        except ValueError:
            print("❌ Por favor, introduce un número válido.")
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego! 🧘")
            break
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
