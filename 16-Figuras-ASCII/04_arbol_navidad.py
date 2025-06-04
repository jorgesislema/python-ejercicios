"""
Ejercicio 4: Árbol de Navidad
============================

Objetivo:
Crear diferentes tipos de árboles navideños con tronco, decoraciones y estrella.

Conceptos a practicar:
- Combinación de múltiples formas
- Patrones de repetición
- Decoraciones con caracteres especiales

Instrucciones:
1. Crear árboles de diferentes alturas
2. Añadir tronco al árbol
3. Decorar con ornamentos y luces
4. Coronar con estrella
"""

def dibujar_arbol_simple(altura):
    """Dibuja un árbol de Navidad simple"""
    print(f"\n🎄 Árbol simple (altura {altura}):")
    print("=" * (altura * 2 + 10))
    
    # Estrella en la cima
    espacios_estrella = " " * altura
    print(espacios_estrella + "⭐")
    
    # Cuerpo del árbol
    for i in range(1, altura + 1):
        espacios = " " * (altura - i)
        hojas = "🟢" * i
        print(espacios + hojas)
    
    # Tronco
    espacios_tronco = " " * (altura - 1)
    print(espacios_tronco + "🟫🟫")
    print(espacios_tronco + "🟫🟫")

def dibujar_arbol_decorado(altura):
    """Dibuja un árbol decorado con ornamentos"""
    print(f"\n🎅 Árbol decorado (altura {altura}):")
    print("=" * (altura * 2 + 15))
    
    # Estrella
    espacios_estrella = " " * altura
    print(espacios_estrella + "⭐")
    
    # Cuerpo con decoraciones
    decoraciones = ["🔴", "🟡", "🔵", "🟣", "🟠", "⚪"]
    
    for i in range(1, altura + 1):
        espacios = " " * (altura - i)
        linea = ""
        
        for j in range(i):
            if (i + j) % 3 == 0:
                # Añadir decoración
                linea += decoraciones[(i + j) % len(decoraciones)]
            else:
                linea += "🟢"
        
        print(espacios + linea)
    
    # Tronco
    espacios_tronco = " " * (altura - 1)
    print(espacios_tronco + "🟫🟫")
    print(espacios_tronco + "🟫🟫")

def dibujar_arbol_ascii(altura):
    """Dibuja un árbol usando caracteres ASCII"""
    print(f"\n🌲 Árbol ASCII (altura {altura}):")
    print("=" * (altura * 2 + 10))
    
    # Estrella
    espacios_estrella = " " * altura
    print(espacios_estrella + "*")
    
    # Cuerpo del árbol
    for i in range(1, altura + 1):
        espacios = " " * (altura - i)
        hojas = "^" * (2 * i - 1)
        print(espacios + hojas)
    
    # Tronco
    for _ in range(2):
        espacios_tronco = " " * (altura - 1)
        print(espacios_tronco + "|||")

def dibujar_arbol_con_luces(altura):
    """Dibuja un árbol con luces parpadeantes"""
    print(f"\n✨ Árbol con luces (altura {altura}):")
    print("=" * (altura * 2 + 15))
    
    # Estrella brillante
    espacios_estrella = " " * altura
    print(espacios_estrella + "🌟")
    
    # Cuerpo con luces
    luces = ["💡", "🔆", "✨", "💫", "🌟"]
    
    for i in range(1, altura + 1):
        espacios = " " * (altura - i)
        linea = ""
        
        for j in range(i):
            if (i + j) % 4 == 0:
                # Añadir luz
                linea += luces[(i + j) % len(luces)]
            else:
                linea += "🟢"
        
        print(espacios + linea)
    
    # Tronco decorativo
    espacios_tronco = " " * (altura - 1)
    print(espacios_tronco + "🟫🟫")
    print(espacios_tronco + "🎁🎁")  # Regalos debajo

def dibujar_bosque(num_arboles):
    """Dibuja un pequeño bosque"""
    print(f"\n🌲🌲 Bosque de {num_arboles} árboles:")
    print("=" * (num_arboles * 8 + 10))
    
    alturas = [3, 4, 3, 5, 3][:num_arboles]
    max_altura = max(alturas)
    
    # Dibujar línea por línea
    for fila in range(max_altura + 3):  # +3 para estrella y tronco
        linea = ""
        
        for i, altura in enumerate(alturas):
            if fila == 0:
                # Estrellas
                if altura >= max_altura - 1:
                    linea += "  ⭐  "
                else:
                    linea += "      "
            elif fila <= altura:
                # Cuerpo del árbol
                nivel = fila
                if nivel <= altura:
                    espacios = " " * (3 - min(nivel, 2))
                    hojas = "🟢" * min(nivel, 3)
                    linea += espacios + hojas + espacios
                else:
                    linea += "      "
            else:
                # Tronco
                linea += "  🟫  "
        
        print(linea)

def dibujar_arbol_nieve(altura):
    """Dibuja un árbol con nieve"""
    print(f"\n❄️ Árbol con nieve (altura {altura}):")
    print("=" * (altura * 2 + 15))
    
    # Estrella
    espacios_estrella = " " * altura
    print(espacios_estrella + "⭐")
    
    # Cuerpo con nieve
    for i in range(1, altura + 1):
        espacios = " " * (altura - i)
        linea = ""
        
        for j in range(i):
            if (i + j) % 5 == 0:
                linea += "❄️"  # Copos de nieve
            elif (i + j) % 3 == 0:
                linea += "⚪"  # Nieve acumulada
            else:
                linea += "🟢"
        
        print(espacios + linea)
    
    # Tronco con nieve
    espacios_tronco = " " * (altura - 1)
    print(espacios_tronco + "🟫🟫")
    print(espacios_tronco + "⚪⚪")  # Nieve en la base

def main():
    """Función principal"""
    print("🎄 GENERADOR DE ÁRBOLES DE NAVIDAD")
    print("=" * 45)
    
    print("\nSelecciona el tipo de árbol:")
    print("1. Árbol simple")
    print("2. Árbol decorado")
    print("3. Árbol ASCII")
    print("4. Árbol con luces")
    print("5. Bosque")
    print("6. Árbol con nieve")
    print("7. Mostrar todos")
    
    try:
        opcion = input("\nElige una opción (1-7): ")
        
        if opcion in ["1", "2", "3", "4", "6"]:
            altura = int(input("Ingresa la altura del árbol (3-10): "))
            if altura < 3 or altura > 10:
                print("❌ La altura debe estar entre 3 y 10")
                return
                
            if opcion == "1":
                dibujar_arbol_simple(altura)
            elif opcion == "2":
                dibujar_arbol_decorado(altura)
            elif opcion == "3":
                dibujar_arbol_ascii(altura)
            elif opcion == "4":
                dibujar_arbol_con_luces(altura)
            elif opcion == "6":
                dibujar_arbol_nieve(altura)
                
        elif opcion == "5":
            num_arboles = int(input("¿Cuántos árboles en el bosque? (2-5): "))
            if 2 <= num_arboles <= 5:
                dibujar_bosque(num_arboles)
            else:
                print("❌ Número de árboles debe estar entre 2 y 5")
                
        elif opcion == "7":
            dibujar_arbol_simple(5)
            dibujar_arbol_decorado(4)
            dibujar_arbol_ascii(5)
            dibujar_arbol_con_luces(4)
            dibujar_bosque(3)
            dibujar_arbol_nieve(5)
        else:
            print("❌ Opción no válida")
            
    except ValueError:
        print("❌ Por favor ingresa un número válido")

if __name__ == "__main__":
    main()
