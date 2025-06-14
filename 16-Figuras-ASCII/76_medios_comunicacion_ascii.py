#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 76: Medios de Comunicación ASCII
=========================================

Objetivo:
- Crear representaciones ASCII de diferentes medios de comunicación
- Implementar dispositivos y tecnologías de comunicación
- Mostrar la evolución tecnológica comunicativa

Conceptos aplicados:
- Representación de tecnologías de comunicación
- Medios tradicionales y modernos
- Historia de las telecomunicaciones
"""

def mostrar_menu():
    """Muestra el menú de opciones disponibles"""
    print("\n" + "="*50)
    print("📱 GENERADOR DE MEDIOS DE COMUNICACIÓN ASCII 📱")
    print("="*50)
    print("1. Teléfono Móvil")
    print("2. Radio Vintage")
    print("3. Televisión")
    print("4. Computadora")
    print("5. Antena Parabólica")
    print("6. Carta/Email")
    print("7. Periódico")
    print("8. Walkie-Talkie")
    print("9. Satélite")
    print("0. Salir")
    print("-"*50)

def telefono_movil():
    """Smartphone moderno"""
    print("📱 TELÉFONO MÓVIL 📱")
    print()
    print("Comunicación instantánea global")
    print()
    
    movil_ascii = [
        "    📱 SMARTPHONE 📱         ",
        "",
        "      ┌─────────────┐        ",
        "      │ ● ●      📶 │        ",
        "      ├─────────────┤        ",
        "      │             │        ",
        "      │   📞 CALL   │        ",
        "      │             │        ",
        "      │  💬 MESSAGE │        ",
        "      │             │        ",
        "      │   📧 EMAIL  │        ",
        "      │             │        ",
        "      │   🌐 WEB    │        ",
        "      │             │        ",
        "      │   📷 CAMERA │        ",
        "      │             │        ",
        "      ├─────────────┤        ",
        "      │      ●      │        ",
        "      └─────────────┘        ",
        "",
        "📞 Llamadas HD",
        "💬 WhatsApp, Telegram",
        "📧 Email instantáneo",
        "🌐 Internet 5G",
        "📷 Fotos 108MP"
    ]
    
    for linea in movil_ascii:
        print(linea)

def radio_vintage():
    """Radio antigua de los años 50"""
    print("📻 RADIO VINTAGE 📻")
    print()
    print("La era dorada de la radiodifusión")
    print()
    
    radio_ascii = [
        "     📻 RADIO VINTAGE 📻     ",
        "",
        "   ╔═══════════════════════╗ ",
        "   ║  ○ ○ ○ ○ ○ ○ ○ ○ ○  ║ ",
        "   ║                       ║ ",
        "   ║    ♪♫ ON AIR ♫♪      ║ ",
        "   ║                       ║ ",
        "   ║  AM ●────────○ FM     ║ ",
        "   ║                       ║ ",
        "   ║ ┌─┐ VOLUME ┌────────┐ ║ ",
        "   ║ │●│  ◀━━━━━▶ │ TUNING │ ║ ",
        "   ║ └─┘         │   ●    │ ║ ",
        "   ║             └────────┘ ║ ",
        "   ║                       ║ ",
        "   ╚═══════════════════════╝ ",
        "     ─┘                 └─   ",
        "",
        "📻 Frecuencia: 101.5 FM",
        "♪ Música clásica",
        "📡 Ondas hertzianas",
        "🎙️ Locutores en vivo"
    ]
    
    for linea in radio_ascii:
        print(linea)

def television():
    """Televisor con programación"""
    print("📺 TELEVISIÓN 📺")
    print()
    print("Ventana al mundo desde casa")
    print()
    
    television_ascii = [
        "       📺 TELEVISIÓN 📺      ",
        "",
        "  ┌─────────────────────────┐ ",
        "  │ ●○○                 📺│ ",
        "  ├─────────────────────────┤ ",
        "  │                         │ ",
        "  │   🎬 CANAL 7 NOTICIAS   │ ",
        "  │                         │ ",
        "  │  ┌─────────────────────┐ │ ",
        "  │  │   👨‍💼 PRESENTADOR   │ │ ",
        "  │  │                     │ │ ",
        "  │  │  📰 NOTICIAS 20:00  │ │ ",
        "  │  │                     │ │ ",
        "  │  │   🌍 TIEMPO: 23°C   │ │ ",
        "  │  └─────────────────────┘ │ ",
        "  │                         │ ",
        "  │  🔊 ▣▣▣▣▣▣▣▣ 📶 CH 7    │ ",
        "  └─────────────────────────┘ ",
        "        ┌─────────────┐       ",
        "        │  🎮 CONTROL │       ",
        "        │ ① ② ③ ④ ⑤  │       ",
        "        │ ⑥ ⑦ ⑧ ⑨ ⓪  │       ",
        "        │  ▲ 🔊 ▼    │       ",
        "        └─────────────┘       ",
        "",
        "📺 HD 1080p",
        "📡 Cable, satélite, streaming",
        "🎬 Entretenimiento familiar"
    ]
    
    for linea in television_ascii:
        print(linea)

def computadora():
    """PC de escritorio con monitor"""
    print("💻 COMPUTADORA 💻")
    print()
    print("Herramienta de trabajo y entretenimiento")
    print()
    
    computadora_ascii = [
        "     💻 COMPUTADORA 💻       ",
        "",
        "  ┌─────────────────────────┐ ",
        "  │ ○ ○ ○               ⚙️ │ ",
        "  ├─────────────────────────┤ ",
        "  │                         │ ",
        "  │  📁 MIS DOCUMENTOS      │ ",
        "  │  🎵 MÚSICA              │ ",
        "  │  🖼️ FOTOS               │ ",
        "  │  💼 TRABAJO             │ ",
        "  │  🎮 JUEGOS              │ ",
        "  │                         │ ",
        "  │  ┌─────────────────┐    │ ",
        "  │  │ > python_code.py│    │ ",
        "  │  │ print('Hello')  │    │ ",
        "  │  │ _               │    │ ",
        "  │  └─────────────────┘    │ ",
        "  └─────────────────────────┘ ",
        "          ┌───────┐           ",
        "          │   ●   │           ",
        "          └───────┘           ",
        "   ┌─────────────────────────┐",
        "   │ ⌨️ QWERTY KEYBOARD     │",
        "   └─────────────────────────┘",
        "      🖱️              🖨️     ",
        "",
        "💻 CPU: Intel i7",
        "💾 RAM: 16GB",
        "💿 SSD: 1TB",
        "🖥️ Monitor 27\" 4K"
    ]
    
    for linea in computadora_ascii:
        print(linea)

def antena_parabolica():
    """Antena satelital"""
    print("📡 ANTENA PARABÓLICA 📡")
    print()
    print("Comunicación satelital de largo alcance")
    print()
    
    antena_ascii = [
        "    📡 ANTENA PARABÓLICA 📡  ",
        "",
        "              🛰️             ",
        "            ╱    ╲           ",
        "          ╱        ╲         ",
        "        ╱            ╲       ",
        "      ╱                ╲     ",
        "    ╱                    ╲   ",
        "   ╱        📡            ╲  ",
        "  ╱      ╱─────╲          ╲ ",
        " ╱      ╱   ●   ╲          ╲",
        "╱      ╱    ●    ╲          ╲",
        "╲      ╲    ●    ╱          ╱",
        " ╲      ╲   ●   ╱          ╱ ",
        "  ╲      ╲─────╱          ╱  ",
        "   ╲        📡            ╱   ",
        "    ╲                    ╱    ",
        "      ╲                ╱      ",
        "        ╲            ╱        ",
        "          ╲        ╱          ",
        "            ╲____╱            ",
        "              ┃┃              ",
        "              ┃┃              ",
        "           ┌──┘└──┐           ",
        "           │ DISH │           ",
        "           └──────┘           ",
        "",
        "📡 Frecuencia: 12 GHz",
        "🛰️ Comunicación vía satélite",
        "🌍 Cobertura global"
    ]
    
    for linea in antena_ascii:
        print(linea)

def carta_email():
    """Carta tradicional vs email"""
    print("📧 CARTA/EMAIL 📧")
    print()
    print("Evolución de la correspondencia")
    print()
    
    carta_ascii = [
        "   📧 CARTA vs EMAIL 📧      ",
        "",
        "  CARTA TRADICIONAL  📮      ",
        "  ┌─────────────────┐        ",
        "  │ Querido amigo:   │        ",
        "  │                 │        ",
        "  │ Te escribo para │        ",
        "  │ contarte que... │        ",
        "  │                 │        ",
        "  │ Un abrazo,      │        ",
        "  │ María           │        ",
        "  │                 │        ",
        "  └─────────────────┘        ",
        "         📮 ✉️               ",
        "",
        "  EMAIL MODERNO  💻          ",
        "  ┌─────────────────────────┐",
        "  │ De: maria@email.com     │",
        "  │ Para: amigo@email.com   │",
        "  │ Asunto: ¡Hola! 👋       │",
        "  ├─────────────────────────┤",
        "  │ Hola!                   │",
        "  │                         │",
        "  │ Te escribo rápidamente  │",
        "  │ para contarte que... 😊 │",
        "  │                         │",
        "  │ Saludos! 🌟            │",
        "  │ [ENVIAR] 📤            │",
        "  └─────────────────────────┘",
        "",
        "✉️ Carta: 3-7 días",
        "📧 Email: Instantáneo",
        "🌍 Comunicación global"
    ]
    
    for linea in carta_ascii:
        print(linea)

def periodico():
    """Periódico con noticias"""
    print("📰 PERIÓDICO 📰")
    print()
    print("Información diaria impresa")
    print()
    
    periodico_ascii = [
        "        📰 PERIÓDICO 📰      ",
        "",
        "╔═══════════════════════════╗",
        "║     EL DIARIO MUNDIAL     ║",
        "║      📅 15 ENE 2024       ║",
        "╠═══════════════════════════╣",
        "║                           ║",
        "║ 🌍 NOTICIAS INTERNACIONALES ║",
        "║ ─────────────────────────  ║",
        "║ • Cumbre mundial en París ║",
        "║ • Avances en medicina     ║",
        "║ • Deportes: Final de Copa ║",
        "║                           ║",
        "║ 🏛️ POLÍTICA               ║",
        "║ ─────────────────────────  ║",
        "║ • Nuevas reformas         ║",
        "║ • Elecciones próximas     ║",
        "║                           ║",
        "║ 💰 ECONOMÍA               ║",
        "║ ─────────────────────────  ║",
        "║ • Bolsa sube 2.5%         ║",
        "║ • Inflación bajo control  ║",
        "║                           ║",
        "║ 🌤️ TIEMPO: Soleado 25°C   ║",
        "║ 🎬 ESPECTÁCULOS: Cine     ║",
        "║ ⚽ DEPORTES: Liga         ║",
        "╚═══════════════════════════╝",
        "",
        "📰 Tirada: 50,000 ejemplares",
        "📈 Información verificada",
        "☕ Perfecto con el café"
    ]
    
    for linea in periodico_ascii:
        print(linea)

def walkie_talkie():
    """Radio portátil de comunicación"""
    print("📻 WALKIE-TALKIE 📻")
    print()
    print("Comunicación por radiofrecuencia")
    print()
    
    walkie_ascii = [
        "    📻 WALKIE-TALKIE 📻     ",
        "",
        "     ┌───┐     ┌───┐       ",
        "     │🔊│     │🔊│       ",
        "     ├───┤     ├───┤       ",
        "     │ ● │     │ ● │       ",
        "     │   │     │   │       ",
        "     │📞│     │📞│       ",
        "     │   │ ))) │   │       ",
        "     │ ● │ ((( │ ● │       ",
        "     │   │ ))) │   │       ",
        "     │🎙️│     │🎙️│       ",
        "     │   │     │   │       ",
        "     │ ● │     │ ● │       ",
        "     │   │     │   │       ",
        "     │📢│     │📢│       ",
        "     └───┘     └───┘       ",
        "",
        "    UNIDAD A → UNIDAD B     ",
        "     \"Roger that! Over\"     ",
        "",
        "📻 Frecuencia: 446 MHz",
        "📡 Alcance: 5-10 km",
        "🔋 Batería recargable",
        "🚁 Usado en emergencias"
    ]
    
    for linea in walkie_ascii:
        print(linea)

def satelite():
    """Satélite de comunicaciones"""
    print("🛰️ SATÉLITE 🛰️")
    print()
    print("Comunicación espacial avanzada")
    print()
    
    satelite_ascii = [
        "      🛰️ SATÉLITE 🛰️        ",
        "",
        "          ✦  ⭐  ✦          ",
        "       ✦     🌌     ✦       ",
        "     ⭐   ┌─────────┐   ⭐   ",
        "    ✦    │ ● ● ● ● │    ✦  ",
        "  ⭐ ───  │ SATÉLITE │  ─── ⭐",
        "    ✦    │ ◄═══════►│    ✦  ",
        "     ⭐   │ ● ● ● ● │   ⭐   ",
        "       ✦  └─────────┘  ✦    ",
        "          ✦  ⭐  ✦          ",
        "             │              ",
        "          ┌──┴──┐           ",
        "          │PANEL│           ",
        "          │SOLAR│           ",
        "          └─────┘           ",
        "             ║              ",
        "        )))  ║  (((         ",
        "       (((   ║   )))        ",
        "      )))    ║    (((       ",
        "            🌍              ",
        "",
        "🛰️ Órbita geosíncrona",
        "📡 Comunicación global",
        "⚡ Energía solar",
        "🌍 Cobertura continental"
    ]
    
    for linea in satelite_ascii:
        print(linea)

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Selecciona una opción (0-9): ").strip()
            
            if opcion == '0':
                print("\n¡Mantente siempre conectado! 📱")
                break
            elif opcion == '1':
                telefono_movil()
            elif opcion == '2':
                radio_vintage()
            elif opcion == '3':
                television()
            elif opcion == '4':
                computadora()
            elif opcion == '5':
                antena_parabolica()
            elif opcion == '6':
                carta_email()
            elif opcion == '7':
                periodico()
            elif opcion == '8':
                walkie_talkie()
            elif opcion == '9':
                satelite()
            else:
                print("❌ Opción no válida. Por favor, elige una opción del 0 al 9.")
                
        except ValueError:
            print("❌ Por favor, introduce un número válido.")
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego! 📡")
            break
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
