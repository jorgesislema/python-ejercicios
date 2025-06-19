#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 84: Elementos del Sistema Solar ASCII
===============================================

Objetivo:
- Crear representaciones de planetas y elementos del sistema solar usando ASCII
- Explorar la astronomía y cosmología básica
- Fomentar el interés por la exploración espacial

Conceptos aplicados:
- Sistema solar
- Astronomía
- Escalas planetarias
- Exploración espacial
"""

import time
import random

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*60)
    print("🌌 GENERADOR DEL SISTEMA SOLAR ASCII 🌌")
    print("="*60)
    print("1. ☀️ Sol")
    print("2. ☿️ Mercurio")
    print("3. ♀️ Venus")
    print("4. 🌍 Tierra")
    print("5. ♂️ Marte")
    print("6. ♃ Júpiter")
    print("7. ♄ Saturno")
    print("8. ♅ Urano")
    print("9. ♆ Neptuno")
    print("0. 🚪 Salir")
    print("-"*60)

def sol():
    """Crea el Sol, estrella central del sistema"""
    print("☀️ SOL ☀️")
    print("Estrella que da vida a nuestro sistema solar")
    print()
    
    sol_ascii = [
        "           \\   |   /",
        "             \\ | /",
        "   \\          \\|/          /",
        "     \\    🔥🔥🔥🔥🔥🔥🔥    /",
        "       \\ 🔥🔥🔥🔥🔥🔥🔥🔥🔥 /",
        "         🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥",
        "   --- 🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥 ---",
        "         🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥",
        "       / 🔥🔥🔥🔥🔥🔥🔥🔥🔥 \\",
        "     /    🔥🔥🔥🔥🔥🔥🔥    \\",
        "   /          /|\\          \\",
        "             / | \\",
        "           /   |   \\",
        "",
        "Temperatura núcleo: 15 millones °C",
        "Masa: 333,000 veces la Tierra",
        "Edad: 4,600 millones de años"
    ]
    
    for linea in sol_ascii:
        print(linea)

def mercurio():
    """Crea Mercurio, el planeta más cercano al Sol"""
    print("☿️ MERCURIO ☿️")
    print("El planeta más pequeño y rápido del sistema solar")
    print()
    
    mercurio_ascii = [
        "        🪨🪨🪨🪨🪨",
        "      🪨🪨🪨🪨🪨🪨🪨",
        "     🪨🪨🪨🪨🪨🪨🪨🪨",
        "    🪨🪨🪨🪨🪨🪨🪨🪨🪨",
        "   🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨",
        "   🪨🪨🪨⚪⚪⚪🪨🪨🪨🪨",
        "   🪨🪨🪨⚪⚪⚪🪨🪨🪨🪨",
        "   🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨",
        "    🪨🪨🪨🪨🪨🪨🪨🪨🪨",
        "     🪨🪨🪨🪨🪨🪨🪨🪨",
        "      🪨🪨🪨🪨🪨🪨🪨",
        "        🪨🪨🪨🪨🪨",
        "",
        "Distancia del Sol: 58 millones km",
        "Día mercuriano: 176 días terrestres",
        "Temperatura: -173°C a 427°C"
    ]
    
    for linea in mercurio_ascii:
        print(linea)

def venus():
    """Crea Venus, el planeta más caliente"""
    print("♀️ VENUS ♀️")
    print("El planeta más caliente, envuelto en nubes de ácido")
    print()
    
    venus_ascii = [
        "       🟨🟨🟨🟨🟨🟨🟨",
        "     🟨🟨🟨🟨🟨🟨🟨🟨🟨",
        "    🟨🟨⛅⛅⛅⛅⛅🟨🟨",
        "   🟨🟨⛅⛅⛅⛅⛅⛅⛅🟨🟨",
        "  🟨🟨⛅⛅⛅⛅⛅⛅⛅⛅⛅🟨",
        "  🟨⛅⛅⛅⛅⛅⛅⛅⛅⛅⛅🟨",
        "  🟨⛅⛅⛅⛅⛅⛅⛅⛅⛅⛅🟨",
        "  🟨🟨⛅⛅⛅⛅⛅⛅⛅⛅⛅🟨",
        "   🟨🟨⛅⛅⛅⛅⛅⛅⛅🟨🟨",
        "    🟨🟨⛅⛅⛅⛅⛅🟨🟨",
        "     🟨🟨🟨🟨🟨🟨🟨🟨🟨",
        "       🟨🟨🟨🟨🟨🟨🟨",
        "",
        "Temperatura superficie: 462°C",
        "Presión: 90 veces la de la Tierra",
        "Nubes de ácido sulfúrico"
    ]
    
    for linea in venus_ascii:
        print(linea)

def tierra():
    """Crea la Tierra, nuestro hogar"""
    print("🌍 TIERRA 🌍")
    print("El único planeta conocido con vida")
    print()
    
    tierra_ascii = [
        "        🌍🌍🌍🌍🌍🌍🌍",
        "      🌍🌍🟫🟫🟫🟫🌍🌍🌍",
        "     🌍🌍🟫🟫🟫🟫🟫🌍🌍🌍",
        "    🌍🌍🟫🟫🟫🟫🟫🟫🌍🌍🌍",
        "   🌍🌍🌍🟫🟫🟫🟫🟫🌍🌍🌍🌍",
        "   🌍🌍🌍🌍🟫🟫🟫🌍🌍🌍🌍🌍",
        "   🌍🌍🌍🌍🌍🟫🌍🌍🌍🌍🌍🌍",
        "   🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍",
        "    🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍",
        "     🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍",
        "      🌍🌍🌍🌍🌍🌍🌍🌍🌍",
        "        🌍🌍🌍🌍🌍🌍🌍",
        "           🌙",
        "Edad: 4,540 millones de años",
        "70% cubierto por océanos",
        "Único planeta con vida conocida"
    ]
    
    for linea in tierra_ascii:
        print(linea)

def marte():
    """Crea Marte, el planeta rojo"""
    print("♂️ MARTE ♂️")
    print("El planeta rojo, objetivo de futuras colonias")
    print()
    
    marte_ascii = [
        "        🔴🔴🔴🔴🔴🔴🔴",
        "      🔴🔴🔴🔴🔴🔴🔴🔴🔴",
        "     🔴🔴🟫🟫🟫🟫🔴🔴🔴🔴",
        "    🔴🔴🟫🟫🟫🟫🟫🔴🔴🔴🔴",
        "   🔴🔴🔴🟫🟫🟫🟫🟫🔴🔴🔴🔴",
        "   🔴🔴🔴🔴⚪⚪⚪🔴🔴🔴🔴🔴",
        "   🔴🔴🔴🔴⚪⚪⚪🔴🔴🔴🔴🔴",
        "   🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴",
        "    🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴",
        "     🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴",
        "      🔴🔴🔴🔴🔴🔴🔴🔴🔴",
        "        🔴🔴🔴🔴🔴🔴🔴",
        "",
        "Día marciano: 24h 37min",
        "Dos lunas: Fobos y Deimos",
        "Temperatura: -143°C a 35°C"
    ]
    
    for linea in marte_ascii:
        print(linea)

def jupiter():
    """Crea Júpiter, el gigante gaseoso"""
    print("♃ JÚPITER ♃")
    print("El planeta más grande, protector del sistema solar interno")
    print()
    
    jupiter_ascii = [
        "     🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤",
        "   🟤🟤🟫🟫🟫🟫🟫🟫🟫🟫🟫🟤🟤🟤🟤",
        "  🟤🟤🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟤🟤🟤🟤",
        " 🟤🟤🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟤🟤🟤🟤",
        "🟤🟤🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟤🟤🟤🟤",
        "🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤",
        "🟤🟤🟤🟤🟤🟤🔴🔴🔴🟤🟤🟤🟤🟤🟤🟤🟤🟤",
        "🟤🟤🟤🟤🟤🟤🔴🔴🔴🟤🟤🟤🟤🟤🟤🟤🟤🟤",
        "🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤",
        "🟤🟤🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟤🟤🟤🟤",
        " 🟤🟤🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟤🟤🟤🟤",
        "  🟤🟤🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟤🟤🟤🟤",
        "   🟤🟤🟫🟫🟫🟫🟫🟫🟫🟫🟫🟤🟤🟤🟤",
        "     🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤🟤",
        "",
        "95 lunas conocidas",
        "Gran Mancha Roja: tormenta gigante",
        "Masa: 2.5 veces todos los planetas juntos"
    ]
    
    for linea in jupiter_ascii:
        print(linea)

def saturno():
    """Crea Saturno con sus famosos anillos"""
    print("♄ SATURNO ♄")
    print("El señor de los anillos del sistema solar")
    print()
    
    saturno_ascii = [
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
        "  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
        "    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
        "      ━━━━━━━��🟨🟨🟨🟨🟨🟨🟨🟨━━━━━━━",
        "        ━━━🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨━━━",
        "         ━🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨━",
        "          🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨",
        "          🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨",
        "          🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨",
        "         ━🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨━",
        "        ━━━🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨━━━",
        "      ━━━━━━━🟨🟨🟨🟨🟨🟨🟨🟨━━━━━━━",
        "    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
        "  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
        "",
        "146 lunas conocidas",
        "Densidad menor que el agua",
        "Anillos de hielo y roca"
    ]
    
    for linea in saturno_ascii:
        print(linea)

def urano():
    """Crea Urano, el planeta inclinado"""
    print("♅ URANO ♅")
    print("El gigante de hielo que rueda de lado")
    print()
    
    urano_ascii = [
        "         🔵🔵🔵🔵🔵🔵🔵🔵🔵",
        "       🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵",
        "      🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵",
        "     🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵",
        "    🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵",
        "   |🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵|",
        "   |🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵|",
        "   |🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵|",
        "    🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵",
        "     🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵",
        "      🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵",
        "       🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵🔵",
        "         🔵🔵🔵🔵🔵🔵🔵🔵🔵",
        "",
        "Rotación: 98° inclinado",
        "27 lunas conocidas",
        "Compuesto de agua, metano y amoníaco"
    ]
    
    for linea in urano_ascii:
        print(linea)

def neptuno():
    """Crea Neptuno, el planeta más lejano"""
    print("♆ NEPTUNO ♆")
    print("El gigante azul con los vientos más fuertes")
    print()
    
    neptuno_ascii = [
        "        🔷🔷🔷🔷🔷🔷🔷🔷🔷",
        "      🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷",
        "     🔷🔷🔷⚡⚡⚡⚡⚡🔷🔷🔷🔷",
        "    🔷🔷🔷⚡⚡⚡⚡⚡⚡🔷🔷🔷🔷",
        "   🔷🔷🔷⚡⚡⚡⚡⚡⚡⚡🔷🔷🔷🔷",
        "   🔷🔷🔷🔷⚡⚡⚡⚡⚡🔷🔷🔷🔷🔷",
        "   🔷🔷🔷🔷🔷⚡⚡⚡🔷🔷🔷🔷🔷🔷",
        "   🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷",
        "    🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷",
        "     🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷",
        "      🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷",
        "        🔷🔷🔷🔷🔷🔷🔷🔷🔷",
        "",
        "Vientos: hasta 2,100 km/h",
        "16 lunas conocidas",
        "Día: 16 horas terrestres"
    ]
    
    for linea in neptuno_ascii:
        print(linea)

def main():
    """Función principal con menú interactivo"""
    planetas_funciones = {
        '1': sol,
        '2': mercurio,
        '3': venus,
        '4': tierra,
        '5': marte,
        '6': jupiter,
        '7': saturno,
        '8': urano,
        '9': neptuno
    }
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("🌌 Selecciona una opción (0-9): ").strip()
            
            if opcion == '0':
                print("\n🌌 ¡Gracias por explorar el cosmos con ASCII! 🌌")
                break
            elif opcion in planetas_funciones:
                print("\n" + "="*60)
                planetas_funciones[opcion]()
                print("="*60)
            else:
                print("❌ Opción no válida. Intenta de nuevo.")
                
        except KeyboardInterrupt:
            print("\n\n🌌 ¡Hasta luego, explorador espacial! 🌌")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        
        input("\n🚀 Presiona Enter para continuar explorando...")

if __name__ == "__main__":
    main()
