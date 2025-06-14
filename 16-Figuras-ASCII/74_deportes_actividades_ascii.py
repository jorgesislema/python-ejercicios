#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 74: Deportes y Actividades ASCII
=========================================

Objetivo:
- Crear representaciones ASCII de diferentes deportes
- Implementar equipos deportivos y campos de juego
- Mostrar la diversidad del deporte mundial

Conceptos aplicados:
- Representación de actividades deportivas
- Equipos y herramientas deportivas
- Cultura del deporte y ejercicio
"""

def mostrar_menu():
    """Muestra el menú de opciones disponibles"""
    print("\n" + "="*50)
    print("⚽ GENERADOR DE DEPORTES ASCII ⚽")
    print("="*50)
    print("1. Fútbol")
    print("2. Baloncesto")
    print("3. Tenis")
    print("4. Natación")
    print("5. Ciclismo")
    print("6. Golf")
    print("7. Boxeo")
    print("8. Yoga")
    print("9. Escalada")
    print("0. Salir")
    print("-"*50)

def futbol():
    """Campo de fútbol con portería"""
    print("⚽ FÚTBOL ⚽")
    print()
    print("El deporte más popular del mundo")
    print()
    
    futbol_ascii = [
        "    ⚽ CAMPO DE FÚTBOL ⚽     ",
        "",
        "┌─────────────────────────────┐",
        "│ ┌─┐                   ┌─┐ │",
        "│ │ │                   │ │ │",
        "│ │G│        ⚽         │G│ │",
        "│ │O│       🏃‍♂️👤        │O│ │",
        "│ │A│      👤  👤       │A│ │",
        "│ │L│     👤 🏃‍♂️ 👤      │L│ │",
        "│ └─┘   👤    👤   👤   └─┘ │",
        "│      🏃‍♂️  👤  👤  🏃‍♂️     │",
        "│     👤      ●      👤    │",
        "│    👤   🏃‍♂️   🏃‍♂️   👤   │",
        "│   👤     👤   👤     👤  │",
        "│  🏃‍♂️     👤 ⚽ 👤     🏃‍♂️ │",
        "│ ┌─┐                   ┌─┐ │",
        "│ │ │                   │ │ │",
        "│ │G│                   │G│ │",
        "│ │O│                   │O│ │",
        "│ │A│                   │A│ │",
        "│ │L│                   │L│ │",
        "│ └─┘                   └─┘ │",
        "└─────────────────────────────┘",
        "",
        "⚽ Equipo vs Equipo",
        "🏟️ Estadio lleno de emoción"
    ]
    
    for linea in futbol_ascii:
        print(linea)

def baloncesto():
    """Cancha de baloncesto"""
    print("🏀 BALONCESTO 🏀")
    print()
    print("Deporte de altura y precisión")
    print()
    
    baloncesto_ascii = [
        "   🏀 CANCHA DE BALONCESTO 🏀  ",
        "",
        "┌─────────────────────────────┐",
        "│    ┌───┐         ┌───┐    │",
        "│    │ 🏀│         │🏀 │    │",
        "│    └─┬─┘         └─┬─┘    │",
        "│      ┃    🏃‍♂️ 👤    ┃      │",
        "│  ╭───┃──╮     ╭───┃───╮  │",
        "│  │   ┃  │ 👤  │   ┃   │  │",
        "│  │   ┃  │🏃‍♂️👤│   ┃   │  │",
        "│  │   ●  │ 👤🏀│   ●   │  │",
        "│  │      │👤🏃‍♂️│       │  │",
        "│  │      │ 👤  │       │  │",
        "│  ╰───┃──╯     ╰───┃───╯  │",
        "│      ┃    👤 🏃‍♂️   ┃      │",
        "│    ┌─┴─┐         ┌─┴─┐    │",
        "│    │🏀 │         │ 🏀│    │",
        "│    └───┘         └───┘    │",
        "└─────────────────────────────┘",
        "",
        "🏀 3 puntos desde la línea",
        "🎯 Precisión y estrategia"
    ]
    
    for linea in baloncesto_ascii:
        print(linea)

def tenis():
    """Cancha de tenis"""
    print("🎾 TENIS 🎾")
    print()
    print("Elegancia y potencia en cada golpe")
    print()
    
    tenis_ascii = [
        "      🎾 CANCHA DE TENIS 🎾     ",
        "",
        "┌─────────────────────────────┐",
        "│                             │",
        "│   🏃‍♂️                 👤    │",
        "│     \\               /      │",
        "│      \\             /       │",
        "│       ┃───────────┃        │",
        "│       ┃           ┃        │",
        "│       ┃           ┃        │",
        "│       ┃     🎾    ┃        │",
        "│═══════╪═══════════╪═══════│",
        "│       ┃           ┃        │",
        "│       ┃           ┃        │",
        "│       ┃           ┃        │",
        "│       ┃───────────┃        │",
        "│      /             \\       │",
        "│     /               \\      │",
        "│   👤                 🏃‍♂️    │",
        "│                             │",
        "└─────────────────────────────┘",
        "",
        "🎾 Pelota a 180 km/h",
        "🏆 Wimbledon, Roland Garros"
    ]
    
    for linea in tenis_ascii:
        print(linea)

def natacion():
    """Piscina de natación"""
    print("🏊 NATACIÓN 🏊")
    print()
    print("Deporte acuático completo")
    print()
    
    natacion_ascii = [
        "     🏊 PISCINA OLÍMPICA 🏊    ",
        "",
        "┌─────────────────────────────┐",
        "│🏁│ │ │ │ │ │ │ │ │ │ │🏁│",
        "│~~│~│~│~│~│~│~│~│~│~│~│~~│",
        "│~~│~│~│~🏊‍♂️~│~│~│~│~│~│~~│",
        "│~~│~│~│~│~│~│~│~│~│~│~│~~│",
        "│~~│~│~│~│~│~🏊‍♀️~│~│~│~│~~│",
        "│~~│~│~│~│~│~│~│~│~│~│~│~~│",
        "│~~│~│~🏊‍♂️~│~│~│~│~│~│~│~~│",
        "│~~│~│~│~│~│~│~│~│~│~│~│~~│",
        "│~~│~│~│~│~│~│~🏊‍♀️~│~│~│~~│",
        "│~~│~│~│~│~│~│~│~│~│~│~│~~│",
        "│~~│~│~│~│~🏊‍♂️~│~│~│~│~│~~│",
        "│~~│~│~│~│~│~│~│~│~│~│~│~~│",
        "│🏁│ │ │ │ │ │ │ │ │ │ │🏁│",
        "└─────────────────────────────┘",
        "",
        "🏊‍♂️ Estilo libre, mariposa, espalda",
        "💧 50m olímpicos"
    ]
    
    for linea in natacion_ascii:
        print(linea)

def ciclismo():
    """Bicicleta y ciclista"""
    print("🚴 CICLISMO 🚴")
    print()
    print("Velocidad y resistencia sobre ruedas")
    print()
    
    ciclismo_ascii = [
        "      🚴 CICLISMO 🚴          ",
        "",
        "          👤                 ",
        "         /│\\                ",
        "        / │ \\               ",
        "       /  │  \\              ",
        "      🔴──┼──🔴             ",
        "     ╱    │    ╲            ",
        "    ╱     │     ╲           ",
        "   ●───────────●           ",
        "  ╱ ╲         ╱ ╲          ",
        " ╱   ╲       ╱   ╲         ",
        "●─────●─────●─────●        ",
        "       ╲   ╱               ",
        "        ╲ ╱                ",
        "         ●                 ",
        "",
        "🚵‍♂️ Ciclismo de montaña",
        "🚴‍♀️ Ciclismo de ruta",
        "🏆 Tour de Francia",
        "",
        "💨💨💨💨💨 → 50 km/h"
    ]
    
    for linea in ciclismo_ascii:
        print(linea)

def golf():
    """Campo de golf"""
    print("⛳ GOLF ⛳")
    print()
    print("Precisión y paciencia en el green")
    print()
    
    golf_ascii = [
        "        ⛳ GOLF ⛳           ",
        "",
        "                    ⛳     ",
        "                   ╱│╲     ",
        "  🏌️‍♂️               ╱ │ ╲    ",
        "   ╲\\__            🟢 │ 🟢   ",
        "    ╲  \\__         🟢🟢🟢    ",
        "     ╲    \\___    🟢🟢🟢🟢    ",
        "      ╲      ●~~🟢🟢🟢🟢🟢   ",
        "       ╲       🟢🟢🟢🟢🟢🟢   ",
        "        ╲     🟢🟢🟢🟢🟢🟢🟢   ",
        "🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫",
        "🟫 T E E   B O X       🟫🟫",
        "🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫",
        "",
        "⛳ Hoyo en uno",
        "🏌️‍♂️ Driver, hierros, putter",
        "🏆 Masters de Augusta"
    ]
    
    for linea in golf_ascii:
        print(linea)

def boxeo():
    """Ring de boxeo"""
    print("🥊 BOXEO 🥊")
    print()
    print("Arte marcial de precisión y fuerza")
    print()
    
    boxeo_ascii = [
        "       🥊 RING DE BOXEO 🥊     ",
        "",
        "┌─────────────────────────────┐",
        "│ ●                       ● │",
        "│ │                       │ │",
        "│ │   🥊                  │ │",
        "│ │    \\👤             │ │",
        "│ │     \\│\\            │ │",
        "│ │      \\│             │ │",
        "│ │       └──┐           │ │",
        "│ │           👤🥊       │ │",
        "│ │          ╱│╲         │ │",
        "│ │         ╱ │          │ │",
        "│ │        ╱              │ │",
        "│ │                       │ │",
        "│ ●                       ● │",
        "└─────────────────────────────┘",
        "",
        "🥊 Combate de 12 rounds",
        "🏆 Título mundial peso pesado",
        "⚡ Jab, cross, hook, uppercut"
    ]
    
    for linea in boxeo_ascii:
        print(linea)

def yoga():
    """Posiciones de yoga"""
    print("🧘 YOGA 🧘")
    print()
    print("Equilibrio entre mente, cuerpo y espíritu")
    print()
    
    yoga_ascii = [
        "         🧘 YOGA 🧘           ",
        "",
        "   Postura del Árbol 🌳       ",
        "                              ",
        "         👤                  ",
        "        ╱│╲                  ",
        "       ╱ │ ╲                 ",
        "      ╱  │  ╲                ",
        "     ╱   │   ╲               ",
        "        ╱│                   ",
        "       ╱ │                   ",
        "      ╱  │                   ",
        "     ╱   │                   ",
        "    ╱    │                   ",
        "   ╱     │                   ",
        "──────────────────────       ",
        "",
        "   Postura de Loto 🪷        ",
        "                              ",
        "         👤                  ",
        "        ╱│╲                  ",
        "       ╱ │ ╲                 ",
        "      ╱╲ │ ╱╲                ",
        "     ╱  ╲│╱  ╲               ",
        "    ╱____●____╲              ",
        "   ╱           ╲             ",
        "──────────────────────       ",
        "",
        "🧘‍♀️ Namaste 🙏",
        "☮️ Paz interior y flexibilidad"
    ]
    
    for linea in yoga_ascii:
        print(linea)

def escalada():
    """Pared de escalada"""
    print("🧗 ESCALADA 🧗")
    print()
    print("Desafío vertical y superación personal")
    print()
    
    escalada_ascii = [
        "      🧗 ESCALADA 🧗         ",
        "",
        "│                           │",
        "│ ●        🧗‍♀️             │",
        "│   ●    ╱ │ ╲             │",
        "│     ● ╱  │  ╲            │",
        "│       ●  │   ●           │",
        "│ ●        │              │",
        "│   ●      │     ●        │",
        "│     ●    │               │",
        "│       ●  │        ●     │",
        "│ ●        │              │",
        "│   ●      │     ●        │",
        "│     ●    │               │",
        "│       ●  │   🧗‍♂️         │",
        "│ ●        │ ╱ │ ╲         │",
        "│   ●      │╱  │  ╲        │",
        "│     ●    ●   │   ●       │",
        "│       ●      │           │",
        "│ ●            │    ●      │",
        "│   ●          │           │",
        "│     ●        │     ●     │",
        "│       ●      │           │",
        "│              │           │",
        "└───────────────────────────┘",
        "",
        "🧗‍♀️ Escalada deportiva",
        "⛰️ Vías de 5.12c",
        "🪢 Cuerda, arnés, mosquetones"
    ]
    
    for linea in escalada_ascii:
        print(linea)

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Selecciona una opción (0-9): ").strip()
            
            if opcion == '0':
                print("\n¡Mantente activo y saludable! 💪")
                break
            elif opcion == '1':
                futbol()
            elif opcion == '2':
                baloncesto()
            elif opcion == '3':
                tenis()
            elif opcion == '4':
                natacion()
            elif opcion == '5':
                ciclismo()
            elif opcion == '6':
                golf()
            elif opcion == '7':
                boxeo()
            elif opcion == '8':
                yoga()
            elif opcion == '9':
                escalada()
            else:
                print("❌ Opción no válida. Por favor, elige una opción del 0 al 9.")
                
        except ValueError:
            print("❌ Por favor, introduce un número válido.")
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego! ⚽")
            break
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
