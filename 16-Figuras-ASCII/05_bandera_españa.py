"""
Ejercicio 5: Bandera de España
=============================

Objetivo:
Crear la bandera de España y otras banderas usando caracteres ASCII y emojis.

Conceptos a practicar:
- Patrones de colores
- Proporciones correctas
- Representación de símbolos nacionales

Instrucciones:
1. Crear la bandera española con sus colores
2. Añadir el escudo (simplificado)
3. Crear otras banderas famosas
4. Usar colores y símbolos apropiados
"""

def dibujar_bandera_españa(ancho=20, alto=12):
    """Dibuja la bandera de España"""
    print("\n🇪🇸 BANDERA DE ESPAÑA")
    print("=" * (ancho + 10))
    
    # Verificar proporciones (2:3 aproximadamente)
    if alto < 6:
        alto = 6
    
    # Calcular alturas de las franjas
    franja_roja = alto // 4
    franja_amarilla = alto - (2 * franja_roja)
    
    # Franja roja superior
    for i in range(franja_roja):
        print("🟥" * ancho)
    
    # Franja amarilla (con escudo en el centro)
    for i in range(franja_amarilla):
        if i == franja_amarilla // 2 and ancho >= 10:
            # Línea central con escudo simplificado
            espacios_izq = "🟨" * ((ancho - 4) // 2)
            escudo = "👑🦅"  # Representación simplificada
            espacios_der = "🟨" * (ancho - len(espacios_izq) - 2)
            print(espacios_izq + escudo + espacios_der)
        else:
            print("🟨" * ancho)
    
    # Franja roja inferior
    for i in range(franja_roja):
        print("🟥" * ancho)

def dibujar_bandera_francia(ancho=21, alto=12):
    """Dibuja la bandera de Francia"""
    print("\n🇫🇷 BANDERA DE FRANCIA")
    print("=" * (ancho + 10))
    
    # Asegurar que el ancho sea divisible por 3
    ancho = (ancho // 3) * 3
    franja = ancho // 3
    
    for i in range(alto):
        linea = "🟦" * franja + "⬜" * franja + "🟥" * franja
        print(linea)

def dibujar_bandera_alemania(ancho=20, alto=12):
    """Dibuja la bandera de Alemania"""
    print("\n🇩🇪 BANDERA DE ALEMANIA")
    print("=" * (ancho + 10))
    
    franja = alto // 3
    resto = alto % 3
    
    # Franja negra
    for i in range(franja):
        print("⬛" * ancho)
    
    # Franja roja
    for i in range(franja):
        print("🟥" * ancho)
    
    # Franja amarilla
    for i in range(franja + resto):
        print("🟨" * ancho)

def dibujar_bandera_italia(ancho=21, alto=12):
    """Dibuja la bandera de Italia"""
    print("\n🇮🇹 BANDERA DE ITALIA")
    print("=" * (ancho + 10))
    
    # Asegurar que el ancho sea divisible por 3
    ancho = (ancho // 3) * 3
    franja = ancho // 3
    
    for i in range(alto):
        linea = "🟢" * franja + "⬜" * franja + "🟥" * franja
        print(linea)

def dibujar_bandera_reino_unido(ancho=20, alto=12):
    """Dibuja una representación simplificada de la Union Jack"""
    print("\n🇬🇧 BANDERA DEL REINO UNIDO (simplificada)")
    print("=" * (ancho + 10))
    
    for i in range(alto):
        linea = ""
        for j in range(ancho):
            # Cruz de San Jorge (vertical y horizontal)
            if i == alto // 2 or j == ancho // 2:
                linea += "🟥"
            # Cruz de San Andrés (diagonales)
            elif i == j or i == (alto - 1 - j):
                linea += "⬜"
            else:
                linea += "🟦"
        print(linea)

def dibujar_bandera_japon(ancho=20, alto=12):
    """Dibuja la bandera de Japón"""
    print("\n🇯🇵 BANDERA DE JAPÓN")
    print("=" * (ancho + 10))
    
    centro_x = ancho // 2
    centro_y = alto // 2
    radio = min(ancho, alto) // 4
    
    for i in range(alto):
        linea = ""
        for j in range(ancho):
            # Calcular distancia del centro
            distancia = ((i - centro_y) ** 2 + (j - centro_x) ** 2) ** 0.5
            
            if distancia <= radio:
                linea += "🔴"  # Círculo rojo
            else:
                linea += "⬜"  # Fondo blanco
        print(linea)

def dibujar_bandera_brasil(ancho=20, alto=12):
    """Dibuja una representación simplificada de la bandera de Brasil"""
    print("\n🇧🇷 BANDERA DE BRASIL (simplificada)")
    print("=" * (ancho + 10))
    
    centro_x = ancho // 2
    centro_y = alto // 2
    
    for i in range(alto):
        linea = ""
        for j in range(ancho):
            # Rombo amarillo simplificado
            distancia_horizontal = abs(j - centro_x)
            distancia_vertical = abs(i - centro_y)
            
            if distancia_horizontal + distancia_vertical <= min(ancho, alto) // 3:
                if distancia_horizontal <= 2 and distancia_vertical <= 1:
                    linea += "🔵"  # Círculo azul central
                else:
                    linea += "🟨"  # Rombo amarillo
            else:
                linea += "🟢"  # Fondo verde
        print(linea)

def dibujar_bandera_personalizada():
    """Permite crear una bandera personalizada"""
    print("\n🎨 CREADOR DE BANDERA PERSONALIZADA")
    print("=" * 40)
    
    print("Colores disponibles:")
    colores = {
        "1": "🟥", "2": "🟦", "3": "🟨", "4": "🟩",
        "5": "🟪", "6": "🟫", "7": "⬛", "8": "⬜"
    }
    
    for key, emoji in colores.items():
        print(f"{key}: {emoji}")
    
    try:
        ancho = int(input("\nAncho de la bandera (10-25): "))
        alto = int(input("Alto de la bandera (6-15): "))
        
        print("\nElige el patrón:")
        print("1. Franjas horizontales")
        print("2. Franjas verticales")
        print("3. Cuadrantes")
        
        patron = input("Patrón (1-3): ")
        
        if patron == "1":
            # Franjas horizontales
            num_franjas = int(input("Número de franjas (2-4): "))
            colores_elegidos = []
            
            for i in range(num_franjas):
                color = input(f"Color para franja {i+1} (1-8): ")
                if color in colores:
                    colores_elegidos.append(colores[color])
            
            # Dibujar bandera
            franja_alto = alto // num_franjas
            for i in range(num_franjas):
                for j in range(franja_alto):
                    print(colores_elegidos[i] * ancho)
                    
        elif patron == "2":
            # Franjas verticales
            num_franjas = int(input("Número de franjas (2-4): "))
            colores_elegidos = []
            
            for i in range(num_franjas):
                color = input(f"Color para franja {i+1} (1-8): ")
                if color in colores:
                    colores_elegidos.append(colores[color])
            
            # Dibujar bandera
            franja_ancho = ancho // num_franjas
            for i in range(alto):
                linea = ""
                for j in range(num_franjas):
                    linea += colores_elegidos[j] * franja_ancho
                print(linea)
                
    except ValueError:
        print("❌ Por favor ingresa números válidos")

def main():
    """Función principal"""
    print("🏁 GENERADOR DE BANDERAS")
    print("=" * 35)
    
    print("\nSelecciona una bandera:")
    print("1. España 🇪🇸")
    print("2. Francia 🇫🇷")
    print("3. Alemania 🇩🇪")
    print("4. Italia 🇮🇹")
    print("5. Reino Unido 🇬🇧")
    print("6. Japón 🇯🇵")
    print("7. Brasil 🇧🇷")
    print("8. Bandera personalizada 🎨")
    print("9. Mostrar todas")
    
    try:
        opcion = input("\nElige una opción (1-9): ")
        
        if opcion == "1":
            dibujar_bandera_españa()
        elif opcion == "2":
            dibujar_bandera_francia()
        elif opcion == "3":
            dibujar_bandera_alemania()
        elif opcion == "4":
            dibujar_bandera_italia()
        elif opcion == "5":
            dibujar_bandera_reino_unido()
        elif opcion == "6":
            dibujar_bandera_japon()
        elif opcion == "7":
            dibujar_bandera_brasil()
        elif opcion == "8":
            dibujar_bandera_personalizada()
        elif opcion == "9":
            dibujar_bandera_españa()
            dibujar_bandera_francia()
            dibujar_bandera_alemania()
            dibujar_bandera_italia()
            dibujar_bandera_reino_unido()
            dibujar_bandera_japon()
            dibujar_bandera_brasil()
        else:
            print("❌ Opción no válida")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
