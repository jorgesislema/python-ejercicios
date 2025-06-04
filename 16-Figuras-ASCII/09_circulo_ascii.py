"""
Ejercicio 9: Círculo ASCII
==========================

Objetivo:
Crear círculos usando caracteres ASCII con diferentes técnicas de aproximación.

Conceptos a practicar:
- Algoritmos de círculo
- Coordenadas cartesianas
- Aproximación de curvas con caracteres

Instrucciones:
1. Usar la ecuación del círculo para determinar posiciones
2. Crear círculos de diferentes radios
3. Implementar círculos sólidos y huecos
"""

import math

def dibujar_circulo_simple(radio):
    """Dibuja un círculo simple usando asteriscos"""
    print(f"\n⭕ Círculo simple (radio {radio}):")
    print("=" * (radio * 4 + 10))
    
    tamaño = radio * 2 + 1
    centro = radio
    
    for i in range(tamaño):
        linea = ""
        for j in range(tamaño):
            # Calcular distancia del centro
            distancia = math.sqrt((i - centro)**2 + (j - centro)**2)
            
            # Si está aproximadamente en el borde del círculo
            if abs(distancia - radio) <= 0.5:
                linea += "* "
            else:
                linea += "  "
        print(linea)

def dibujar_circulo_solido(radio):
    """Dibuja un círculo sólido"""
    print(f"\n🔴 Círculo sólido (radio {radio}):")
    print("=" * (radio * 4 + 10))
    
    tamaño = radio * 2 + 1
    centro = radio
    
    for i in range(tamaño):
        linea = ""
        for j in range(tamaño):
            distancia = math.sqrt((i - centro)**2 + (j - centro)**2)
            
            if distancia <= radio:
                linea += "█ "
            else:
                linea += "  "
        print(linea)

def dibujar_circulo_emoji(radio):
    """Dibuja un círculo usando emojis"""
    print(f"\n🟡 Círculo emoji (radio {radio}):")
    print("=" * (radio * 4 + 10))
    
    tamaño = radio * 2 + 1
    centro = radio
    
    for i in range(tamaño):
        linea = ""
        for j in range(tamaño):
            distancia = math.sqrt((i - centro)**2 + (j - centro)**2)
            
            if distancia <= radio * 0.3:
                linea += "🔴"  # Centro
            elif distancia <= radio * 0.6:
                linea += "🟡"  # Medio
            elif distancia <= radio:
                linea += "🟢"  # Borde
            else:
                linea += "  "
        print(linea)

def dibujar_circulo_con_centro(radio):
    """Dibuja un círculo con punto central marcado"""
    print(f"\n🎯 Círculo con centro (radio {radio}):")
    print("=" * (radio * 4 + 10))
    
    tamaño = radio * 2 + 1
    centro = radio
    
    for i in range(tamaño):
        linea = ""
        for j in range(tamaño):
            distancia = math.sqrt((i - centro)**2 + (j - centro)**2)
            
            # Punto central
            if i == centro and j == centro:
                linea += "⊙ "
            # Borde del círculo
            elif abs(distancia - radio) <= 0.5:
                linea += "○ "
            else:
                linea += "  "
        print(linea)

def dibujar_anillos_concentricos(radio_max):
    """Dibuja anillos concéntricos"""
    print(f"\n🌀 Anillos concéntricos (radio máx {radio_max}):")
    print("=" * (radio_max * 4 + 10))
    
    tamaño = radio_max * 2 + 1
    centro = radio_max
    
    for i in range(tamaño):
        linea = ""
        for j in range(tamaño):
            distancia = math.sqrt((i - centro)**2 + (j - centro)**2)
            
            # Determinar en qué anillo está
            anillo = int(distancia) + 1
            
            if anillo <= radio_max:
                # Alternar caracteres por anillo
                if anillo % 2 == 1:
                    linea += "● "
                else:
                    linea += "○ "
            else:
                linea += "  "
        print(linea)

def main():
    """Función principal"""
    print("⭕ GENERADOR DE CÍRCULOS ASCII")
    print("=" * 35)
    
    print("\nSelecciona el tipo de círculo:")
    print("1. Círculo simple")
    print("2. Círculo sólido")
    print("3. Círculo emoji")
    print("4. Círculo con centro")
    print("5. Anillos concéntricos")
    print("6. Mostrar todos")
    
    try:
        opcion = input("\nElige una opción (1-6): ")
        radio = int(input("Radio del círculo (3-10): "))
        
        if radio < 3 or radio > 10:
            print("❌ El radio debe estar entre 3 y 10")
            return
        
        if opcion == "1":
            dibujar_circulo_simple(radio)
        elif opcion == "2":
            dibujar_circulo_solido(radio)
        elif opcion == "3":
            dibujar_circulo_emoji(radio)
        elif opcion == "4":
            dibujar_circulo_con_centro(radio)
        elif opcion == "5":
            dibujar_anillos_concentricos(radio)
        elif opcion == "6":
            dibujar_circulo_simple(radio)
            dibujar_circulo_solido(radio)
            dibujar_circulo_emoji(radio)
            dibujar_circulo_con_centro(radio)
            dibujar_anillos_concentricos(radio)
        else:
            print("❌ Opción no válida")
            
    except ValueError:
        print("❌ Por favor ingresa un número válido")

if __name__ == "__main__":
    main()
