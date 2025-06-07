"""
Ejercicio 38: Espacios y Planetas ASCII

Objetivo:
- Crear sistema solar completo en ASCII
- Incluir planetas, estrellas y galaxias
- Simular órbitas planetarias
- Crear escenas espaciales épicas

Conceptos:
- Astronomía ASCII
- Escalas espaciales
- Movimiento orbital
- Exploración espacial
"""

def sistema_solar():
    """Sistema solar completo"""
    print("🌌 SISTEMA SOLAR 🌌")
    print("═" * 80)
    
    sistema = [
        "                           ☀️ SOL ☀️",
        "                      (Estrella central)",
        "",
        "        ☿               🌍              ♂️",
        "    Mercurio          Tierra           Marte",
        "     (58M km)         (150M km)       (228M km)",
        "",
        "    ♀️                    🪐              ♃",
        "   Venus              Saturno         Júpiter",
        "  (108M km)            (1.4B km)      (778M km)",
        "",
        "         ♅                    ♆",
        "       Urano                Neptuno",
        "      (2.9B km)            (4.5B km)",
        "",
        "                    ⭐ ⭐ ⭐",
        "                 Cinturón de asteroides",
        "",
        "    🌑🌒🌓🌔🌕🌖🌗🌘",
        "       Fases lunares",
        "",
        "              🛸 🚀 🛰️",
        "         Exploración espacial"
    ]
    
    for linea in sistema:
        print(linea)
    
    print("\n🌌 Nuestro hogar cósmico 🌌")

def planeta_tierra():
    """Planeta Tierra detallado"""
    print("🌍 PLANETA TIERRA 🌍")
    print("═" * 40)
    
    tierra = [
        "        ╭─────────╮",
        "       ╱           ╲",
        "      ╱  🌍 🌊 🌿  ╲",
        "     ╱               ╲",
        "    ╱ 🏔️  🌊  🌍  🏜️ ╲",
        "   ╱                   ╲",
        "  ╱  🌿  🌊  🏔️  🌍   ╲",
        " ╱                     ╲",
        "╱ 🌊  🌿  🌍  🌊  🏔️  ╲",
        "║                       ║",
        "║ 🏜️  🌍  🌊  🌿  🌊  ║",
        "║                       ║",
        "╲ 🌍  🏔️  🌿  🌊  🏜️  ╱",
        " ╲                     ╱",
        "  ╲  🌊  🌍  🏔️  🌿   ╱",
        "   ╲                   ╱",
        "    ╲ 🌿  🌊  🌍  🏔️ ╱",
        "     ╲               ╱",
        "      ╲  🌊 🌍 🌿  ╱",
        "       ╲           ╱",
        "        ╲_________╱",
        "",
        "        🌙 LUNA 🌙",
        "      ╭─────────╮",
        "     ╱ ●   ●   ● ╲",
        "    ╱ ●  🌙  ●  ● ╲",
        "   ╱ ●   ●   ●   ● ╲",
        "  ╱ ●  ●  ●  ●  ●  ╲",
        " ╱___________________╲",
        "╱_____________________╲",
        "╲_____________________╱",
        " ╲___________________╱",
        "  ╲_________________╱",
        "   ╲_______________╱",
        "    ╲_____________╱",
        "     ╲___________╱",
        "      ╲_________╱"
    ]
    
    for linea in tierra:
        print(linea)
    
    print("\n🌍 El planeta azul 🌍")
    print("💧 71% océanos, 29% tierra")

