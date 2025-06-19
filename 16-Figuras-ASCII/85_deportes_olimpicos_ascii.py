#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 85: Deportes Olímpicos ASCII
======================================

Objetivo:
- Crear representaciones de diferentes disciplinas olímpicas usando ASCII
- Explorar la diversidad deportiva y los valores olímpicos
- Fomentar el espíritu deportivo y la competencia sana

Conceptos aplicados:
- Deportes olímpicos
- Movimiento olímpico
- Disciplinas deportivas
- Valores del deporte
"""

import time
import random

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*60)
    print("🏅 GENERADOR DE DEPORTES OLÍMPICOS ASCII 🏅")
    print("="*60)
    print("1. 🏃 Atletismo - Carreras")
    print("2. 🏊 Natación")
    print("3. 🤸 Gimnasia artística")
    print("4. 🏋️ Halterofilia")
    print("5. 🚴 Ciclismo")
    print("6. 🏐 Voleibol")
    print("7. 🏹 Tiro con arco")
    print("8. 🥊 Boxeo")
    print("9. 🏅 Ceremonia de premiación")
    print("0. 🚪 Salir")
    print("-"*60)

def atletismo():
    """Crea una escena de carreras de atletismo"""
    print("🏃 ATLETISMO - CARRERAS 🏃")
    print("La base de los Juegos Olímpicos desde la antigüedad")
    print()
    
    atletismo_ascii = [
        "                🏁                    ",
        "               ||||                   ",
        "               ||||                   ",
        "  🏃‍♂️💨         ||||         💨🏃‍♀️      ",
        "    \\o/         ||||         \\o/      ",
        "     |          ||||          |       ",
        "    / \\         ||||         / \\      ",
        "==================================== ",
        "==================================== ",
        "==================================== ",
        "==================================== ",
        "==================================== ",
        "==================================== ",
        "==================================== ",
        "==================================== ",
        "",
        "🏃‍♂️ CARRIL 1    🏃‍♀️ CARRIL 2",
        "⏱️ Tiempo récord: 9.58s (100m)",
        "🏟️ Pista oficial: 400 metros"
    ]
    
    for linea in atletismo_ascii:
        print(linea)

def natacion():
    """Crea una piscina olímpica de natación"""
    print("🏊 NATACIÓN 🏊")
    print("Elegancia y potencia en el agua")
    print()
    
    natacion_ascii = [
        "🏊‍♂️💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦🏊‍♀️",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "         🏊‍♂️💦💦💦💦💦💦💦               ",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "                    💦💦💦💦🏊‍♀️         ",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "    🏊‍♂️💦💦💦💦💦💦💦💦💦               ",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "                         💦💦💦🏊‍♀️      ",
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵",
        "",
        "🏊‍♂️ Estilos: libre, espalda, pecho, mariposa",
        "🏆 Piscina olímpica: 50m x 25m",
        "⏱️ Récord 100m libre: 46.91s"
    ]
    
    for linea in natacion_ascii:
        print(linea)

def gimnasia():
    """Crea una rutina de gimnasia artística"""
    print("🤸 GIMNASIA ARTÍSTICA 🤸")
    print("Arte, fuerza y precisión en movimiento")
    print()
    
    gimnasia_ascii = [
        "                 🤸‍♀️",
        "                 /|\\",
        "                / | \\",
        "               /  |  \\",
        "═══════════════════════════════════",
        "                                  ",
        "              🤸‍♂️                 ",
        "              /|\\                 ",
        "             / | \\                ",
        "            /  |  \\               ",
        "      ⭕      ⭕      ⭕           ",
        "      ||      ||      ||           ",
        "      ||      ||      ||           ",
        "██████████████████████████████████",
        "",
        "🤸‍♀️ Aparatos femeninos: barra, asimétricas",
        "🤸‍♂️ Aparatos masculinos: anillas, paralelas",
        "⭐ Puntuación perfecta: 10.0 puntos"
    ]
    
    for linea in gimnasia_ascii:
        print(linea)

def halterofilia():
    """Crea una escena de levantamiento de pesas"""
    print("🏋️ HALTEROFILIA 🏋️")
    print("Fuerza pura y técnica perfecta")
    print()
    
    halterofilia_ascii = [
        "           ⚫================⚫",
        "          ⚫                  ⚫",
        "         ⚫       🏋️‍♂️         ⚫",
        "        ⚫        \\💪/         ⚫",
        "       ⚫          |            ⚫",
        "      ⚫          / \\            ⚫",
        "     ⚫                           ⚫",
        "    ⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫",
        "    ███████████████████████████████",
        "    ███████████████████████████████",
        "    ███████████████████████████████",
        "",
        "🏆 Modalidades:",
        "  • Arrancada (Snatch)",
        "  • Dos tiempos (Clean & Jerk)",
        "💪 Récord mundial: 484kg (total)",
        "⚖️ Categorías por peso corporal"
    ]
    
    for linea in halterofilia_ascii:
        print(linea)

def ciclismo():
    """Crea una carrera de ciclismo"""
    print("🚴 CICLISMO 🚴")
    print("Velocidad, resistencia y estrategia sobre ruedas")
    print()
    
    ciclismo_ascii = [
        "    🚴‍♂️      🚴‍♀️      🚴‍♂️",
        "   ⭕ ⭕    ⭕ ⭕    ⭕ ⭕",
        "     🏁                    ",
        "════════════════════════════════════",
        "                                   ",
        "         🚴‍♀️      🚴‍♂️",
        "        ⭕ ⭕    ⭕ ⭕",
        "════════════════════════════════════",
        "                                   ",
        "  🚴‍♂️             🚴‍♀️",
        " ⭕ ⭕           ⭕ ⭕",
        "════════════════════════════════════",
        "",
        "🚴‍♂️ Modalidades olímpicas:",
        "  • Ruta        • Contrarreloj",
        "  • Pista       • BMX",
        "  • Montaña",
        "🏆 Vuelta máxima: 250km (ruta)"
    ]
    
    for linea in ciclismo_ascii:
        print(linea)

def voleibol():
    """Crea un partido de voleibol"""
    print("🏐 VOLEIBOL 🏐")
    print("Trabajo en equipo y coordinación perfecta")
    print()
    
    voleibol_ascii = [
        "                    🏐                 ",
        "                   /|\\                ",
        "                  / | \\               ",
        "    🏐💨                      💨🏐     ",
        "   🤾‍♂️                          🤾‍♀️   ",
        "   /|\\        ||||||||         /|\\   ",
        "  / | \\       ||||||||        / | \\  ",
        " 🤾‍♀️  🤾‍♂️     ||||||||     🤾‍♂️  🤾‍♀️ ",
        " /|\\ /|\\      ||||||||     /|\\ /|\\ ",
        "/ | / | \\     ||||||||    / | \\ | \\",
        "══════════════════════════════════════",
        "██████████████████████████████████████",
        "",
        "🏐 Red altura: 2.43m (hombres), 2.24m (mujeres)",
        "🏆 Sets: mejor de 5, puntos hasta 25",
        "👥 Equipos: 6 jugadores por lado"
    ]
    
    for linea in voleibol_ascii:
        print(linea)

def tiro_arco():
    """Crea una competencia de tiro con arco"""
    print("🏹 TIRO CON ARCO 🏹")
    print("Precisión milimétrica y concentración absoluta")
    print()
    
    tiro_arco_ascii = [
        "                           🎯",
        "                          ⭕⭕",
        "                         ⭕🟡⭕",
        "                         ⭕⭕⭕",
        "                          ⭕⭕",
        "                            ↗",
        "   🏹                      /",
        "  ➤====================   /",
        " 🧍‍♂️                      /",
        " /|\\                     /",
        "/ | \\                   /",
        "                       /",
        "══════════════════════════════════════",
        "",
        "🎯 Distancia olímpica: 70 metros",
        "🏹 Diana: 10 anillos concéntricos",
        "🥇 Puntuación máxima: 10 puntos",
        "⏱️ Tiempo límite: 40 segundos/3 flechas"
    ]
    
    for linea in tiro_arco_ascii:
        print(linea)

def boxeo():
    """Crea un combate de boxeo"""
    print("🥊 BOXEO 🥊")
    print("Arte noble de la defensa personal")
    print()
    
    boxeo_ascii = [
        "     🥊💥                    💥🥊",
        "    🥊🧍‍♂️💨                💨🧍‍♀️🥊",
        "     /|\\                    /|\\",
        "    / | \\                  / | \\",
        "   💨   💨                💨   💨",
        "┌─────────────────────────────────────┐",
        "│                                     │",
        "│  🔔 ROUND 1                        │",
        "│                                     │",
        "│     🧍‍♂️              🧍‍♀️           │",
        "│     /|\\              /|\\           │",
        "│    / | \\            / | \\          │",
        "└─────────────────────────────────────┘",
        "███████████████████████████████████████",
        "",
        "🥊 Categorías por peso: 13 divisiones",
        "⏰ Rounds: 3 rounds x 3 minutos",
        "🏆 Puntuación: 10 puntos sistema"
    ]
    
    for linea in boxeo_ascii:
        print(linea)

def ceremonia():
    """Crea una ceremonia de premiación"""
    print("🏅 CEREMONIA DE PREMIACIÓN 🏅")
    print("El momento más emocionante para los atletas")
    print()
    
    ceremonia_ascii = [
        "                   🏅",
        "                  /|\\",
        "                 🧍‍♀️",
        "                 /|\\",
        "                / | \\",
        "            ████████████",
        "           █     🥇     █",
        "          █      ORO     █",
        "         ████████████████",
        "    🥈         █         🥉",
        "   /|\\         █        /|\\",
        "  🧍‍♂️          █         🧍‍♀️",
        "  /|\\          █        /|\\",
        " / | \\         █       / | \\",
        "███████     ███████   ███████",
        "█ PLATA █   █  ORO  █ █ BRONCE █",
        "███████     ███████   ███████",
        "",
        "🎵 Himno nacional del ganador",
        "🏅 Medallas: Oro, Plata, Bronce",
        "🌹 Entrega de flores y diplomas"
    ]
    
    for linea in ceremonia_ascii:
        print(linea)

def main():
    """Función principal con menú interactivo"""
    deportes_funciones = {
        '1': atletismo,
        '2': natacion,
        '3': gimnasia,
        '4': halterofilia,
        '5': ciclismo,
        '6': voleibol,
        '7': tiro_arco,
        '8': boxeo,
        '9': ceremonia
    }
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("🏅 Selecciona una opción (0-9): ").strip()
            
            if opcion == '0':
                print("\n🏅 ¡Gracias por competir en los Juegos Olímpicos ASCII! 🏅")
                print("🌟 ¡Que el espíritu olímpico te acompañe siempre! 🌟")
                break
            elif opcion in deportes_funciones:
                print("\n" + "="*60)
                deportes_funciones[opcion]()
                print("="*60)
            else:
                print("❌ Opción no válida. Intenta de nuevo.")
                
        except KeyboardInterrupt:
            print("\n\n🏅 ¡Hasta luego, campeón olímpico! 🏅")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        
        input("\n🏆 Presiona Enter para continuar compitiendo...")

if __name__ == "__main__":
    main()
