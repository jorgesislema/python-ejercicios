#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 75: Elementos del Clima ASCII
======================================

Objetivo:
- Crear representaciones ASCII de diferentes estados del clima
- Implementar fenómenos meteorológicos diversos
- Mostrar las variaciones atmosféricas

Conceptos aplicados:
- Representación de fenómenos meteorológicos
- Estados atmosféricos y climatología
- Elementos naturales del tiempo
"""

def mostrar_menu():
    """Muestra el menú de opciones disponibles"""
    print("\n" + "="*50)
    print("🌤️ GENERADOR DE CLIMA ASCII 🌤️")
    print("="*50)
    print("1. Sol Radiante")
    print("2. Lluvia Intensa")
    print("3. Tormenta Eléctrica")
    print("4. Nieve")
    print("5. Niebla")
    print("6. Viento Fuerte")
    print("7. Arcoíris")
    print("8. Granizo")
    print("9. Aurora Boreal")
    print("0. Salir")
    print("-"*50)

def sol_radiante():
    """Sol brillante y radiante"""
    print("☀️ SOL RADIANTE ☀️")
    print()
    print("Día soleado con cielos despejados")
    print()
    
    sol_ascii = [
        "              \\   |   /          ",
        "               \\  |  /           ",
        "            \\   \\ | /   /        ",
        "             \\   \\|/   /         ",
        "          \\   \\   ☀️   /   /      ",
        "           \\   \\ /|\\ /   /       ",
        "        ────────────────────     ",
        "           /   / \\|\\ \\   \\       ",
        "          /   /   ☀️   \\   \\      ",
        "             /   /|\\   \\         ",
        "            /   / | \\   \\        ",
        "               /  |  \\           ",
        "              /   |   \\          ",
        "",
        "🌡️ Temperatura: 28°C",
        "☀️ Radiación UV alta",
        "🌤️ Cielos despejados",
        "💧 Humedad: 45%"
    ]
    
    for linea in sol_ascii:
        print(linea)

def lluvia_intensa():
    """Lluvia cayendo intensamente"""
    print("🌧️ LLUVIA INTENSA 🌧️")
    print()
    print("Precipitación abundante")
    print()
    
    lluvia_ascii = [
        "     ☁️☁️☁️☁️☁️☁️☁️☁️          ",
        "   ☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️        ",
        "  ☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️       ",
        " ☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️      ",
        "☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️     ",
        " ☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️      ",
        "  ☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️       ",
        "   ☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️        ",
        "    💧 💧 💧 💧 💧 💧 💧       ",
        "   💧 💧 💧 💧 💧 💧 💧 💧      ",
        "  💧 💧 💧 💧 💧 💧 💧 💧 💧     ",
        " 💧 💧 💧 💧 💧 💧 💧 💧 💧 💧    ",
        "💧 💧 💧 💧 💧 💧 💧 💧 💧 💧 💧   ",
        " 💧 💧 💧 💧 💧 💧 💧 💧 💧 💧    ",
        "  💧 💧 💧 💧 💧 💧 💧 💧 💧     ",
        "   💧 💧 💧 💧 💧 💧 💧 💧      ",
        "    💧 💧 💧 💧 💧 💧 💧       ",
        "",
        "🌧️ Precipitación: 15mm/h",
        "🌡️ Temperatura: 18°C",
        "💨 Viento: 12 km/h"
    ]
    
    for linea in lluvia_ascii:
        print(linea)

def tormenta_electrica():
    """Tormenta con rayos"""
    print("⛈️ TORMENTA ELÉCTRICA ⛈️")
    print()
    print("Fenómeno eléctrico atmosférico")
    print()
    
    tormenta_ascii = [
        "   ⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫        ",
        "  ⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫      ",
        " ⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫     ",
        "⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫    ",
        "⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫   ",
        " ⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫     ",
        "  ⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫      ",
        "    ⚡        ⚡               ",
        "     ⚡        ⚡              ",
        "      ⚡        ⚡             ",
        "   💧   ⚡   💧   ⚡   💧        ",
        "  💧 💧  ⚡ 💧 💧  ⚡ 💧 💧       ",
        " 💧 💧 💧 ⚡💧 💧 💧⚡💧 💧 💧     ",
        "💧 💧 💧 💧⚡💧 💧💧⚡💧 💧 💧 💧   ",
        " 💧 💧 💧 💧💧 💧💧💧 💧 💧 💧     ",
        "  💧 💧 💧 💧 💧 💧 💧 💧 💧      ",
        "   💧 💧 💧 💧 💧 💧 💧 💧       ",
        "",
        "⚡ Descargas eléctricas",
        "🌩️ Truenos y relámpagos",
        "💧 Lluvia torrencial",
        "⚠️ Mantente en interior"
    ]
    
    for linea in tormenta_ascii:
        print(linea)

def nieve():
    """Nevada suave"""
    print("❄️ NIEVE ❄️")
    print()
    print("Copos blancos cayendo suavemente")
    print()
    
    nieve_ascii = [
        "     ☁️☁️☁️☁️☁️☁️☁️☁️          ",
        "   ☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️        ",
        "  ☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️       ",
        " ☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️      ",
        "☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️     ",
        " ☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️      ",
        "  ☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️       ",
        "                              ",
        "    ❄️   ❄️   ❄️   ❄️        ",
        "  ❄️   ❄️   ❄️   ❄️   ❄️     ",
        "    ❄️   ❄️   ❄️   ❄️        ",
        "  ❄️   ❄️   ❄️   ❄️   ❄️     ",
        "    ❄️   ❄️   ❄️   ❄️        ",
        "  ❄️   ❄️   ❄️   ❄️   ❄️     ",
        "    ❄️   ❄️   ❄️   ❄️        ",
        "  ❄️   ❄️   ❄️   ❄️   ❄️     ",
        "    ❄️   ❄️   ❄️   ❄️        ",
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜    ",
        "",
        "❄️ Copos únicos e irrepetibles",
        "🌡️ Temperatura: -5°C",
        "☃️ Perfecta para muñecos de nieve"
    ]
    
    for linea in nieve_ascii:
        print(linea)

def niebla():
    """Niebla densa"""
    print("🌫️ NIEBLA 🌫️")
    print()
    print("Visibilidad reducida por vapor de agua")
    print()
    
    niebla_ascii = [
        "🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️  ",
        "  🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️    ",
        "    🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️      ",
        "🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️  ",
        "  🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️    ",
        "    🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️      ",
        "🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️  ",
        "  🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️    ",
        "    🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️      ",
        "🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️  ",
        "  🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️    ",
        "    🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️      ",
        "🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️  ",
        "  🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️    ",
        "    🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️      ",
        "",
        "👁️ Visibilidad: < 100 metros",
        "🚗 Conduce con precaución",
        "🌡️ Temperatura: 8°C",
        "💧 Humedad: 95%"
    ]
    
    for linea in niebla_ascii:
        print(linea)

def viento_fuerte():
    """Viento intenso"""
    print("💨 VIENTO FUERTE 💨")
    print()
    print("Ráfagas intensas moviendo todo")
    print()
    
    viento_ascii = [
        "                  🌳          ",
        "                 ╱            ",
        "               ╱              ",
        "🌳           ╱                ",
        " ╲         ╱                  ",
        "  ╲      ╱    💨💨💨💨💨→      ",
        "   ╲   ╱      💨💨💨💨💨→      ",
        "    ╲╱        💨💨💨💨💨→      ",
        "              💨💨💨💨💨→      ",
        "     🏠       💨💨💨💨💨→      ",
        "    ╱ ╲       💨💨💨💨💨→      ",
        "   ╱   ╲      💨💨💨💨💨→      ",
        "  ╱_____╲     💨💨💨💨💨→      ",
        "              💨💨💨💨💨→      ",
        "   🍃🍃🍃      💨💨💨💨💨→      ",
        " 🍃🍃🍃🍃🍃    💨💨💨💨💨→      ",
        "🍃🍃🍃🍃🍃🍃   💨💨💨💨💨→      ",
        "",
        "💨 Velocidad: 85 km/h",
        "🌪️ Ráfagas de viento",
        "⚠️ Objetos volando",
        "🌳 Árboles balanceándose"
    ]
    
    for linea in viento_ascii:
        print(linea)

def arcoiris():
    """Arcoíris después de la lluvia"""
    print("🌈 ARCOÍRIS 🌈")
    print()
    print("Belleza después de la tormenta")
    print()
    
    arcoiris_ascii = [
        "     ☁️☁️☁️        ☀️         ",
        "   ☁️☁️☁️☁️☁️       \\|/        ",
        "  ☁️☁️☁️☁️☁️☁️      ☀️         ",
        " ☁️☁️☁️☁️☁️☁️☁️     /|\\        ",
        "☁️☁️☁️☁️☁️☁️☁️☁️               ",
        " ☁️☁️☁️☁️☁️☁️☁️                ",
        "  ☁️☁️☁️☁️☁️☁️                 ",
        "   ☁️☁️☁️☁️☁️    🟥🟥🟥🟥🟥🟥🟥  ",
        "    ☁️☁️☁️      🟧🟧🟧🟧🟧🟧🟧🟧 ",
        "               🟨🟨🟨🟨🟨🟨🟨🟨🟨",
        "              🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩",
        "             🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦",
        "            🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪",
        "           🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪",
        "          💧 💧 💧 💧 💧 💧 💧  ",
        "         💧 💧 💧 💧 💧 💧 💧 💧 ",
        "        💧 💧 💧 💧 💧 💧 💧 💧  ",
        "",
        "🌈 Espectro visible de colores",
        "🔴🟠🟡🟢🔵🟣 Rojo a violeta",
        "☀️ Sol + 💧 Lluvia = 🌈 Magia"
    ]
    
    for linea in arcoiris_ascii:
        print(linea)

def granizo():
    """Granizada intensa"""
    print("🧊 GRANIZO 🧊")
    print()
    print("Hielo cayendo del cielo")
    print()
    
    granizo_ascii = [
        "     ⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫         ",
        "   ⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫       ",
        "  ⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫      ",
        " ⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫     ",
        "⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫    ",
        " ⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫     ",
        "  ⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫      ",
        "   ⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫       ",
        "    ●   ●   ●   ●   ●        ",
        "   ● ● ● ● ● ● ● ● ● ●       ",
        "  ● ● ● ● ● ● ● ● ● ● ●      ",
        " ● ● ● ● ● ● ● ● ● ● ● ●     ",
        "● ● ● ● ● ● ● ● ● ● ● ● ●    ",
        " ● ● ● ● ● ● ● ● ● ● ● ●     ",
        "  ● ● ● ● ● ● ● ● ● ● ●      ",
        "   ● ● ● ● ● ● ● ● ● ●       ",
        "    ●   ●   ●   ●   ●        ",
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜    ",
        "",
        "🧊 Piedras de hielo",
        "📏 Tamaño: 2-5 cm",
        "🚗 Daños en vehículos",
        "⚠️ Busca refugio inmediato"
    ]
    
    for linea in granizo_ascii:
        print(linea)

def aurora_boreal():
    """Aurora boreal mística"""
    print("🌌 AURORA BOREAL 🌌")
    print()
    print("Danza de luces en el cielo ártico")
    print()
    
    aurora_ascii = [
        "⭐    ⭐      ⭐        ⭐     ",
        "   ⭐      ⭐      ⭐    ⭐   ",
        "      ⭐  💚💚💚💚💚  ⭐      ",
        "⭐      💚💚💚💚💚💚💚        ",
        "      💚💚💚💚💚💚💚💚💚      ",
        "   💚💚💚💙💚💚💚💙💚💚💚   ⭐",
        " 💚💚💚💙💙💚💚💚💙💙💚💚💚   ",
        "💚💚💙💙💜💚💚💚💜💙💙💚💚 ⭐ ",
        " 💚💙💙💜💜💚💚💚💜💜💙💙💚   ",
        "  💚💙💜💜💚💚💚💚💚💜💜💙💚  ",
        "   💚💙💜💚💚💚💚💚💚💜💙💚   ",
        "⭐   💚💙💚💚💚💚💚💚💚💙💚  ⭐",
        "     💚💚💚💚💚💚💚💚💚💚     ",
        "      💚💚💚💚💚💚💚💚💚      ",
        "⭐      💚💚💚💚💚💚💚    ⭐  ",
        "          💚💚💚💚💚          ",
        "    ⭐      💚💚💚      ⭐    ",
        "",
        "🌌 Fenómeno electromagnético",
        "🇳🇴 Visible en Noruega, Islandia",
        "💚💙💜 Verde, azul, violeta",
        "✨ Belleza cósmica natural"
    ]
    
    for linea in aurora_ascii:
        print(linea)

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Selecciona una opción (0-9): ").strip()
            
            if opcion == '0':
                print("\n¡Que tengas un clima perfecto! 🌤️")
                break
            elif opcion == '1':
                sol_radiante()
            elif opcion == '2':
                lluvia_intensa()
            elif opcion == '3':
                tormenta_electrica()
            elif opcion == '4':
                nieve()
            elif opcion == '5':
                niebla()
            elif opcion == '6':
                viento_fuerte()
            elif opcion == '7':
                arcoiris()
            elif opcion == '8':
                granizo()
            elif opcion == '9':
                aurora_boreal()
            else:
                print("❌ Opción no válida. Por favor, elige una opción del 0 al 9.")
                
        except ValueError:
            print("❌ Por favor, introduce un número válido.")
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego! 🌤️")
            break
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
