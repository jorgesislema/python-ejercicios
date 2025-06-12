"""
Ejercicio 51: Monumentos Mundiales ASCII

Objetivo:
- Crear representaciones ASCII de monumentos famosos del mundo
- Incluir variantes: Torre Eiffel, Estatua de la Libertad, Coliseo, etc.
- Permitir personalización y mostrar datos históricos

Conceptos:
- Arte ASCII de arquitectura mundial
- Representación de patrimonio cultural
- Historia y geografía visual
"""

def torre_eiffel_ascii():
    """Torre Eiffel ASCII"""
    print("🗼 TORRE EIFFEL ASCII 🗼")
    print("═" * 50)
    
    torre = [
        "           ╱▲╲",
        "          ╱  ╲",
        "         ╱    ╲",
        "        ╱      ╲",
        "       ╱________╲",
        "      ╱          ╲",
        "     ╱   ╱────╲   ╲",
        "    ╱   ╱      ╲   ╲",
        "   ╱   ╱   🗼   ╲   ╲",
        "  ╱   ╱__________╲   ╲",
        " ╱   ╱            ╲   ╲",
        "╱   ╱              ╲   ╲",
        "╲  ╱________________╲  ╱",
        " ╲╱__________________╲╱",
        "    ■              ■",
        "    ■              ■",
        "    ■              ■",
        "    ■■■■■■■■■■■■■■■■■■"
    ]
    
    for linea in torre:
        print(linea)
    
    print("\n🗼 Torre Eiffel - París, Francia")
    print("📏 Altura: 330 metros")
    print("📅 Construida: 1887-1889")
    print("👷 Arquitecto: Gustave Eiffel")

def estatua_libertad_ascii():
    """Estatua de la Libertad ASCII"""
    print("🗽 ESTATUA DE LA LIBERTAD ASCII 🗽")
    print("═" * 50)
    
    estatua = [
        "         ╱🔥╲",
        "        ╱   ╲",
        "       ╱  ★  ╲",
        "      ╱_______╲",
        "     ╱ ▲ ▲ ▲ ▲ ╲",
        "    ╱  ◉     ◉  ╲",
        "   ╱     ___     ╲",
        "  ╱      ╲_╱      ╲",
        " ╱_________________╲",
        "│       🗽        │",
        "│    ╱─────╲      │",
        "│   ╱       ╲     │",
        "│  │    📜   │    │",
        "│   ╲       ╱     │",
        "│    ╲_____╱      │",
        "╰─────────────────╯",
        "      ■■■■■■■",
        "      ■■■■■■■"
    ]
    
    for linea in estatua:
        print(linea)
    
    print("\n🗽 Estatua de la Libertad - Nueva York, EE.UU.")
    print("📏 Altura: 93 metros (con pedestal)")
    print("📅 Inaugurada: 1886")
    print("🎁 Regalo de Francia a Estados Unidos")

def coliseo_romano_ascii():
    """Coliseo Romano ASCII"""
    print("🏛️ COLISEO ROMANO ASCII 🏛️")
    print("═" * 60)
    
    coliseo = [
        "       ╭─────────────────────╮",
        "      ╱  ╭─╮ ╭─╮ ╭─╮ ╭─╮  ╲",
        "     ╱  ╱   ╲╱   ╲╱   ╲╱   ╲ ╲",
        "    ╱  │ ◉ ││ ◉ ││ ◉ ││ ◉ │ ╲",
        "   ╱   ╲___╱╲___╱╲___╱╲___╱   ╲",
        "  ╱    ╭─╮ ╭─╮ ╭─╮ ╭─╮ ╭─╮    ╲",
        " ╱    ╱   ╲╱   ╲╱   ╲╱   ╲╱    ╲",
        "│     │ ○ ││ ○ ││ ○ ││ ○ ││     │",
        "│     ╲___╱╲___╱╲___╱╲___╱╲     │",
        "│      ╭─╮ ╭─╮ ╭─╮ ╭─╮ ╭─╮     │",
        "│     ╱   ╲╱   ╲╱   ╲╱   ╲╱    │",
        "│     │ ◦ ││ ◦ ││ ◦ ││ ◦ ││     │",
        " ╲    ╲___╱╲___╱╲___╱╲___╱╲    ╱",
        "  ╲____________________________╱",
        "      ■■■■■■■■■■■■■■■■■■■■",
        "      ■■■■■■■■■■■■■■■■■■■■"
    ]
    
    for linea in coliseo:
        print(linea)
    
    print("\n🏛️ Coliseo Romano - Roma, Italia")
    print("📏 Capacidad: 50,000-80,000 espectadores")
    print("📅 Construido: 70-80 d.C.")
    print("⚔️ Sede de combates de gladiadores")

