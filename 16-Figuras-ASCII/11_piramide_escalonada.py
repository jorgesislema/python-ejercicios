"""
Ejercicio 11: Pirámide Escalonada
================================

Objetivo:
Crear pirámides escalonadas y ziggurats usando diferentes patrones.

Conceptos a practicar:
- Estructuras escalonadas
- Patrones de construcción
- Arquitectura antigua

Instrucciones:
1. Crear escalones de diferentes anchos
2. Construir la pirámide de abajo hacia arriba
3. Añadir detalles decorativos
"""

def dibujar_piramide_escalonada(altura):
    """Dibuja una pirámide escalonada"""
    print(f"\n🏛️ Pirámide escalonada (altura {altura}):")
    print("=" * (altura * 4 + 10))
    
    for i in range(altura, 0, -1):
        # Calcular espacios y bloques
        espacios = " " * (altura - i)
        bloques = "█" * (i * 2)
        print(espacios + bloques)

def dibujar_ziggurat(niveles):
    """Dibuja un ziggurat mesopotámico"""
    print(f"\n🏯 Ziggurat ({niveles} niveles):")
    print("=" * (niveles * 6 + 10))
    
    for i in range(niveles, 0, -1):
        # Cada nivel tiene diferentes anchos
        espacios = " " * (niveles - i)
        ancho_base = i * 3
        
        # Dibujar múltiples filas por nivel
        filas_por_nivel = max(1, i // 2)
        for j in range(filas_por_nivel):
            bloques = "▓" * ancho_base
            print(espacios + bloques)

def main():
    """Función principal"""
    print("🏛️ GENERADOR DE PIRÁMIDES")
    print("=" * 35)
    
    try:
        altura = int(input("Altura de la pirámide (3-10): "))
        if 3 <= altura <= 10:
            dibujar_piramide_escalonada(altura)
            dibujar_ziggurat(altura)
        else:
            print("❌ La altura debe estar entre 3 y 10")
    except ValueError:
        print("❌ Por favor ingresa un número válido")

if __name__ == "__main__":
    main()
