#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 89: Maravillas del Mundo Moderno ASCII
================================================

Objetivo:
- Crear representaciones de las nuevas maravillas del mundo usando ASCII
- Explorar logros arquitectónicos y de ingeniería contemporáneos
- Apreciar la creatividad y capacidad humana moderna

Conceptos aplicados:
- Arquitectura moderna
- Ingeniería avanzada
- Iconos urbanos
- Turismo mundial
"""

import time
import random

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*60)
    print("🏗️ GENERADOR DE MARAVILLAS MODERNAS ASCII 🏗️")
    print("="*60)
    print("1. 🗼 Torre Eiffel")
    print("2. 🏢 Empire State")
    print("3. 🌉 Golden Gate")
    print("4. 🕌 Burj Khalifa")
    print("5. 🎡 London Eye")
    print("6. 🗽 CN Tower")
    print("7. 🌊 Ópera de Sydney")
    print("8. 🏗️ Puente de Brooklyn")
    print("9. 🌆 Skyline de Manhattan")
    print("0. 🚪 Salir")
    print("-"*60)

def torre_eiffel_moderna():
    """Crea la Torre Eiffel iluminada"""
    print("🗼 TORRE EIFFEL 🗼")
    print("Ícono eterno de París - Elegancia en hierro")
    print()
    
    torre_moderna = [
        "                  ✨✨✨",
        "                   |||",
        "                   |||",
        "                  /|||\\",
        "                 / ||| \\",
        "                /  |||  \\",
        "               /   |||   \\",
        "              /    |||    \\",
        "         💫  /     |||     \\  💫",
        "            /      |||      \\",
        "           /       |||       \\",
        "          /        |||        \\",
        "         /=========|||=========\\",
        "        /          |||          \\",
        "       /           |||           \\",
        "  ✨  /            |||            \\  ✨",
        "     /             |||             \\",
        "    /              |||              \\",
        "   /===============|||===============\\",
        "  /                |||                \\",
        " /                 |||                 \\",
        "/___________________|||___________________\\",
        "💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫",
        "",
        "🗼 Altura: 330 metros (con antena)",
        "⚡ Iluminación: 20,000 bombillas LED",
        "👥 Visitantes: 7 millones al año"
    ]
    
    for linea in torre_moderna:
        print(linea)

def empire_state():
    """Crea el Empire State Building"""
    print("🏢 EMPIRE STATE BUILDING 🏢")
    print("Rascacielos icónico de Nueva York - Art Déco")
    print()
    
    empire_ascii = [
        "              ⚡⚡⚡⚡⚡",
        "             ████████████",
        "            ██████████████",
        "           ████████████████",
        "          ██████████████████",
        "         ████████████████████",
        "        ██████████████████████",
        "       ████████████████████████",
        "      ██████████████████████████",
        "     ████████████████████████████",
        "    ██████████████████████████████",
        "   ████████████████████████████████",
        "  ██████████████████████████████████",
        " ████████████████████████████████████",
        "██████████████████████████████████████",
        "██  🏢 EMPIRE STATE BUILDING 🏢  ██",
        "██████████████████████████████████████",
        "██████████████████████████████████████",
        "██████████████████████████████████████",
        "██████████████████████████████████████",
        "🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃",
        "",
        "🏢 Pisos: 102 niveles habitables",
        "⚡ Construcción: 410 días (1930-1931)",
        "🎬 Famoso por: King Kong, cine clásico"
    ]
    
    for linea in empire_ascii:
        print(linea)

def golden_gate():
    """Crea el puente Golden Gate"""
    print("🌉 GOLDEN GATE BRIDGE 🌉")
    print("Puente colgante más fotografiado del mundo - San Francisco")
    print()
    
    golden_gate_ascii = [
        "                 ☁️        ☁️",
        "               ☁️  ☁️    ☁️  ☁️",
        "  🗼             🗼      🗼             🗼",
        "  ║              ║      ║              ║",
        "  ║    ╔════════╗║      ║╔════════╗    ║",
        "  ║    ║🌉GOLDEN║║ GATE ║║BRIDGE🌉║    ║",
        "  ║    ╚════════╝║      ║╚════════╝    ║",
        "  ║🔴🔴🔴🔴🔴🔴🔴🔴║      ║🔴🔴🔴🔴🔴🔴🔴🔴║",
        "🔴🔴              🔴🔴🔴🔴🔴🔴              🔴🔴",
        "🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴",
        "🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴",
        "🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊",
        "                 ⛵        ⛵",
        "🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊",
        "",
        "🌉 Longitud: 2,737 metros",
        "🔴 Color: 'International Orange'",
        "🌊 Bahía: conecta SF con Marin County"
    ]
    
    for linea in golden_gate_ascii:
        print(linea)

def burj_khalifa():
    """Crea el Burj Khalifa de Dubai"""
    print("🕌 BURJ KHALIFA 🕌")
    print("El edificio más alto del mundo - Dubai")
    print()
    
    burj_ascii = [
        "                    ⭐",
        "                    ||",
        "                   ||||",
        "                  ||||||",
        "                 ||||||||",
        "                ||||||||||",
        "               ||||||||||||",
        "              ||||||||||||||",
        "             ||||||||||||||||",
        "            ||||||||||||||||||",
        "           ||||||||||||||||||||",
        "          ||||||||||||||||||||||",
        "         ||||||||||||||||||||||||",
        "        ||||||||||||||||||||||||||",
        "       ||||||||||||||||||||||||||||",
        "      ||||||||||||||||||||||||||||||",
        "     ||||||||||||||||||||||||||||||||",
        "    ||||||||||||||||||||||||||||||||||",
        "   ||||||||||||||||||||||||||||||||||||",
        "  ||||||||||||||||||||||||||||||||||||||",
        " ||||||||||||||||||||||||||||||||||||||||",
        "||||||||||||||||||||||||||||||||||||||||||",
        "🏜️🏜️🏜️🏜️🏜️🏜️🏜️🏜️🏜️🏜️🏜️🏜️🏜️🏜️🏜️🏜️🏜️🏜️🏜️🏜️🏜️",
        "",
        "🕌 Altura: 828 metros (163 pisos)",
        "🏗️ Construcción: 6 años (2004-2010)",
        "💫 Récords: edificio, estructura, observatorio"
    ]
    
    for linea in burj_ascii:
        print(linea)

def london_eye():
    """Crea la London Eye"""
    print("🎡 LONDON EYE 🎡")
    print("La noria de observación más alta de Europa - Londres")
    print()
    
    london_eye_ascii = [
        "              ☁️    ☁️",
        "        🎡               🎡",
        "     🎡                     🎡",
        "   🎡                         🎡",
        "  🎡         LONDON           🎡",
        " 🎡            EYE             🎡",
        "🎡                             🎡",
        "🎡              |              🎡",
        "🎡              |              🎡",
        "🎡              |              🎡",
        "🎡              |              🎡",
        " 🎡             |             🎡",
        "  🎡            |            🎡",
        "   🎡           |           🎡",
        "     🎡         |         🎡",
        "        🎡       |       🎡",
        "              ████████",
        "🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊",
        "        RIVER THAMES",
        "",
        "🎡 Altura: 135 metros",
        "👥 Capacidad: 800 personas",
        "⏰ Revolución completa: 30 minutos"
    ]
    
    for linea in london_eye_ascii:
        print(linea)

def cn_tower():
    """Crea la CN Tower de Toronto"""
    print("🗽 CN TOWER 🗽")
    print("Torre de comunicaciones más alta del hemisferio occidental")
    print()
    
    cn_tower_ascii = [
        "                    📡",
        "                    ||",
        "                    ||",
        "                    ||",
        "                    ||",
        "                    ||",
        "                    ||",
        "                    ||",
        "                ████████",
        "               ██████████",
        "              ████████████",
        "               ██████████",
        "                ████████",
        "                    ||",
        "                    ||",
        "                    ||",
        "                ████████",
        "               ██████████",
        "              ████████████",
        "             ██████████████",
        "            ████████████████",
        "           ██████████████████",
        "🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢",
        "",
        "📡 Altura: 553.3 metros",
        "🏢 Mirador: EdgeWalk a 356m",
        "📺 Función: torre de telecomunicaciones"
    ]
    
    for linea in cn_tower_ascii:
        print(linea)

def opera_sydney():
    """Crea la Ópera de Sydney"""
    print("🌊 ÓPERA DE SYDNEY 🌊")
    print("Obra maestra arquitectónica - Patrimonio de la Humanidad")
    print()
    
    opera_ascii = [
        "              ⛅       ⛅",
        "                ☀️",
        "          🎭 SYDNEY OPERA 🎭",
        "       ╭─╮    ╭─╮    ╭─╮",
        "      ╱   ╲  ╱   ╲  ╱   ╲",
        "     ╱     ╲╱     ╲╱     ╲",
        "    ╱                     ╲",
        "   ╱        HOUSE          ╲",
        "  ╱                         ╲",
        " ╱___________________________╲",
        "█████████████████████████████████",
        "█  🎼  🎭  🎪  🎨  🎹  🎺  🎸  █",
        "█████████████████████████████████",
        "🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊",
        "         ⛵    ⛵    ⛵",
        "🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊",
        "",
        "🎭 Arquitecto: Jørn Utzon (Dinamarca)",
        "🎪 Salas: Ópera, teatro, conciertos",
        "🌊 Ubicación: Puerto de Sydney"
    ]
    
    for linea in opera_ascii:
        print(linea)

def puente_brooklyn():
    """Crea el Puente de Brooklyn"""
    print("🏗️ PUENTE DE BROOKLYN 🏗️")
    print("Pionero de los puentes colgantes - Nueva York")
    print()
    
    brooklyn_ascii = [
        "       🏢                     🏢",
        "     🏢🏢🏢                 🏢🏢🏢",
        "   🏢🏢🏢🏢🏢             🏢🏢🏢🏢🏢",
        "  🗼      🗼             🗼      🗼",
        "  ║       ║             ║       ║",
        "  ║   ▲   ║             ║   ▲   ║",
        "  ║  ▲ ▲  ║             ║  ▲ ▲  ║",
        "  ║ ▲   ▲ ║             ║ ▲   ▲ ║",
        "  ║▲     ▲║             ║▲     ▲║",
        "▲▲║       ║▲▲▲▲▲▲▲▲▲▲▲▲▲║       ║▲▲",
        "████████████████████████████████████",
        "🚗 🚗 🚗 🚗 🚗 🚗 🚗 🚗 🚗 🚗 🚗 🚗",
        "████████████████████████████████████",
        "🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊",
        "        ⛵      ⛵      ⛵",
        "🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊",
        "",
        "🏗️ Inaugurado: 1883 (primer puente colgante)",
        "🌉 Longitud: 1,825 metros",
        "🚗 Conecta: Manhattan y Brooklyn"
    ]
    
    for linea in brooklyn_ascii:
        print(linea)

def skyline_manhattan():
    """Crea el skyline de Manhattan"""
    print("🌆 SKYLINE DE MANHATTAN 🌆")
    print("El horizonte más famoso del mundo - Nueva York")
    print()
    
    skyline_ascii = [
        "      ⭐    ☁️    ⭐        ☁️    ⭐",
        "  🏢    🏢🏢🏢    🏢🏢🏢🏢    🏢🏢",
        " 🏢🏢  🏢🏢🏢🏢  🏢🏢🏢🏢🏢  🏢🏢🏢🏢",
        "🏢🏢🏢 🏢🏢🏢🏢🏢 🏢🏢🏢🏢🏢🏢 🏢🏢🏢🏢🏢",
        "🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢",
        "🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢",
        "🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢🏢",
        "💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡",
        "💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡",
        "💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡",
        "💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡",
        "🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊",
        "   🚢              ⛵          🛥️",
        "🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊",
        "",
        "🏢 Rascacielos: Empire State, Chrysler, One WTC",
        "🌉 Puentes: Brooklyn, Manhattan, Williamsburg",
        "🗽 Icono: Estatua de la Libertad visible"
    ]
    
    for linea in skyline_ascii:
        print(linea)

def main():
    """Función principal con menú interactivo"""
    maravillas_funciones = {
        '1': torre_eiffel_moderna,
        '2': empire_state,
        '3': golden_gate,
        '4': burj_khalifa,
        '5': london_eye,
        '6': cn_tower,
        '7': opera_sydney,
        '8': puente_brooklyn,
        '9': skyline_manhattan
    }
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("🏗️ Selecciona una opción (0-9): ").strip()
            
            if opcion == '0':
                print("\n🏗️ ¡Gracias por admirar las maravillas modernas! 🏗️")
                print("🌟 ¡El ingenio humano no tiene límites! 🌟")
                break
            elif opcion in maravillas_funciones:
                print("\n" + "="*60)
                maravillas_funciones[opcion]()
                print("="*60)
            else:
                print("❌ Opción no válida. Intenta de nuevo.")
                
        except KeyboardInterrupt:
            print("\n\n🏗️ ¡Hasta luego, admirador de la arquitectura! 🏗️")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        
        input("\n🌆 Presiona Enter para continuar explorando...")

if __name__ == "__main__":
    main()
