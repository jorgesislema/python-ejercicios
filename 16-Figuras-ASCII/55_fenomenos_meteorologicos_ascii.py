"""
EJERCICIO 55: Fenómenos Meteorológicos ASCII

Objetivo:
- Crear representaciones ASCII de diferentes fenómenos meteorológicos
- Practicar la animación visual con caracteres
- Explorar patrones naturales y efectos climáticos

Conceptos a practicar:
- Uso de caracteres para simular movimiento
- Representación de patrones naturales
- Creación de efectos visuales con ASCII
- Diseño de interfaces temáticas
"""

def mostrar_menu():
    print("\n" + "="*50)
    print("🌦️ FENÓMENOS METEOROLÓGICOS ASCII 🌦️")
    print("="*50)
    print("0. Salir")
    print("1. Lluvia ☔")
    print("2. Nieve ❄️")
    print("3. Tormenta eléctrica ⚡")
    print("4. Tornado 🌪️")
    print("5. Arco iris 🌈")
    print("6. Niebla 🌫️")
    print("7. Granizo 🧊")
    print("8. Viento 💨")
    print("9. Aurora boreal 🌌")
    print("="*50)

def dibujar_lluvia():
    print("\n☔ LLUVIA")
    print("-" * 30)
    lluvia = """
     ☁️☁️☁️☁️☁️☁️☁️☁️☁️
    ☁️               ☁️
   ☁️                 ☁️
    
    │ │ │ │ │ │ │ │ │
     │ │ │ │ │ │ │ │
    │ │ │ │ │ │ │ │ │
     │ │ │ │ │ │ │ │
    │ │ │ │ │ │ │ │ │
     │ │ │ │ │ │ │ │
    │ │ │ │ │ │ │ │ │
     │ │ │ │ │ │ │ │
    │ │ │ │ │ │ │ │ │
    
    ~~~~~~~~~~~~~~~~~~~
    """
    print(lluvia)
    print("Precipitación acuosa que nutre la tierra 🌱")

def dibujar_nieve():
    print("\n❄️ NIEVE")
    print("-" * 30)
    nieve = """
     ☁️☁️☁️☁️☁️☁️☁️☁️☁️
    ☁️               ☁️
   ☁️                 ☁️
    
      ❄️   ❅   ❆   ❄️
    ❅     ❄️   ❅     ❆
      ❆       ❄️   ❅
    ❄️   ❅       ❆   ❄️
      ❅   ❆   ❄️     ❅
    ❆     ❄️       ❅
      ❄️       ❅   ❆
    ❅   ❆   ❄️       ❄️
      ❅       ❆   ❅
    
    ▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️
    """
    print(nieve)
    print("Cristales de hielo que cubren el paisaje ⛄")

def dibujar_tormenta():
    print("\n⚡ TORMENTA ELÉCTRICA")
    print("-" * 30)
    tormenta = """
    ☁️⚡☁️⚡☁️⚡☁️⚡☁️
   ⚡               ⚡
  ☁️                 ☁️
    
    ⚡     ⚡⚡⚡     ⚡
       ⚡⚡     ⚡⚡
    ⚡⚡   ⚡⚡⚡   ⚡⚡
     ⚡⚡⚡  │  ⚡⚡⚡
       ⚡⚡ │ ⚡⚡
         ⚡│⚡
          │
          │
    
    █████████████████
    ≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋
    """
    print(tormenta)
    print("Descargas eléctricas atmosféricas espectaculares ⛈️")

def dibujar_tornado():
    print("\n🌪️ TORNADO")
    print("-" * 30)
    tornado = """
    ☁️☁️☁️☁️☁️☁️☁️☁️☁️
   ☁️               ☁️
  ☁️                 ☁️
   ☁️               ☁️
    ☁️             ☁️
     ☁️           ☁️
      ☁️         ☁️
       ☁️       ☁️
        ☁️     ☁️
         ☁️   ☁️
          ☁️ ☁️
           ☁️
           ╱│╲
          ╱ │ ╲
         ╱  │  ╲
        ╱   │   ╲
       ╱    │    ╲
    ███████████████
    """
    print(tornado)
    print("Vórtice de viento destructivo y poderoso 🌀")

