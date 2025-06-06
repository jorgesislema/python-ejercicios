#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 28: Pájaros ASCII
===========================

Objetivo:
- Crear diferentes tipos de pájaros usando caracteres ASCII
- Implementar pájaros volando y posados
- Mostrar bandadas y escenas de vuelo

Conceptos aplicados:
- Formas aéreas dinámicas
- Patrones de vuelo
- Ecosistemas aviares
"""

import time
import random

def pajaro_simple():
    """Pájaro básico volando"""
    print("🐦 PÁJARO SIMPLE 🐦")
    print()
    
    pajaro = [
        "   v   ",
        "  /|\\  ",
        " / | \\ "
    ]
    
    for linea in pajaro:
        print(linea)

def pajaro_detallado():
    """Pájaro más detallado con cabeza"""
    print("🕊️ PÁJARO DETALLADO 🕊️")
    print()
    
    pajaro = [
        "    ____",
        "   ( o >",
        "  /\\_) >",
        " /__/   "
    ]
    
    for linea in pajaro:
        print(linea)

def aguila():
    """Águila majestuosa"""
    print("🦅 ÁGUILA 🦅")
    print()
    
    aguila_figura = [
        "       ^       ",
        "      /|\\      ",
        "     / | \\     ",
        "    /  |  \\    ",
        "   /   |   \\   ",
        "  /    ∘    \\  ",
        " /           \\ ",
        "/             \\"
    ]
    
    for linea in aguila_figura:
        print(linea)

def colibri():
    """Colibrí pequeño y rápido"""
    print("🐦 COLIBRÍ 🐦")
    print()
    
    colibri_figura = [
        "  \\   /  ",
        "   \\_/   ",
        "    |>   ",
        "   / \\   "
    ]
    
    for linea in colibri_figura:
        print(linea)

def gaviota():
    """Gaviota marina"""
    print("🪶 GAVIOTA 🪶")
    print()
    
    gaviota_figura = [
        "     ~     ",
        "    /|\\    ",
        "   / | \\   ",
        "  /  |  \\  ",
        " /   ∘   \\ ",
        "/         \\"
    ]
    
    for linea in gaviota_figura:
        print(linea)

def flamenco():
    """Flamenco elegante"""
    print("🦩 FLAMENCO 🦩")
    print()
    
    flamenco_figura = [
        "    🦩    ",
        "    |     ",
        "   /|\\    ",
        "  / | \\   ",
        "    |     ",
        "    |     ",
        "   / \\    ",
        "  /   \\   "
    ]
    
    for linea in flamenco_figura:
        print(linea)

def pinguino():
    """Pingüino antartico"""
    print("🐧 PINGÜINO 🐧")
    print()
    
    pinguino_figura = [
        "   (o)   ",
        "  /   \\  ",
        " | ⚫ ⚫ | ",
        " |  >  | ",
        "  \\___/  ",
        "   | |   ",
        "  _| |_  "
    ]
    
    for linea in pinguino_figura:
        print(linea)

def pajaro_posado():
    """Pájaro posado en una rama"""
    print("🌳 PÁJARO POSADO 🌳")
    print()
    
    escena = [
        "     🐦     ",
        "     /|\\    ",
        "    / | \\   ",
        "~~~~~~~~~~~~",
        "    |||     ",
        "    |||     ",
        "  🌿|||🌿   "
    ]
    
    for linea in escena:
        print(linea)

def bandada_pajaros():
    """Bandada de pájaros volando"""
    print("🌤️ BANDADA VOLANDO 🌤️")
    print()
    
    bandada = [
        "  v     v     v  ",
        "    v     v      ",
        "v     v     v    ",
        "    v     v   v  ",
        "  v     v     v  "
    ]
    
    for linea in bandada:
        print(linea)

def nido_con_polluelos():
    """Nido con polluelos"""
    print("🥚 NIDO CON POLLUELOS 🥚")
    print()
    
    nido = [
        "    🐣 🐣    ",
        "   \\     /   ",
        "    \\___/    ",
        "   /~~~~~\\   ",
        "  /~~~~~~~\\  ",
        " ~~~~~~~~~~~  ",
        "      |       ",
        "    __|__     "
    ]
    
    for linea in nido:
        print(linea)

def pajaro_cantando():
    """Pájaro cantando con notas musicales"""
    print("🎵 PÁJARO CANTANDO 🎵")
    print()
    
    escena = [
        " ♪ ♫ ♪ ♫ ♪  ",
        "    🐦       ",
        "   /|\\  ♪    ",
        "  / | \\      ",
        "~~~~~~~~~~~~ ",
        "    |||      ",
        "  🌿|||🌿    "
    ]
    
    for linea in escena:
        print(linea)

def loro_colorido():
    """Loro tropical colorido"""
    print("🦜 LORO COLORIDO 🦜")
    print()
    
    loro = [
        "   🟢🟡🔴   ",
        "  🟢 ● ● 🔴 ",
        " 🟢   >   🔴",
        "  🟢 === 🔴 ",
        "   🟢🟡🔴   ",
        "     |      ",
        "    /|\\     "
    ]
    
    for linea in loro:
        print(linea)

def cigüeña():
    """Cigüeña con su característico cuello largo"""
    print("🕊️ CIGÜEÑA 🕊️")
    print()
    
    cigueña = [
        "      🐦    ",
        "      |     ",
        "      |     ",
        "     /|\\    ",
        "    / | \\   ",
        "      |     ",
        "      |     ",
        "     / \\    ",
        "    /   \\   "
    ]
    
    for linea in cigueña:
        print(linea)

def pajaros_animados():
    """Simulación de pájaros volando"""
    print("🎬 PÁJAROS ANIMADOS 🎬")
    print("(Presiona Ctrl+C para detener)")
    print()
    
    frames = [
        ["  v  ", " /|\\ ", "/ | \\"],
        ["  ^  ", " \\|/ ", "\\ | /"],
        ["  v  ", " /|\\ ", "/ | \\"],
        ["  ~  ", " -|- ", "- | -"]
    ]
    
    posiciones = [(0, 0), (5, 1), (10, 0), (15, 1), (20, 0)]
    
    try:
        for ciclo in range(5):
            for i, frame in enumerate(frames):
                print("\033[H\033[J", end="")  # Limpiar pantalla
                print("🎬 PÁJAROS ANIMADOS 🎬")
                print("(Presiona Ctrl+C para detener)")
                print()
                
                # Múltiples pájaros en diferentes posiciones
                for j, (x_pos, y_pos) in enumerate(posiciones):
                    x_offset = (x_pos + ciclo * 2 + j) % 25
                    
                    for k, linea in enumerate(frame):
                        if k == 0:
                            print(" " * y_pos)
                        print(" " * x_offset + linea)
                
                time.sleep(0.4)
    except KeyboardInterrupt:
        print("\n¡Vuelo interrumpido!")

def volando_en_v():
    """Pájaros volando en formación V"""
    print("✈️ FORMACIÓN EN V ✈️")
    print()
    
    formacion = [
        "        v        ",
        "      v   v      ",
        "    v       v    ",
        "  v           v  ",
        "v               v"
    ]
    
    for linea in formacion:
        print(linea)

def pajaro_matematico(envergadura=7):
    """Pájaro generado matemáticamente"""
    print(f"🔢 PÁJARO MATEMÁTICO (Envergadura: {envergadura}) 🔢")
    print()
    
    centro = envergadura // 2
    
    # Crear la forma del pájaro
    for i in range(3):
        linea = ""
        if i == 0:  # Cabeza y pico
            espacios = " " * centro
            linea = espacios + "v"
        elif i == 1:  # Cuerpo y alas extendidas
            ala_izq = "/" + " " * (centro - 1)
            cuerpo = "|"
            ala_der = " " * (centro - 1) + "\\"
            linea = ala_izq + cuerpo + ala_der
        else:  # Parte inferior de las alas
            ala_izq = "/" + " " * (centro - 1)
            cuerpo = " "
            ala_der = " " * (centro - 1) + "\\"
            linea = ala_izq + cuerpo + ala_der
        
        print(linea)

def aviario():
    """Aviario con múltiples especies"""
    print("🏞️ AVIARIO 🏞️")
    print()
    
    aviario_escena = [
        "┌────────────────────────┐",
        "│ 🦜    🐦    🦅    🕊️ │",
        "│   🌿      🌿      🌿   │",
        "│ ~~~~~~  ~~~~~~  ~~~~~~ │",
        "│   |||     |||     |||  │",
        "│ 🦩      🐧      🦢    │",
        "│   🌿  🌊🌊🌊  🌿     │",
        "│ 🐣 🐣   🐟🐟   🦆 🦆 │",
        "└────────────────────────┘"
    ]
    
    for linea in aviario_escena:
        print(linea)

def menu_pajaros():
    """Menú interactivo para diferentes tipos de pájaros"""
    while True:
        print("\n" + "="*50)
        print("🐦 GENERADOR DE PÁJAROS ASCII 🐦")
        print("="*50)
        print("1. Pájaro simple")
        print("2. Pájaro detallado")
        print("3. Águila")
        print("4. Colibrí")
        print("5. Gaviota")
        print("6. Flamenco")
        print("7. Pingüino")
        print("8. Pájaro posado")
        print("9. Bandada volando")
        print("10. Nido con polluelos")
        print("11. Pájaro cantando")
        print("12. Loro colorido")
        print("13. Cigüeña")
        print("14. Pájaros animados")
        print("15. Formación en V")
        print("16. Pájaro matemático")
        print("17. Aviario")
        print("18. Todos los pájaros")
        print("0. Salir")
        print("-"*50)
        
        try:
            opcion = input("Selecciona una opción (0-18): ").strip()
            
            if opcion == '0':
                print("¡Que vueles libre como un pájaro! 🕊️")
                break
            elif opcion == '1':
                pajaro_simple()
            elif opcion == '2':
                pajaro_detallado()
            elif opcion == '3':
                aguila()
            elif opcion == '4':
                colibri()
            elif opcion == '5':
                gaviota()
            elif opcion == '6':
                flamenco()
            elif opcion == '7':
                pinguino()
            elif opcion == '8':
                pajaro_posado()
            elif opcion == '9':
                bandada_pajaros()
            elif opcion == '10':
                nido_con_polluelos()
            elif opcion == '11':
                pajaro_cantando()
            elif opcion == '12':
                loro_colorido()
            elif opcion == '13':
                cigüeña()
            elif opcion == '14':
                pajaros_animados()
            elif opcion == '15':
                volando_en_v()
            elif opcion == '16':
                envergadura = int(input("Introduce la envergadura del pájaro (5-15): ") or "7")
                pajaro_matematico(max(5, min(15, envergadura)))
            elif opcion == '17':
                aviario()
            elif opcion == '18':
                pajaro_simple()
                print("\n" + "-"*30 + "\n")
                pajaro_detallado()
                print("\n" + "-"*30 + "\n")
                aguila()
                print("\n" + "-"*30 + "\n")
                colibri()
                print("\n" + "-"*30 + "\n")
                flamenco()
                print("\n" + "-"*30 + "\n")
                pinguino()
                print("\n" + "-"*30 + "\n")
                bandada_pajaros()
                print("\n" + "-"*30 + "\n")
                aviario()
            else:
                print("❌ Opción no válida. Intenta de nuevo.")
                
        except ValueError:
            print("❌ Por favor, introduce un número válido.")
        except KeyboardInterrupt:
            print("\n¡Hasta luego! 🐦")
            break
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_pajaros()
