"""
Ejercicio 49: Planetas y Sistema Solar ASCII

Objetivo:
- Crear representaciones ASCII del sistema solar y planetas
- Incluir variantes: Sol, planetas, órbitas, fases lunares
- Permitir personalización y mostrar datos astronómicos

Conceptos:
- Astronomía en ASCII
- Sistema solar
- Escalas y proporciones
"""

def sol_ascii():
    """Sol ASCII con rayos"""
    print("☀️ SOL ASCII ☀️")
    print("═" * 40)
    
    print("""
         \\   |   /
          \\  |  /
        \\  \\ | /  /
         \\  \\|/  /
      ────  ☀️  ────
         /  /|\\  \\
        /  / | \\  \\
          /  |  \\
         /   |   \\
    """)
    
    print("☀️ El Sol - Estrella del sistema solar")
    print("🌡️ Temperatura: ~5,500°C en superficie")
    print("📏 Diámetro: ~1,392,000 km")

def planetas_interiores():
    """Planetas interiores del sistema solar"""
    print("🪐 PLANETAS INTERIORES ASCII 🪐")
    print("═" * 50)
    
    print("1. MERCURIO:")
    print("    ●")
    print("  Más cercano al Sol")
    
    print("\n2. VENUS:")
    print("    ◉")
    print("  El planeta más caliente")
    
    print("\n3. TIERRA:")
    print("    🌍")
    print("  Nuestro hogar")
    
    print("\n4. MARTE:")
    print("    🔴")
    print("  El planeta rojo")

def planetas_exteriores():
    """Planetas exteriores del sistema solar"""
    print("🪐 PLANETAS EXTERIORES ASCII 🪐")
    print("═" * 50)
    
    print("5. JÚPITER:")
    print("     ●●●●●")
    print("    ●●●●●●●")
    print("     ●●●●●")
    print("  El gigante gaseoso")
    
    print("\n6. SATURNO:")
    print("     ─────")
    print("    ●●●●●●●")
    print("     ─────")
    print("  Con sus famosos anillos")
    
    print("\n7. URANO:")
    print("      │")
    print("    ──●──")
    print("      │")
    print("  Rota de lado")
    
    print("\n8. NEPTUNO:")
    print("    ◉◉◉")
    print("   ◉◉◉◉◉")
    print("    ◉◉◉")
    print("  El más ventoso")

def sistema_solar_completo():
    """Sistema solar completo ASCII"""
    print("🌌 SISTEMA SOLAR COMPLETO ASCII 🌌")
    print("═" * 60)
    
    print("                    ☀️")
    print("              ●        <- Mercurio")
    print("            ◉          <- Venus")
    print("          🌍            <- Tierra")
    print("        🔴              <- Marte")
    print("      ●●●●●             <- Júpiter")
    print("    ─●●●●●─             <- Saturno")
    print("   ──●──                <- Urano")
    print("  ◉◉◉                   <- Neptuno")
    
    print("\nDistancias aproximadas del Sol:")
    print("Mercurio: 58M km    |  Venus: 108M km")
    print("Tierra: 150M km     |  Marte: 228M km")
    print("Júpiter: 778M km    |  Saturno: 1,430M km")
    print("Urano: 2,880M km    |  Neptuno: 4,500M km")

