#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 24: Luna y Fases Lunares ASCII
========================================

Objetivo:
- Crear representaciones de la luna en diferentes fases
- Mostrar el ciclo lunar completo
- Implementar lunas decorativas y paisajes nocturnos

Conceptos aplicados:
- Formas curvas con ASCII
- Secuencias y ciclos
- Paisajes nocturnos
"""

def luna_nueva():
    """Luna nueva (no visible)"""
    print("🌑 LUNA NUEVA 🌑")
    print()
    
    cielo = [
        "✨   ✨     ✨   ✨",
        "    ✨   ✨     ✨ ",
        "✨     ⭐     ✨  ",
        "   ✨     ✨     ✨",
        "✨   ✨   ✨   ✨ "
    ]
    
    for linea in cielo:
        print(linea)

def luna_creciente():
    """Luna creciente"""
    print("🌒 LUNA CRECIENTE 🌒")
    print()
    
    luna = [
        "    ✨ /```\\     ✨",
        "   ✨ |     )     ✨",
        "✨   |      )     ✨",
        "   ✨ |     )     ✨",
        "    ✨ \\___/     ✨"
    ]
    
    for linea in luna:
        print(linea)

def cuarto_creciente():
    """Cuarto creciente"""
    print("🌓 CUARTO CRECIENTE 🌓")
    print()
    
    luna = [
        "   ✨   /```|     ✨",
        "  ✨   /    |      ✨",
        "✨    |     |      ✨",
        "  ✨   \\    |      ✨",
        "   ✨   \\___|     ✨"
    ]
    
    for linea in luna:
        print(linea)

def luna_gibosa_creciente():
    """Luna gibosa creciente"""
    print("🌔 LUNA GIBOSA CRECIENTE 🌔")
    print()
    
    luna = [
        "   ✨  /````)     ✨",
        "  ✨  /      )     ✨",
        "✨   |       )     ✨",
        "  ✨  \\      )     ✨",
        "   ✨  \\____/     ✨"
    ]
    
    for linea in luna:
        print(linea)

def luna_llena():
    """Luna llena"""
    print("🌕 LUNA LLENA 🌕")
    print()
    
    luna = [
        "   ✨   /```\\     ✨",
        "  ✨   /  🌝  \\     ✨",
        "✨    |   O   |     ✨",
        "  ✨   \\  U  /     ✨",
        "   ✨   \\___/     ✨"
    ]
    
    for linea in luna:
        print(linea)

def luna_gibosa_menguante():
    """Luna gibosa menguante"""
    print("🌖 LUNA GIBOSA MENGUANTE 🌖")
    print()
    
    luna = [
        "   ✨  (````\\     ✨",
        "  ✨  (      \\     ✨",
        "✨   (       |     ✨",
        "  ✨  (      /     ✨",
        "   ✨  \\____/     ✨"
    ]
    
    for linea in luna:
        print(linea)

def cuarto_menguante():
    """Cuarto menguante"""
    print("🌗 CUARTO MENGUANTE 🌗")
    print()
    
    luna = [
        "   ✨   |```\\     ✨",
        "  ✨    |    \\     ✨",
        "✨      |     |     ✨",
        "  ✨    |    /     ✨",
        "   ✨   |___/     ✨"
    ]
    
    for linea in luna:
        print(linea)

def luna_menguante():
    """Luna menguante"""
    print("🌘 LUNA MENGUANTE 🌘")
    print()
    
    luna = [
        "   ✨  (```\\     ✨",
        "  ✨  (     |     ✨",
        "✨   (      |     ✨",
        "  ✨  (     |     ✨",
        "   ✨  \\___/     ✨"
    ]
    
    for linea in luna:
        print(linea)

def paisaje_nocturno():
    """Paisaje nocturno con luna"""
    print("🌃 PAISAJE NOCTURNO 🌃")
    print()
    
    paisaje = [
        "✨    ✨   /```\\   ✨    ✨",
        "   ✨     | 🌙 |     ✨   ",
        "✨    ✨   \\___/   ✨    ✨",
        "    ✨       ✨       ✨  ",
        "✨    ✨       ✨    ✨   ",
        "    🏠    🌲    🏠       ",
        "  🌲    🏠    🌲    🏠   ",
        "~~~~~~~~~~~~~~~~~~~~~~~ ",
        "^^^^^^^^^^^^^^^^^^^^^^^ "
    ]
    
    for linea in paisaje:
        print(linea)

def luna_romantica():
    """Luna romántica con corazones"""
    print("💕 LUNA ROMÁNTICA 💕")
    print()
    
    escena = [
        "✨  💕  /```\\  💕  ✨",
        "  💕   | ♥ ♥ |   💕  ",
        "✨     |  u  |     ✨",
        "  💕   \\  ♡  /   💕  ",
        "✨  💕  \\___/  💕  ✨",
        "    💕    💕    💕   ",
        "💕    💕    💕    💕 "
    ]
    
    for linea in escena:
        print(linea)

def ciclo_lunar_completo():
    """Mostrar el ciclo lunar completo"""
    print("🌙 CICLO LUNAR COMPLETO 🌙")
    print("="*40)
    
    fases = [
        ("Luna Nueva", "🌑"),
        ("Luna Creciente", "🌒"),
        ("Cuarto Creciente", "🌓"),
        ("Luna Gibosa Creciente", "🌔"),
        ("Luna Llena", "🌕"),
        ("Luna Gibosa Menguante", "🌖"),
        ("Cuarto Menguante", "🌗"),
        ("Luna Menguante", "🌘")
    ]
    
    for i, (nombre, emoji) in enumerate(fases, 1):
        print(f"{i}. {emoji} {nombre}")
    
    print("="*40)

def luna_matematica(fase=0.5):
    """Luna generada matemáticamente según la fase"""
    print(f"🔢 LUNA MATEMÁTICA (Fase: {fase:.1f}) 🔢")
    print()
    
    size = 9
    centro = size // 2
    radio = 3
    
    # Crear matriz
    matriz = [[' ' for _ in range(size)] for _ in range(size)]
    
    # Estrellas de fondo
    matriz[0][1] = '✨'
    matriz[1][7] = '✨'
    matriz[6][0] = '✨'
    matriz[7][8] = '✨'
    
    # Dibujar círculo de luna
    for i in range(size):
        for j in range(size):
            distancia = ((i - centro) ** 2 + (j - centro) ** 2) ** 0.5
            if distancia <= radio:
                # Determinar si el punto está iluminado según la fase
                x_rel = j - centro
                if fase == 0:  # Luna nueva
                    matriz[i][j] = ' '
                elif fase <= 0.5:  # Creciente
                    if x_rel <= radio * (2 * fase - 1):
                        matriz[i][j] = '█'
                else:  # Menguante
                    if x_rel >= radio * (2 * fase - 1):
                        matriz[i][j] = '█'
    
    # Imprimir matriz
    for fila in matriz:
        print(''.join(fila))

def menu_lunas():
    """Menú interactivo para diferentes tipos de lunas"""
    while True:
        print("\n" + "="*50)
        print("🌙 GENERADOR DE LUNAS ASCII 🌙")
        print("="*50)
        print("1. Luna nueva")
        print("2. Luna creciente")
        print("3. Cuarto creciente")
        print("4. Luna gibosa creciente")
        print("5. Luna llena")
        print("6. Luna gibosa menguante")
        print("7. Cuarto menguante")
        print("8. Luna menguante")
        print("9. Paisaje nocturno")
        print("10. Luna romántica")
        print("11. Ciclo lunar completo")
        print("12. Luna matemática")
        print("13. Todas las fases")
        print("0. Salir")
        print("-"*50)
        
        try:
            opcion = input("Selecciona una opción (0-13): ").strip()
            
            if opcion == '0':
                print("¡Buenas noches! 🌙")
                break
            elif opcion == '1':
                luna_nueva()
            elif opcion == '2':
                luna_creciente()
            elif opcion == '3':
                cuarto_creciente()
            elif opcion == '4':
                luna_gibosa_creciente()
            elif opcion == '5':
                luna_llena()
            elif opcion == '6':
                luna_gibosa_menguante()
            elif opcion == '7':
                cuarto_menguante()
            elif opcion == '8':
                luna_menguante()
            elif opcion == '9':
                paisaje_nocturno()
            elif opcion == '10':
                luna_romantica()
            elif opcion == '11':
                ciclo_lunar_completo()
            elif opcion == '12':
                fase = float(input("Introduce la fase lunar (0.0-1.0): ") or "0.5")
                luna_matematica(max(0, min(1, fase)))
            elif opcion == '13':
                luna_nueva()
                print("\n" + "-"*30 + "\n")
                luna_creciente()
                print("\n" + "-"*30 + "\n")
                cuarto_creciente()
                print("\n" + "-"*30 + "\n")
                luna_gibosa_creciente()
                print("\n" + "-"*30 + "\n")
                luna_llena()
                print("\n" + "-"*30 + "\n")
                luna_gibosa_menguante()
                print("\n" + "-"*30 + "\n")
                cuarto_menguante()
                print("\n" + "-"*30 + "\n")
                luna_menguante()
                print("\n" + "-"*30 + "\n")
                paisaje_nocturno()
                print("\n" + "-"*30 + "\n")
                luna_romantica()
            else:
                print("❌ Opción no válida. Intenta de nuevo.")
                
        except ValueError:
            print("❌ Por favor, introduce un número válido.")
        except KeyboardInterrupt:
            print("\n¡Hasta luego! 🌙")
            break
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_lunas()
