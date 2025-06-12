"""
Ejercicio 52: Juegos Clásicos ASCII

Objetivo:
- Crear representaciones de juegos clásicos en ASCII
- Incluir variantes: Pac-Man, Tetris, Space Invaders, Pong, Snake
- Permitir visualización de tableros y personajes

Conceptos:
- Juegos retro en ASCII
- Representación de píxeles con caracteres
- Nostalgia gaming
"""

def pacman_ascii():
    """Pac-Man con fantasmas"""
    print("👻 PAC-MAN ASCII 👻")
    print("═" * 40)
    
    print("Tablero de Pac-Man:")
    tablero = [
        "┌─────────────────────┐",
        "│ ● ● ● ● ● ● ● ● ● │",
        "│ ● ┌─┐ ● ● ● ┌─┐ ● │",
        "│ ○ │ │ ● ● ● │ │ ○ │",
        "│ ● └─┘ ● ● ● └─┘ ● │",
        "│ ● ● ● ● 🕳️ ● ● ● ● │",
        "│ ● ● ● ● ● ● ● ● ● │",
        "│   🟡    👻👻👻    │",
        "│ ● ● ● ● ● ● ● ● ● │",
        "│ ● ● ● ● ● ● ● ● ● │",
        "└─────────────────────┘"
    ]
    
    for linea in tablero:
        print(linea)
    
    print("\n🟡 Pac-Man | 👻 Fantasmas | ● Puntos | ○ Power Pellets")
    print("¡Wakka wakka wakka!")

def tetris_ascii():
    """Tetris con piezas"""
    print("🧩 TETRIS ASCII 🧩")
    print("═" * 30)
    
    print("Tablero de Tetris:")
    tablero = [
        "┌──────────┐",
        "│          │",
        "│    ■■    │",
        "│    ■■    │ <- Pieza O",
        "│          │",
        "│   ■■■■   │ <- Pieza I",
        "│          │",
        "│    ■     │",
        "│   ■■■    │ <- Pieza T",
        "│          │",
        "│ ■■■■■■■■ │",
        "│ ■■■□■■■■ │",
        "│ ■■■■■■■■ │",
        "└──────────┘"
    ]
    
    for linea in tablero:
        print(linea)
    
    print("\nPiezas: I, O, T, S, Z, J, L")
    print("¡Completa las líneas!")

def space_invaders_ascii():
    """Space Invaders"""
    print("👾 SPACE INVADERS ASCII 👾")
    print("═" * 40)
    
    juego = [
        "                                    ",
        "  👾   👾   👾   👾   👾   👾     ",
        "    👾   👾   👾   👾   👾       ",
        "  👾   👾   👾   👾   👾   👾     ",
        "                │                 ",
        "                │                 ",
        "               ║║║                ",
        "              ║║║║║               ",
        "                                  ",
        "    ▒▒▒     ▒▒▒     ▒▒▒     ▒▒▒  ",
        "   ▒▒▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒ ",
        "                                  ",
        "              ▲▲▲                 ",
        "             ▲▲▲▲▲                "
    ]
    
    for linea in juego:
        print(linea)
    
    print("\n👾 Invasores | ▲ Nave | ▒ Bunkers | │ Disparo")

def pong_ascii():
    """Pong clásico"""
    print("🏓 PONG ASCII 🏓")
    print("═" * 40)
    
    pong = [
        "┌──────────────────────────────────┐",
        "│                                  │",
        "│ │                            │   │",
        "│ │                            │   │",
        "│ │           ●                │   │",
        "│ │                            │   │",
        "│ │                            │   │",
        "│                                  │",
        "└──────────────────────────────────┘",
        "Jugador 1: 3    Jugador 2: 2"
    ]
    
    for linea in pong:
        print(linea)
    
    print("\n● Pelota | │ Paletas")
    print("¡El primer videojuego!")

def snake_ascii():
    """Snake (serpiente)"""
    print("🐍 SNAKE ASCII 🐍")
    print("═" * 30)
    
    snake_game = [
        "┌────────────────────────┐",
        "│                        │",
        "│   🍎                   │",
        "│                        │",
        "│        ●●●●●●●         │",
        "│                        │",
        "│                        │",
        "│                  ●     │",
        "│                ●●●     │",
        "│              ●●●       │",
        "│            ●●●         │",
        "│                        │",
        "└────────────────────────┘",
        "Score: 150   Length: 12"
    ]
    
    for linea in snake_game:
        print(linea)
    
    print("\n🐍 Serpiente | 🍎 Comida")
    print("¡No te muerdas la cola!")