def piramides_giza_ascii():
    """Pirámides de Giza ASCII"""
    print("🔺 PIRÁMIDES DE GIZA ASCII 🔺")
    print("═" * 60)
    
    piramides = [
        "        ▲                    ▲",
        "       ╱ ╲                  ╱ ╲",
        "      ╱   ╲       ▲        ╱   ╲",
        "     ╱  🔺 ╲     ╱ ╲      ╱ 🔺  ╲",
        "    ╱_______╲   ╱   ╲    ╱_______╲",
        "   ╱         ╲ ╱ 🔺  ╲  ╱         ╲",
        "  ╱           ╲╱_______╲╱           ╲",
        " ╱_____________╲       ╱_____________╲",
        "╱_______________╲_____╱_______________╲",
        "■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■",
        "🐪      🌵    🏺    🌵      🐪"
    ]
    
    for linea in piramides:
        print(linea)
    
    print("\n🔺 Pirámides de Giza - Egipto")
    print("👑 Keops, Kefrén y Micerinos")
    print("📅 Construidas: ~2580-2510 a.C.")
    print("🏺 Una de las 7 Maravillas del Mundo Antiguo")

def gran_muralla_china_ascii():
    """Gran Muralla China ASCII"""
    print("🏯 GRAN MURALLA CHINA ASCII 🏯")
    print("═" * 60)
    
    muralla = [
        "╭───╮   ╭───╮   ╭───╮   ╭───╮   ╭───╮",
        "│🏯│   │🏯│   │🏯│   │🏯│   │🏯│",
        "│   │═══│   │═══│   │═══│   │═══│   │",
        "│   ║   │   ║   │   ║   │   ║   │   │",
        "│   ║   │   ║   │   ║   │   ║   │   │",
        "╰───╨───╯   ╰───╨───╯   ╰───╨───╯   ╰─",
        "    ╱╲       ╱╲       ╱╲       ╱╲",
        "   ╱  ╲     ╱  ╲     ╱  ╲     ╱  ╲",
        "  ╱____╲___╱____╲___╱____╲___╱____╲",
        "  🏔️    🌲    🏔️    🌲    🏔️    🌲"
    ]
    
    for linea in muralla:
        print(linea)
    
    print("\n🏯 Gran Muralla China")
    print("📏 Longitud: ~21,000 km")
    print("📅 Construida: Siglos VII a.C. - XVII d.C.")
    print("🛡️ Defensa contra invasiones del norte")

def taj_mahal_ascii():
    """Taj Mahal ASCII"""
    print("🕌 TAJ MAHAL ASCII 🕌")
    print("═" * 50)
    
    taj = [
        "          ☪️",
        "         ╱ ╲",
        "        ╱   ╲",
        "       ╱ 🕌  ╲",
        "      ╱_______╲",
        "     ╱         ╲",
        "    ╱           ╲",
        "   ╱    ╭───╮    ╲",
        "  ╱    ╱ ⬜  ╲    ╲",
        " ╱    ╱   ♦   ╲    ╲",
        "╱____╱_________╲____╲",
        "│ ⬜ │    🕌    │ ⬜ │",
        "│    │  ╱───╲  │    │",
        "│ ♦  │ ╱ ⬜  ╲ │  ♦ │",
        "│____│╱_______╲│____│",
        "■■■■■■■■■■■■■■■■■■■■■"
    ]
    
    for linea in taj:
        print(linea)
    
    print("\n🕌 Taj Mahal - Agra, India")
    print("💕 Mausoleo en honor a Mumtaz Mahal")
    print("📅 Construido: 1632-1653")
    print("🏛️ Patrimonio de la Humanidad")

