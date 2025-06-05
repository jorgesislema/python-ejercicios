"""
Ejercicio 18: Tablero de Ajedrez
================================

Objetivo:
Crear un tablero de ajedrez con casillas alternadas y piezas.

Conceptos a practicar:
- Patrones alternados
- Grillas regulares
- Representación de juegos

Instrucciones:
1. Crear casillas blancas y negras alternadas
2. Añadir coordenadas (a-h, 1-8)
3. Incluir piezas de ajedrez
"""

def dibujar_tablero_simple(tamaño=8):
    """Dibuja un tablero de ajedrez simple"""
    print(f"\n♟️ Tablero de ajedrez ({tamaño}x{tamaño}):")
    print("=" * (tamaño * 4 + 10))
    
    # Números de fila
    print("  ", end="")
    for i in range(tamaño):
        print(f" {chr(ord('A') + i)} ", end="")
    print()
    
    for fila in range(tamaño):
        print(f"{tamaño - fila} ", end="")  # Números de columna
        
        for col in range(tamaño):
            if (fila + col) % 2 == 0:
                print("⬜", end="")  # Casilla blanca
            else:
                print("⬛", end="")  # Casilla negra
        
        print(f" {tamaño - fila}")  # Números de columna al final
    
    # Números de fila al final
    print("  ", end="")
    for i in range(tamaño):
        print(f" {chr(ord('A') + i)} ", end="")
    print()

def dibujar_tablero_con_piezas():
    """Dibuja un tablero con piezas en posición inicial"""
    print("\n♔ Tablero con piezas:")
    print("=" * 35)
    
    # Piezas iniciales
    piezas_blancas = ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
    piezas_negras = ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
    peones_blancos = "♙"
    peones_negros = "♟"
    
    tablero = []
    
    # Fila 8 (piezas negras)
    tablero.append(piezas_negras)
    # Fila 7 (peones negros)
    tablero.append([peones_negros] * 8)
    # Filas 6-3 (vacías)
    for _ in range(4):
        fila = []
        for col in range(8):
            if (len(tablero) + col) % 2 == 0:
                fila.append("⬜")
            else:
                fila.append("⬛")
        tablero.append(fila)
    # Fila 2 (peones blancos)
    tablero.append([peones_blancos] * 8)
    # Fila 1 (piezas blancas)
    tablero.append(piezas_blancas)
    
    # Dibujar el tablero
    print("  ", end="")
    for i in range(8):
        print(f" {chr(ord('A') + i)} ", end="")
    print()
    
    for i, fila in enumerate(tablero):
        print(f"{8 - i} ", end="")
        for pieza in fila:
            print(f"{pieza} ", end="")
        print(f" {8 - i}")
    
    print("  ", end="")
    for i in range(8):
        print(f" {chr(ord('A') + i)} ", end="")
    print()

def dibujar_tablero_personalizado():
    """Permite crear un tablero personalizado"""
    print("\n🎯 Tablero personalizado:")
    print("=" * 30)
    
    try:
        tamaño = int(input("Tamaño del tablero (4-12): "))
        if tamaño < 4 or tamaño > 12:
            print("❌ El tamaño debe estar entre 4 y 12")
            return
        
        print("Selecciona el estilo:")
        print("1. Blanco y negro (⬜⬛)")
        print("2. Números alternados")
        print("3. Letras alternadas")
        
        estilo = input("Estilo (1-3): ")
        
        print("  ", end="")
        for i in range(tamaño):
            print(f" {chr(ord('A') + i)} ", end="")
        print()
        
        for fila in range(tamaño):
            print(f"{tamaño - fila:2} ", end="")
            
            for col in range(tamaño):
                if estilo == "1":
                    if (fila + col) % 2 == 0:
                        print("⬜", end="")
                    else:
                        print("⬛", end="")
                elif estilo == "2":
                    print(f"{(fila + col) % 10} ", end="")
                elif estilo == "3":
                    letra = chr(ord('A') + (fila + col) % 26)
                    print(f"{letra} ", end="")
            
            print(f" {tamaño - fila}")
        
        print("  ", end="")
        for i in range(tamaño):
            print(f" {chr(ord('A') + i)} ", end="")
        print()
        
    except ValueError:
        print("❌ Por favor ingresa un número válido")

def main():
    """Función principal"""
    print("♔ GENERADOR DE TABLEROS DE AJEDREZ")
    print("=" * 45)
    
    print("\nSelecciona el tipo de tablero:")
    print("1. Tablero simple")
    print("2. Tablero con piezas")
    print("3. Tablero personalizado")
    print("4. Mostrar todos")
    
    try:
        opcion = input("\nElige una opción (1-4): ")
        
        if opcion == "1":
            dibujar_tablero_simple()
        elif opcion == "2":
            dibujar_tablero_con_piezas()
        elif opcion == "3":
            dibujar_tablero_personalizado()
        elif opcion == "4":
            dibujar_tablero_simple()
            dibujar_tablero_con_piezas()
        else:
            print("❌ Opción no válida")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
