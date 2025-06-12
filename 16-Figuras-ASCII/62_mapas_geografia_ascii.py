"""
EJERCICIO 62: Mapas y Geografía ASCII

Objetivo:
- Crear representaciones ASCII de mapas y elementos geográficos
- Practicar la representación cartográfica con caracteres
- Explorar conceptos de geografía física y política

Conceptos a practicar:
- Representación de accidentes geográficos
- Uso de símbolos cartográficos
- Creación de mapas temáticos
- Diseño de elementos topográficos
"""

def mostrar_menu():
    print("\n" + "="*50)
    print("🗺️ MAPAS Y GEOGRAFÍA ASCII 🗺️")
    print("="*50)
    print("0. Salir")
    print("1. Continentes del mundo 🌍")
    print("2. Isla tropical 🏝️")
    print("3. Cordillera montañosa ⛰️")
    print("4. Delta de río 🌊")
    print("5. Península 🏖️")
    print("6. Archipiélago 🏝️")
    print("7. Valle y meseta 🏔️")
    print("8. Costa con bahías 🏖️")
    print("9. Mapa del tesoro 💰")
    print("="*50)

def dibujar_continentes_mundo():
    print("\n🌍 CONTINENTES DEL MUNDO")
    print("-" * 30)
    continentes = """
      🗺️ PLANISFERIO MUNDIAL 🗺️
    
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    ≈≈ 🇺🇸 AMÉRICA ≈≈≈ 🇪🇺 EUROPA ≈≈
    ≈≈ DEL NORTE   ≈≈≈     ≈≈≈≈≈≈≈
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ 🇷🇺 ASIA ≈≈≈≈
    ≈≈≈ 🇧🇷 AMÉRICA ≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    ≈≈≈ DEL SUR    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    ≈≈≈≈≈≈≈ 🇿🇦 ÁFRICA ≈≈≈ 🇦🇺 ≈≈≈
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ OCEANÍA ≈≈
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    ≈≈≈≈≈≈≈ ❄️ ANTÁRTIDA ❄️ ≈≈≈≈≈≈
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    
    Superficie total: 510 millones km² 🌎
    """
    print(continentes)
    print("Vista global de los continentes terrestres 🌐")

def dibujar_isla_tropical():
    print("\n🏝️ ISLA TROPICAL")
    print("-" * 30)
    isla = """
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    ≈≈≈≈╭─────────────╮≈≈≈≈≈≈≈≈
    ≈≈≈╱ 🌴 🌺 🌴 🌺 ╲≈≈≈≈≈≈≈
    ≈≈╱ 🦜  🏖️  🏖️  🦜 ╲≈≈≈≈≈
    ≈╱ 🌺 ⛰️ 🌋 ⛰️ 🌺 ╲≈≈≈≈
    ≈│ 🌴 🏖️ 🌊 🏖️ 🌴 │≈≈≈≈
    ≈╲ 🐚 🏝️ 🌸 🏝️ 🐚 ╱≈≈≈≈
    ≈≈╲ 🦀  🏖️  🏖️  🦀 ╱≈≈≈≈≈
    ≈≈≈╲ 🌴 🌺 🌴 🌺 ╱≈≈≈≈≈≈≈
    ≈≈≈≈╰─────────────╯≈≈≈≈≈≈≈≈
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    
    Clima: Tropical húmedo 🌡️ 28°C
    """
    print(isla)
    print("Paraíso tropical rodeado de aguas cristalinas 🏄‍♂️")

def dibujar_cordillera_montana():
    print("\n⛰️ CORDILLERA MONTAÑOSA")
    print("-" * 30)
    cordillera = """
    ❄️ PICOS NEVADOS ❄️
    
              ⛰️
             ╱▲╲
            ╱ ▲ ╲
      ⛰️   ╱  ▲  ╲   ⛰️
     ╱▲╲ ╱   ▲   ╲ ╱▲╲
    ╱ ▲ ╲   ▲▲▲   ╱ ▲ ╲
      ▲  ╲ ▲▲▲▲▲ ╱  ▲
       ▲▲ ╲▲▲▲▲╱ ▲▲
        ▲▲▲▲▲▲▲▲▲▲
         ▲▲▲▲▲▲▲▲
    🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲
    ████████████████████
    
    Altitud: 3000-5000 msnm 📏
    Ecosistema: Montano y alpino 🦅
    """
    print(cordillera)
    print("Cadena montañosa con picos nevados y biodiversidad 🏔️")

def dibujar_delta_rio():
    print("\n🌊 DELTA DE RÍO")
    print("-" * 30)
    delta = """
    🏔️ FUENTE DEL RÍO 🏔️
         │
         ├─🌊─┐
         │    │
         │    ├─🌊─┐
         │    │    │
         ├─🌊─┤    │
         │    │    │
         │    ├─🌊─┤
         │    │    │
         └─🌊─┤    │
              │    │
              └─🌊─┘
                │
    🌿🌿🌿🌿🌿🌊🌿🌿🌿🌿🌿
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    ≈≈≈ ESTUARIO Y MAR ≈≈≈
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    
    Sedimentos: Tierra fértil 🌱
    """
    print(delta)
    print("Desembocadura fluvial formando tierras fértiles 🚢")