def jupiter_gigante():
    """Júpiter el gigante gaseoso"""
    print("♃ JÚPITER - EL GIGANTE ♃")
    print("═" * 50)
    
    jupiter = [
        "           ╭─────────────────╮",
        "          ╱                   ╲",
        "         ╱  ═══════════════   ╲",
        "        ╱   ♃ ═══════════ ♃   ╲",
        "       ╱    ═══════════════    ╲",
        "      ╱     ═══════════════     ╲",
        "     ╱      ═══════════════      ╲",
        "    ╱       ═══════════════       ╲",
        "   ╱        ═══════════════        ╲",
        "  ╱         ═══════════════         ╲",
        " ╱          ═══ 🌀 ═══════          ╲",
        "╱           ═══════════════           ╲",
        "║           ═══════════════           ║",
        "║          ♃ ═══════════ ♃          ║",
        "║           ═══════════════           ║",
        "╲           ═══════════════           ╱",
        " ╲          ═══════════════          ╱",
        "  ╲         ═══════════════         ╱",
        "   ╲        ═══════════════        ╱",
        "    ╲       ═══════════════       ╱",
        "     ╲      ═══════════════      ╱",
        "      ╲     ═══════════════     ╱",
        "       ╲    ═══════════════    ╱",
        "        ╲   ═══════════════   ╱",
        "         ╲  ═══════════════  ╱",
        "          ╲                 ╱",
        "           ╲_______________╱",
        "",
        "    🌙🌙🌙🌙   LUNAS   🌙🌙🌙🌙",
        "   Ío  Europa  Ganímedes  Calisto",
        "",
        "🌀 Gran Mancha Roja - Tormenta gigante",
        "⚡ Más grande que la Tierra"
    ]
    
    for linea in jupiter:
        print(linea)
    
    print("\n♃ El protector del sistema solar ♃")
    print("🛡️ Su gravedad desvía asteroides")

def saturno_anillos():
    """Saturno con sus anillos"""
    print("🪐 SATURNO - SEÑOR DE LOS ANILLOS 🪐")
    print("═" * 60)
    
    saturno = [
        "          ═══════════════════════════",
        "         ═══════════════════════════",
        "        ═══════════════════════════",
        "       ╱═══════════════════════════╲",
        "      ╱                             ╲",
        "     ╱    ═══════════════════════    ╲",
        "    ╱     🪐 ═══════════════ 🪐     ╲",
        "   ╱      ═══════════════════════      ╲",
        "  ╱       ═══════════════════════       ╲",
        " ╱        ═══════════════════════        ╲",
        "╱         ═══════════════════════         ╲",
        "║         ═══════════════════════         ║",
        "║        🪐 ═══════════════ 🪐        ║",
        "║         ═══════════════════════         ║",
        "╲         ═══════════════════════         ╱",
        " ╲        ═══════════════════════        ╱",
        "  ╲       ═══════════════════════       ╱",
        "   ╲      ═══════════════════════      ╱",
        "    ╲     ═══════════════════════     ╱",
        "     ╲    ═══════════════════════    ╱",
        "      ╲                             ╱",
        "       ╲═══════════════════════════╱",
        "        ═══════════════════════════",
        "         ═══════════════════════════",
        "          ═══════════════════════════",
        "",
        "        💍 ANILLOS ESPECTACULARES 💍",
        "       🧊 Compuestos de hielo y roca 🧊",
        "",
        "      🌙 Titán - Luna con atmósfera 🌙",
        "     🌙 Encélado - Géiseres de agua 🌙"
    ]
    
    for linea in saturno:
        print(linea)
    
    print("\n🪐 La joya del sistema solar 🪐")
    print("💎 Densidad menor que el agua")

