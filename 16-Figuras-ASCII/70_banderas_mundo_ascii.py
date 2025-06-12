#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 70: Banderas del Mundo ASCII
=====================================

Objetivo:
- Crear representaciones ASCII de banderas internacionales
- Implementar diferentes patrones y colores nacionales
- Mostrar diversidad cultural mundial

Conceptos aplicados:
- Representación de símbolos nacionales
- Patrones geométricos y colores
- Geografía y cultura mundial
"""

def mostrar_menu():
    """Muestra el menú de opciones disponibles"""
    print("\n" + "="*50)
    print("🏳️ GENERADOR DE BANDERAS DEL MUNDO ASCII 🏳️")
    print("="*50)
    print("1. España")
    print("2. Estados Unidos")
    print("3. Reino Unido")
    print("4. Francia")
    print("5. Japón")
    print("6. Brasil")
    print("7. Canadá")
    print("8. Alemania")
    print("9. Italia")
    print("0. Salir")
    print("-"*50)

def bandera_espana():
    """Bandera de España"""
    print("🇪🇸 BANDERA DE ESPAÑA 🇪🇸")
    print()
    print("Roja y amarilla con escudo nacional")
    print()
    
    bandera = [
        "████████████████████████████████",
        "████████████████████████████████",
        "████████████████████████████████",
        "████████████████████████████████",
        "🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨",
        "🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨",
        "🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨",
        "🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨",
        "🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨",
        "🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨",
        "🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨",
        "🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨",
        "████████████████████████████████",
        "████████████████████████████████",
        "████████████████████████████████",
        "████████████████████████████████"
    ]
    
    for linea in bandera:
        print(linea)

def bandera_estados_unidos():
    """Bandera de Estados Unidos"""
    print("🇺🇸 BANDERA DE ESTADOS UNIDOS 🇺🇸")
    print()
    print("Stars and Stripes - 50 estrellas y 13 franjas")
    print()
    
    bandera = [
        "🟦⭐⭐⭐⭐⭐⭐⭐🟥🟥🟥🟥🟥🟥🟥🟥",
        "🟦⭐⭐⭐⭐⭐⭐⭐⬜⬜⬜⬜⬜⬜⬜⬜",
        "🟦⭐⭐⭐⭐⭐⭐⭐🟥🟥🟥🟥🟥🟥🟥🟥",
        "🟦⭐⭐⭐⭐⭐⭐⭐⬜⬜⬜⬜⬜⬜⬜⬜",
        "🟦⭐⭐⭐⭐⭐⭐⭐🟥🟥🟥🟥🟥🟥🟥🟥",
        "🟦⭐⭐⭐⭐⭐⭐⭐⬜⬜⬜⬜⬜⬜⬜⬜",
        "🟦⭐⭐⭐⭐⭐⭐⭐🟥🟥🟥🟥🟥🟥🟥🟥",
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜",
        "🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥",
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜",
        "🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥",
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜",
        "🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥"
    ]
    
    for linea in bandera:
        print(linea)

def bandera_reino_unido():
    """Bandera del Reino Unido"""
    print("🇬🇧 BANDERA DEL REINO UNIDO 🇬🇧")
    print()
    print("Union Jack - Unión de cruces de San Jorge, San Andrés y San Patricio")
    print()
    
    bandera = [
        "🟦🟦🟦⬜⬜⬜🟦🟦🟦⬜⬜⬜🟦🟦🟦🟦",
        "🟦🟦⬜🟥🟥🟥⬜🟦⬜🟥🟥🟥⬜🟦🟦🟦",
        "🟦⬜🟥🟥🟥🟥🟥⬜🟥🟥🟥🟥🟥⬜🟦🟦",
        "⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜🟦",
        "⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜🟦",
        "⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜🟦",
        "🟦⬜🟥🟥🟥🟥🟥⬜🟥🟥🟥🟥🟥⬜🟦🟦",
        "🟦🟦⬜🟥🟥🟥⬜🟦⬜🟥🟥🟥⬜🟦🟦🟦",
        "🟦🟦🟦⬜⬜⬜🟦🟦🟦⬜⬜⬜🟦🟦🟦🟦",
        "🟦🟦⬜🟥🟥🟥⬜🟦⬜🟥🟥🟥⬜🟦🟦🟦",
        "🟦⬜🟥🟥🟥🟥🟥⬜🟥🟥🟥🟥🟥⬜🟦🟦",
        "⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜🟦"
    ]
    
    for linea in bandera:
        print(linea)

def bandera_francia():
    """Bandera de Francia"""
    print("🇫🇷 BANDERA DE FRANCIA 🇫🇷")
    print()
    print("Tricolor - Azul, blanco y rojo vertical")
    print()
    
    bandera = [
        "🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥",
        "🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥",
        "🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥",
        "🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥",
        "🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥",
        "🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥",
        "🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥",
        "🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥",
        "🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥",
        "🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥",
        "🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥",
        "🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥"
    ]
    
    for linea in bandera:
        print(linea)

def bandera_japon():
    """Bandera de Japón"""
    print("🇯🇵 BANDERA DE JAPÓN 🇯🇵")
    print()
    print("Hinomaru - Sol naciente")
    print()
    
    bandera = [
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜",
        "⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜",
        "⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜",
        "⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜"
    ]
    
    for linea in bandera:
        print(linea)

def bandera_brasil():
    """Bandera de Brasil"""
    print("🇧🇷 BANDERA DE BRASIL 🇧🇷")
    print()
    print("Ordem e Progresso - Verde, amarillo y azul")
    print()
    
    bandera = [
        "🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩",
        "🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩",
        "🟩🟩🟩🟩🟩🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩🟩",
        "🟩🟩🟩🟩🟨🟨🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩",
        "🟩🟩🟩🟨🟨🟨🟦🟦🟨🟨🟨🟩🟩🟩🟩🟩",
        "🟩🟩🟨🟨🟨🟦🟦🟦🟦🟨🟨🟨🟩🟩🟩🟩",
        "🟩🟩🟨🟨🟨🟦🟦🟦🟦🟨🟨🟨🟩🟩🟩🟩",
        "🟩🟩🟩🟨🟨🟨🟦🟦🟨🟨🟨🟩🟩🟩🟩🟩",
        "🟩🟩🟩🟩🟨🟨🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩",
        "🟩🟩🟩🟩🟩🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩🟩",
        "🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩",
        "🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩"
    ]
    
    for linea in bandera:
        print(linea)

def bandera_canada():
    """Bandera de Canadá"""
    print("🇨🇦 BANDERA DE CANADÁ 🇨🇦")
    print()
    print("Hoja de arce roja sobre fondo blanco")
    print()
    
    bandera = [
        "🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥",
        "🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥",
        "🟥🟥🟥⬜⬜⬜🟥🟥⬜⬜⬜⬜⬜🟥🟥🟥",
        "🟥🟥🟥⬜⬜🟥🟥🟥🟥⬜⬜⬜⬜🟥🟥🟥",
        "🟥🟥🟥⬜🟥🟥🟥🟥🟥🟥⬜⬜⬜🟥🟥🟥",
        "🟥🟥🟥⬜🟥🟥🟥🟥🟥🟥⬜⬜⬜🟥🟥🟥",
        "🟥🟥🟥⬜⬜🟥🟥🟥🟥⬜⬜⬜⬜🟥🟥🟥",
        "🟥🟥🟥⬜⬜⬜🟥🟥⬜⬜⬜⬜⬜🟥🟥🟥",
        "🟥🟥🟥⬜⬜⬜⬜🟥⬜⬜⬜⬜⬜🟥🟥🟥",
        "🟥🟥🟥⬜⬜⬜⬜🟥⬜⬜⬜⬜⬜🟥🟥🟥",
        "🟥🟥🟥⬜⬜⬜⬜🟥⬜⬜⬜⬜⬜🟥🟥🟥",
        "🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥"
    ]
    
    for linea in bandera:
        print(linea)

def bandera_alemania():
    """Bandera de Alemania"""
    print("🇩🇪 BANDERA DE ALEMANIA 🇩🇪")
    print()
    print("Negro, rojo y amarillo horizontal")
    print()
    
    bandera = [
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛",
        "🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥",
        "🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥",
        "🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥",
        "🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥",
        "🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨",
        "🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨",
        "🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨",
        "🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨"
    ]
    
    for linea in bandera:
        print(linea)

def bandera_italia():
    """Bandera de Italia"""
    print("🇮🇹 BANDERA DE ITALIA 🇮🇹")
    print()
    print("Verde, blanco y rojo vertical")
    print()
    
    bandera = [
        "🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥",
        "🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥",
        "🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥",
        "🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥",
        "🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥",
        "🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥",
        "🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥",
        "🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥",
        "🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥",
        "🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥",
        "🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥",
        "🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥"
    ]
    
    for linea in bandera:
        print(linea)

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Selecciona una opción (0-9): ").strip()
            
            if opcion == '0':
                print("\n¡Explora el mundo! 🌍")
                break
            elif opcion == '1':
                bandera_espana()
            elif opcion == '2':
                bandera_estados_unidos()
            elif opcion == '3':
                bandera_reino_unido()
            elif opcion == '4':
                bandera_francia()
            elif opcion == '5':
                bandera_japon()
            elif opcion == '6':
                bandera_brasil()
            elif opcion == '7':
                bandera_canada()
            elif opcion == '8':
                bandera_alemania()
            elif opcion == '9':
                bandera_italia()
            else:
                print("❌ Opción no válida. Por favor, elige una opción del 0 al 9.")
                
        except ValueError:
            print("❌ Por favor, introduce un número válido.")
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego! 🌍")
            break
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
