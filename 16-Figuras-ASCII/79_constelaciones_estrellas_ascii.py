#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 79: Constelaciones y Estrellas ASCII
==============================================

Objetivo:
- Crear representaciones ASCII de constelaciones famosas
- Implementar mapas estelares y patrones astronómicos
- Mostrar la belleza del universo nocturno

Conceptos aplicados:
- Representación de astronomía y cosmología
- Patrones estelares y navegación
- Mitología astronómica
"""

def mostrar_menu():
    """Muestra el menú de opciones disponibles"""
    print("\n" + "="*50)
    print("⭐ GENERADOR DE CONSTELACIONES ASCII ⭐")
    print("="*50)
    print("1. Osa Mayor")
    print("2. Orión")
    print("3. Cassiopeia")
    print("4. Cruz del Sur")
    print("5. Escorpión")
    print("6. Cygnus (Cisne)")
    print("7. Leo")
    print("8. Vía Láctea")
    print("9. Cielo Estrellado")
    print("0. Salir")
    print("-"*50)

def osa_mayor():
    """Constelación de la Osa Mayor"""
    print("🐻 OSA MAYOR 🐻")
    print()
    print("El Gran Carro - Guía de navegación")
    print()
    
    osa_ascii = [
        "    ⭐ OSA MAYOR ⭐         ",
        "",
        "                ⭐         ",
        "              ╱            ",
        "            ╱              ",
        "          ⭐                ",
        "        ╱                  ",
        "      ╱                    ",
        "    ⭐                     ",
        "   ╱ ╲                     ",
        "  ╱   ╲                    ",
        " ╱     ╲                   ",
        "⭐       ⭐                 ",
        "           ╲               ",
        "            ╲              ",
        "             ⭐            ",
        "              ╲            ",
        "               ╲           ",
        "                ⭐         ",
        "                 ╲         ",
        "                  ╲        ",
        "                   ⭐      ",
        "",
        "🐻 Ursa Major",
        "🧭 Apunta a la Estrella Polar",
        "🌌 Visible todo el año en el norte"
    ]
    
    for linea in osa_ascii:
        print(linea)

def orion():
    """Constelación de Orión"""
    print("🏹 ORIÓN 🏹")
    print()
    print("El Cazador celestial")
    print()
    
    orion_ascii = [
        "       🏹 ORIÓN 🏹         ",
        "",
        "         ⭐               ",
        "        ╱ ╲               ",
        "       ╱   ╲              ",
        "      ⭐     ⭐            ",
        "     ╱ ╲   ╱ ╲            ",
        "    ╱   ╲ ╱   ╲           ",
        "   ╱     ⭐     ╲          ",
        "  ╱    ╱  ╲    ╲         ",
        " ╱    ╱    ╲    ╲        ",
        "⭐   ╱      ╲   ⭐        ",
        "   ╱   ⭐⭐⭐   ╲          ",
        "  ╱  CINTURÓN  ╲         ",
        " ╱              ╲        ",
        "⭐                ⭐       ",
        " ╲              ╱        ",
        "  ╲            ╱         ",
        "   ⭐        ⭐           ",
        "",
        "🏹 Betelgeuse (hombro)",
        "⭐ Cinturón: Alnitak, Alnilam, Mintaka",
        "🌌 Visible en invierno"
    ]
    
    for linea in orion_ascii:
        print(linea)

def cassiopeia():
    """Constelación de Cassiopeia"""
    print("👑 CASSIOPEIA 👑")
    print()
    print("La Reina sentada en su trono")
    print()
    
    cassiopeia_ascii = [
        "      👑 CASSIOPEIA 👑      ",
        "",
        "  ⭐                       ",
        "    ╲                      ",
        "     ╲                     ",
        "      ⭐                   ",
        "       ╱ ╲                 ",
        "      ╱   ╲                ",
        "     ╱     ╲               ",
        "    ╱       ⭐             ",
        "   ╱       ╱ ╲             ",
        "  ╱       ╱   ╲            ",
        " ╱       ╱     ╲           ",
        "╱       ╱       ⭐         ",
        "       ╱       ╱ ╲         ",
        "      ╱       ╱   ╲        ",
        "     ╱       ╱     ╲       ",
        "    ╱       ╱       ⭐     ",
        "   ╱       ╱               ",
        "  ╱       ╱                ",
        " ╱       ╱                 ",
        "",
        "👑 Forma de 'W' o 'M'",
        "🌟 5 estrellas principales",
        "🧭 Opuesta a la Osa Mayor"
    ]
    
    for linea in cassiopeia_ascii:
        print(linea)

def cruz_del_sur():
    """Constelación de la Cruz del Sur"""
    print("✝️ CRUZ DEL SUR ✝️")
    print()
    print("Guía del hemisferio sur")
    print()
    
    cruz_ascii = [
        "     ✝️ CRUZ DEL SUR ✝️     ",
        "",
        "                           ",
        "         ⭐               ",
        "        ╱ ╲               ",
        "       ╱   ╲              ",
        "      ╱     ╲             ",
        "     ╱       ╲            ",
        "    ╱         ╲           ",
        "   ╱           ╲          ",
        "  ⭐─────⭐─────⭐         ",
        "   ╲           ╱          ",
        "    ╲         ╱           ",
        "     ╲       ╱            ",
        "      ╲     ╱             ",
        "       ╲   ╱              ",
        "        ╲ ╱               ",
        "         ⭐               ",
        "                           ",
        "    🌌 SACO DE CARBÓN     ",
        "        (nebulosa)         ",
        "",
        "✝️ Crux - la cruz más pequeña",
        "🧭 Apunta al Polo Sur celeste",
        "🇦🇺 Emblema de Australia y Brasil"
    ]
    
    for linea in cruz_ascii:
        print(linea)

def escorpion():
    """Constelación de Escorpión"""
    print("🦂 ESCORPIÓN 🦂")
    print()
    print("El enemigo mortal de Orión")
    print()
    
    escorpion_ascii = [
        "       🦂 ESCORPIÓN 🦂      ",
        "",
        "    ⭐                     ",
        "   ╱ ╲                     ",
        "  ╱   ╲                    ",
        " ╱     ⭐                  ",
        "╱     ╱ ╲                  ",
        "     ╱   ╲                 ",
        "    ╱     ⭐               ",
        "   ╱     ╱ ╲               ",
        "  ╱     ╱   ╲              ",
        " ╱     ╱     ⭐            ",
        "╱     ╱     ╱ ╲            ",
        "     ╱     ╱   ╲           ",
        "    ╱     ╱     ⭐         ",
        "   ╱     ╱     ╱ ╲         ",
        "  ╱     ╱     ╱   ╲        ",
        " ╱     ╱     ╱     ⭐      ",
        "╱     ╱     ╱       ╲      ",
        "     ╱     ╱         ╲     ",
        "    ╱     ╱           ⭐   ",
        "",
        "🦂 Antares - corazón rojo",
        "🌌 Visible en verano",
        "⚔️ Enemigo mítico de Orión"
    ]
    
    for linea in escorpion_ascii:
        print(linea)

def cygnus():
    """Constelación del Cisne"""
    print("🦢 CYGNUS (CISNE) 🦢")
    print()
    print("La Cruz del Norte")
    print()
    
    cygnus_ascii = [
        "    🦢 CYGNUS (CISNE) 🦢   ",
        "",
        "         ⭐               ",
        "        ╱ ╲               ",
        "       ╱   ╲              ",
        "      ╱     ╲             ",
        "     ╱       ╲            ",
        "    ╱         ╲           ",
        "   ╱           ╲          ",
        "  ╱             ╲         ",
        " ⭐───────⭐───────⭐       ",
        "  ╲             ╱         ",
        "   ╲           ╱          ",
        "    ╲         ╱           ",
        "     ╲       ╱            ",
        "      ╲     ╱             ",
        "       ╲   ╱              ",
        "        ╲ ╱               ",
        "         ⭐               ",
        "        ╱ ╲               ",
        "       ╱   ╲              ",
        "      ╱     ╲             ",
        "     ⭐       ⭐           ",
        "",
        "🦢 Deneb - cola del cisne",
        "✝️ También llamada Cruz del Norte",
        "🌌 Vuela por la Vía Láctea"
    ]
    
    for linea in cygnus_ascii:
        print(linea)

def leo():
    """Constelación de Leo"""
    print("🦁 LEO 🦁")
    print()
    print("El León Real")
    print()
    
    leo_ascii = [
        "        🦁 LEO 🦁          ",
        "",
        "    ⭐                     ",
        "   ╱ ╲                     ",
        "  ╱   ╲                    ",
        " ╱     ⭐                  ",
        "╱     ╱ ╲                  ",
        "     ╱   ╲                 ",
        "    ╱     ⭐               ",
        "   ╱       ╲               ",
        "  ╱         ╲              ",
        " ╱           ⭐            ",
        "╱           ╱ ╲            ",
        "           ╱   ╲           ",
        "          ╱     ⭐         ",
        "         ╱     ╱ ╲         ",
        "        ╱     ╱   ╲        ",
        "       ╱     ╱     ⭐      ",
        "      ╱     ╱     ╱ ╲      ",
        "     ╱     ╱     ╱   ╲     ",
        "    ⭐     ╱     ╱     ⭐   ",
        "",
        "🦁 Regulus - corazón del león",
        "👑 Rey de las constelaciones",
        "🌸 Visible en primavera"
    ]
    
    for linea in leo_ascii:
        print(linea)

def via_lactea():
    """La Vía Láctea"""
    print("🌌 VÍA LÁCTEA 🌌")
    print()
    print("Nuestra galaxia hogar")
    print()
    
    via_lactea_ascii = [
        "      🌌 VÍA LÁCTEA 🌌      ",
        "",
        "⭐  ⭐    ⭐  ⭐    ⭐  ⭐ ",
        "  ⭐    ⭐  ⭐    ⭐  ⭐   ",
        "⭐  ⭐ ✨⭐✨⭐✨ ⭐  ⭐ ",
        "  ⭐ ✨⭐✨⭐✨⭐✨⭐✨ ⭐  ",
        "⭐ ✨⭐✨⭐✨⭐✨⭐✨⭐✨ ⭐",
        " ✨⭐✨⭐✨🌟✨⭐✨⭐✨⭐✨ ",
        "✨⭐✨⭐✨⭐✨⭐✨⭐✨⭐✨⭐✨",
        " ✨⭐✨⭐✨🌟✨⭐✨⭐✨⭐✨ ",
        "⭐ ✨⭐✨⭐✨⭐✨⭐✨⭐✨ ⭐",
        "  ⭐ ✨⭐✨⭐✨⭐✨⭐✨ ⭐  ",
        "⭐  ⭐ ✨⭐✨⭐✨ ⭐  ⭐ ",
        "  ⭐    ⭐  ⭐    ⭐  ⭐   ",
        "⭐  ⭐    ⭐  ⭐    ⭐  ⭐ ",
        "",
        "🌌 200-400 mil millones de estrellas",
        "🌟 Centro galáctico: Sagitario A*",
        "☀️ El Sol está en el brazo de Orión"
    ]
    
    for linea in via_lactea_ascii:
        print(linea)

def cielo_estrellado():
    """Cielo nocturno completo"""
    print("🌃 CIELO ESTRELLADO 🌃")
    print()
    print("La majestuosidad de la noche")
    print()
    
    cielo_ascii = [
        "     🌃 CIELO ESTRELLADO 🌃  ",
        "",
        "⭐    ⭐        ⭐      ⭐   ",
        "   ⭐      ⭐         ⭐    ",
        "      ⭐ ✨   ⭐  ⭐        ",
        "⭐ ✨     ⭐     ✨    ⭐   ",
        "    ⭐  ✨  ⭐ ✨  ⭐       ",
        " ⭐   ✨ ⭐ ✨ ⭐ ✨  ⭐    ",
        "   ✨ ⭐ ✨ 🌟 ✨ ⭐ ✨     ",
        "⭐ ✨ ⭐ ✨ ⭐ ✨ ⭐ ✨ ⭐  ",
        " ✨ ⭐ ✨ ⭐ ✨ ⭐ ✨ ⭐ ✨   ",
        "⭐ ✨ ⭐ ✨ 🌟 ✨ ⭐ ✨ ⭐  ",
        " ✨ ⭐ ✨ ⭐ ✨ ⭐ ✨ ⭐ ✨   ",
        "⭐ ✨ ⭐ ✨ ⭐ ✨ ⭐ ✨ ⭐  ",
        "   ✨ ⭐ ✨ 🌟 ✨ ⭐ ✨     ",
        " ⭐   ✨ ⭐ ✨ ⭐ ✨  ⭐    ",
        "    ⭐  ✨  ⭐ ✨  ⭐       ",
        "⭐ ✨     ⭐     ✨    ⭐   ",
        "      ⭐ ✨   ⭐  ⭐        ",
        "   ⭐      ⭐         ⭐    ",
        "⭐    ⭐        ⭐      ⭐   ",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "       🏔️ 🏔️ 🏔️         ",
        "",
        "🌃 Magnitud aparente visible",
        "🔭 Mejor observación: zonas oscuras",
        "🌕 Fase lunar: nueva (sin luna)"
    ]
    
    for linea in cielo_ascii:
        print(linea)

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Selecciona una opción (0-9): ").strip()
            
            if opcion == '0':
                print("\n¡Que las estrellas guíen tu camino! ⭐")
                break
            elif opcion == '1':
                osa_mayor()
            elif opcion == '2':
                orion()
            elif opcion == '3':
                cassiopeia()
            elif opcion == '4':
                cruz_del_sur()
            elif opcion == '5':
                escorpion()
            elif opcion == '6':
                cygnus()
            elif opcion == '7':
                leo()
            elif opcion == '8':
                via_lactea()
            elif opcion == '9':
                cielo_estrellado()
            else:
                print("❌ Opción no válida. Por favor, elige una opción del 0 al 9.")
                
        except ValueError:
            print("❌ Por favor, introduce un número válido.")
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego! 🌌")
            break
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
