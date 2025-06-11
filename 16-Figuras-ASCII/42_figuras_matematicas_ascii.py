"""
Ejercicio 42: Figuras Matemáticas ASCII

Objetivo:
- Crear figuras matemáticas y patrones geométricos en ASCII
- Incluir variantes: espiral, fractal simple, curva seno, mosaico geométrico
- Permitir personalización de tamaño y complejidad

Conceptos:
- Uso de funciones matemáticas
- Arte ASCII avanzado
- Bucles y coordenadas
"""
import math

def espiral_ascii(tamano=15):
    print("🌀 ESPIRAL ASCII 🌀\n" + "═"*40)
    n = tamano
    matriz = [[' ' for _ in range(n)] for _ in range(n)]
    x, y = 0, 0
    dx, dy = 0, 1
    for i in range(n*n):
        matriz[x][y] = '*'
        if matriz[(x+dx)%n][(y+dy)%n] != ' ':
            dx, dy = dy, -dx
        x += dx
        y += dy
    for fila in matriz:
        print(''.join(fila))

def curva_seno_ascii(longitud=60, altura=10):
    print("🌊 CURVA SENO ASCII 🌊\n" + "═"*40)
    for y in range(altura, -altura, -1):
        linea = ''
        for x in range(longitud):
            valor = int(altura * math.sin(2 * math.pi * x / longitud))
            if valor == y:
                linea += '*'
            else:
                linea += ' '
        print(linea)

def mosaico_geometrico_ascii(tamano=10):
    print("🔷 MOSAICO GEOMÉTRICO ASCII 🔷\n" + "═"*40)
    for i in range(tamano):
        linea = ''
        for j in range(tamano):
            if (i+j)%2 == 0:
                linea += '■'
            else:
                linea += ' '
        print(linea)

def fractal_simple_ascii(n=32):
    print("🌿 FRACTAL SIMPLE ASCII 🌿\n" + "═"*40)
    def fractal(x, y, n):
        if n < 1:
            return
        print(' ' * x + '*')
        fractal(x+1, y, n//2)
        fractal(x-1, y, n//2)
    fractal(n//2, 0, n//2)

def menu_principal():
    while True:
        print("\n" + "═"*40)
        print("🧮 FIGURAS MATEMÁTICAS ASCII 🧮")
        print("═"*40)
        print("1. Espiral")
        print("2. Curva seno")
        print("3. Mosaico geométrico")
        print("4. Fractal simple")
        print("0. Salir")
        print("═"*40)
        opcion = input("Selecciona una figura: ")
        if opcion == "1":
            t = int(input("Tamaño de la espiral (10-30): ") or 15)
            espiral_ascii(t)
        elif opcion == "2":
            l = int(input("Longitud de la curva (20-100): ") or 60)
            a = int(input("Altura de la curva (5-15): ") or 10)
            curva_seno_ascii(l, a)
        elif opcion == "3":
            t = int(input("Tamaño del mosaico (5-20): ") or 10)
            mosaico_geometrico_ascii(t)
        elif opcion == "4":
            n = int(input("Tamaño del fractal (16-64): ") or 32)
            fractal_simple_ascii(n)
        elif opcion == "0":
            print("¡Hasta luego, matemático! 🧮")
            break
        else:
            print("Opción no válida")
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
