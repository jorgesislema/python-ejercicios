#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 69: Juegos Clásicos ASCII
===================================

Objetivo:
- Crear representaciones ASCII de juegos clásicos
- Implementar tableros y elementos de juego tradicionales
- Mostrar diferentes juegos de mesa y cartas

Conceptos aplicados:
- Representación visual de juegos
- Tableros y patrones geométricos
- Elementos interactivos de entretenimiento
"""

def mostrar_menu():
    """Muestra el menú de opciones disponibles"""
    print("\n" + "="*50)
    print("🎮 GENERADOR DE JUEGOS CLÁSICOS ASCII 🎮")
    print("="*50)
    print("1. Ajedrez")
    print("2. Damas")
    print("3. Tres en Raya")
    print("4. Dominó")
    print("5. Cartas Póker")
    print("6. Dados")
    print("7. Ruleta")
    print("8. Scrabble")
    print("9. Laberinto")
    print("0. Salir")
    print("-"*50)

def ajedrez():
    """Tablero de ajedrez con piezas"""
    print("♟️ TABLERO DE AJEDREZ ♟️")
    print()
    print("El ajedrez es un juego de estrategia milenario")
    print()
    
    tablero = [
        "  a b c d e f g h",
        "8 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ 8",
        "7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ 7",
        "6 . . . . . . . . 6",
        "5 . . . . . . . . 5",
        "4 . . . . . . . . 4",
        "3 . . . . . . . . 3",
        "2 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ 2",
        "1 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ 1",
        "  a b c d e f g h"
    ]
    
    for linea in tablero:
        print(linea)

def damas():
    """Tablero de damas"""
    print("🔴 TABLERO DE DAMAS 🔴")
    print()
    print("Juego de estrategia con fichas rojas y negras")
    print()
    
    tablero = [
        "  1 2 3 4 5 6 7 8",
        "a ⬛🔴⬛🔴⬛🔴⬛🔴 a",
        "b 🔴⬛🔴⬛🔴⬛🔴⬛ b",
        "c ⬛🔴⬛🔴⬛🔴⬛🔴 c",
        "d ⬜⬛⬜⬛⬜⬛⬜⬛ d",
        "e ⬛⬜⬛⬜⬛⬜⬛⬜ e",
        "f ⚫⬛⚫⬛⚫⬛⚫⬛ f",
        "g ⬛⚫⬛⚫⬛⚫⬛⚫ g",
        "h ⚫⬛⚫⬛⚫⬛⚫⬛ h",
        "  1 2 3 4 5 6 7 8"
    ]
    
    for linea in tablero:
        print(linea)

def tres_en_raya():
    """Juego de tres en raya"""
    print("❌ TRES EN RAYA ❌")
    print()
    print("Clásico juego de X y O")
    print()
    
    tablero = [
        "     |     |     ",
        "  X  |  O  |  X  ",
        "_____|_____|_____",
        "     |     |     ",
        "  O  |  X  |  O  ",
        "_____|_____|_____",
        "     |     |     ",
        "  X  |  O  |  X  ",
        "     |     |     "
    ]
    
    for linea in tablero:
        print(linea)

def domino():
    """Fichas de dominó"""
    print("⚫ DOMINÓ ⚫")
    print()
    print("Juego tradicional con fichas numeradas")
    print()
    
    fichas = [
        "┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐",
        "│ ● ● │ │ ●   │ │     │ │ ● ● │",
        "│ ● ● │ │  ●  │ │  ●  │ │     │",
        "├─────┤ ├─────┤ ├─────┤ ├─────┤",
        "│ ●   │ │ ● ● │ │ ● ● │ │ ● ● │",
        "│  ●  │ │ ● ● │ │ ● ● │ │ ● ● │",
        "└─────┘ └─────┘ └─────┘ └─────┘"
    ]
    
    for linea in fichas:
        print(linea)

def cartas_poker():
    """Cartas de póker"""
    print("🃏 CARTAS DE PÓKER 🃏")
    print()
    print("Mano ganadora: Escalera real")
    print()
    
    cartas = [
        "┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐",
        "│10 ♠ │ │ J ♠ │ │ Q ♠ │ │ K ♠ │ │ A ♠ │",
        "│     │ │     │ │     │ │     │ │     │",
        "│  ♠  │ │  ♠  │ │  ♠  │ │  ♠  │ │  ♠  │",
        "│     │ │     │ │     │ │     │ │     │",
        "│ ♠ 10│ │ ♠ J │ │ ♠ Q │ │ ♠ K │ │ ♠ A │",
        "└─────┘ └─────┘ └─────┘ └─────┘ └─────┘"
    ]
    
    for linea in cartas:
        print(linea)

def dados():
    """Dados de seis caras"""
    print("🎲 DADOS 🎲")
    print()
    print("Resultado de la tirada: 7 (suma)")
    print()
    
    dado1 = [
        "┌─────┐",
        "│     │",
        "│  ●  │",
        "│     │",
        "└─────┘"
    ]
    
    dado2 = [
        "┌─────┐",
        "│ ●   │",
        "│  ●  │",
        "│   ● │",
        "└─────┘"
    ]
    
    # Mostrar dados lado a lado
    for i in range(len(dado1)):
        print(dado1[i] + "  " + dado2[i])

def ruleta():
    """Ruleta de casino"""
    print("🎰 RULETA 🎰")
    print()
    print("Mesa de ruleta europea")
    print()
    
    ruleta_grafica = [
        "      🔴 0 ⚫      ",
        "   ┌─────────────┐   ",
        "  ⚫│  32  15  19│🔴  ",
        " 🔴│ 4    2   21 │⚫  ",
        " ⚫│  25  17  34 │🔴  ",
        " 🔴│ 6   29   13 │⚫  ",
        "  ⚫│  36  11  30│🔴  ",
        "   └─────────────┘   ",
        "        ╲   ╱        ",
        "         ╲ ╱         ",
        "          ●          "
    ]
    
    for linea in ruleta_grafica:
        print(linea)

def scrabble():
    """Tablero de Scrabble"""
    print("🔤 SCRABBLE 🔤")
    print()
    print("Juego de palabras con fichas de letras")
    print()
    
    tablero = [
        "┌─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┐",
        "│★│ │ │◆│ │ │ │★│ │ │ │◆│ │ │★│",
        "├─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┤",
        "│ │◇│ │ │ │◆│ │ │ │◆│ │ │ │◇│ │",
        "├─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┤",
        "│ │ │◇│ │ │ │◆│ │◆│ │ │ │◇│ │ │",
        "├─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┤",
        "│◆│ │ │P│A│L│A│B│R│A│ │ │ │ │◆│",
        "├─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┼─┤",
        "│ │ │ │ │ │ │◆│ │◆│ │ │ │ │ │ │",
        "└─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┘"
    ]
    
    for linea in tablero:
        print(linea)

def laberinto():
    """Laberinto clásico"""
    print("🗿 LABERINTO 🗿")
    print()
    print("Encuentra la salida del laberinto")
    print()
    
    laberinto_mapa = [
        "┌─────────────────────┐",
        "│🟢  │     │     │   │",
        "│ ██ │ ███ │ ███ │ ██│",
        "│    │     │     │   │",
        "│ ██ ███ █████ ███ ██│",
        "│ │    │       │    │",
        "│ │ ██ │ █████ │ ██ │",
        "│   │    │   │    │ │",
        "│ ███ ██ │ █ │ ██ ██│",
        "│     │    █    │   🔴",
        "└─────────────────────┘"
    ]
    
    for linea in laberinto_mapa:
        print(linea)

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Selecciona una opción (0-9): ").strip()
            
            if opcion == '0':
                print("\n¡Que disfrutes jugando! 🎮")
                break
            elif opcion == '1':
                ajedrez()
            elif opcion == '2':
                damas()
            elif opcion == '3':
                tres_en_raya()
            elif opcion == '4':
                domino()
            elif opcion == '5':
                cartas_poker()
            elif opcion == '6':
                dados()
            elif opcion == '7':
                ruleta()
            elif opcion == '8':
                scrabble()
            elif opcion == '9':
                laberinto()
            else:
                print("❌ Opción no válida. Por favor, elige una opción del 0 al 9.")
                
        except ValueError:
            print("❌ Por favor, introduce un número válido.")
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego! 🎮")
            break
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
