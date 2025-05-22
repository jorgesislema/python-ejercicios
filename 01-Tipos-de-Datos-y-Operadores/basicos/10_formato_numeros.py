"""
Ejercicio 10: Formato de Números

Objetivo: Aprender a formatear números para su visualización.

Instrucciones:
1. Utiliza diferentes métodos para formatear números (enteros, flotantes, etc.).
2. Aplica formateo para mostrar números con notación científica, con símbolos de moneda, etc.
3. Usa el módulo locale para formatear números según convenciones regionales.
4. Implementa ejemplos prácticos de formateo de números.
"""

def main():
    # Formateo básico de números con f-strings
    print("=== Formateo Básico con f-strings ===")
    
    num_entero = 1234567
    num_decimal = 123.456789
    
    # Formateo simple
    print(f"Número entero: {num_entero}")
    print(f"Número decimal: {num_decimal}")
    
    # Controlando decimales
    print(f"Número decimal con 2 decimales: {num_decimal:.2f}")
    print(f"Número decimal con 4 decimales: {num_decimal:.4f}")
    
    # Ancho fijo y alineación
    print(f"Alineado a la derecha con ancho 10: '{num_entero:10d}'")
    print(f"Alineado a la izquierda con ancho 10: '{num_entero:<10d}'")
    print(f"Centrado con ancho 10: '{num_entero:^10d}'")
    
    # Rellenado con ceros
    print(f"Rellenado con ceros (8 dígitos): {num_entero:08d}")
    
    # Formateo con separador de miles
    print(f"Con separador de miles: {num_entero:,d}")
    print(f"Con separador de miles y 2 decimales: {num_decimal:,.2f}")
    
    # Formateo avanzado de números
    print("\n=== Formateo Avanzado de Números ===")
    
    # Notación científica
    num_grande = 1234567890
    print(f"Notación científica: {num_grande:e}")
    print(f"Notación científica (3 decimales): {num_grande:.3e}")
    
    # Notación de porcentaje
    porcentaje = 0.1234
    print(f"Porcentaje: {porcentaje:.2%}")
    
    # Número con signo
    positivo = 42
    negativo = -42
    print(f"Positivo con signo: {positivo:+d}")
    print(f"Negativo con signo: {negativo:+d}")
    
    # Formateo hexadecimal, octal y binario
    num = 255
    print(f"Decimal: {num:d}")
    print(f"Hexadecimal: {num:#x} o {num:x}")
    print(f"Octal: {num:#o} o {num:o}")
    print(f"Binario: {num:#b} o {num:b}")
    
    # Formateo con el método format()
    print("\n=== Formateo con el Método format() ===")
    
    # Formato básico
    print("Número decimal con 2 decimales: {:.2f}".format(num_decimal))
    
    # Usando índices
    print("El número {0} formateado es {0:.3f}".format(num_decimal))
    
    # Usando nombres
    print("Valores: {a}, {b:.2f}, {c:+d}".format(a=num_entero, b=num_decimal, c=positivo))
    
    # Formateo de moneda
    dinero = 1234.56
    print("Formato de moneda: ${:.2f}".format(dinero))
    print("Formato de moneda: {:,.2f} €".format(dinero))
    
    # Formateo utilizando locale
    print("\n=== Formateo con locale ===")
    print("(Nota: El resultado dependerá de la configuración regional de tu sistema)")
    
    import locale
    
    # Configurar locale para España (es_ES)
    try:
        locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
        print("Locale configurado para España")
    except locale.Error:
        try:
            # Intentar con otro formato de locale para Windows
            locale.setlocale(locale.LC_ALL, 'Spanish_Spain')
            print("Locale configurado para España (Windows)")
        except locale.Error:
            print("No se pudo configurar el locale para España, usando el predeterminado")
    
    # Formateo de números según locale
    try:
        print(f"Número formateado según locale: {locale.format_string('%d', num_entero, grouping=True)}")
        print(f"Decimal formateado según locale: {locale.format_string('%.2f', num_decimal, grouping=True)}")
        
        # Formateo de moneda según locale
        print(f"Moneda formateada según locale: {locale.currency(dinero, grouping=True)}")
    except:
        print("Error al formatear con locale, es posible que tu sistema no tenga soporte completo.")
    
    # Restaurar locale predeterminado
    locale.setlocale(locale.LC_ALL, '')
    
    # Ejemplos prácticos
    print("\n=== Ejemplos Prácticos ===")
    
    # Tabla de conversión de temperaturas
    print("Tabla de Conversión de Temperaturas (Celsius a Fahrenheit):")
    print("-" * 50)
    print("| {:^8} | {:^12} | {:^20} |".format("Celsius", "Fahrenheit", "Descripción"))
    print("-" * 50)
    
    for celsius in range(-20, 41, 10):
        fahrenheit = (celsius * 9/5) + 32
        if celsius < 0:
            descripcion = "Muy frío"
        elif celsius < 10:
            descripcion = "Frío"
        elif celsius < 25:
            descripcion = "Templado"
        else:
            descripcion = "Caluroso"
        
        print("| {:^8.1f} | {:^12.1f} | {:^20} |".format(celsius, fahrenheit, descripcion))
    
    print("-" * 50)
    
    # Factura simplificada
    print("\nFactura Simplificada:")
    print("-" * 40)
    
    productos = [
        {"nombre": "Laptop", "precio": 999.99, "cantidad": 1},
        {"nombre": "Mouse", "precio": 25.50, "cantidad": 2},
        {"nombre": "Teclado", "precio": 45.75, "cantidad": 1}
    ]
    
    for producto in productos:
        nombre = producto["nombre"]
        precio = producto["precio"]
        cantidad = producto["cantidad"]
        total = precio * cantidad
        
        print("{:<10} {:>3} x {:>8.2f} € = {:>9.2f} €".format(nombre, cantidad, precio, total))
    
    subtotal = sum(p["precio"] * p["cantidad"] for p in productos)
    iva = subtotal * 0.21
    total = subtotal + iva
    
    print("-" * 40)
    print("{:<22} {:>9.2f} €".format("Subtotal:", subtotal))
    print("{:<22} {:>9.2f} €".format("IVA (21%):", iva))
    print("{:<22} {:>9.2f} €".format("Total:", total))
    
    # Ejercicios para el usuario
    print("\n=== EJERCICIOS PARA PRACTICAR ===")
    print("1. Crea una función que reciba un número decimal y lo formatee como porcentaje con 1 decimal")
    print("2. Implementa una tabla de conversión de divisas (por ejemplo, euros a dólares, yenes, etc.)")
    print("3. Desarrolla un programa que muestre una tabla de amortización de un préstamo (capital, intereses, etc.)")
    print("4. Crea una función que formatee un número grande (como 1234567) de forma legible (como 1.23M para millones)")

if __name__ == "__main__":
    main()
