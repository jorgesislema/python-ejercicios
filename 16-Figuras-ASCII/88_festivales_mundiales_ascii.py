#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 88: Festivales Mundiales ASCII
========================================

Objetivo:
- Crear representaciones de festivales culturales del mundo usando ASCII
- Explorar la diversidad cultural y tradiciones globales
- Promover el entendimiento intercultural

Conceptos aplicados:
- Diversidad cultural mundial
- Tradiciones festivas
- Patrimonio inmaterial
- Celebraciones estacionales
"""

import time
import random

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*60)
    print("🎉 GENERADOR DE FESTIVALES MUNDIALES ASCII 🎉")
    print("="*60)
    print("1. 🎆 Año Nuevo Chino")
    print("2. 🎊 Carnaval de Río")
    print("3. 🏮 Festival de Linternas")
    print("4. 🌸 Hanami (Japón)")
    print("5. 🕯️ Diwali (India)")
    print("6. 🎭 Oktoberfest (Alemania)")
    print("7. 💀 Día de Muertos (México)")
    print("8. 🔥 Holi (India)")
    print("9. 🌻 Midsummer (Suecia)")
    print("0. 🚪 Salir")
    print("-"*60)

def ano_nuevo_chino():
    """Crea celebración del Año Nuevo Chino"""
    print("🎆 AÑO NUEVO CHINO 🎆")
    print("Festival de Primavera - La celebración más importante de China")
    print()
    
    ano_chino_ascii = [
        "🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆",
        "                    🐲",
        "              🐲🐲🐲🐲🐲🐲🐲",
        "            🐲              🐲",
        "           🐲  🥟 🥟 🥟 🥟  🐲",
        "          🐲                 🐲",
        "         🐲    🏮   🏮   🏮   🐲",
        "        🐲                    🐲",
        "       🐲      🧧 恭喜发财 🧧   🐲",
        "      🐲                       🐲",
        "     🐲         👨‍👩‍👧‍👦         🐲",
        "    🐲                          🐲",
        "   🐲    🧨🧨🧨🧨🧨🧨🧨🧨🧨    🐲",
        "  🐲                            🐲",
        " 🐲🐲🐲🐲🐲🐲🐲🐲🐲🐲🐲🐲🐲🐲🐲🐲🐲🐲🐲🐲🐲🐲",
        "🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆",
        "",
        "🐲 Danza del dragón: buena fortuna",
        "🧧 Sobres rojos: dinero de la suerte",
        "🥟 Dumplings: prosperidad familiar"
    ]
    
    for linea in ano_chino_ascii:
        print(linea)

def carnaval_rio():
    """Crea el famoso Carnaval de Río"""
    print("🎊 CARNAVAL DE RÍO 🎊")
    print("La mayor fiesta del mundo - Brasil")
    print()
    
    carnaval_ascii = [
        "🎊🎉🎊🎉🎊🎉🎊🎉🎊🎉🎊🎉🎊🎉🎊🎉🎊🎉🎊",
        "  🎭                           🎭",
        "    🎭   💃🏽 SAMBA! 🕺🏽   🎭",
        "      🎭                   🎭",
        "        🎭  🥁🎺🎵🎶🎵  🎭",
        "          🎭             🎭",
        "   💃🏽      🎭 🇧🇷 🎭      🕺🏽",
        "    |         🎭   🎭         |",
        "   /|\\          🎭🎭         /|\\",
        "  / | \\                     / | \\",
        "               🥁🎺🎵",
        "      🎊    💃🏽   🕺🏽    🎊",
        "        🎊   |     |   🎊",
        "          🎊/|\\   /|\\ 🎊",
        "            / | \\ / | \\",
        "🎊🎉🎊🎉🎊🎉🎊🎉🎊🎉🎊🎉🎊🎉🎊🎉🎊🎉🎊",
        "████████████████████████████████████████",
        "",
        "💃🏽 Escolas de samba: competencia nacional",
        "🎭 Disfraces: creatividad sin límites",
        "🎵 Música: samba, batucada, alegría"
    ]
    
    for linea in carnaval_ascii:
        print(linea)

def festival_linternas():
    """Crea el Festival de Linternas asiático"""
    print("🏮 FESTIVAL DE LINTERNAS 🏮")
    print("Iluminando el cielo con deseos y esperanzas")
    print()
    
    linternas_ascii = [
        "      🌙         ⭐         ⭐",
        "   🏮     🏮         🏮     🏮",
        "     🏮 🏮     🏮 🏮     🏮 🏮",
        "        🏮         🏮         🏮",
        "  🏮         🏮         🏮",
        "    🏮     🏮     🏮     🏮",
        "       🏮     🏮     🏮",
        "   🏮     🏮         🏮     🏮",
        "      🏮         🏮         🏮",
        "          🏮   🏮   🏮",
        "     🏮     🏮 🏮 🏮     🏮",
        "        🏮       🏮       🏮",
        "   🏮       🏮     🏮       🏮",
        "      🏮       🏮 🏮       🏮",
        "         🏮   🏮   🏮   🏮",
        "    🏮     🏮   🏮   🏮     🏮",
        "       🏮     🏮 🏮     🏮",
        "🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊",
        "",
        "🏮 Deseos escritos: amor, salud, prosperidad",
        "💫 Simbolismo: liberación de preocupaciones",
        "🌏 Celebrado en: Tailandia, China, Taiwán"
    ]
    
    for linea in linternas_ascii:
        print(linea)

def hanami():
    """Crea la celebración del Hanami japonés"""
    print("🌸 HANAMI 🌸")
    print("Contemplación de las flores de cerezo - Japón")
    print()
    
    hanami_ascii = [
        "          🌸      🌸      🌸",
        "        🌸  🌸  🌸  🌸  🌸  🌸",
        "      🌸      🌸      🌸      🌸",
        "    🌸  🌸  🌸  🌸  🌸  🌸  🌸  🌸",
        "  🌸      🌸      🌸      🌸      🌸",
        "🌸  🌸  🌸  🌸  🌸  🌸  🌸  🌸  🌸",
        "████████████████████████████████████",
        "████████████████████████████████████",
        "████████████████████████████████████",
        "████████████████████████████████████",
        "          👘      👘      👘",
        "          /|\\     /|\\     /|\\",
        "         / | \\   / | \\   / | \\",
        "      🍱🍱  🍱🍱  🍱🍱  🍱🍱",
        "      🍶🍶  🍶🍶  🍶🍶  🍶🍶",
        "🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿",
        "",
        "🌸 Duración: solo 2 semanas al año",
        "🍱 Picnic tradicional: bento y sake",
        "📸 Mono no aware: belleza efímera de la vida"
    ]
    
    for linea in hanami_ascii:
        print(linea)

def diwali():
    """Crea el Festival de Luces Diwali"""
    print("🕯️ DIWALI 🕯️")
    print("Festival de Luces - Victoria del bien sobre el mal")
    print()
    
    diwali_ascii = [
        "🕯️      🕯️      🕯️      🕯️      🕯️",
        "  🕯️  🕯️  🕯️  🕯️  🕯️  🕯️  🕯️",
        "    🕯️      🕯️      🕯️      🕯️",
        "💫    ╔═══════════════════════╗    💫",
        "    ╔═╝   🕯️ RANGOLI 🕯️    ╚═╗",
        "  ╔═╝  🔴🟡🔵🟣🟢🟠🔴🟡🔵  ╚═╗",
        " ╔╝   🟡🔵🟣🟢🟠🔴🟡🔵🟣🟢   ╚╗",
        "╔╝   🔵🟣🟢🟠🔴🟡🔵🟣🟢🟠🔴   ╚╗",
        "║   🟣🟢🟠🔴🟡🔵🟣🟢🟠🔴🟡🔵   ║",
        "╚╗   🟢🟠🔴🟡🔵🟣🟢🟠🔴🟡🔵   ╔╝",
        " ╚╗   🟠🔴🟡🔵🟣🟢🟠🔴🟡🔵   ╔╝",
        "  ╚═╗  🔴🟡🔵🟣🟢🟠🔴🟡🔵  ╔═╝",
        "    ╚═╗   🕯️ LAKSHMI 🕯️   ╔═╝",
        "💫    ╚═══════════════════════╝    💫",
        "    🕯️      🕯️      🕯️      🕯️",
        "  🕯️  🕯️  🕯️  🕯️  🕯️  🕯️  🕯️",
        "🕯️      🕯️      🕯️      🕯️      🕯️",
        "",
        "💫 Diosa Lakshmi: prosperidad y fortuna",
        "🎨 Rangoli: arte decorativo con colores",
        "🪔 Diyas: lámparas de aceite tradicionales"
    ]
    
    for linea in diwali_ascii:
        print(linea)

def oktoberfest():
    """Crea el Oktoberfest alemán"""
    print("🎭 OKTOBERFEST 🎭")
    print("La fiesta de la cerveza más famosa del mundo - Múnich")
    print()
    
    oktoberfest_ascii = [
        "🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶🎵",
        "        🏰 MÜNCHEN OKTOBERFEST 🏰",
        "   👨‍🍳      🍺🍺🍺🍺🍺🍺      👩‍🍳",
        "   /|\\       🍺 PROST! 🍺       /|\\",
        "  / | \\        🍺🍺🍺🍺        / | \\",
        "             🥨🥨🥨🥨🥨🥨",
        "   🎵    🍺    🥨 MIT 🥨    🍺    🎶",
        "        /|\\    🥨SENF🥨    /|\\",
        "       / | \\   🥨🥨🥨🥨🥨   / | \\",
        "🎺🎺🎺🎺🎺🎺🎺🎺🎺🎺🎺🎺🎺🎺🎺🎺🎺🎺🎺",
        "   🍺     🎭     🥨     🎭     🍺",
        "    \\     /|\\     |     /|\\     /",
        "     \\   / | \\    |    / | \\   /",
        "      \\ /  |  \\   |   /  |  \\ /",
        "🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶🎵",
        "████████████████████████████████████",
        "",
        "🍺 Cerveza: Märzen, Weissbier, Pilsner",
        "🥨 Comida: pretzel, salchichas, chucrut",
        "🎵 Música: polka, bandas bávaras"
    ]
    
    for linea in oktoberfest_ascii:
        print(linea)

def dia_muertos():
    """Crea la celebración del Día de Muertos"""
    print("💀 DÍA DE MUERTOS 💀")
    print("Tradición mexicana - Honrando a los ancestros")
    print()
    
    muertos_ascii = [
        "           🌼 CEMPASÚCHIL 🌼",
        "      🌼    🌼    🌼    🌼    🌼",
        "   💀         OFRENDA         💀",
        " ┌─────────────────────────────────┐",
        " │  🕯️ 📸 🕯️ 👴🏽 👵🏽 🕯️ 📸 🕯️  │",
        " │                               │",
        " │  🍞 🍫 🍯 🍎 🍊 🥖 🧄 🌽  │",
        " │                               │",
        " │  💀 CALAVERAS DE AZÚCAR 💀   │",
        " │    💀    💀    💀    💀      │",
        " │                               │",
        " │  🌮 🫔 🥘 🍲 🌶️ 🥑 🫘 🧅  │",
        " │                               │",
        " │      🥃 MEZCAL 🥃           │",
        " └─────────────────────────────────┘",
        "🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼🌼",
        "",
        "💀 Catrina: elegante dama de la muerte",
        "🌼 Cempasúchil: flores para guiar almas",
        "🍞 Pan de muerto: dulce tradicional"
    ]
    
    for linea in muertos_ascii:
        print(linea)

def holi():
    """Crea el Festival de Colores Holi"""
    print("🔥 HOLI 🔥")
    print("Festival de Colores - Celebración de la primavera")
    print()
    
    holi_ascii = [
        "🔴🟡🔵🟣🟢🟠🔴🟡🔵🟣🟢🟠🔴🟡🔵🟣🟢🟠",
        "                💥HOLI HAI!💥",
        "   🟡         🔴💨💨💨🔴         🟡",
        "     🔵    💨🟣       🟣💨    🔵",
        "       🟢💨🟠           🟠💨🟢",
        "   🔴    🟡               🟡    🔴",
        "     🟣    👨‍👩‍👧‍👦 ✨ 👪    🟣",
        "   🟢      /|\\ /|\\ /|\\ /|\\      🟢",
        "     🟠   / | / | \\ | \\ | \\   🟠",
        "   🔵                           🔵",
        "     🟡  💨🔴🟣🟢🟠🔴🟣🟢💨  🟡",
        "   🟣      💨🔴     🔴💨      🟣",
        "     🟢      💨🟡 🟡💨      🟢",
        "   🟠          💨💨💨          🟠",
        "🔴🟡🔵🟣🟢🟠🔴🟡🔵🟣🟢🟠🔴🟡🔵🟣🟢🟠",
        "🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿",
        "",
        "🌈 Gulal: polvos coloridos naturales",
        "🔥 Holika Dahan: hoguera purificadora",
        "💃 Danza: celebración comunitaria"
    ]
    
    for linea in holi_ascii:
        print(linea)

def midsummer():
    """Crea el festival Midsummer sueco"""
    print("🌻 MIDSUMMER 🌻")
    print("Celebración del solsticio de verano - Suecia")
    print()
    
    midsummer_ascii = [
        "              ☀️ SOL DE MEDIANOCHE ☀️",
        "    🌻      🌻      🌻      🌻      🌻",
        "  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻",
        "              🌸MIDSOMMAR🌸",
        "             ┌─────────────┐",
        "             │      🌸     │",
        "             │   🌸🌸🌸   │",
        "             │  🌸🌸🌸🌸  │",
        "             │ 🌸🌸🌸🌸🌸 │",
        "             │  🌸🌸🌸🌸  │",
        "             │   🌸🌸🌸   │",
        "             │      🌸     │",
        "             └─────┬───────┘",
        "                   ║",
        "          💃🏼      ║      🕺🏼",
        "          /|\\     ████     /|\\",
        "         / | \\             / | \\",
        "   🎵  💃🏼   🕺🏼   💃🏼   🕺🏼  🎶",
        "      /|\\ /|\\ /|\\ /|\\",
        "     / | / | \\ | \\ | \\",
        "🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻",
        "",
        "🌸 Midsommarstång: poste decorado con flores",
        "💃🏼 Danzas: rondas tradicionales suecas",
        "🐟 Comida: arenque, patatas nuevas, aquavit"
    ]
    
    for linea in midsummer_ascii:
        print(linea)

def main():
    """Función principal con menú interactivo"""
    festivales_funciones = {
        '1': ano_nuevo_chino,
        '2': carnaval_rio,
        '3': festival_linternas,
        '4': hanami,
        '5': diwali,
        '6': oktoberfest,
        '7': dia_muertos,
        '8': holi,
        '9': midsummer
    }
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("🎉 Selecciona una opción (0-9): ").strip()
            
            if opcion == '0':
                print("\n🎉 ¡Gracias por celebrar la diversidad cultural mundial! 🎉")
                print("🌍 ¡Que todos los festivales llenen tu vida de alegría! 🌍")
                break
            elif opcion in festivales_funciones:
                print("\n" + "="*60)
                festivales_funciones[opcion]()
                print("="*60)
            else:
                print("❌ Opción no válida. Intenta de nuevo.")
                
        except KeyboardInterrupt:
            print("\n\n🎉 ¡Hasta luego, viajero cultural! 🎉")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        
        input("\n🌈 Presiona Enter para continuar celebrando...")

if __name__ == "__main__":
    main()