def breakout_ascii():
    """Breakout (Arkanoid)"""
    print("🧱 BREAKOUT ASCII 🧱")
    print("═" * 40)
    
    breakout = [
        "┌──────────────────────────────────┐",
        "│ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ │",
        "│ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ ▓▓ │",
        "│ ▒▒ ▒▒ ▒▒ ▒▒ ▒▒ ▒▒ ▒▒ ▒▒ ▒▒ ▒▒ │",
        "│ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ │",
        "│                                  │",
        "│                                  │",
        "│              ●                   │",
        "│                                  │",
        "│                                  │",
        "│                                  │",
        "│           ═══════                │",
        "└──────────────────────────────────┘",
        "Lives: 3   Score: 2450"
    ]
    
    for linea in breakout:
        print(linea)
    
    print("\n■▓▒░ Ladrillos | ● Pelota | ═ Paleta")

def asteroids_ascii():
    """Asteroids"""
    print("☄️ ASTEROIDS ASCII ☄️")
    print("═" * 40)
    
    asteroids = [
        "                                    ",
        "    ☄️              ☄️            ",
        "              ●                   ",
        "                    ☄️            ",
        "  ☄️        /│\\                  ",
        "            / │ \\                 ",
        "                                  ",
        "                        ☄️        ",
        "      ☄️                         ",
        "                ☄️                ",
        "              ●                   ",
        "                                  "
    ]
    
    for linea in asteroids:
        print(linea)
    
    print("\n/│\\ Nave | ☄️ Asteroides | ● Disparos")
    print("¡Destruye todos los asteroides!")

def frogger_ascii():
    """Frogger"""
    print("🐸 FROGGER ASCII 🐸")
    print("═" * 40)
    
    frogger = [
        "🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠",
        "🌊🌊🪵🪵🪵🌊🌊🪵🪵🪵🌊🌊🪵🪵🌊",
        "🌊🐢🌊🌊🌊🐢🌊🌊🌊🌊🐢🌊🌊🌊🌊",
        "🌊🌊🌊🪵🪵🪵🌊🌊🪵🪵🪵🌊🌊🌊🌊",
        "🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊",
        "│ │ │ │ │ │ │ │ │ │ │ │ │ │ │",
        "🚗     🚙   🚚       🚗     🚙",
        "    🚕     🚐   🚛         🚕",
        "🚌       🚗     🚙   🚚      ",
        "  🚐   🚚         🚗   🚙    ",
        "▓▓▓▓▓▓▓▓▓▓▓▓▓🐸▓▓▓▓▓▓▓▓▓▓▓▓"
    ]
    
    for linea in frogger:
        print(linea)
    
    print("\n🐸 Rana | 🚗🚙🚚 Tráfico | 🪵🐢 Río | 🏠 Meta")

def donkey_kong_ascii():
    """Donkey Kong"""
    print("🦍 DONKEY KONG ASCII 🦍")
    print("═" * 40)
    
    dk = [
        "       🦍                         ",
        "   ●●● ╱─╲ ●●●   <- Barriles     ",
        "  ╱─────────────╲                ",
        " ╱               ╲               ",
        "╱_________________╲              ",
        "│                 │              ",
        "│    ●        👨   │ <- Mario     ",
        "╱─────────────────╲              ",
        "│                 │              ",
        "│  👨               │              ",
        "╱─────────────────╲              ",
        "│                 │              ",
        "│             👨   │              ",
        "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓              "
    ]
    
    for linea in dk:
        print(linea)
    
    print("\n🦍 Donkey Kong | 👨 Mario | ● Barriles")
    print("¡Sube las escaleras!")

def menu_principal():
    """Menú principal del programa"""
    while True:
        print("\n" + "═" * 50)
        print("🎮 JUEGOS CLÁSICOS ASCII 🎮")
        print("═" * 50)
        print("1. Pac-Man")
        print("2. Tetris")
        print("3. Space Invaders")
        print("4. Pong")
        print("5. Snake")
        print("6. Breakout")
        print("7. Asteroids")
        print("8. Frogger")
        print("9. Donkey Kong")
        print("0. Salir")
        print("═" * 50)
        
        opcion = input("Selecciona un juego: ")
        
        if opcion == "1":
            pacman_ascii()
        elif opcion == "2":
            tetris_ascii()
        elif opcion == "3":
            space_invaders_ascii()
        elif opcion == "4":
            pong_ascii()
        elif opcion == "5":
            snake_ascii()
        elif opcion == "6":
            breakout_ascii()
        elif opcion == "7":
            asteroids_ascii()
        elif opcion == "8":
            frogger_ascii()
        elif opcion == "9":
            donkey_kong_ascii()
        elif opcion == "0":
            print("¡Game Over! 🎮")
            break
        else:
            print("Opción no válida")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
