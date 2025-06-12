#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 100: Galería de Arte ASCII - Celebración Final
========================================================

Objetivo:
- Crear una galería de arte ASCII que celebre la culminación de 100 ejercicios
- Combinar elementos de todos los ejercicios anteriores
- Demostrar la versatilidad y creatividad del arte ASCII

Conceptos aplicados:
- Arte ASCII avanzado
- Composición visual
- Integración de elementos
- Celebración del aprendizaje
"""

import time
import random

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*70)
    print("🎨 GALERÍA DE ARTE ASCII - EJERCICIO 100 🎨")
    print("🏆 ¡CELEBRACIÓN FINAL DE 100 EJERCICIOS! 🏆")
    print("="*70)
    print("1. 🖼️ Cuadro del Universo")
    print("2. 🏛️ Museo de las Civilizaciones")
    print("3. 🌍 Mapa del Mundo ASCII")
    print("4. 🎭 Teatro de la Vida")
    print("5. 🌈 Arcoíris de Emociones")
    print("6. 🚀 Viaje a través del Tiempo")
    print("7. 🎼 Sinfonía Visual")
    print("8. 🌟 Constelación de Logros")
    print("9. 🎉 Gran Celebración Final")
    print("0. 🚪 Salir")
    print("-"*70)

def cuadro_universo():
    """Crea un cuadro que representa todo el universo"""
    print("🖼️ CUADRO DEL UNIVERSO 🖼️")
    print("Una representación completa del cosmos y la vida")
    print()
    
    universo = [
        "╔══════════════════════════════════════════════════════════════╗",
        "║                    🌌 EL UNIVERSO 🌌                        ║",
        "║                                                              ║",
        "║  ⭐ ☀️      🌍 🌙        🪐 ⭐      🌟 💫                 ║",
        "║     ⭐  🌞     🌊🌊     🌙   🪐🪐     ⭐⭐               ║",
        "║  🌟    🔥🔥   🏔️🏔️🏔️   🌛    🌌    💫   ⭐           ║",
        "║    ☀️   🌋   🌲🌲🌲🌲🌲   🌚      🌟    ⭐    🌟        ║",
        "║  ⭐   💥    🦁🦓🐘🦒      💫  🛸        💫   ⭐         ║",
        "║     🌟 ☄️   👨‍👩‍👧‍👦 🏠 🏢 🏭     🌟      ☀️     ⭐        ║",
        "║  💫    🌠   🚗🚢✈️🚀        ⭐   🌌       🌟          ║",
        "║    ⭐   🔬💻📱🎭🎨🎵        💫    ⭐   💫    ⭐       ║",
        "║  🌟    🌈❤️💖🕊️🌸💫          🌟       ⭐   🌟        ║",
        "║     ⭐    💭💡🔮✨             ⭐   💫      ⭐         ║",
        "║  💫      🙏🕯️🎯🏆                🌟   ⭐    💫       ║",
        "║    🌟      ∞ ♾️ ⚛️                  ⭐     🌟        ║",
        "║       ⭐                              💫    ⭐       ║",
        "║                                                              ║",
        "╚══════════════════════════════════════════════════════════════╝",
        "",
        "🎨 Obra: 'La Totalidad de la Existencia'",
        "👨‍🎨 Artista: Tu creatividad con ASCII",
        "📅 Año: 2024 - Ejercicio 100"
    ]
    
    for linea in universo:
        print(linea)

def museo_civilizaciones():
    """Crea un museo con elementos de todas las civilizaciones"""
    print("🏛️ MUSEO DE LAS CIVILIZACIONES 🏛️")
    print("Un recorrido por la historia humana")
    print()
    
    museo = [
        "🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️",
        "║                 MUSEO MUNDIAL                        ║",
        "║                                                      ║",
        "║ SALA 1: ANTIGÜEDAD                                   ║",
        "║ 🏺 🗿 🏛️ 🐫 🦅 📜 ⚱️ 🕌 ⛩️ 🗼                     ║",
        "║                                                      ║",
        "║ SALA 2: NATURALEZA                                   ║",
        "║ 🌋 🌊 🏔️ 🌲 🦁 🐧 🦋 🌸 🌙 ☀️ ⭐                   ║",
        "║                                                      ║",
        "║ SALA 3: TECNOLOGÍA                                   ║",
        "║ 💡 📞 🚗 ✈️ 📺 💻 🌐 📱 🚀 🤖 🧬                   ║",
        "║                                                      ║",
        "║ SALA 4: ARTE Y CULTURA                               ║",
        "║ 🎭 🎨 🎵 🎪 🎬 📚 🖼️ 🎼 🎯 🏆 🎉                   ║",
        "║                                                      ║",
        "║ SALA 5: DEPORTES Y JUEGOS                            ║",
        "║ ⚽ 🏀 🎾 🏊‍♂️ 🚴‍♀️ 🥊 🏹 🎯 ♟️ 🎮 🎲                   ║",
        "║                                                      ║",
        "║ SALA 6: FUTURO                                       ║",
        "║ 🛸 🌌 🔮 ⚛️ 🧪 🌍 💫 ✨ 🌟 💎 ♾️                   ║",
        "🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️🏛️",
        "",
        "🎓 Has completado un viaje por 100 ejercicios",
        "🏆 Cada sala representa temas que dominaste",
        "📖 Tu conocimiento en ASCII art es completo"
    ]
    
    for linea in museo:
        print(linea)

def mapa_mundo():
    """Crea un mapa ASCII del mundo con elementos culturales"""
    print("🌍 MAPA DEL MUNDO ASCII 🌍")
    print("Nuestro hogar: Planeta Tierra con diversidad cultural")
    print()
    
    mapa = [
        "                    🌍 PLANETA TIERRA 🌍",
        "    🇺🇸🗽       🇬🇧🎡      🇷🇺🏰       🇨🇳🐲",
        "  🇨🇦🍁           🇫🇷🗼      🇩🇪🍺       🇯🇵🌸",
        "    🇲🇽💀         🇪🇸💃      🇮🇹🍕       🇰🇷🎮",
        "                                            🇹🇭🏮",
        "  🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊",
        "    🇧🇷⚽         🇳🇬🥁      🇪🇬🏺       🇮🇳🕯️",
        "    🇦🇷🥩         🇿🇦💎      🇦🇪🕌       🇲🇾🌴",
        "    🇨🇱🏔️         🇲🇦🐪      🇰🇪🦁       🇮🇩🌋",
        "                                            🇵🇭🏝️",
        "  🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊",
        "                              🇦🇺🦘       🇳🇿🥝",
        "                              🇦🇶🐧",
        "══════════════════════════════════════════════════════",
        "🌈 DIVERSIDAD: Cada país aporta su cultura única",
        "🤝 UNIDAD: Todos compartimos el mismo planeta",
        "💙 AMOR: El arte ASCII conecta culturas"
    ]
    
    for linea in mapa:
        print(linea)

def teatro_vida():
    """Crea un teatro que representa las etapas de la vida"""
    print("🎭 TEATRO DE LA VIDA 🎭")
    print("Obra en tres actos: Pasado, Presente y Futuro")
    print()
    
    teatro = [
        "          🎭 GRAN TEATRO DE LA VIDA 🎭",
        "    ╔════════════════════════════════════════╗",
        "    ║  🎬 ACTO I: EL PASADO 🏺               ║",
        "    ║    🦕 → 🗿 → 🏛️ → 🏰 → ⚔️            ║",
        "    ║                                        ║",
        "    ║  🎬 ACTO II: EL PRESENTE 🌍           ║",
        "    ║    👶 → 👧 → 👨 → 👴 → ⭐            ║",
        "    ║    🏠 → 🏫 → 🏢 → 🏥 → ⛪            ║",
        "    ║                                        ║",
        "    ║  🎬 ACTO III: EL FUTURO 🚀            ║",
        "    ║    💻 → 🤖 → 🛸 → 🌌 → ♾️            ║",
        "    ╚════════════════════════════════════════╝",
        "         🎫 🎫 🎫 🎫 🎫 🎫 🎫 🎫",
        "    👏 AUDIENCIA: ¡100 EJERCICIOS COMPLETADOS! 👏",
        "        👥 👥 👥 👥 👥 👥 👥 👥",
        "        📱 📱 📱 📱 📱 📱 📱 📱",
        "",
        "🎭 Director: Tu dedicación y perseverancia",
        "🌟 Protagonista: Tú, maestro del ASCII art",
        "👏 Final: ¡Standing ovation por tu logro!"
    ]
    
    for linea in teatro:
        print(linea)

def arcoiris_emociones():
    """Crea un arcoíris de emociones"""
    print("🌈 ARCOÍRIS DE EMOCIONES 🌈")
    print("Espectro completo de sentimientos humanos")
    print()
    
    arcoiris = [
        "                    ☀️",
        "              🌈          🌈",
        "           🌈               🌈",
        "         🌈   😊 ALEGRÍA      🌈",
        "       🌈      🎉 CELEBRACIÓN    🌈",
        "      🌈        💖 AMOR           🌈",
        "     🌈          🌟 ESPERANZA       🌈",
        "    🌈            💪 FORTALEZA        🌈",
        "   🌈              🧠 SABIDURÍA         🌈",
        "  🌈                🎯 DETERMINACIÓN      🌈",
        " 🌈                  🤝 AMISTAD            🌈",
        "🌈                    🏆 TRIUNFO             🌈",
        "                       ✨ CREATIVIDAD",
        "                        💫 INSPIRACIÓN",
        "                         🔮 IMAGINACIÓN",
        "🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿",
        "",
        "🎨 Cada color representa una emoción positiva",
        "✨ Has experimentado todas al crear ASCII art",
        "💫 Tu arcoíris personal: 100 ejercicios de crecimiento"
    ]
    
    for linea in arcoiris:
        print(linea)

def viaje_tiempo():
    """Crea un viaje a través del tiempo"""
    print("🚀 VIAJE A TRAVÉS DEL TIEMPO 🚀")
    print("Desde el Big Bang hasta el infinito")
    print()
    
    viaje = [
        "⚛️ BIG BANG ⚛️ → 🌌 UNIVERSO → ⭐ ESTRELLAS → 🌍 TIERRA",
        "       ↓               ↓              ↓           ↓",
        "   💥 INICIO       🌟 EXPANSIÓN   ☀️ FUSIÓN   🌊 VIDA",
        "",
        "🦕 DINOSAURIOS → 🐒 EVOLUCIÓN → 👤 HUMANOS → 🏛️ CIVILIZACIÓN",
        "       ↓               ↓              ↓           ↓",
        "   🌋 JURÁSICO    🧬 SELECCIÓN   🔥 FUEGO    🏗️ CONSTRUCCIÓN",
        "",
        "📜 ESCRITURA → 💡 INVENCIÓN → 💻 DIGITAL → 🤖 IA",
        "       ↓               ↓              ↓           ↓",
        "   📚 CONOCIMIENTO  ⚙️ INDUSTRIA   🌐 INTERNET  🧠 FUTURO",
        "",
        "🚀 ESPACIO → 🌌 GALAXIAS → ♾️ INFINITO → ❓ MISTERIO",
        "       ↓               ↓              ↓           ↓",
        "   🛸 EXPLORACIÓN  🔭 DESCUBRIMIENTO 💫 ETERNIDAD 🔮 POSIBILIDAD",
        "",
        "╔═══════════════════════════════════════════════════════╗",
        "║  🎓 TÚ AQUÍ: ¡100 EJERCICIOS ASCII COMPLETADOS! 🎓   ║",
        "║     Has viajado por toda la historia del arte        ║",
        "╚═══════════════════════════════════════════════════════╝"
    ]
    
    for linea in viaje:
        print(linea)

def sinfonia_visual():
    """Crea una sinfonía visual"""
    print("🎼 SINFONÍA VISUAL 🎼")
    print("Música convertida en arte ASCII")
    print()
    
    sinfonia = [
        "♪ ♫ ♪ ♫ 🎼 SINFONÍA EN ASCII MAYOR 🎼 ♫ ♪ ♫ ♪",
        "",
        "🎵 PRIMER MOVIMIENTO: Allegro Vivace",
        "▬▬▲▬▬▬▲▬▬▲▲▬▬▬▲▬▬▬▲▲▲▬▬▲▬▬▬▲▬▬▲▲▬▬▬▲▬▬",
        "🎹🎺🎻🥁🎸🎷🎪🎭🎨🖼️📸🎬🎮🎯🎲🃏🎰🎡🎢🎠",
        "",
        "🎵 SEGUNDO MOVIMIENTO: Andante Emotivo",
        "~~~∩~~~∩~~~∩~~~∩~~~∩~~~∩~~~∩~~~∩~~~∩~~~",
        "💙💚💛🧡❤️💜🖤🤍🤎💗💓💕💖💘💝💞💟❣️💔",
        "",
        "🎵 TERCER MOVIMIENTO: Scherzo Playful",
        "↗️↘️↗️↘️↗️↘️↗️↘️↗️↘️↗️↘️↗️↘️↗️↘️↗️↘️↗️↘️",
        "😀😃😄😁😆😅🤣😂🙂🙃😉😊😇🥰😍🤩😘😗",
        "",
        "🎵 CUARTO MOVIMIENTO: Finale Grandioso",
        "🌟⭐✨💫⚡🔥💥💯🎆🎇🎊🎉🥳🎈🎁🏆🥇🎖️🏅👑",
        "",
        "🎼 COMPOSITOR: ¡TÚ! - Maestro de 100 ejercicios",
        "👏 OVACIÓN: El público se pone de pie",
        "🌟 ENCORE: ¡Más arte ASCII, por favor!"
    ]
    
    for linea in sinfonia:
        print(linea)

def constelacion_logros():
    """Crea una constelación de logros"""
    print("🌟 CONSTELACIÓN DE LOGROS 🌟")
    print("Tus 100 ejercicios brillan como estrellas")
    print()
    
    constelacion = [
        "              🌌 CONSTELACIÓN ASCII 🌌",
        "",
        "    ⭐         ⭐           ⭐         ⭐",
        "     \\         |           /         /",
        "      ⭐---⭐---⭐---⭐---⭐---⭐---⭐",
        "           |       |       |       |",
        "          ⭐       ⭐       ⭐       ⭐",
        "         / \\       |       |       /",
        "        ⭐   ⭐     ⭐       ⭐     ⭐",
        "       /     \\     |       |     /",
        "      ⭐       ⭐   ⭐       ⭐   ⭐",
        "               \\   |       |   /",
        "                ⭐ ⭐       ⭐ ⭐",
        "                   \\       /",
        "                    ⭐---⭐",
        "                      |",
        "                     ⭐",
        "",
        "🏆 CADA ESTRELLA = UN EJERCICIO COMPLETADO",
        "⭐ TOTAL: 100 estrellas brillantes",
        "🌟 RESULTADO: ¡Una constelación única!"
    ]
    
    for linea in constelacion:
        print(linea)

def gran_celebracion():
    """Crea la gran celebración final"""
    print("🎉 GRAN CELEBRACIÓN FINAL 🎉")
    print("¡Felicitaciones por completar 100 ejercicios de ASCII!")
    print()
    
    celebracion = [
        "🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆",
        "🎆                                                           🎆",
        "🎆    🏆 ¡¡¡FELICITACIONES!!! 🏆                         🎆",
        "🎆                                                           🎆",
        "🎆     🎯 HAS COMPLETADO 100 EJERCICIOS DE ASCII! 🎯        🎆",
        "🎆                                                           🎆",
        "🎆   🌟 LOGROS DESBLOQUEADOS: 🌟                           🎆",
        "🎆   ✅ Maestro del Arte ASCII                              🎆",
        "🎆   ✅ Explorador de Culturas                              🎆",
        "🎆   ✅ Conocedor de Historia                               🎆",
        "🎆   ✅ Amante de la Naturaleza                             🎆",
        "🎆   ✅ Entusiasta de la Tecnología                        🎆",
        "🎆   ✅ Creativo sin Límites                               🎆",
        "🎆   ✅ Perseverante Extraordinario                        🎆",
        "🎆   ✅ Graduado ASCII Magna Cum Laude                     🎆",
        "🎆                                                           🎆",
        "🎆   🎓 DIPLOMA HONORÍFICO: 🎓                            🎆",
        "🎆   'Por excelencia en creatividad ASCII'                  🎆",
        "🎆                                                           🎆",
        "🎆   💫 ¡TU VIAJE APENAS COMIENZA! 💫                     🎆",
        "🎆   Sigue creando, sigue explorando, sigue soñando...      🎆",
        "🎆                                                           🎆",
        "🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆",
        "",
        "🎊 ¡Gracias por acompañarnos en este viaje! 🎊",
        "🌈 ¡El arte ASCII vivirá para siempre! 🌈",
        "🚀 ¡Hacia el infinito y más allá! 🚀"
    ]
    
    for linea in celebracion:
        print(linea)
        time.sleep(0.1)  # Efecto de revelación gradual

def main():
    """Función principal con menú interactivo"""
    galeria_funciones = {
        '1': cuadro_universo,
        '2': museo_civilizaciones,
        '3': mapa_mundo,
        '4': teatro_vida,
        '5': arcoiris_emociones,
        '6': viaje_tiempo,
        '7': sinfonia_visual,
        '8': constelacion_logros,
        '9': gran_celebracion
    }
    
    print("🎨 ¡BIENVENIDO A LA GALERÍA FINAL! 🎨")
    print("🏆 ¡HAS LLEGADO AL EJERCICIO 100! 🏆")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("🎨 Selecciona una obra de arte (0-9): ").strip()
            
            if opcion == '0':
                print("\n🎨 ¡Gracias por completar los 100 ejercicios de ASCII! 🎨")
                print("🏆 ¡Eres oficialmente un maestro del arte ASCII! 🏆")
                print("🌟 ¡Que tu creatividad siga brillando siempre! 🌟")
                print("\n🎉 ¡FELICITACIONES POR TU LOGRO EXTRAORDINARIO! 🎉")
                break
            elif opcion in galeria_funciones:
                print("\n" + "="*70)
                galeria_funciones[opcion]()
                print("="*70)
                if opcion == '9':  # Si es la gran celebración
                    print("\n🎊 ¡MOMENTO ESPECIAL! 🎊")
                    print("Has completado tu última obra maestra...")
            else:
                print("❌ Opción no válida. Intenta de nuevo.")
                
        except KeyboardInterrupt:
            print("\n\n🎨 ¡Hasta luego, maestro del ASCII art! 🎨")
            print("🏆 ¡100/100 ejercicios completados! 🏆")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        
        input("\n🖼️ Presiona Enter para continuar admirando el arte...")

if __name__ == "__main__":
    main()