def dibujar_peninsula():
    print("\n🏖️ PENÍNSULA")
    print("-" * 30)
    peninsula = """
    ████████████████████████
    ███ TIERRA CONTINENTAL ███
    ████████████████████████
         │                │
         │  🏖️ PENÍNSULA │
         │      🏰       │
    ≈≈≈≈≈│      🏛️       │≈≈≈≈≈
    ≈≈≈≈≈│  🌴     🌴   │≈≈≈≈≈
    ≈≈≈≈≈│      🏖️       │≈≈≈≈≈
    ≈≈≈≈≈│               │≈≈≈≈≈
    ≈≈≈≈≈│  🦀  ⛵  🐚  │≈≈≈≈≈
    ≈≈≈≈≈└───────────────┘≈≈≈≈≈
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    
    Característica: Rodeada por agua 💧
    """
    print(peninsula)
    print("Territorio que se adentra en el mar 🌊")

def dibujar_archipielago():
    print("\n🏝️ ARCHIPIÉLAGO")
    print("-" * 30)
    archipielago = """
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    ≈≈≈🏝️≈≈≈≈🏝️≈≈≈≈🏝️≈≈≈≈≈≈
    ≈≈ 🌴 ≈≈≈ 🌺 ≈≈≈ 🌴 ≈≈≈≈≈
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    ≈≈≈≈≈🏝️≈≈≈≈≈≈≈🏝️≈≈≈≈≈≈≈≈
    ≈≈≈≈ 🦜 ≈≈≈≈≈≈ 🏖️ ≈≈≈≈≈≈≈
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    ≈≈🏝️≈≈≈≈≈≈≈≈≈≈≈≈≈🏝️≈≈≈≈≈
    ≈ 🌺 ≈≈≈≈≈≈≈≈≈≈≈≈≈ 🌴 ≈≈≈≈
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    ≈≈≈≈≈≈🏝️≈≈≈🏝️≈≈≈≈≈≈≈≈≈≈≈
    ≈≈≈≈≈ 🐚 ≈≈ 🦀 ≈≈≈≈≈≈≈≈≈≈
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    
    Formación: Origen volcánico 🌋
    """
    print(archipielago)
    print("Conjunto de islas dispersas en el océano ⛵")

def dibujar_valle_meseta():
    print("\n🏔️ VALLE Y MESETA")
    print("-" * 30)
    valle_meseta = """
    ⛰️ MESETA ELEVADA ⛰️
    ████████████████████████
    ██ 🌾 🏠 🌾 🏠 🌾 ██
    ████████████████████████
    ███████│     │███████
           │     │
           │ 🌊  │  VALLE
           │     │
           │ 🌳  │
           │     │
           │ 🦌  │
           │     │
           │ 🌸  │
    ███████│     │███████
    ████████████████████████
    
    Características: Tierra plana elevada
    Uso: Agricultura y ganadería 🐄
    """
    print(valle_meseta)
    print("Contraste topográfico entre alturas y depresiones 📊")

def dibujar_costa_bahias():
    print("\n🏖️ COSTA CON BAHÍAS")
    print("-" * 30)
    costa = """
    ████████████████████████
    ██ 🏰 PUERTO 🏰 ████
    ████████████████████████
    ████╲               ╱████
    ████ ╲ BAHÍA NORTE ╱ ████
    ████  ╲___________╱  ████
    ████≈≈≈⛵≈🐟≈⛵≈≈≈████
    ████≈≈≈≈≈≈≈≈≈≈≈≈≈████
    ████  ╱─────────╲  ████
    ████ ╱ BAHÍA SUR ╲ ████
    ████╱             ╲████
    ████████████████████████
    
    Actividades: Pesca y navegación ⚓
    Protección: Refugio natural 🛡️
    """
    print(costa)
    print("Litoral con bahías protegidas para navegación 🚢")

def dibujar_mapa_tesoro():
    print("\n💰 MAPA DEL TESORO")
    print("-" * 30)
    mapa_tesoro = """
    ╔═══ MAPA PIRATA 1775 ═══╗
    ║                         ║
    ║ 🏝️ ISLA CALAVERA 🏝️     ║
    ║                         ║
    ║  🌴    ⛰️    🌴        ║
    ║    ╲   │   ╱           ║
    ║     ╲  │  ╱  🦜        ║
    ║      ╲ │ ╱             ║
    ║ 🐚    ╲│╱    🌺        ║
    ║         X              ║
    ║    💰 TESORO 💰        ║
    ║                        ║
    ║ 🦀  30 pasos N  🏖️     ║
    ║                        ║
    ╚════════════════════════╝
    
    "Donde la calavera sonríe, 
     allí yace el oro del capitán" ☠️
    """
    print(mapa_tesoro)
    print("Antiguo mapa náutico con ubicación del tesoro 🗺️")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (0-9): ").strip()
        
        if opcion == "0":
            print("\n¡Gracias por explorar la geografía mundial! 🗺️")
            break
        elif opcion == "1":
            dibujar_continentes_mundo()
        elif opcion == "2":
            dibujar_isla_tropical()
        elif opcion == "3":
            dibujar_cordillera_montana()
        elif opcion == "4":
            dibujar_delta_rio()
        elif opcion == "5":
            dibujar_peninsula()
        elif opcion == "6":
            dibujar_archipielago()
        elif opcion == "7":
            dibujar_valle_meseta()
        elif opcion == "8":
            dibujar_costa_bahias()
        elif opcion == "9":
            dibujar_mapa_tesoro()
        else:
            print("\n❌ Opción no válida. Por favor, selecciona un número del 0 al 9.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
