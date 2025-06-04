"""
Ejercicio 1: Triángulo Básico
============================

Objetivo:
Crear un triángulo usando asteriscos (*) con altura variable.

Conceptos a practicar:
- Bucles anidados
- Concatenación de strings
- Espacios y alineación

Instrucciones:
1. Pedir al usuario la altura del triángulo
2. Dibujar un triángulo centrado
3. Usar asteriscos para formar la figura
"""

def dibujar_triangulo(altura):
    """Dibuja un triángulo de asteriscos"""
    print(f"\n🔺 Triángulo de altura {altura}:")
    print("=" * (altura * 2 + 5))
    
    for i in range(1, altura + 1):
        # Calcular espacios para centrar
        espacios = " " * (altura - i)
        # Calcular asteriscos (números impares: 1, 3, 5, 7...)
        asteriscos = "*" * (2 * i - 1)
        print(espacios + asteriscos)

def dibujar_triangulo_hueco(altura):
    """Dibuja un triángulo hueco"""
    print(f"\n🔻 Triángulo hueco de altura {altura}:")
    print("=" * (altura * 2 + 5))
    
    for i in range(1, altura + 1):
        espacios = " " * (altura - i)
        
        if i == 1:
            # Primera línea: solo un asterisco
            print(espacios + "*")
        elif i == altura:
            # Última línea: línea completa
            asteriscos = "*" * (2 * i - 1)
            print(espacios + asteriscos)
        else:
            # Líneas intermedias: solo bordes
            espacios_internos = " " * (2 * i - 3)
            print(espacios + "*" + espacios_internos + "*")

def dibujar_triangulo_invertido(altura):
    """Dibuja un triángulo invertido"""
    print(f"\n🔽 Triángulo invertido de altura {altura}:")
    print("=" * (altura * 2 + 5))
    
    for i in range(altura, 0, -1):
        espacios = " " * (altura - i)
        asteriscos = "*" * (2 * i - 1)
        print(espacios + asteriscos)

def main():
    """Función principal"""
    print("🎨 GENERADOR DE TRIÁNGULOS ASCII")
    print("=" * 40)
    
    try:
        altura = int(input("Ingresa la altura del triángulo (1-20): "))
        
        if altura < 1 or altura > 20:
            print("❌ Por favor ingresa un número entre 1 y 20")
            return
        
        # Menú de opciones
        print("\nSelecciona el tipo de triángulo:")
        print("1. Triángulo sólido")
        print("2. Triángulo hueco")
        print("3. Triángulo invertido")
        print("4. Mostrar todos")
        
        opcion = input("\nElige una opción (1-4): ")
        
        if opcion == "1":
            dibujar_triangulo(altura)
        elif opcion == "2":
            dibujar_triangulo_hueco(altura)
        elif opcion == "3":
            dibujar_triangulo_invertido(altura)
        elif opcion == "4":
            dibujar_triangulo(altura)
            dibujar_triangulo_hueco(altura)
            dibujar_triangulo_invertido(altura)
        else:
            print("❌ Opción no válida")
            
    except ValueError:
        print("❌ Por favor ingresa un número válido")

if __name__ == "__main__":
    main()
