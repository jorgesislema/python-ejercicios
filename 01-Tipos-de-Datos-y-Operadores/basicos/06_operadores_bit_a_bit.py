"""
Ejercicio 6: Operadores a Nivel de Bits

Objetivo: Comprender y utilizar operadores a nivel de bits en Python.

Instrucciones:
1. Aprende a representar números en binario, octal y hexadecimal.
2. Utiliza los operadores bit a bit: AND (&), OR (|), XOR (^), NOT (~), desplazamiento (<<, >>).
3. Muestra ejemplos prácticos de uso de estos operadores.
4. Comprende cómo funcionan las máscaras de bits.
"""

def main():
    # Representación de números en diferentes bases
    decimal = 42
    
    print("=== Representación de Números en Diferentes Bases ===")
    print(f"Decimal: {decimal}")
    print(f"Binario: {bin(decimal)}")
    print(f"Octal: {oct(decimal)}")
    print(f"Hexadecimal: {hex(decimal)}")
    
    # Convertir de otras bases a decimal
    print("\n=== Conversión de Otras Bases a Decimal ===")
    binario_str = "101010"  # 42 en binario
    octal_str = "52"       # 42 en octal
    hex_str = "2a"         # 42 en hexadecimal
    
    print(f"Binario {binario_str} a decimal: {int(binario_str, 2)}")
    print(f"Octal {octal_str} a decimal: {int(octal_str, 8)}")
    print(f"Hexadecimal {hex_str} a decimal: {int(hex_str, 16)}")
    
    # Operadores bit a bit
    a = 60  # 0011 1100 en binario
    b = 13  # 0000 1101 en binario
    
    print("\n=== Operadores Bit a Bit ===")
    print(f"a = {a} ({bin(a)})")
    print(f"b = {b} ({bin(b)})")
    
    # Operador AND bit a bit
    result_and = a & b
    print(f"a & b = {result_and} ({bin(result_and)})")
    
    # Operador OR bit a bit
    result_or = a | b
    print(f"a | b = {result_or} ({bin(result_or)})")
    
    # Operador XOR bit a bit
    result_xor = a ^ b
    print(f"a ^ b = {result_xor} ({bin(result_xor)})")
    
    # Operador NOT bit a bit (complemento a uno)
    result_not_a = ~a
    print(f"~a = {result_not_a} ({bin(result_not_a & 0xFFFFFFFF)})")
    
    # Operadores de desplazamiento
    # Desplazamiento a la izquierda (multiplicación por 2)
    result_left = a << 2
    print(f"a << 2 = {result_left} ({bin(result_left)})")
    
    # Desplazamiento a la derecha (división por 2)
    result_right = a >> 2
    print(f"a >> 2 = {result_right} ({bin(result_right)})")
    
    # Ejemplos prácticos de uso de operadores bit a bit
    print("\n=== Ejemplos Prácticos ===")
    
    # 1. Verificar si un número es par o impar usando AND bit a bit
    num = 25
    is_odd = num & 1
    print(f"¿{num} es impar? {bool(is_odd)}")
    
    # 2. Intercambiar dos variables sin usar una variable temporal
    x = 5
    y = 10
    print(f"Antes del intercambio: x = {x}, y = {y}")
    
    x = x ^ y
    y = x ^ y
    x = x ^ y
    
    print(f"Después del intercambio: x = {x}, y = {y}")
    
    # 3. Uso de máscaras de bits para trabajar con flags
    print("\n=== Máscaras de Bits y Flags ===")
    
    # Definir flags como potencias de 2
    READ = 1     # 0001
    WRITE = 2    # 0010
    EXECUTE = 4  # 0100
    DELETE = 8   # 1000
    
    # Establecer permisos usando OR bit a bit
    permissions = 0
    permissions |= READ    # Agregar permiso de lectura
    permissions |= WRITE   # Agregar permiso de escritura
    
    print(f"Permisos actuales: {bin(permissions)}")
    
    # Verificar permisos usando AND bit a bit
    can_read = permissions & READ
    can_execute = permissions & EXECUTE
    
    print(f"¿Tiene permiso de lectura? {bool(can_read)}")
    print(f"¿Tiene permiso de ejecución? {bool(can_execute)}")
    
    # Quitar un permiso usando XOR bit a bit
    permissions ^= WRITE  # Quitar permiso de escritura
    print(f"Permisos después de quitar WRITE: {bin(permissions)}")
    
    # Ejercicios para el usuario
    print("\n=== EJERCICIOS PARA PRACTICAR ===")
    print("1. Escribe una función que determine el número de bits '1' en la representación binaria de un número")
    print("2. Implementa una función que use operadores bit a bit para convertir letras minúsculas a mayúsculas")
    print("3. Crea una función que invierta los bits de un número (0→1, 1→0) usando operadores bit a bit")
    print("4. Implementa un sistema de permisos para un archivo usando máscaras de bits")

if __name__ == "__main__":
    main()
