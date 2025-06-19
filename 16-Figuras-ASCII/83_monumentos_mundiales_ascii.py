#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 83: Monumentos Mundiales ASCII
========================================

Objetivo:
- Crear representaciones de famosos monumentos mundiales usando ASCII
- Explorar la arquitectura y cultura de diferentes civilizaciones
- Promover el conocimiento del patrimonio mundial

Conceptos aplicados:
- Patrimonio mundial UNESCO
- Arquitectura histórica
- Diversidad cultural
- Turismo virtual
"""

import time
import random

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*60)
    print("🏛️ GENERADOR DE MONUMENTOS MUNDIALES ASCII 🏛️")
    print("="*60)
    print("1. 🗼 Torre Eiffel (Francia)")
    print("2. 🏛️ Partenón (Grecia)")
    print("3. 🗽 Estatua de la Libertad (USA)")
    print("4. 🏰 Taj Mahal (India)")
    print("5. 🏯 Torre de Pisa (Italia)")
    print("6. 🗿 Moái (Isla de Pascua)")
    print("7. 🏛️ Coliseo Romano (Italia)")
    print("8. 🕌 Sagrada Familia (España)")
    print("9. 🏔️ Machu Picchu (Perú)")
    print("0. 🚪 Salir")
    print("-"*60)

def torre_eiffel():
    """Crea la icónica Torre Eiffel"""
    print("🗼 TORRE EIFFEL 🗼")
    print("Símbolo de París y Francia, construida en 1889")
    print()
    
    torre = [
        "                    ⛳",
        "                    ||",
        "                    ||",
        "                   /||\\",
        "                  / || \\",
        "                 /  ||  \\",
        "                /   ||   \\",
        "               /    ||    \\",
        "              /     ||     \\",
        "             /      ||      \\",
        "            /       ||       \\",
        "           /        ||        \\",
        "          /=========||=========\\",
        "         /          ||          \\",
        "        /           ||           \\",
        "       /            ||            \\",
        "      /             ||             \\",
        "     /              ||              \\",
        "    /               ||               \\",
        "   /================||================\\",
        "  /                 ||                 \\",
        " /                  ||                  \\",
        "/___________________||___________________\\",
        "█████████████████████████████████████████",
        "█████████████████████████████████████████"
    ]
    
    for linea in torre:
        print(linea)

def partenon():
    """Crea el majestuoso Partenón"""
    print("🏛️ PARTENÓN 🏛️")
    print("Templo griego dedicado a la diosa Atenea (447-432 a.C.)")
    print()
    
    partenon_ascii = [
        "     ═════════════════════════════════════",
        "    ╔═════════════════════════════════════╗",
        "   ╔═══════════════════════════════════════╗",
        "  ╔═════════════════════════════════════════╗",
        " ╔═══════════════════════════════════════════╗",
        "╔═════════════════════════════════════════════╗",
        "█ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ █",
        "█ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ █",
        "█ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ █",
        "█ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ █",
        "█ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ █",
        "█ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ █",
        "█ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ █",
        "█ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ █",
        "███████████████████████████████████████████████",
        "███████████████████████████████████████████████",
        "███████████████████████████████████████████████"
    ]
    
    for linea in partenon_ascii:
        print(linea)

def estatua_libertad():
    """Crea la Estatua de la Libertad"""
    print("🗽 ESTATUA DE LA LIBERTAD 🗽")
    print("Símbolo de libertad y democracia, regalo de Francia a USA")
    print()
    
    estatua = [
        "              ⭐⭐⭐",
        "             ⭐🔥🔥🔥⭐",
        "            ⭐🔥🔥🔥🔥🔥⭐",
        "           ⭐🔥🔥🔥🔥🔥🔥⭐",
        "            ⭐🔥🔥🔥🔥🔥⭐",
        "             ⭐🔥🔥🔥⭐",
        "              ⭐⭐⭐",
        "               ■■■",
        "              ■■■■■",
        "             ■■●●●■■",
        "            ■■■●●●■■■",
        "           ■■■■●●●■■■■",
        "          ■■■■■■■■■■■■■",
        "         ■■■■■■■■■■■■■■■",
        "        ■■■■■■■■■■■■■■■■■",
        "       ■■■■■■■■■■■■■■■■■■■",
        "      ■■■■■■■■■■■■■■■■■■■■■",
        "     ■■■■■■■■■■■■■■■■■■■■■■■",
        "    ■■■■■■■■■■■■■■■■■■■■■■■■■",
        "   ■■■■■■■■■■■■■■■■■■■■■■■■■■■",
        "██████████████████████████████████",
        "██████████████████████████████████",
        "██████████████████████████████████"
    ]
    
    for linea in estatua:
        print(linea)

def taj_mahal():
    """Crea el romántico Taj Mahal"""
    print("🏰 TAJ MAHAL 🏰")
    print("Mausoleo de mármol blanco, símbolo de amor eterno")
    print()
    
    taj = [
        "                    🌙",
        "                   ◐◑◐",
        "                  ◐◑◐◑◐",
        "                 ◐◑◐◑◐◑◐",
        "                ◐◑◐◑◐◑◐◑◐",
        "               ◐◑◐◑◐◑◐◑◐◑◐",
        "              ███████████████",
        "             █████████████████",
        "            ███████████████████",
        "           █████████████████████",
        "          ███████████████████████",
        "    🕌   ██████████████████████   🕌",
        "   ████  ██████████████████████  ████",
        "  ██████ ██████████████████████ ██████",
        " ████████████████████████████████████████",
        "██████████████████████████████████████████",
        "██████████████████████████████████████████",
        "██████████████████████████████████████████",
        "██████████████████████████████████████████",
        "██████████████████████████████████████████"
    ]
    
    for linea in taj:
        print(linea)

def torre_pisa():
    """Crea la famosa Torre de Pisa inclinada"""
    print("🏯 TORRE DE PISA 🏯")
    print("Torre campanario inclinada de la catedral de Pisa")
    print()
    
    torre_pisa = [
        "                 ⛪",
        "                ████",
        "               ██████",
        "              ████████",
        "             ██████████",
        "            ████████████",
        "           ██████████████",
        "          ████████████████",
        "         ██████████████████",
        "        ████████████████████",
        "       ██████████████████████",
        "      ████████████████████████",
        "     ██████████████████████████",
        "    ████████████████████████████",
        "   ██████████████████████████████",
        "  ████████████████████████████████",
        " ██████████████████████████████████",
        "████████████████████████████████████",
        "████████████████████████████████████",
        "████████████████████████████████████"
    ]
    
    for linea in torre_pisa:
        print(linea)

def moai():
    """Crea las misteriosas estatuas Moái"""
    print("🗿 MOÁI 🗿")
    print("Estatuas monolíticas de la Isla de Pascua (Rapa Nui)")
    print()
    
    moai_ascii = [
        "    ████████        ████████        ████████",
        "   ██████████      ██████████      ██████████",
        "  ████████████    ████████████    ████████████",
        " ██████████████  ██████████████  ██████████████",
        "████████████████████████████████████████████████",
        "████  ████  ████████  ████  ████████  ████  ████",
        "████  ████  ████████  ████  ████████  ████  ████",
        "████████████████████████████████████████████████",
        "████        ████████        ████████        ████",
        "████        ████████        ████████        ████",
        "████████████████████████████████████████████████",
        "████████████████████████████████████████████████",
        "████████████████████████████████████████████████",
        "████████████████████████████████████████████████",
        "████████████████████████████████████████████████",
        "████████████████████████████████████████████████",
        "████████████████████████████████████████████████",
        "🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿",
        "🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿"
    ]
    
    for linea in moai_ascii:
        print(linea)

def coliseo_romano():
    """Crea el imponente Coliseo Romano"""
    print("🏛️ COLISEO ROMANO 🏛️")
    print("Anfiteatro Flavio, icono de la Roma Imperial")
    print()
    
    coliseo = [
        "  ╔══════════════════════════════════════════════╗",
        " ╔════════════════════════════════════════════════╗",
        "╔══════════════════════════════════════════════════╗",
        "██ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ██",
        "██ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ██",
        "██                                              ██",
        "██ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ██",
        "██ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ██",
        "██                                              ██",
        "██ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ██",
        "██ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ██",
        "██                                              ██",
        "██ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ██",
        "██ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ██",
        "██                                              ██",
        "████████████████████████████████████████████████████",
        "████████████████████████████████████████████████████",
        "████████████████████████████████████████████████████"
    ]
    
    for linea in coliseo:
        print(linea)

def sagrada_familia():
    """Crea la Sagrada Familia de Gaudí"""
    print("🕌 SAGRADA FAMILIA 🕌")
    print("Obra maestra de Antoni Gaudí en Barcelona")
    print()
    
    sagrada = [
        "  ✠   ✠     ✠     ✠     ✠     ✠   ✠",
        " ╱│╲ ╱│╲   ╱│╲   ╱│╲   ╱│╲   ╱│╲ ╱│╲",
        "╱ │ ╲╱ │ ╲ ╱ │ ╲ ╱ │ ╲ ╱ │ ╲ ╱ │ ╲╱ │ ╲",
        "  │   │   │   │   │   │   │   │   │",
        "  │   │   │   │   │   │   │   │   │",
        "██│██ │ ██│██ │ ██│██ │ ██│██ │ ██│██",
        "  │   │   │   │   │   │   │   │   │",
        "  │   │   │   │   │   │   │   │   │",
        "██│██ │ ██│██ │ ██│██ │ ██│██ │ ██│██",
        "  │   │   │   │   │   │   │   │   │",
        "  │   │   │   │   │   │   │   │   │",
        "██│██ │ ██│██ │ ██│██ │ ██│██ │ ██│██",
        "  │   │   │   │   │   │   │   │   │",
        "  │   │   │   │   │   │   │   │   │",
        "██│██ │ ██│██ │ ██│██ │ ██│██ │ ██│██",
        "██████████████████████████████████████",
        "██████████████████████████████████████",
        "██████████████████████████████████████"
    ]
    
    for linea in sagrada:
        print(linea)

def machu_picchu():
    """Crea la ciudadela inca de Machu Picchu"""
    print("🏔️ MACHU PICCHU 🏔️")
    print("Ciudad perdida de los incas en los Andes peruanos")
    print()
    
    machu = [
        "                🌤️        ☁️",
        "    ▲▲▲▲                      ▲▲▲▲▲",
        "   ▲▲▲▲▲▲        ☁️          ▲▲▲▲▲▲▲",
        "  ▲▲▲▲▲▲▲▲                 ▲▲▲▲▲▲▲▲▲",
        " ▲▲▲▲▲▲▲▲▲▲               ▲▲▲▲▲▲▲▲▲▲▲",
        "▲▲▲▲▲▲▲▲▲▲▲▲             ▲▲▲▲▲▲▲▲▲▲▲▲▲",
        "  ████ ████ ████ ████ ████ ████ ████",
        "  ████ ████ ████ ████ ████ ████ ████",
        "  ████ ████ ████ ████ ████ ████ ████",
        "  ████ ████ ████ ████ ████ ████ ████",
        "  ████ ████ ████ ████ ████ ████ ████",
        "██████████████████████████████████████",
        "██████████████████████████████████████",
        "  ████ ████ ████ ████ ████ ████ ████",
        "  ████ ████ ████ ████ ████ ████ ████",
        "██████████████████████████████████████",
        "🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿",
        "🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿"
    ]
    
    for linea in machu:
        print(linea)

def main():
    """Función principal con menú interactivo"""
    monumentos_funciones = {
        '1': torre_eiffel,
        '2': partenon,
        '3': estatua_libertad,
        '4': taj_mahal,
        '5': torre_pisa,
        '6': moai,
        '7': coliseo_romano,
        '8': sagrada_familia,
        '9': machu_picchu
    }
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("🏛️ Selecciona una opción (0-9): ").strip()
            
            if opcion == '0':
                print("\n🏛️ ¡Gracias por viajar por el mundo con ASCII! 🏛️")
                break
            elif opcion in monumentos_funciones:
                print("\n" + "="*60)
                monumentos_funciones[opcion]()
                print("="*60)
            else:
                print("❌ Opción no válida. Intenta de nuevo.")
                
        except KeyboardInterrupt:
            print("\n\n🏛️ ¡Hasta luego, viajero mundial! 🏛️")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        
        input("\n🗺️ Presiona Enter para continuar explorando...")

if __name__ == "__main__":
    main()
