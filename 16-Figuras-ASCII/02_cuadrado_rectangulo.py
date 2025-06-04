"""
Ejercicio 2: Cuadrado y Rectángulo
=================================

Objetivo:
Crear cuadrados y rectángulos con diferentes estilos (sólido, hueco, con bordes).

Conceptos a practicar:
- Bucles simples y anidados
- Condicionales para crear formas
- Caracteres de dibujo ASCII

Instrucciones:
1. Crear funciones para dibujar cuadrados
2. Implementar variaciones (sólido, hueco, con bordes especiales)
3. Permitir personalización de tamaño
"""

def dibujar_cuadrado_solido(lado):
    """Dibuja un cuadrado sólido"""
    print(f"\n■ Cuadrado sólido {lado}x{lado}:")
    print("=" * (lado + 10))
    
    for i in range(lado):
        print("█" * lado)

def dibujar_cuadrado_hueco(lado):
    """Dibuja un cuadrado hueco"""
    print(f"\n□ Cuadrado hueco {lado}x{lado}:")
    print("=" * (lado + 10))
    
    for i in range(lado):
        if i == 0 or i == lado - 1:
            # Primera y última fila: línea completa
            print("█" * lado)
        else:
            # Filas intermedias: solo bordes
            print("█" + " " * (lado - 2) + "█")

def dibujar_rectangulo(ancho, alto):
    """Dibuja un rectángulo"""
    print(f"\n▭ Rectángulo {ancho}x{alto}:")
    print("=" * (ancho + 10))
    
    for i in range(alto):
        if i == 0 or i == alto - 1:
            print("█" * ancho)
        else:
            print("█" + " " * (ancho - 2) + "█")

def dibujar_cuadrado_asteriscos(lado):
    """Dibuja un cuadrado con asteriscos"""
    print(f"\n* Cuadrado con asteriscos {lado}x{lado}:")
    print("=" * (lado + 10))
    
    for i in range(lado):
        if i == 0 or i == lado - 1:
            print("* " * lado)
        else:
            print("* " + "  " * (lado - 2) + "*")

def dibujar_cuadrado_numeros(lado):
    """Dibuja un cuadrado numerado"""
    print(f"\n# Cuadrado numerado {lado}x{lado}:")
    print("=" * (lado * 2 + 10))
    
    for i in range(lado):
        fila = ""
        for j in range(lado):
            if i == 0 or i == lado - 1 or j == 0 or j == lado - 1:
                fila += f"{(i + j) % 10} "
            else:
                fila += "  "
        print(fila)

def dibujar_cuadrado_patron(lado):
    """Dibuja un cuadrado con patrón alternado"""
    print(f"\n⬛ Cuadrado con patrón {lado}x{lado}:")
    print("=" * (lado * 2 + 10))
    
    for i in range(lado):
        fila = ""
        for j in range(lado):
            if (i + j) % 2 == 0:
                fila += "█ "
            else:
                fila += "░ "
        print(fila)

def main():
    """Función principal"""
    print("🎨 GENERADOR DE CUADRADOS Y RECTÁNGULOS ASCII")
    print("=" * 50)
    
    try:
        print("\nSelecciona el tipo de figura:")
        print("1. Cuadrado sólido")
        print("2. Cuadrado hueco")
        print("3. Rectángulo")
        print("4. Cuadrado con asteriscos")
        print("5. Cuadrado numerado")
        print("6. Cuadrado con patrón")
        print("7. Mostrar todos los cuadrados")
        
        opcion = input("\nElige una opción (1-7): ")
        
        if opcion in ["1", "2", "4", "5", "6", "7"]:
            lado = int(input("Ingresa el tamaño del lado (3-15): "))
            if lado < 3 or lado > 15:
                print("❌ Por favor ingresa un número entre 3 y 15")
                return
                
            if opcion == "1":
                dibujar_cuadrado_solido(lado)
            elif opcion == "2":
                dibujar_cuadrado_hueco(lado)
            elif opcion == "4":
                dibujar_cuadrado_asteriscos(lado)
            elif opcion == "5":
                dibujar_cuadrado_numeros(lado)
            elif opcion == "6":
                dibujar_cuadrado_patron(lado)
            elif opcion == "7":
                dibujar_cuadrado_solido(lado)
                dibujar_cuadrado_hueco(lado)
                dibujar_cuadrado_asteriscos(lado)
                dibujar_cuadrado_numeros(lado)
                dibujar_cuadrado_patron(lado)
                
        elif opcion == "3":
            ancho = int(input("Ingresa el ancho (3-20): "))
            alto = int(input("Ingresa el alto (3-15): "))
            
            if ancho < 3 or ancho > 20 or alto < 3 or alto > 15:
                print("❌ Dimensiones fuera de rango")
                return
                
            dibujar_rectangulo(ancho, alto)
        else:
            print("❌ Opción no válida")
            
    except ValueError:
        print("❌ Por favor ingresa números válidos")

if __name__ == "__main__":
    main()
