"""
Ejercicio 48: Figuras Geométricas 3D ASCII

Objetivo:
- Crear representaciones 3D de figuras geométricas en ASCII
- Incluir variantes: cubo, pirámide, cilindro, esfera, prisma
- Permitir personalización de tamaño y perspectiva

Conceptos:
- Geometría 3D en ASCII
- Perspectiva y profundidad
- Matemáticas aplicadas al arte ASCII
"""

import math

def cubo_3d(tamano=6):
    """Cubo 3D ASCII"""
    print("📦 CUBO 3D ASCII 📦")
    print("═" * 40)
    
    # Cara frontal del cubo
    print("Cubo 3D isométrico:")
    for i in range(tamano):
        # Línea superior con perspectiva
        if i == 0:
            print(" " * tamano + "╭" + "─" * (tamano-2) + "╮" + "╱" * tamano)
        elif i == tamano - 1:
            print("╰" + "─" * (tamano-2) + "╯" + "╱" * tamano + "╯")
        else:
            print("│" + " " * (tamano-2) + "│" + "╱" * tamano + "│")
    
    print(f"\nCubo de {tamano}x{tamano}x{tamano}")

def piramide_3d(altura=8):
    """Pirámide 3D ASCII"""
    print("🔺 PIRÁMIDE 3D ASCII 🔺")
    print("═" * 40)
    
    print("Pirámide vista frontal:")
    for i in range(altura):
        espacios = " " * (altura - i - 1)
        caracteres = "▲" * (2 * i + 1)
        print(espacios + caracteres)
    
    print("\nPirámide isométrica:")
    for i in range(altura):
        espacios = " " * (altura - i - 1)
        if i == 0:
            print(espacios + "▲")
        elif i == altura - 1:
            print("▲" + "─" * (2 * i - 1) + "▲")
        else:
            print(espacios + "▲" + " " * (2 * i - 1) + "▲")
    
    print(f"\nPirámide de altura {altura}")

def cilindro_3d(altura=8, radio=4):
    """Cilindro 3D ASCII"""
    print("🥤 CILINDRO 3D ASCII 🥤")
    print("═" * 40)
    
    # Parte superior (elipse)
    print("Cilindro 3D:")
    print(" " * (radio//2) + "╭" + "─" * (radio*2) + "╮")
    print("╱" + " " * (radio*2) + "╲")
    
    # Cuerpo del cilindro
    for i in range(altura - 2):
        print("│" + " " * (radio*2) + "│")
    
    # Parte inferior
    print("╲" + "_" * (radio*2) + "╱")
    print(" " * (radio//2) + "╰" + "─" * (radio*2) + "╯")
    
    print(f"\nCilindro: altura={altura}, radio={radio}")

def esfera_3d(radio=6):
    """Esfera 3D ASCII"""
    print("⚪ ESFERA 3D ASCII ⚪")
    print("═" * 40)
    
    print("Esfera vista frontal:")
    for y in range(-radio, radio + 1):
        linea = ""
        for x in range(-radio, radio + 1):
            if x*x + y*y <= radio*radio:
                # Efecto de sombreado básico
                if x < 0 and y < 0:
                    linea += "▓"  # Sombra
                elif x > 0 and y < 0:
                    linea += "▒"  # Media sombra
                else:
                    linea += "░"  # Luz
            else:
                linea += " "
        print(linea)
    
    print(f"\nEsfera de radio {radio}")

def prisma_triangular(altura=8, base=6):
    """Prisma triangular 3D ASCII"""
    print("🔷 PRISMA TRIANGULAR 3D ASCII 🔷")
    print("═" * 40)
    
    print("Prisma triangular:")
    
    # Base triangular superior
    for i in range(base):
        espacios = " " * (base - i - 1)
        if i == 0:
            print(espacios + "▲")
        elif i == base - 1:
            print("▲" + "─" * (2 * i - 1) + "▲")
        else:
            print(espacios + "╱" + " " * (2 * i - 1) + "╲")
    
    # Altura del prisma
    for j in range(altura - base):
        print("│" + " " * (2 * base - 3) + "│")
    
    # Base triangular inferior
    print("▲" + "─" * (2 * base - 3) + "▲")
    
    print(f"\nPrisma: altura={altura}, base={base}")

def tetraedro_3d(tamano=8):
    """Tetraedro 3D ASCII"""
    print("🔺 TETRAEDRO 3D ASCII 🔺")
    print("═" * 40)
    
    print("Tetraedro (pirámide triangular):")
    
    for i in range(tamano):
        espacios = " " * (tamano - i - 1)
        if i == 0:
            print(espacios + "▲")
        elif i == tamano - 1:
            print("▲" + "─" * (2 * i - 1) + "▲")
        else:
            print(espacios + "╱" + "─" * (2 * i - 1) + "╲")
    
    print(f"\nTetraedro de tamaño {tamano}")

def hexaedro_3d(tamano=6):
    """Hexaedro (cubo) con aristas marcadas"""
    print("⬛ HEXAEDRO 3D ASCII ⬛")
    print("═" * 40)
    
    print("Hexaedro (cubo con aristas):")
    
    # Parte superior con perspectiva
    print(" " * tamano + "●" + "─" * (tamano-2) + "●" + "╱" * tamano + "●")
    
    for i in range(1, tamano-1):
        print(" " * (tamano-i) + "│" + " " * (tamano-2) + "│" + "╱" * i + "│")
    
    # Parte media
    print("●" + "─" * (tamano-2) + "●" + "╱" * tamano + "●")
    
    for i in range(1, tamano-1):
        print("│" + " " * (tamano-2) + "│" + " " * (tamano-i) + "│")
    
    # Parte inferior
    print("●" + "─" * (tamano-2) + "●" + " " * tamano + "●")
    
    print(f"\nHexaedro de {tamano}x{tamano}x{tamano}")

def menu_principal():
    """Menú principal del programa"""
    while True:
        print("\n" + "═" * 50)
        print("📐 FIGURAS GEOMÉTRICAS 3D ASCII 📐")
        print("═" * 50)
        print("1. Cubo 3D")
        print("2. Pirámide 3D")
        print("3. Cilindro 3D")
        print("4. Esfera 3D")
        print("5. Prisma triangular")
        print("6. Tetraedro 3D")
        print("7. Hexaedro (cubo con aristas)")
        print("0. Salir")
        print("═" * 50)
        
        opcion = input("Selecciona una figura 3D: ")
        
        if opcion == "1":
            t = int(input("Tamaño del cubo (4-10): ") or 6)
            cubo_3d(t)
        elif opcion == "2":
            a = int(input("Altura de la pirámide (5-12): ") or 8)
            piramide_3d(a)
        elif opcion == "3":
            a = int(input("Altura del cilindro (6-12): ") or 8)
            r = int(input("Radio del cilindro (3-8): ") or 4)
            cilindro_3d(a, r)
        elif opcion == "4":
            r = int(input("Radio de la esfera (4-10): ") or 6)
            esfera_3d(r)
        elif opcion == "5":
            a = int(input("Altura del prisma (6-12): ") or 8)
            b = int(input("Base del prisma (4-8): ") or 6)
            prisma_triangular(a, b)
        elif opcion == "6":
            t = int(input("Tamaño del tetraedro (5-12): ") or 8)
            tetraedro_3d(t)
        elif opcion == "7":
            t = int(input("Tamaño del hexaedro (4-10): ") or 6)
            hexaedro_3d(t)
        elif opcion == "0":
            print("¡Hasta luego, geómetra! 📐")
            break
        else:
            print("Opción no válida")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
