"""
EJERCICIO 61: Ecosistemas y Biomas ASCII

Objetivo:
- Crear representaciones ASCII de diferentes ecosistemas
- Practicar la representación de la biodiversidad
- Explorar la interacción entre organismos y ambiente

Conceptos a practicar:
- Representación de cadenas alimentarias
- Uso de caracteres para simular diferentes biomas
- Creación de ecosistemas complejos
- Diseño de ambientes naturales diversos
"""

def mostrar_menu():
    print("\n" + "="*50)
    print("🌍 ECOSISTEMAS Y BIOMAS ASCII 🌍")
    print("="*50)
    print("0. Salir")
    print("1. Selva tropical 🌳")
    print("2. Desierto 🌵")
    print("3. Tundra ártica ❄️")
    print("4. Arrecife de coral 🐠")
    print("5. Bosque templado 🍂")
    print("6. Sabana africana 🦁")
    print("7. Manglar 🌿")
    print("8. Pradera 🌾")
    print("9. Ecosistema polar 🐧")
    print("="*50)

def dibujar_selva_tropical():
    print("\n🌳 SELVA TROPICAL")
    print("-" * 30)
    selva = """
    🌤️ Dosel Superior 🌤️
    
    🌳🌿🦜🌳🌿🐵🌳🌿🦋🌳
      ║ ∩ ∩ ║ ∩ ∩ ║ ∩ ∩
      ║ │ │ ║ │ │ ║ │ │
      ║ ├─┤ ║ ├─┤ ║ ├─┤
    🌿║ │ │ ║ │ │ ║ │ │🌿
      ║ └─┘ ║ └─┘ ║ └─┘
    🦋║     ║ 🐒 ║     ║🐍
      ║  🌺  ║  🌺  ║  🌺
    🐆║ 🦋 ║🌸🦜🌸║ 🐸 ║🌺
      ████████████████████
    🐜🍄🐛🍃🐸🍂🐜🍄🐛
    
    Biodiversidad: 50% especies mundo 🌎
    """
    print(selva)
    print("Ecosistema con mayor biodiversidad del planeta 🦎")

def dibujar_desierto():
    print("\n🌵 DESIERTO")
    print("-" * 30)
    desierto = """
    ☀️☀️☀️ 45°C ☀️☀️☀️
    
         🌵      🌵
        ╱│╲     ╱│╲
       ╱ │ ╲   ╱ │ ╲
         │       │
       ══╧═══  ══╧═══
    
    🦂        🐍        🦎
      ⋅  ⋅  ⋅  ⋅  ⋅  ⋅
    ⋅  ⋅  ⋅  ⋅  ⋅  ⋅  ⋅
      ⋅  🦂  ⋅  ⋅  🦎  ⋅
    ⋅  ⋅  ⋅  🐍  ⋅  ⋅  ⋅
      ⋅  ⋅  ⋅  ⋅  ⋅  ⋅
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    
    Adaptación: Conservar agua 💧
    """
    print(desierto)
    print("Bioma árido donde la vida se adapta a la escasez 🏜️")

def dibujar_tundra_artica():
    print("\n❄️ TUNDRA ÁRTICA")
    print("-" * 30)
    tundra = """
    ❄️❄️❄️ -30°C ❄️❄️❄️
    
    🐻‍❄️      🦌      🐺
      ❅  ❅  ❅  ❅  ❅
    ❅    ❅    ❅    ❅
      ❅    ❅    ❅
    
    ░░░░░░░░░░░░░░░░░░░░
    ▓▓▓ PERMAFROST ▓▓▓
    ████████████████████
    
    🌱 Musgos y líquenes 🌱
      ❅  🦉  ❅  🐰  ❅
    
    Cadena: Líquenes→Caribú→Lobo
    """
    print(tundra)
    print("Bioma helado con vida adaptada al frío extremo 🧊")

def dibujar_arrecife_coral():
    print("\n🐠 ARRECIFE DE CORAL")
    print("-" * 30)
    arrecife = """
    🌊🌊🌊 Zona Tropical 🌊🌊🌊
    
    🐠 🐡 🦈 🐟 🐠 🦑 🐡
      ≋ ≋ ≋ ≋ ≋ ≋ ≋
    🐢    🌿     🌺    🐙
      ≋ ≋ ≋ ≋ ≋ ≋ ≋
    🐠 🦀 🪸 🦐 🪸 🦞 🐟
      ≋ ≋ ≋ ≋ ≋ ≋ ≋
    🌿 🪸 🐚 🪸 🐚 🪸 🌿
      ≋ ≋ ≋ ≋ ≋ ≋ ≋
    🦀 🪸 🌿 🪸 🌿 🪸 🦀
    ~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Simbiosis: Coral + Algas 🤝
    """
    print(arrecife)
    print("Ecosistema marino de gran diversidad y colorido 🌈")