def cristo_redentor_ascii():
    """Cristo Redentor ASCII"""
    print("✝️ CRISTO REDENTOR ASCII ✝️")
    print("═" * 50)
    
    cristo = [
        "         ╱─────╲",
        "        ╱   ○   ╲",
        "       ╱    │    ╲",
        "      ╱     │     ╲",
        "     ╱──────┼──────╲",
        "    ╱       │       ╲",
        "   ╱     ✝️ │ ✝️     ╲",
        "  ╱         │         ╲",
        " ╱          │          ╲",
        "╱___________│___________╲",
        "            │",
        "            │",
        "            │",
        "         ╱──┴──╲",
        "        ╱      ╲",
        "       ╱________╲",
        "       ■■■■■■■■■■",
        "    🌴    🏔️    🌴"
    ]
    
    for linea in cristo:
        print(linea)
    
    print("\n✝️ Cristo Redentor - Río de Janeiro, Brasil")
    print("📏 Altura: 38 metros")
    print("📅 Inaugurado: 1931")
    print("🏔️ Ubicado en el Cerro del Corcovado")

def machu_picchu_ascii():
    """Machu Picchu ASCII"""
    print("🏔️ MACHU PICCHU ASCII 🏔️")
    print("═" * 60)
    
    machu = [
        "      🏔️           🏔️           🏔️",
        "    ╱    ╲       ╱    ╲       ╱    ╲",
        "   ╱      ╲     ╱      ╲     ╱      ╲",
        "  ╱  ▲▲▲   ╲   ╱  ▲▲▲   ╲   ╱  ▲▲▲  ╲",
        " ╱  ▲ ▲ ▲   ╲ ╱  ▲ ▲ ▲   ╲ ╱  ▲ ▲ ▲  ╲",
        "╱___▲▲▲▲▲____╲╱___▲▲▲▲▲____╲╱___▲▲▲▲▲___╲",
        "│ ┌─┐ ┌─┐ ┌─┐ ││ ┌─┐ ┌─┐ ┌─┐ ││ ┌─┐ ┌─┐ ┌─┐ │",
        "│ │ │ │ │ │ │ ││ │ │ │ │ │ │ ││ │ │ │ │ │ │ │",
        "│ └─┘ └─┘ └─┘ ││ └─┘ └─┘ └─┘ ││ └─┘ └─┘ └─┘ │",
        "╰───────────────╲╱─────────────╲╱─────────────╯",
        "                 ╲             ╱",
        "                  ╲___________╱",
        "                  ☁️  ☁️  ☁️",
        "            🦙        🌿      🦙"
    ]
    
    for linea in machu:
        print(linea)
    
    print("\n🏔️ Machu Picchu - Cusco, Perú")
    print("⛰️ Ciudad perdida de los Incas")
    print("📅 Construida: ~1450 d.C.")
    print("🦙 Patrimonio de la Humanidad")

def menu_principal():
    """Menú principal del programa"""
    while True:
        print("\n" + "═" * 60)
        print("🗼 MONUMENTOS MUNDIALES ASCII 🏛️")
        print("═" * 60)
        print("1. Torre Eiffel (Francia)")
        print("2. Estatua de la Libertad (EE.UU.)")
        print("3. Coliseo Romano (Italia)")
        print("4. Pirámides de Giza (Egipto)")
        print("5. Gran Muralla China")
        print("6. Taj Mahal (India)")
        print("7. Cristo Redentor (Brasil)")
        print("8. Machu Picchu (Perú)")
        print("0. Salir")
        print("═" * 60)
        
        opcion = input("Selecciona un monumento: ")
        
        if opcion == "1":
            torre_eiffel_ascii()
        elif opcion == "2":
            estatua_libertad_ascii()
        elif opcion == "3":
            coliseo_romano_ascii()
        elif opcion == "4":
            piramides_giza_ascii()
        elif opcion == "5":
            gran_muralla_china_ascii()
        elif opcion == "6":
            taj_mahal_ascii()
        elif opcion == "7":
            cristo_redentor_ascii()
        elif opcion == "8":
            machu_picchu_ascii()
        elif opcion == "0":
            print("¡Hasta luego, viajero! 🌍")
            break
        else:
            print("Opción no válida")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
