"""
Ejercicio 10: Diamante ASCII
============================

Objetivo:
Crear diferentes tipos de diamantes usando patrones geométricos.

Conceptos a practicar:
- Simetría en dos ejes
- Patrones piramidales
- Figuras compuestas

Instrucciones:
1. Crear la parte superior del diamante (triángulo)
2. Crear la parte inferior (triángulo invertido)
3. Combinar ambas partes
4. Añadir variaciones decorativas
"""

def dibujar_diamante_simple(tamaño):
    """Dibuja un diamante simple"""
    print(f"\n💎 Diamante simple (tamaño {tamaño}):")
    print("=" * (tamaño * 2 + 10))
    
    # Parte superior del diamante
    for i in range(tamaño):
        espacios = " " * (tamaño - i - 1)
        asteriscos = "*" * (2 * i + 1)
        print(espacios + asteriscos)
    
    # Parte inferior del diamante
    for i in range(tamaño - 2, -1, -1):
        espacios = " " * (tamaño - i - 1)
        asteriscos = "*" * (2 * i + 1)
        print(espacios + asteriscos)

def dibujar_diamante_hueco(tamaño):
    """Dibuja un diamante hueco"""
    print(f"\n💍 Diamante hueco (tamaño {tamaño}):")
    print("=" * (tamaño * 2 + 10))
    
    # Parte superior
    for i in range(tamaño):
        espacios = " " * (tamaño - i - 1)
        
        if i == 0:
            print(espacios + "*")
        else:
            espacios_internos = " " * (2 * i - 1)
            print(espacios + "*" + espacios_internos + "*")
    
    # Parte inferior
    for i in range(tamaño - 2, -1, -1):
        espacios = " " * (tamaño - i - 1)
        
        if i == 0:
            print(espacios + "*")
        else:
            espacios_internos = " " * (2 * i - 1)
            print(espacios + "*" + espacios_internos + "*")

def dibujar_diamante_emoji(tamaño):
    """Dibuja un diamante con emojis"""
    print(f"\n💎 Diamante emoji (tamaño {tamaño}):")
    print("=" * (tamaño * 2 + 10))
    
    emojis = ["💎", "💍", "✨", "🔷", "🔹"]
    
    # Parte superior
    for i in range(tamaño):
        espacios = " " * (tamaño - i - 1)
        emoji = emojis[i % len(emojis)]
        linea = emoji * (i + 1)
        print(espacios + linea)
    
    # Parte inferior
    for i in range(tamaño - 2, -1, -1):
        espacios = " " * (tamaño - i - 1)
        emoji = emojis[i % len(emojis)]
        linea = emoji * (i + 1)
        print(espacios + linea)

def dibujar_diamante_numerico(tamaño):
    """Dibuja un diamante con números"""
    print(f"\n🔢 Diamante numérico (tamaño {tamaño}):")
    print("=" * (tamaño * 2 + 10))
    
    # Parte superior
    for i in range(tamaño):
        espacios = " " * (tamaño - i - 1)
        numeros = ""
        
        # Números ascendentes
        for j in range(i + 1):
            numeros += str(j + 1)
        
        # Números descendentes
        for j in range(i - 1, -1, -1):
            numeros += str(j + 1)
        
        print(espacios + numeros)
    
    # Parte inferior
    for i in range(tamaño - 2, -1, -1):
        espacios = " " * (tamaño - i - 1)
        numeros = ""
        
        # Números ascendentes
        for j in range(i + 1):
            numeros += str(j + 1)
        
        # Números descendentes
        for j in range(i - 1, -1, -1):
            numeros += str(j + 1)
        
        print(espacios + numeros)

def dibujar_diamante_con_brillo(tamaño):
    """Dibuja un diamante con efecto de brillo"""
    print(f"\n✨ Diamante brillante (tamaño {tamaño}):")
    print("=" * (tamaño * 2 + 15))
    
    caracteres = [".", "*", "◆", "♦", "💎"]
    
    # Parte superior
    for i in range(tamaño):
        espacios = " " * (tamaño - i - 1)
        linea = ""
        
        for j in range(2 * i + 1):
            # Crear efecto de brillo desde el centro
            distancia_centro = abs(j - i)
            char_index = min(distancia_centro, len(caracteres) - 1)
            linea += caracteres[char_index]
        
        print(espacios + linea)
    
    # Parte inferior
    for i in range(tamaño - 2, -1, -1):
        espacios = " " * (tamaño - i - 1)
        linea = ""
        
        for j in range(2 * i + 1):
            distancia_centro = abs(j - i)
            char_index = min(distancia_centro, len(caracteres) - 1)
            linea += caracteres[char_index]
        
        print(espacios + linea)

def main():
    """Función principal"""
    print("💎 GENERADOR DE DIAMANTES ASCII")
    print("=" * 40)
    
    print("\nSelecciona el tipo de diamante:")
    print("1. Diamante simple")
    print("2. Diamante hueco")
    print("3. Diamante emoji")
    print("4. Diamante numérico")
    print("5. Diamante brillante")
    print("6. Mostrar todos")
    
    try:
        opcion = input("\nElige una opción (1-6): ")
        tamaño = int(input("Tamaño del diamante (3-8): "))
        
        if tamaño < 3 or tamaño > 8:
            print("❌ El tamaño debe estar entre 3 y 8")
            return
        
        if opcion == "1":
            dibujar_diamante_simple(tamaño)
        elif opcion == "2":
            dibujar_diamante_hueco(tamaño)
        elif opcion == "3":
            dibujar_diamante_emoji(tamaño)
        elif opcion == "4":
            dibujar_diamante_numerico(tamaño)
        elif opcion == "5":
            dibujar_diamante_con_brillo(tamaño)
        elif opcion == "6":
            dibujar_diamante_simple(tamaño)
            dibujar_diamante_hueco(tamaño)
            dibujar_diamante_emoji(tamaño)
            dibujar_diamante_numerico(tamaño)
            dibujar_diamante_con_brillo(tamaño)
        else:
            print("❌ Opción no válida")
            
    except ValueError:
        print("❌ Por favor ingresa un número válido")

if __name__ == "__main__":
    main()