def orbitas_planetas():
    """Órbitas de los planetas ASCII"""
    print("🌀 ÓRBITAS PLANETARIAS ASCII 🌀")
    print("═" * 50)
    
    print("Vista desde arriba del sistema solar:")
    print("""
                ◯ ◯ ◯ ◯ ◯ ◯
              ◯             ◯
            ◯                 ◯
          ◯         ☀️         ◯
            ◯                 ◯
              ◯             ◯
                ◯ ◯ ◯ ◯ ◯ ◯
    """)
    
    print("Órbitas concéntricas:")
    for i, planeta in enumerate(["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]):
        espacios = "  " * i
        print(f"{espacios}○ {planeta}")

def fases_luna():
    """Fases de la Luna ASCII"""
    print("🌙 FASES DE LA LUNA ASCII 🌙")
    print("═" * 50)
    
    print("Ciclo lunar completo:")
    print("""
    Luna Nueva    Cuarto        Luna Llena    Cuarto
                 Creciente                   Menguante
    
        ●           ◐             ○            ◑
        
    """)
    
    print("Fases detalladas:")
    fases = [
        ("●", "Luna Nueva", "No visible"),
        ("◗", "Cuarto Creciente", "Lado derecho iluminado"),
        ("○", "Luna Llena", "Completamente iluminada"),
        ("◖", "Cuarto Menguante", "Lado izquierdo iluminado")
    ]
    
    for simbolo, nombre, descripcion in fases:
        print(f"{simbolo} {nombre}: {descripcion}")

def eclipses_ascii():
    """Eclipses solares y lunares ASCII"""
    print("🌒 ECLIPSES ASCII 🌒")
    print("═" * 50)
    
    print("ECLIPSE SOLAR:")
    print("☀️ ---- 🌑 ---- 🌍")
    print("Sol    Luna   Tierra")
    print("La Luna bloquea la luz del Sol")
    
    print("\nECLIPSE LUNAR:")
    print("☀️ ---- 🌍 ---- 🌕")
    print("Sol   Tierra   Luna")
    print("La Tierra bloquea la luz hacia la Luna")
    
    print("\nTipos de eclipse solar:")
    print("🌑 Total: Corona visible")
    print("🌘 Parcial: Parcialmente cubierto")
    print("💍 Anular: Anillo de fuego")

def constelaciones_ascii():
    """Constelaciones básicas ASCII"""
    print("⭐ CONSTELACIONES ASCII ⭐")
    print("═" * 50)
    
    print("OSA MAYOR:")
    print("""
    ★       ★
      ★   ★
        ★
      ★   ★
    """)
    
    print("ORIÓN:")
    print("""
      ★     ★
        ★ ★ ★
          ★
        ★   ★
      ★       ★
    """)
    
    print("CRUZ DEL SUR:")
    print("""
        ★
      ★   ★
        ★
        ★
    """)

def planetas_enanos():
    """Planetas enanos ASCII"""
    print("🪨 PLANETAS ENANOS ASCII 🪨")
    print("═" * 50)
    
    print("Más allá de Neptuno:")
    print("• Plutón: El más famoso")
    print("• Eris: Más masivo que Plutón")
    print("• Makemake: Con forma de huevo")
    print("• Haumea: Muy alargado")
    print("• Ceres: En el cinturón de asteroides")
    
    print("\nRepresentación:")
    print("○ Plutón")
    print("◦ Eris") 
    print("∘ Makemake")
    print("⬭ Haumea")
    print("● Ceres")

def menu_principal():
    """Menú principal del programa"""
    while True:
        print("\n" + "═" * 60)
        print("🌌 PLANETAS Y SISTEMA SOLAR ASCII 🌌")
        print("═" * 60)
        print("1. El Sol")
        print("2. Planetas interiores")
        print("3. Planetas exteriores")
        print("4. Sistema solar completo")
        print("5. Órbitas planetarias")
        print("6. Fases de la Luna")
        print("7. Eclipses")
        print("8. Constelaciones")
        print("9. Planetas enanos")
        print("0. Salir")
        print("═" * 60)
        
        opcion = input("Selecciona una opción astronómica: ")
        
        if opcion == "1":
            sol_ascii()
        elif opcion == "2":
            planetas_interiores()
        elif opcion == "3":
            planetas_exteriores()
        elif opcion == "4":
            sistema_solar_completo()
        elif opcion == "5":
            orbitas_planetas()
        elif opcion == "6":
            fases_luna()
        elif opcion == "7":
            eclipses_ascii()
        elif opcion == "8":
            constelaciones_ascii()
        elif opcion == "9":
            planetas_enanos()
        elif opcion == "0":
            print("¡Hasta luego, astronauta! 🚀")
            break
        else:
            print("Opción no válida")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