def sol_estrella():
    """El Sol - nuestra estrella"""
    print("☀️ EL SOL - NUESTRA ESTRELLA ☀️")
    print("═" * 60)
    
    sol = [
        "    ╲  |  ╱      ╲  |  ╱      ╲  |  ╱",
        "     ╲ | ╱        ╲ | ╱        ╲ | ╱",
        "   ═══╲|╱═══    ═══╲|╱═══    ═══╲|╱═══",
        "       ╲╱           ╲╱           ╲╱",
        "         ╭─────────────────╮",
        "        ╱                   ╲",
        "       ╱  🔥🔥🔥🔥🔥🔥🔥🔥🔥  ╲",
        "      ╱ 🔥                 🔥 ╲",
        "     ╱ 🔥   ☀️ ☀️ ☀️ ☀️   🔥 ╲",
        "    ╱ 🔥  ☀️           ☀️  🔥 ╲",
        "   ╱ 🔥  ☀️     ☀️     ☀️  🔥 ╲",
        "  ╱ 🔥  ☀️   ☀️ ☀️ ☀️   ☀️  🔥 ╲",
        " ╱ 🔥  ☀️  ☀️       ☀️  ☀️  🔥 ╲",
        "╱ 🔥  ☀️ ☀️  ☀️ ☀️ ☀️  ☀️ ☀️  🔥 ╲",
        "║🔥  ☀️ ☀️ ☀️ ☀️ ☀️ ☀️ ☀️ ☀️ ☀️  🔥║",
        "║ 🔥 ☀️ ☀️ ☀️ ☀️ ☀️ ☀️ ☀️ ☀️ 🔥 ║",
        "╲ 🔥  ☀️ ☀️  ☀️ ☀️ ☀️  ☀️ ☀️  🔥 ╱",
        " ╲ 🔥  ☀️  ☀️       ☀️  ☀️  🔥 ╱",
        "  ╲ 🔥  ☀️   ☀️ ☀️ ☀️   ☀️  🔥 ╱",
        "   ╲ 🔥  ☀️     ☀️     ☀️  🔥 ╱",
        "    ╲ 🔥  ☀️           ☀️  🔥 ╱",
        "     ╲ 🔥   ☀️ ☀️ ☀️ ☀️   🔥 ╱",
        "      ╲ 🔥                 🔥 ╱",
        "       ╲  🔥🔥🔥🔥🔥🔥🔥🔥🔥  ╱",
        "        ╲                   ╱",
        "         ╲_________________╱",
        "       ╱╲           ╱╲           ╱╲",
        "   ═══╱ |╲═══    ═══╱ |╲═══    ═══╱ |╲═══",
        "     ╱  |  ╲      ╱  |  ╲      ╱  |  ╲",
        "    ╱   |   ╲    ╱   |   ╲    ╱   |   ╲"
    ]
    
    for linea in sol:
        print(linea)
    
    print("\n☀️ DATOS SOLARES ☀️")
    print("🌡️ Temperatura: 5,778 K en superficie")
    print("⚡ Fusión nuclear: 4 millones toneladas/segundo")
    print("💡 Energía que llega a la Tierra en 1 hora")
    print("   podría abastecer al mundo por 1 año")

def galaxia_via_lactea():
    """La Vía Láctea"""
    print("🌌 VÍA LÁCTEA - NUESTRA GALAXIA 🌌")
    print("═" * 70)
    
    galaxia = [
        "                    ⭐ ⭐ ⭐ ⭐ ⭐",
        "                 ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐",
        "              ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐",
        "           ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐",
        "        ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐",
        "     ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐",
        "  ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ 🕳️ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐",
        "⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐",
        "  ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐",
        "     ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐",
        "        ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐",
        "           ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐",
        "              ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐",
        "                 ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐",
        "                    ⭐ ⭐ ⭐ ⭐ ⭐",
        "",
        "         🕳️ CENTRO GALÁCTICO 🕳️",
        "        (Agujero negro supermasivo)",
        "",
        "    🌟 400 mil millones de estrellas 🌟",
        "      ☀️ Nuestro Sol está aquí ☀️",
        "        ↗️ Brazo de Orión ↖️",
        "",
        "   🌌 Diámetro: 100,000 años luz 🌌",
        "     🔄 Rotación: 225 millones años 🔄"
    ]
    
    for linea in galaxia:
        print(linea)
    
    print("\n🌌 Nuestro hogar galáctico 🌌")