def dibujar_bosque_templado():
    print("\n🍂 BOSQUE TEMPLADO")
    print("-" * 30)
    bosque = """
    🍂 Otoño 20°C 🍂
    
    🌳🍂🐿️🌳🍃🦅🌳🍂🐿️
      ║   ║   ║   ║   ║
      ║   ║   ║   ║   ║
    🍄║🦔 ║🐰 ║🦌 ║🦔 ║🍄
      ████████████████
    
    🍂🍃🍂🍃🍂🍃🍂🍃🍂
    🐛 🍄 🐜 🍄 🐛 🍄 🐜
    
    Estaciones: Cambio foliar 🔄
    Fauna: Hibernación invierno 😴
    """
    print(bosque)
    print("Bioma de cuatro estaciones con rica biodiversidad 🌸")

def dibujar_sabana_africana():
    print("\n🦁 SABANA AFRICANA")
    print("-" * 30)
    sabana = """
    ☀️ Estación Seca 35°C ☀️
    
       🌴      🌴      🌴
         🦒      🐘    🦏
    
    🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾
      🦁   🦓   🐃   🦛
    🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾
        🐆     🐒     🦮
    🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾
    
    Migración: Ñu siguiendo lluvia ☔
    Cadena: Hierba→Herbívoros→Carnívoros
    """
    print(sabana)
    print("Ecosistema de grandes migraciones y depredadores 🏃‍♂️")

def dibujar_manglar():
    print("\n🌿 MANGLAR")
    print("-" * 30)
    manglar = """
    🌿 Estuario Salobre 🌿
    
    🌳~~~🌳~~~🌳~~~🌳
     ╱│╲ ╱│╲ ╱│╲ ╱│╲
    ╱ │ ╲│ ╲│ ╲│ ╲
      ╲│╱ ╲│╱ ╲│╱ ╲│╱
    ≈≈≈│≈≈≈│≈≈≈│≈≈≈│≈≈
    🦀 ≈ 🦐 ≈ 🐟 ≈ 🦀 ≈
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    🪸 🦞 🐚 🦀 🐠 🦐 🪸
    
    Función: Filtro natural agua 💧
    Protección: Costa contra erosión 🛡️
    """
    print(manglar)
    print("Ecosistema costero que filtra y protege 🌊")

def dibujar_pradera():
    print("\n🌾 PRADERA")
    print("-" * 30)
    pradera = """
    🌤️ Clima Continental 🌤️
    
    🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾
      🐎    🐄    🐑
    🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾
    🦅     🐰     🦔
    🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾
      🐛    🐜    🦗
    🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾
    ████████████████████
    
    Suelo: Rico en materia orgánica 🌱
    Agricultura: Cereales principales 🌽
    """
    print(pradera)
    print("Bioma herbáceo ideal para agricultura y ganadería 🚜")

def dibujar_ecosistema_polar():
    print("\n🐧 ECOSISTEMA POLAR")
    print("-" * 30)
    polar = """
    ❄️❄️❄️ Antártida -40°C ❄️❄️❄️
    
         🐧🐧🐧🐧🐧
           ♦ ♦ ♦
    ████████████████████
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    🐋 ≈ 🦭 ≈ 🐟 ≈ 🦈 ≈
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    🦐 ≈ 🦑 ≈ 🐠 ≈ 🐟 ≈
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    
    Base alimentaria: Krill 🦐
    Adaptación: Grasa corporal 🧊
    """
    print(polar)
    print("Ecosistema extremo de alta especialización 🔬")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (0-9): ").strip()
        
        if opcion == "0":
            print("\n¡Gracias por explorar los ecosistemas del mundo! 🌍")
            break
        elif opcion == "1":
            dibujar_selva_tropical()
        elif opcion == "2":
            dibujar_desierto()
        elif opcion == "3":
            dibujar_tundra_artica()
        elif opcion == "4":
            dibujar_arrecife_coral()
        elif opcion == "5":
            dibujar_bosque_templado()
        elif opcion == "6":
            dibujar_sabana_africana()
        elif opcion == "7":
            dibujar_manglar()
        elif opcion == "8":
            dibujar_pradera()
        elif opcion == "9":
            dibujar_ecosistema_polar()
        else:
            print("\n❌ Opción no válida. Por favor, selecciona un número del 0 al 9.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