def dibujar_arco_iris():
    print("\n🌈 ARCO IRIS")
    print("-" * 30)
    arco_iris = """
    ☁️             ☁️
      ╭─────────────╮
     ╱ 🔴🔴🔴🔴🔴🔴🔴 ╲
    ╱  🟠🟠🟠🟠🟠🟠🟠  ╲
   ╱   🟡🟡🟡🟡🟡🟡🟡   ╲
  ╱    🟢🟢🟢🟢🟢🟢🟢    ╲
 ╱     🔵🔵🔵🔵🔵🔵🔵     ╲
╱      🟣🟣🟣🟣🟣🟣🟣      ╲
       🟤🟤🟤🟤🟤🟤🟤
    
     🌳    🏠    🌳
    ████████████████
    """
    print(arco_iris)
    print("Espectro de colores tras la lluvia 🌤️")

def dibujar_niebla():
    print("\n🌫️ NIEBLA")
    print("-" * 30)
    niebla = """
    ≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋
   ≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋
  ≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋
    ≋≋≋🌳≋≋≋≋≋🏠≋≋≋≋
   ≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋
  ≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋
    ≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋
   ≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋
  ≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋
    ≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋
   ≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋
  ≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋
    ≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋
    """
    print(niebla)
    print("Suspensión de gotas que reduce la visibilidad 👻")

def dibujar_granizo():
    print("\n🧊 GRANIZO")
    print("-" * 30)
    granizo = """
     ⛈️⛈️⛈️⛈️⛈️⛈️⛈️⛈️⛈️
    ⛈️               ⛈️
   ⛈️                 ⛈️
    
    ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯
     ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯
    ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯
     ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯
    ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯
     ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯
    ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯
     ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯
    
    ▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣
    """
    print(granizo)
    print("Bolas de hielo que caen con fuerza 🥎")

def dibujar_viento():
    print("\n💨 VIENTO")
    print("-" * 30)
    viento = """
    🌳~~~> 🌳~~~> 🌳~~~>
     ╱       ╱       ╱
    ╱       ╱       ╱
    
    ~~~> ~~~> ~~~> ~~~>
      ~~~> ~~~> ~~~>
    ~~~> ~~~> ~~~> ~~~>
      ~~~> ~~~> ~~~>
    ~~~> ~~~> ~~~> ~~~>
      ~~~> ~~~> ~~~>
    
    🍃 🍃 🍃 🍃 🍃 ~~~~>
      🍃 🍃 🍃 ~~~~>
    🍃 🍃 🍃 🍃 ~~~~>
    
    🏠💨    🏠💨    🏠💨
    """
    print(viento)
    print("Movimiento del aire que transporta energía 🍃")

def dibujar_aurora_boreal():
    print("\n🌌 AURORA BOREAL")
    print("-" * 30)
    aurora = """
    ✨ ⭐ ✨ ⭐ ✨ ⭐ ✨
      ┊ ░ ░ ░ ░ ░ ┊
     ┊ ░ 🟢 🟢 🟢 ░ ┊
    ┊ ░ 🟢 💚 💚 🟢 ░ ┊
     ┊ ░ 💚 💙 💚 ░ ┊
    ┊ ░ 💚 💙 🔵 💙 💚 ░ ┊
     ┊ ░ 💙 🔵 💙 ░ ┊
    ┊ ░ 💙 🟣 🟣 💙 ░ ┊
     ┊ ░ 🟣 🟣 ░ ┊
    ┊ ░ ░ 🟣 ░ ░ ┊
     ┊ ░ ░ ░ ░ ┊
      ┊ ░ ░ ░ ┊
    
    ⛰️  🏠  ⛰️  🌲  ⛰️
    ████████████████████
    """
    print(aurora)
    print("Luces celestiales danzando en el cielo polar 🎭")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (0-9): ").strip()
        
        if opcion == "0":
            print("\n¡Gracias por explorar los fenómenos meteorológicos! 🌦️")
            break
        elif opcion == "1":
            dibujar_lluvia()
        elif opcion == "2":
            dibujar_nieve()
        elif opcion == "3":
            dibujar_tormenta()
        elif opcion == "4":
            dibujar_tornado()
        elif opcion == "5":
            dibujar_arco_iris()
        elif opcion == "6":
            dibujar_niebla()
        elif opcion == "7":
            dibujar_granizo()
        elif opcion == "8":
            dibujar_viento()
        elif opcion == "9":
            dibujar_aurora_boreal()
        else:
            print("\n❌ Opción no válida. Por favor, selecciona un número del 0 al 9.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
