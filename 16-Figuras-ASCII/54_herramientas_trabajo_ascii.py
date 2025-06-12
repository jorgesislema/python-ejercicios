"""
EJERCICIO 54: Herramientas de Trabajo ASCII

Objetivo:
- Crear figuras ASCII de herramientas de trabajo y oficina
- Practicar el diseño de objetos técnicos con caracteres
- Explorar diferentes estilos de representación de herramientas

Conceptos a practicar:
- Uso de caracteres especiales para detalles técnicos
- Representación de formas geométricas complejas
- Creación de patrones repetitivos
- Diseño de interfaces de usuario interactivas
"""

def mostrar_menu():
    print("\n" + "="*50)
    print("🔧 HERRAMIENTAS DE TRABAJO ASCII 🔧")
    print("="*50)
    print("0. Salir")
    print("1. Martillo 🔨")
    print("2. Destornillador 🪛")
    print("3. Ordenador 💻")
    print("4. Teléfono 📞")
    print("5. Calculadora 🔢")
    print("6. Llave inglesa 🔧")
    print("7. Sierra ⚒️")
    print("8. Taladro 🔩")
    print("9. Caja de herramientas 🧰")
    print("="*50)

def dibujar_martillo():
    print("\n🔨 MARTILLO")
    print("-" * 30)
    martillo = """
    ╔═══════════╗
    ║███████████║
    ║███████████║
    ╚══════╤════╝
           │
           │ ░░░
           │ ░░░
           │ ░░░
           │ ░░░
           │ ░░░
           │ ░░░
           │ ░░░
           │ ░░░
           └─────
    """
    print(martillo)
    print("Herramienta básica para golpear y construir 🏗️")

def dibujar_destornillador():
    print("\n🪛 DESTORNILLADOR")
    print("-" * 30)
    destornillador = """
    ╔═╗
    ║ ║
    ║ ║
    ╚═╝
      │
      │ ░░░░░░░░░░░
      │ ░░░░░░░░░░░
      │ ░░░░░░░░░░░
      │ ░░░░░░░░░░░
      │ ░░░░░░░░░░░
      └─────────────
    """
    print(destornillador)
    print("Herramienta para apretar y aflojar tornillos 🔩")

def dibujar_ordenador():
    print("\n💻 ORDENADOR")
    print("-" * 30)
    ordenador = """
    ╔══════════════════════════╗
    ║ ○ ○ ○                    ║
    ║                          ║
    ║  > Sistema iniciado...   ║
    ║  > Procesando datos...   ║
    ║  > █████████████         ║
    ║  > 87% completado        ║
    ║                          ║
    ║  [OK] [CANCELAR] [AYUDA] ║
    ║                          ║
    ╚═══════════╤══════════════╝
                │
    ╔═══════════╧══════════════╗
    ║ ○ ● ◐ ◑ ◒ ◓ ◔ ◕ ◖ ◗ ◘ ◙ ║
    ╚══════════════════════════╝
    """
    print(ordenador)
    print("Herramienta digital moderna para trabajo y comunicación 💼")

def dibujar_telefono():
    print("\n📞 TELÉFONO")
    print("-" * 30)
    telefono = """
        ╔═══════╗
        ║ ● ● ● ║
        ║       ║
      ╔═╝ 1 2 3 ╚═╗
      ║ 4 5 6     ║
      ║ 7 8 9     ║
      ║ * 0 #     ║
      ║           ║
      ║  ♪ ♫ ♪ ♫  ║
      ╚═══════════╝
          │   │
          │   │
       ╔══╧═══╧══╗
       ║  ○   ○  ║
       ║    ∩    ║
       ╚═════════╝
    """
    print(telefono)
    print("Dispositivo de comunicación tradicional ☎️")

def dibujar_calculadora():
    print("\n🔢 CALCULADORA")
    print("-" * 30)
    calculadora = """
    ╔═══════════════╗
    ║ 123456789.00  ║
    ╠═══════════════╣
    ║ C  CE  ÷   ×  ║
    ║ 7   8   9  -  ║
    ║ 4   5   6  +  ║
    ║ 1   2   3     ║
    ║ 0   .   = ▌▌▌ ║
    ╚═══════════════╝
    """
    print(calculadora)
    print("Herramienta para cálculos matemáticos 📊")

def dibujar_llave_inglesa():
    print("\n🔧 LLAVE INGLESA")
    print("-" * 30)
    llave = """
    ╔═══╗     ╔══════════╗
    ║   ╚═══╤═╝          ║
    ║       │   ░░░░░░░  ║
    ║   ╔═══╧═╗ ░░░░░░░  ║
    ╚═══╝     ╚══════════╝
                 │││││││
                 │││││││
    """
    print(llave)
    print("Herramienta ajustable para tuercas y tornillos ⚙️")

def dibujar_sierra():
    print("\n⚒️ SIERRA")
    print("-" * 30)
    sierra = """
    ╔═══════════════════════════╗
    ║ ░░░░░░░░░░░░░░░░░░░░░░░░░ ║
    ╚═╤═══════════════════════╤═╝
      │ ∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧∧ │
      │ ∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨∨ │
      │                       │
      │ ░░░░░░░░░░░░░░░░░░░░░ │
      └───────────────────────┘
    """
    print(sierra)
    print("Herramienta para cortar madera y materiales 🪚")

def dibujar_taladro():
    print("\n🔩 TALADRO")
    print("-" * 30)
    taladro = """
           ◄─────►
    ╔══════════════════╗
    ║  ◄─► ON/OFF      ║
    ║ ╔══════════════╗ ║
    ║ ║ ░░░░░░░░░░░░ ║ ║
    ║ ╚══════════════╝ ║
    ║     [∘]          ║
    ╚═══════╤══════════╝
            │
    ╔═══════╧═══════╗
    ║    ○ ○ ○ ○    ║
    ║    ░░░░░░░░    ║
    ╚═══════════════╝
    """
    print(taladro)
    print("Herramienta eléctrica para perforar 🏗️")

def dibujar_caja_herramientas():
    print("\n🧰 CAJA DE HERRAMIENTAS")
    print("-" * 30)
    caja = """
         ╔════════════════════════╗
         ║                        ║
    ╔════╩════════════════════════╩════╗
    ║ 🔨 🪛 🔧 ⚒️ 🔩 📏 ✂️ 🪓 🔗 ║
    ║                              ║
    ║ ╔══╗ ╔══╗ ╔══╗ ╔══╗ ╔══╗    ║
    ║ ║░░║ ║░░║ ║░░║ ║░░║ ║░░║    ║
    ║ ╚══╝ ╚══╝ ╚══╝ ╚══╝ ╚══╝    ║
    ║                              ║
    ║ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦ ♦      ║
    ╚══════════════════════════════╝
    """
    print(caja)
    print("Contenedor organizado para todas las herramientas 🛠️")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (0-9): ").strip()
        
        if opcion == "0":
            print("\n¡Gracias por usar el generador de herramientas ASCII! 🔧")
            break
        elif opcion == "1":
            dibujar_martillo()
        elif opcion == "2":
            dibujar_destornillador()
        elif opcion == "3":
            dibujar_ordenador()
        elif opcion == "4":
            dibujar_telefono()
        elif opcion == "5":
            dibujar_calculadora()
        elif opcion == "6":
            dibujar_llave_inglesa()
        elif opcion == "7":
            dibujar_sierra()
        elif opcion == "8":
            dibujar_taladro()
        elif opcion == "9":
            dibujar_caja_herramientas()
        else:
            print("\n❌ Opción no válida. Por favor, selecciona un número del 0 al 9.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
