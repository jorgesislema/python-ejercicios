"""
Ejercicio 8: Flecha Direccional
===============================

Objetivo:
Crear flechas direccionales en diferentes orientaciones y estilos.

Conceptos a practicar:
- Patrones direccionales
- Rotación de figuras
- Indicadores visuales

Instrucciones:
1. Crear flechas en las 4 direcciones principales
2. Hacer flechas de diferentes tamaños
3. Añadir estilos decorativos
"""

def dibujar_flecha_arriba(tamaño=5):
    """Dibuja una flecha apuntando hacia arriba"""
    print(f"\n⬆️ Flecha arriba (tamaño {tamaño}):")
    print("=" * (tamaño * 2 + 5))
    
    # Punta de la flecha
    for i in range(tamaño):
        espacios = " " * (tamaño - i - 1)
        asteriscos = "*" * (2 * i + 1)
        print(espacios + asteriscos)
    
    # Cola de la flecha
    for i in range(tamaño // 2):
        espacios = " " * (tamaño - 1)
        print(espacios + "*")

def dibujar_flecha_abajo(tamaño=5):
    """Dibuja una flecha apuntando hacia abajo"""
    print(f"\n⬇️ Flecha abajo (tamaño {tamaño}):")
    print("=" * (tamaño * 2 + 5))
    
    # Cola de la flecha
    for i in range(tamaño // 2):
        espacios = " " * (tamaño - 1)
        print(espacios + "*")
    
    # Punta de la flecha
    for i in range(tamaño, 0, -1):
        espacios = " " * (tamaño - i)
        asteriscos = "*" * (2 * i - 1)
        print(espacios + asteriscos)

def dibujar_flecha_derecha(tamaño=5):
    """Dibuja una flecha apuntando hacia la derecha"""
    print(f"\n➡️ Flecha derecha (tamaño {tamaño}):")
    print("=" * (tamaño * 2 + 5))
    
    altura = tamaño * 2 - 1
    
    for i in range(altura):
        linea = ""
        
        # Cola de la flecha
        if i == altura // 2:
            linea += "*" * tamaño
        elif abs(i - altura // 2) <= 1:
            linea += "*" * (tamaño - 1)
        else:
            linea += " " * (tamaño - 1)
        
        # Punta de la flecha
        distancia_centro = abs(i - altura // 2)
        if distancia_centro < tamaño:
            linea += "*" * (tamaño - distancia_centro)
        
        print(linea)

def dibujar_flecha_izquierda(tamaño=5):
    """Dibuja una flecha apuntando hacia la izquierda"""
    print(f"\n⬅️ Flecha izquierda (tamaño {tamaño}):")
    print("=" * (tamaño * 2 + 5))
    
    altura = tamaño * 2 - 1
    
    for i in range(altura):
        linea = ""
        
        # Punta de la flecha
        distancia_centro = abs(i - altura // 2)
        if distancia_centro < tamaño:
            espacios = " " * distancia_centro
            linea += espacios + "*" * (tamaño - distancia_centro)
        else:
            linea += " " * tamaño
        
        # Cola de la flecha
        if i == altura // 2:
            linea += "*" * tamaño
        elif abs(i - altura // 2) <= 1:
            linea += "*" * (tamaño - 1)
        
        print(linea)

def dibujar_todas_las_flechas(tamaño=5):
    """Dibuja todas las flechas en un patrón"""
    print(f"\n🧭 Todas las direcciones (tamaño {tamaño}):")
    print("=" * 40)
    
    dibujar_flecha_arriba(tamaño)
    
    print("\n" + " " * 10 + "⬅️ ← → ➡️")
    
    dibujar_flecha_abajo(tamaño)

def main():
    """Función principal"""
    print("🎯 GENERADOR DE FLECHAS DIRECCIONALES")
    print("=" * 45)
    
    print("\nSelecciona el tipo de flecha:")
    print("1. Flecha arriba ⬆️")
    print("2. Flecha abajo ⬇️")
    print("3. Flecha derecha ➡️")
    print("4. Flecha izquierda ⬅️")
    print("5. Todas las direcciones 🧭")
    
    try:
        opcion = input("\nElige una opción (1-5): ")
        tamaño = int(input("Tamaño de la flecha (3-8): "))
        
        if tamaño < 3 or tamaño > 8:
            print("❌ El tamaño debe estar entre 3 y 8")
            return
        
        if opcion == "1":
            dibujar_flecha_arriba(tamaño)
        elif opcion == "2":
            dibujar_flecha_abajo(tamaño)
        elif opcion == "3":
            dibujar_flecha_derecha(tamaño)
        elif opcion == "4":
            dibujar_flecha_izquierda(tamaño)
        elif opcion == "5":
            dibujar_todas_las_flechas(tamaño)
        else:
            print("❌ Opción no válida")
            
    except ValueError:
        print("❌ Por favor ingresa un número válido")

if __name__ == "__main__":
    main()
