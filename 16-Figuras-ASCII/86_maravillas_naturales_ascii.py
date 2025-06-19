#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 86: Maravillas Naturales ASCII
========================================

Objetivo:
- Crear representaciones de fenómenos y paisajes naturales únicos usando ASCII
- Explorar la diversidad geológica y natural del planeta
- Fomentar la conciencia ambiental y conservación

Conceptos aplicados:
- Geografía física
- Fenómenos naturales
- Conservación ambiental
- Patrimonio natural mundial
"""

import time
import random

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*60)
    print("🌍 GENERADOR DE MARAVILLAS NATURALES ASCII 🌍")
    print("="*60)
    print("1. 🌋 Volcán en erupción")
    print("2. 🌈 Aurora boreal")
    print("3. 🏔️ Cadena montañosa")
    print("4. 🌊 Géiser")
    print("5. 🏜️ Desierto con dunas")
    print("6. 🕳️ Gran cañón")
    print("7. 🏝️ Isla tropical")
    print("8. ❄️ Glaciar")
    print("9. 🌲 Bosque de secuoyas")
    print("0. 🚪 Salir")
    print("-"*60)

def volcan():
    """Crea un volcán en erupción"""
    print("🌋 VOLCÁN EN ERUPCIÓN 🌋")
    print("Poder ancestral de la Tierra en acción")
    print()
    
    volcan_ascii = [
        "                 🔥💥🔥",
        "               🔥💥🔥💥🔥",
        "             🔥💥🔥💥🔥💥🔥",
        "            🔥💥   |   💥🔥",
        "           🔥💥    |    💥🔥",
        "          🔥💥     |     💥🔥",
        "         🔥💥      |      💥🔥",
        "        🔥💥       |       💥🔥",
        "       🔥💥        |        💥🔥",
        "      🔥💥         |         💥🔥",
        "     🔥💥          |          💥🔥",
        "    🔥💥     ▲▲▲▲▲▲▲▲▲▲▲     💥🔥",
        "   🔥💥     ▲            ▲     💥🔥",
        "  🔥💥     ▲              ▲     💥🔥",
        " 🔥💥     ▲                ▲     💥🔥",
        "🔥💥     ▲                  ▲     💥🔥",
        "💥      ▲                    ▲      💥",
        "       ▲                      ▲",
        "      ▲________________________▲",
        "██████████████████████████████████████",
        "",
        "🌋 Temperatura lava: 1000-1200°C",
        "💨 Gases: vapor, SO2, CO2, cenizas",
        "⚠️ Radio peligroso: hasta 30 km"
    ]
    
    for linea in volcan_ascii:
        print(linea)

def aurora_boreal():
    """Crea una aurora boreal"""
    print("🌈 AURORA BOREAL 🌈")
    print("Danza de luces en el cielo polar")
    print()
    
    aurora_ascii = [
        "🟢    🟣       🟡     🔵       🟢",
        " 🟢🟣  🟡🔵  🟢🟣  🟡🔵  🟢🟣",
        "  🟡🔵🟢🟣🟡🔵🟢🟣🟡🔵🟢🟣",
        "   🟣🟢🟡🔵🟣🟢🟡🔵🟣🟢🟡",
        "    🔵🟣🟢🟡🔵🟣🟢🟡🔵🟣",
        "     🟡🔵🟣🟢🟡🔵🟣🟢🟡",
        "      🟢🟡🔵🟣🟢🟡🔵🟣",
        "       🟣🟢🟡🔵🟣🟢🟡",
        "        🔵🟣🟢🟡🔵🟣",
        "         🟡🔵🟣🟢🟡",
        "          🟢🟡🔵🟣",
        "           🟣🟢🟡",
        "            🔵🟣",
        "             🟡",
        "▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲",
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜",
        "",
        "🧲 Causa: partículas solares + campo magnético",
        "📍 Ubicación: círculo polar ártico",
        "🎨 Colores: verde, azul, rojo, violeta"
    ]
    
    for linea in aurora_ascii:
        print(linea)

def cadena_montanosa():
    """Crea una majestuosa cadena montañosa"""
    print("🏔️ CADENA MONTAÑOSA 🏔️")
    print("Columna vertebral de la Tierra")
    print()
    
    montanas_ascii = [
        "          ☁️        ☁️           ☁️",
        "        ❄️▲❄️      ❄️▲❄️       ❄️▲❄️",
        "       ❄️▲▲▲❄️    ❄️▲▲▲❄️     ❄️▲▲▲❄️",
        "      ❄️▲▲▲▲▲❄️  ❄️▲▲▲▲▲❄️   ❄️▲▲▲▲▲❄️",
        "     ❄️▲▲▲▲▲▲▲❄️❄️▲▲▲▲▲▲▲❄️ ❄️▲▲▲▲▲▲▲❄️",
        "    🟫▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲🟫",
        "   🟫🟫▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲🟫🟫",
        "  🟫🟫🟫▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲🟫🟫🟫",
        " 🟫🟫🟫🟫▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲🟫🟫🟫🟫",
        "🟫🟫🟫🟫🟫▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲🟫🟫🟫🟫🟫",
        "🌲🌲🌲🌲🌲🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🌲🌲🌲🌲🌲",
        "🌲🌲🌲🌲🌲🌲🟫🟫🟫🟫🟫🟫🟫🟫🟫🌲🌲🌲🌲🌲🌲",
        "🌲🌲🌲🌲🌲🌲🌲🟫🟫🟫🟫🟫🟫🟫🌲🌲🌲🌲🌲🌲🌲",
        "🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿",
        "",
        "🏔️ Picos más altos: Himalaya, Andes, Alpes",
        "❄️ Línea de nieve: 3000-5000m altitud",
        "🌡️ Temperatura baja: -6.5°C cada 1000m"
    ]
    
    for linea in montanas_ascii:
        print(linea)

def geiser():
    """Crea un géiser en erupción"""
    print("🌊 GÉISER 🌊")
    print("Fuente termal que desafía la gravedad")
    print()
    
    geiser_ascii = [
        "               💧💧💧",
        "              💧💧💧💧💧",
        "             💧💧💧💧💧💧💧",
        "            💧💧💧💧💧💧💧💧💧",
        "           💧💧💧💧💧💧💧💧💧💧💧",
        "          💧💧💧💧💧💧💧💧💧💧💧💧💧",
        "         💧💧💧💧💧💧💧💧💧💧💧💧💧💧💧",
        "        💧💧💧        |        💧💧💧",
        "       💧💧💧         |         💧💧💧",
        "      💧💧💧          |          💧💧💧",
        "     💧💧💧           |           💧💧💧",
        "    💧💧💧            |            💧💧💧",
        "   💧💧💧             |             💧💧💧",
        "  💧💧💧              |              💧💧💧",
        " 💧💧💧          ████████████          💧💧💧",
        "💧💧💧          █🌡️🌡️🌡️🌡️🌡️█          💧💧💧",
        "              █🌡️🌡️🌡️🌡️🌡️█",
        "              █🌡️🌡️🌡️🌡️🌡️█",
        "🟫🟫🟫🟫🟫🟫🟫█🌡️🌡️🌡️🌡️🌡️█🟫🟫🟫🟫🟫🟫🟫",
        "🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫",
        "",
        "🌡️ Temperatura agua: 70-100°C",
        "⏰ Intervalos: 30min - 2 horas",
        "📍 Famosos: Yellowstone, Islandia"
    ]
    
    for linea in geiser_ascii:
        print(linea)

def desierto():
    """Crea un desierto con dunas"""
    print("🏜️ DESIERTO CON DUNAS 🏜️")
    print("Mar de arena bajo el sol ardiente")
    print()
    
    desierto_ascii = [
        "                    ☀️",
        "                             🦅",
        "                                     ☁️",
        "🌵              🐪                      ",
        " |          ▓▓▓▓▓▓▓▓                   ",
        " |        ▓▓       ▓▓▓▓                ",
        "🌵       ▓▓           ▓▓▓              ",
        "        ▓▓              ▓▓▓            ",
        "       ▓▓                 ▓▓▓          ",
        "      ▓▓                    ▓▓▓        ",
        "     ▓▓                       ▓▓▓      ",
        "    ▓▓           🦎             ▓▓▓    ",
        "   ▓▓                            ▓▓▓  ",
        "  ▓▓                               ▓▓▓",
        " ▓▓                                  ▓▓",
        "▓▓              🌵                    ▓▓",
        "                 |",
        "🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨",
        "",
        "🌡️ Temperatura día: 50°C, noche: 0°C",
        "💧 Precipitación: menos de 250mm/año",
        "🐪 Fauna adaptada: camellos, reptiles"
    ]
    
    for linea in desierto_ascii:
        print(linea)

def gran_canon():
    """Crea un gran cañón"""
    print("🕳️ GRAN CAÑÓN 🕳️")
    print("Escultura natural de millones de años")
    print()
    
    canon_ascii = [
        "🦅                                      🦅",
        "🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵🌵",
        "▓▓                                    ▓▓",
        "▓▓▓                                  ▓▓▓",
        " ▓▓▓                                ▓▓▓ ",
        "  ▓▓▓                              ▓▓▓  ",
        "   ▓▓▓                            ▓▓▓   ",
        "    ▓▓▓                          ▓▓▓    ",
        "     ▓▓▓                        ▓▓▓     ",
        "      ▓▓▓                      ▓▓▓      ",
        "       ▓▓▓                    ▓▓▓       ",
        "        ▓▓▓                  ▓▓▓        ",
        "         ▓▓▓                ▓▓▓         ",
        "          ▓▓▓              ▓▓▓          ",
        "           ▓▓▓            ▓▓▓           ",
        "            ▓▓▓    🏞️    ▓▓▓            ",
        "             ▓▓▓   ~~~   ▓▓▓             ",
        "              ▓▓▓ ~~~~~ ▓▓▓              ",
        "               ▓▓▓~~~~~▓▓▓               ",
        "🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫",
        "",
        "📏 Profundidad: hasta 1,800 metros",
        "⏰ Formación: 5-6 millones de años",
        "🌊 Río Colorado: escultor principal"
    ]
    
    for linea in canon_ascii:
        print(linea)

def isla_tropical():
    """Crea una isla tropical paradisíaca"""
    print("🏝️ ISLA TROPICAL 🏝️")
    print("Paraíso en medio del océano infinito")
    print()
    
    isla_ascii = [
        "                 ☀️",
        "                          🦅",
        "              ☁️                ☁️",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "~~~~~~~~~      🌴    🌴    🌴      ~~~~~~~~~~~~~~",
        "~~~~~~~~       🌺🌺🌺🌺🌺🌺🌺       ~~~~~~~~~~~~~",
        "~~~~~~~         🌺🟨🟨🟨🟨🟨🌺        ~~~~~~~~~~~~",
        "~~~~~~           🟨🟨🟨🟨🟨🟨🟨         ~~~~~~~~~~~",
        "~~~~~             🟨🟨🟨🟨🟨🟨          ~~~~~~~~~~",
        "~~~~               🟨🟨🟨🟨🟨            ~~~~~~~~~",
        "~~~                 🟨🟨🟨🟨              ~~~~~~~~",
        "~~                   🟨🟨🟨                ~~~~~~~",
        "~                     🟨🟨                  ~~~~~~",
        "                       🟨                    ~~~~~",
        "🐠🐠🐠🐠🐠🐠🐠🐠🐠🐠🐠🐠🐠🐠🐠🐠🐠🐠🐠🐠🐠🐠🐠🐠🐠",
        "🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵",
        "",
        "🌴 Flora: palmeras, hibiscos, orquídeas",
        "🐠 Fauna marina: peces tropicales, corales",
        "🌡️ Clima: 24-30°C todo el año"
    ]
    
    for linea in isla_ascii:
        print(linea)

def glaciar():
    """Crea un imponente glaciar"""
    print("❄️ GLACIAR ❄️")
    print("Río de hielo milenario en movimiento")
    print()
    
    glaciar_ascii = [
        "            ⛄❄️☁️❄️⛄",
        "          ❄️❄️❄️❄️❄️❄️❄️",
        "        ❄️❄️❄️❄️❄️❄️❄️❄️❄️",
        "      ❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️",
        "    ❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️",
        "  🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊",
        " 🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊",
        "🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊",
        "🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊",
        " 🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊",
        "  🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊",
        "   🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊",
        "    🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊",
        "      🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊🧊",
        "        🧊🧊🧊🧊🐧🧊🧊🧊🧊🧊🧊",
        "          🧊🧊🧊🧊🧊🧊🧊🧊🧊",
        "🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵",
        "",
        "⏰ Edad del hielo: miles de años",
        "📏 Grosor: hasta 300 metros",
        "🌡️ Temperatura: -10°C a -40°C"
    ]
    
    for linea in glaciar_ascii:
        print(linea)

def bosque_secuoyas():
    """Crea un bosque de secuoyas gigantes"""
    print("🌲 BOSQUE DE SECUOYAS 🌲")
    print("Los seres vivos más altos y longevos del planeta")
    print()
    
    secuoyas_ascii = [
        "                🌤️        ☁️",
        "        🌲              🌲         🌲",
        "       🌲🌲            🌲🌲       🌲🌲",
        "      🌲🌲🌲          🌲🌲🌲     🌲🌲🌲",
        "     🌲🌲🌲🌲        🌲🌲🌲🌲   🌲🌲🌲🌲",
        "    🌲🌲🌲🌲🌲      🌲🌲🌲🌲🌲 🌲🌲🌲🌲🌲",
        "   🌲🌲🌲🌲🌲🌲    🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲",
        "  🌲🌲🌲🌲🌲🌲🌲  🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲",
        " 🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲",
        "   ████    ████    ████    ████    ████",
        "   ████    ████    ████    ████    ████",
        "   ████    ████    ████    ████    ████",
        "   ████    ████    ████    ████    ████",
        "   ████    ████    ████    ████    ████",
        "   ████    ████    ████    ████    ████",
        "   ████    ████ 🦌 ████    ████    ████",
        "🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿",
        "",
        "🌲 Altura: hasta 115 metros",
        "⏰ Edad: hasta 2,000 años",
        "📍 Ubicación: California, EE.UU."
    ]
    
    for linea in secuoyas_ascii:
        print(linea)

def main():
    """Función principal con menú interactivo"""
    maravillas_funciones = {
        '1': volcan,
        '2': aurora_boreal,
        '3': cadena_montanosa,
        '4': geiser,
        '5': desierto,
        '6': gran_canon,
        '7': isla_tropical,
        '8': glaciar,
        '9': bosque_secuoyas
    }
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("🌍 Selecciona una opción (0-9): ").strip()
            
            if opcion == '0':
                print("\n🌍 ¡Gracias por explorar las maravillas naturales con ASCII! 🌍")
                print("🌱 ¡Protejamos nuestro planeta para las futuras generaciones! 🌱")
                break
            elif opcion in maravillas_funciones:
                print("\n" + "="*60)
                maravillas_funciones[opcion]()
                print("="*60)
            else:
                print("❌ Opción no válida. Intenta de nuevo.")
                
        except KeyboardInterrupt:
            print("\n\n🌍 ¡Hasta luego, explorador de la naturaleza! 🌍")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        
        input("\n🌿 Presiona Enter para continuar explorando...")

if __name__ == "__main__":
    main()