def naves_espaciales():
    """Naves espaciales y exploración"""
    print("🚀 EXPLORACIÓN ESPACIAL 🚀")
    print("═" * 60)
    
    naves = [
        "           🚀 COHETE SATURNO V 🚀",
        "              (Misiones Apollo)",
        "                   ▲",
        "                  ╱ ╲",
        "                 ╱ 🚀 ╲",
        "                ╱_____╲",
        "                ║     ║",
        "                ║  🧑‍🚀  ║",
        "                ║     ║",
        "                ╠═════╣",
        "                ║     ║",
        "                ║ ⛽  ║",
        "                ║     ║",
        "                ╠═════╣",
        "                ║     ║",
        "                ║ ⛽  ║",
        "                ║     ║",
        "                ╚═════╝",
        "               🔥🔥🔥🔥🔥",
        "",
        "🛸 NAVE ESPACIAL FUTURISTA 🛸",
        "         ╭───────────╮",
        "        ╱             ╲",
        "       ╱ 👽 🛸 👽 🛸 ╲",
        "      ╱_________________╲",
        "     ╱___________________╲",
        "    ╱_____________________╲",
        "   ═══════════════════════════",
        "  💫                         💫",
        "",
        "    🛰️ ESTACIÓN ESPACIAL 🛰️",
        "      ═══╦═══════════╦═══",
        "         ║  🔬 👨‍🚀 🔬  ║",
        "         ║           ║",
        "      🌞═╩═══════════╩═🌍",
        "         ║           ║",
        "         ║  📡 🛰️ 📡  ║",
        "      ═══╩═══════════╩═══"
    ]
    
    for linea in naves:
        print(linea)
    
    print("\n🚀 La conquista del espacio 🚀")
    print("🌟 Explorando lo desconocido 🌟")

def sistema_animado():
    """Sistema solar con órbitas animadas"""
    import time
    import os
    
    print("🌌 ÓRBITAS PLANETARIAS 🌌")
    
    for i in range(12):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🌌 SISTEMA SOLAR EN MOVIMIENTO 🌌")
        print("═" * 60)
        
        # Posiciones orbitales
        mercurio_pos = i % 8
        venus_pos = i % 10
        tierra_pos = i % 12
        marte_pos = i % 16
        
        orbita = [' '] * 40
        
        # Colocar Sol en el centro
        orbita[20] = '☀️'
        
        # Colocar planetas en sus órbitas
        if mercurio_pos < 4:
            orbita[16 + mercurio_pos] = '☿'
        elif mercurio_pos < 6:
            orbita[19 + (mercurio_pos - 4)] = '☿'
        else:
            orbita[21 + (8 - mercurio_pos)] = '☿'
        
        if venus_pos < 5:
            orbita[13 + venus_pos] = '♀️'
        elif venus_pos < 8:
            orbita[18 + (venus_pos - 5)] = '♀️'
        else:
            orbita[21 + (10 - venus_pos)] = '♀️'
        
        print("".join(orbita))
        
        # Mostrar información
        print(f"\nFrame: {i+1}/12")
        print("☿ Mercurio  ♀️ Venus  🌍 Tierra  ♂️ Marte")
        print("Velocidades orbitales diferentes")
        
        time.sleep(0.8)

def menu_principal():
    """Menú principal del programa"""
    while True:
        print("\n" + "═" * 60)
        print("🌌 OBSERVATORIO ASTRONÓMICO ASCII 🌌")
        print("═" * 60)
        print("1. Sistema solar")
        print("2. Planeta Tierra")
        print("3. Júpiter gigante")
        print("4. Saturno y sus anillos")
        print("5. El Sol - nuestra estrella")
        print("6. Vía Láctea")
        print("7. Naves espaciales")
        print("8. Sistema animado")
        print("0. Salir")
        print("═" * 60)
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            sistema_solar()
        elif opcion == "2":
            planeta_tierra()
        elif opcion == "3":
            jupiter_gigante()
        elif opcion == "4":
            saturno_anillos()
        elif opcion == "5":
            sol_estrella()
        elif opcion == "6":
            galaxia_via_lactea()
        elif opcion == "7":
            naves_espaciales()
        elif opcion == "8":
            sistema_animado()
        elif opcion == "0":
            print("¡Que las estrellas te guíen! 🌟")
            break
        else:
            print("Opción no válida")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
