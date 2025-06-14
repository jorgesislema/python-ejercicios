#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 71: Emociones y Expresiones ASCII
==========================================

Objetivo:
- Crear representaciones ASCII de diferentes emociones y expresiones
- Implementar caras y gestos expresivos
- Mostrar diversidad de sentimientos humanos

Conceptos aplicados:
- Representación de emociones humanas
- Arte expresivo con caracteres ASCII
- Psicología y comunicación no verbal
"""

def mostrar_menu():
    """Muestra el menú de opciones disponibles"""
    print("\n" + "="*50)
    print("😊 GENERADOR DE EMOCIONES ASCII 😊")
    print("="*50)
    print("1. Felicidad")
    print("2. Tristeza")
    print("3. Sorpresa")
    print("4. Enojo")
    print("5. Miedo")
    print("6. Amor")
    print("7. Aburrimiento")
    print("8. Confusión")
    print("9. Risa")
    print("0. Salir")
    print("-"*50)

def felicidad():
    """Expresión de felicidad"""
    print("😊 FELICIDAD 😊")
    print()
    print("La alegría se refleja en una sonrisa radiante")
    print()
    
    cara_feliz = [
        "      ╭─────────╮      ",
        "    ╱             ╲    ",
        "   ╱      ●   ●    ╲   ",
        "  │                 │  ",
        "  │        ⌒        │  ",
        "  │     ╭─────╮     │  ",
        "  │    ╱       ╲    │  ",
        "   ╲  ╱         ╲  ╱   ",
        "    ╲╱           ╲╱    ",
        "      ╲─────────╱      ",
        "",
        "   ✨ ¡SONRÍE! ✨     ",
        "   La felicidad es      ",
        "   contagiosa 😄        "
    ]
    
    for linea in cara_feliz:
        print(linea)

def tristeza():
    """Expresión de tristeza"""
    print("😢 TRISTEZA 😢")
    print()
    print("Lágrimas que expresan melancolía")
    print()
    
    cara_triste = [
        "      ╭─────────╮      ",
        "    ╱             ╲    ",
        "   ╱      ●   ●    ╲   ",
        "  │        ┊   ┊    │  ",
        "  │        ╲   ╱    │  ",
        "  │         ╲ ╱     │  ",
        "  │          ─      │  ",
        "   ╲               ╱   ",
        "    ╲             ╱    ",
        "      ╲─────────╱      ",
        "",
        "    💧 Está bien      ",
        "    sentirse triste    ",
        "    a veces 💙         "
    ]
    
    for linea in cara_triste:
        print(linea)

def sorpresa():
    """Expresión de sorpresa"""
    print("😲 SORPRESA 😲")
    print()
    print("¡Ojos muy abiertos de asombro!")
    print()
    
    cara_sorpresa = [
        "      ╭─────────╮      ",
        "    ╱             ╲    ",
        "   ╱     ╭─╮ ╭─╮   ╲   ",
        "  │      │●│ │●│    │  ",
        "  │      ╰─╯ ╰─╯    │  ",
        "  │                 │  ",
        "  │        ╭─╮      │  ",
        "  │        │ │      │  ",
        "   ╲       ╰─╯     ╱   ",
        "    ╲             ╱    ",
        "      ╲─────────╱      ",
        "",
        "    ⚡ ¡INCREÍBLE!     ",
        "    No me lo esperaba   ",
        "    😯                  "
    ]
    
    for linea in cara_sorpresa:
        print(linea)

def enojo():
    """Expresión de enojo"""
    print("😠 ENOJO 😠")
    print()
    print("Ceño fruncido y mirada intensa")
    print()
    
    cara_enojada = [
        "      ╭─────────╮      ",
        "    ╱   ╲     ╱   ╲    ",
        "   ╱     ╲   ╱     ╲   ",
        "  │       ● ●       │  ",
        "  │       ╲ ╱       │  ",
        "  │        ─        │  ",
        "  │     ╲─────╱     │  ",
        "   ╲     ╲___╱     ╱   ",
        "    ╲             ╱    ",
        "      ╲─────────╱      ",
        "",
        "    🔥 Respira hondo   ",
        "    La ira pasa,       ",
        "    la calma queda 🧘  "
    ]
    
    for linea in cara_enojada:
        print(linea)

def miedo():
    """Expresión de miedo"""
    print("😨 MIEDO 😨")
    print()
    print("Ojos muy abiertos de terror")
    print()
    
    cara_asustada = [
        "      ╭─────────╮      ",
        "    ╱             ╲    ",
        "   ╱    ╭───╮╭───╮ ╲   ",
        "  │     │ ● ││ ● │  │  ",
        "  │     ╰───╯╰───╯  │  ",
        "  │                 │  ",
        "  │        ___      │  ",
        "  │       (   )     │  ",
        "   ╲       ╲_╱     ╱   ",
        "    ╲             ╱    ",
        "      ╲─────────╱      ",
        "",
        "    👻 No te preocupes ",
        "    El miedo es normal  ",
        "    Eres valiente 💪   "
    ]
    
    for linea in cara_asustada:
        print(linea)

def amor():
    """Expresión de amor"""
    print("😍 AMOR 😍")
    print()
    print("Ojos de corazón y sonrisa enamorada")
    print()
    
    cara_enamorada = [
        "      ╭─────────╮      ",
        "    ╱             ╲    ",
        "   ╱      ♥   ♥    ╲   ",
        "  │                 │  ",
        "  │        ♡        │  ",
        "  │     ╭─────╮     │  ",
        "  │    ╱   ♡   ╲    │  ",
        "   ╲  ╱         ╲  ╱   ",
        "    ╲╱           ╲╱    ",
        "      ╲─────────╱      ",
        "",
        "    💕 El amor todo    ",
        "    lo puede, todo     ",
        "    lo embellece 💖    "
    ]
    
    for linea in cara_enamorada:
        print(linea)

def aburrimiento():
    """Expresión de aburrimiento"""
    print("😑 ABURRIMIENTO 😑")
    print()
    print("Expresión plana y sin energía")
    print()
    
    cara_aburrida = [
        "      ╭─────────╮      ",
        "    ╱             ╲    ",
        "   ╱      ●   ●    ╲   ",
        "  │                 │  ",
        "  │                 │  ",
        "  │        ___      │  ",
        "  │                 │  ",
        "   ╲               ╱   ",
        "    ╲             ╱    ",
        "      ╲─────────╱      ",
        "",
        "    💤 ¿Qué hacemos?   ",
        "    Busquemos algo     ",
        "    divertido 🎯       "
    ]
    
    for linea in cara_aburrida:
        print(linea)

def confusion():
    """Expresión de confusión"""
    print("🤔 CONFUSIÓN 🤔")
    print()
    print("Una ceja levantada, preguntándose qué pasa")
    print()
    
    cara_confundida = [
        "      ╭─────────╮      ",
        "    ╱      ╱      ╲    ",
        "   ╱      ╱   ●    ╲   ",
        "  │      ●          │  ",
        "  │                 │  ",
        "  │        ╱─╲      │  ",
        "  │       ╱   ╲     │  ",
        "   ╲               ╱   ",
        "    ╲             ╱    ",
        "      ╲─────────╱      ",
        "",
        "    ❓ ¿Qué significa? ",
        "    Preguntar no es    ",
        "    malo 🤷‍♀️           "
    ]
    
    for linea in cara_confundida:
        print(linea)

def risa():
    """Expresión de risa intensa"""
    print("😂 RISA 😂")
    print()
    print("Carcajada a lágrima viva")
    print()
    
    cara_riendo = [
        "      ╭─────────╮      ",
        "    ╱             ╲    ",
        "   ╱      ╲   ╱    ╲   ",
        "  │        ╲ ╱      │  ",
        "  │         ●       │  ",
        "  │   ╭─────────╮   │  ",
        "  │  ╱  HA HA HA ╲  │  ",
        "   ╲╱   ╲_______╱  ╲╱   ",
        "    ╲             ╱    ",
        "      ╲─────────╱      ",
        "",
        "    🎭 ¡Qué gracioso!  ",
        "    La risa es la      ",
        "    mejor medicina 😄  "
    ]
    
    for linea in cara_riendo:
        print(linea)

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Selecciona una opción (0-9): ").strip()
            
            if opcion == '0':
                print("\n¡Que tengas un día lleno de emociones positivas! 😊")
                break
            elif opcion == '1':
                felicidad()
            elif opcion == '2':
                tristeza()
            elif opcion == '3':
                sorpresa()
            elif opcion == '4':
                enojo()
            elif opcion == '5':
                miedo()
            elif opcion == '6':
                amor()
            elif opcion == '7':
                aburrimiento()
            elif opcion == '8':
                confusion()
            elif opcion == '9':
                risa()
            else:
                print("❌ Opción no válida. Por favor, elige una opción del 0 al 9.")
                
        except ValueError:
            print("❌ Por favor, introduce un número válido.")
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego! 😊")
            break
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
