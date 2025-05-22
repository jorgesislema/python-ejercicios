"""
Ejercicio Avanzado: Operaciones Binarias Avanzadas y Manipulación de Bits

En este ejercicio aprenderás:
1. Operaciones binarias avanzadas en Python
2. Manipulación de bits a nivel bajo
3. Aplicaciones prácticas de las operaciones de bits
4. Técnicas de optimización usando operaciones binarias
5. Representación y manejo de datos binarios

Las operaciones binarias son fundamentales en programación de bajo nivel,
optimización de algoritmos, criptografía, y sistemas embebidos.
"""

# 1. Representación binaria y conversiones
print("1. Representación binaria y conversiones")
print("-" * 50)

# Representación binaria de enteros
numero = 42
repr_binaria = bin(numero)
repr_octal = oct(numero)
repr_hexa = hex(numero)

print(f"Número decimal: {numero}")
print(f"Representación binaria: {repr_binaria}")
print(f"Representación octal: {repr_octal}")
print(f"Representación hexadecimal: {repr_hexa}")

# Conversión desde otras bases a decimal
binario_str = "101010"  # 42 en binario
octal_str = "52"       # 42 en octal
hexa_str = "2a"        # 42 en hexadecimal

print(f"\nConversiones a decimal:")
print(f"Binario {binario_str} → {int(binario_str, 2)}")
print(f"Octal {octal_str} → {int(octal_str, 8)}")
print(f"Hexadecimal {hexa_str} → {int(hexa_str, 16)}")

# Formateo de cadenas para diferentes bases
print(f"\nFormateo de cadenas:")
print(f"Binario (8 dígitos): {numero:08b}")
print(f"Octal: {numero:o}")
print(f"Hexadecimal: {numero:x}")
print(f"Hexadecimal (mayúsculas): {numero:X}")

# 2. Operadores de bits avanzados
print("\n2. Operadores de bits avanzados")
print("-" * 50)

a = 0b1100  # 12 decimal
b = 0b1010  # 10 decimal

print(f"a = {a} (binario: {bin(a)})")
print(f"b = {b} (binario: {bin(b)})")

# Operadores básicos
print(f"\nOperadores básicos:")
print(f"AND: a & b = {a & b} (binario: {bin(a & b)})")
print(f"OR: a | b = {a | b} (binario: {bin(a | b)})")
print(f"XOR: a ^ b = {a ^ b} (binario: {bin(a ^ b)})")
print(f"NOT: ~a = {~a} (binario: {bin(~a & 0xff)})")  # Limitado a 8 bits para claridad
print(f"Desplazamiento izquierda: a << 2 = {a << 2} (binario: {bin(a << 2)})")
print(f"Desplazamiento derecha: a >> 2 = {a >> 2} (binario: {bin(a >> 2)})")

# 3. Manipulación de bits individuales
print("\n3. Manipulación de bits individuales")
print("-" * 50)

numero = 0b10101010  # 170 decimal

# Verificar un bit específico (en la posición 3)
posicion = 3
bit = (numero >> posicion) & 1
print(f"Bit en posición {posicion} de {bin(numero)}: {bit}")

# Establecer un bit específico (bit 2)
posicion = 2
numero_con_bit = numero | (1 << posicion)
print(f"Establecer bit en posición {posicion}: {bin(numero_con_bit)}")

# Limpiar un bit específico (bit 1)
posicion = 1
numero_sin_bit = numero & ~(1 << posicion)
print(f"Limpiar bit en posición {posicion}: {bin(numero_sin_bit)}")

# Cambiar un bit específico (bit 4)
posicion = 4
numero_bit_cambiado = numero ^ (1 << posicion)
print(f"Cambiar bit en posición {posicion}: {bin(numero_bit_cambiado)}")

# Verificar si un número es potencia de 2
def es_potencia_de_dos(n):
    return n > 0 and (n & (n - 1)) == 0

for i in range(1, 10):
    print(f"{i} {'es' if es_potencia_de_dos(i) else 'no es'} potencia de 2")

# 4. Máscaras de bits
print("\n4. Máscaras de bits")
print("-" * 50)

# Crear una máscara para los 4 bits menos significativos
mascara = 0b1111  # 15 decimal
print(f"Máscara: {bin(mascara)}")

# Aplicar máscara para extraer los 4 bits menos significativos
numero = 0b10101111  # 175 decimal
bits_extraidos = numero & mascara
print(f"Número: {bin(numero)}")
print(f"4 bits menos significativos: {bin(bits_extraidos)}")

# Usar máscara para combinar bits
numero1 = 0b11110000  # 240 decimal (bits altos)
numero2 = 0b00001111  # 15 decimal (bits bajos)
combinacion = numero1 | numero2
print(f"Combinación: {bin(combinacion)}")

# 5. Banderas y estados usando bits
print("\n5. Banderas y estados usando bits")
print("-" * 50)

# Definir constantes de banderas
ACTIVO     = 0b00000001  # 1
PREMIUM    = 0b00000010  # 2
VERIFICADO = 0b00000100  # 4
ADMIN      = 0b00001000  # 8
BLOQUEADO  = 0b00010000  # 16

print(f"Banderas disponibles:")
print(f"ACTIVO: {bin(ACTIVO)}")
print(f"PREMIUM: {bin(PREMIUM)}")
print(f"VERIFICADO: {bin(VERIFICADO)}")
print(f"ADMIN: {bin(ADMIN)}")
print(f"BLOQUEADO: {bin(BLOQUEADO)}")

# Estado de un usuario como combinación de banderas
usuario1 = ACTIVO | PREMIUM | VERIFICADO
usuario2 = ACTIVO | ADMIN

print(f"\nEstado usuario1: {bin(usuario1)}")
print(f"Estado usuario2: {bin(usuario2)}")

# Verificar estados
print(f"\nVerificaciones usuario1:")
print(f"¿Activo? {bool(usuario1 & ACTIVO)}")
print(f"¿Premium? {bool(usuario1 & PREMIUM)}")
print(f"¿Admin? {bool(usuario1 & ADMIN)}")

# Agregar una bandera
usuario1 |= ADMIN
print(f"\nUsuario1 después de agregar ADMIN: {bin(usuario1)}")

# Quitar una bandera
usuario1 &= ~PREMIUM
print(f"Usuario1 después de quitar PREMIUM: {bin(usuario1)}")

# Alternar una bandera
usuario1 ^= VERIFICADO
print(f"Usuario1 después de alternar VERIFICADO: {bin(usuario1)}")

# 6. Optimizaciones usando bits
print("\n6. Optimizaciones usando bits")
print("-" * 50)

# Multiplicar por potencias de 2 usando desplazamiento
numero = 10
print(f"Multiplicar por 2: {numero} * 2 = {numero << 1}")
print(f"Multiplicar por 4: {numero} * 4 = {numero << 2}")
print(f"Multiplicar por 8: {numero} * 8 = {numero << 3}")

# Dividir por potencias de 2 usando desplazamiento
numero = 100
print(f"Dividir por 2: {numero} / 2 = {numero >> 1}")
print(f"Dividir por 4: {numero} / 4 = {numero >> 2}")
print(f"Dividir por 8: {numero} / 8 = {numero >> 3}")

# Intercambiar valores usando XOR (sin variable temporal)
a, b = 5, 10
print(f"\nIntercambio sin variable temporal:")
print(f"Antes: a = {a}, b = {b}")
a ^= b
b ^= a
a ^= b
print(f"Después: a = {a}, b = {b}")

# 7. Aplicaciones: Algoritmos y estructuras de datos
print("\n7. Aplicaciones: Algoritmos y estructuras de datos")
print("-" * 50)

# Conjunto de bits (bitset) para representar un conjunto eficientemente
def print_conjunto(conjunto):
    elementos = [i for i in range(32) if conjunto & (1 << i)]
    print(f"Conjunto: {elementos}")

# Crear conjuntos
conjunto_a = (1 << 1) | (1 << 3) | (1 << 5) | (1 << 7)  # {1, 3, 5, 7}
conjunto_b = (1 << 2) | (1 << 3) | (1 << 6) | (1 << 7)  # {2, 3, 6, 7}

print("Conjunto A:")
print_conjunto(conjunto_a)
print("Conjunto B:")
print_conjunto(conjunto_b)

# Operaciones de conjuntos
union = conjunto_a | conjunto_b
interseccion = conjunto_a & conjunto_b
diferencia = conjunto_a & ~conjunto_b

print("\nUnión:")
print_conjunto(union)
print("Intersección:")
print_conjunto(interseccion)
print("Diferencia (A - B):")
print_conjunto(diferencia)

# 8. Aplicaciones prácticas: Criptografía básica
print("\n8. Aplicaciones prácticas: Criptografía básica")
print("-" * 50)

# Cifrado XOR simple
def cifrar_xor(texto, clave):
    return bytes([b ^ clave for b in texto.encode()])

def descifrar_xor(bytes_cifrados, clave):
    return bytes([b ^ clave for b in bytes_cifrados]).decode()

mensaje = "Hola mundo!"
clave = 42

bytes_cifrados = cifrar_xor(mensaje, clave)
mensaje_descifrado = descifrar_xor(bytes_cifrados, clave)

print(f"Mensaje original: {mensaje}")
print(f"Mensaje cifrado (hex): {bytes_cifrados.hex()}")
print(f"Mensaje descifrado: {mensaje_descifrado}")

# 9. Trabajando con bytes y bytearray
print("\n9. Trabajando con bytes y bytearray")
print("-" * 50)

# Crear objetos bytes y bytearray
datos_bytes = bytes([0x41, 0x42, 0x43, 0x44])  # Inmutable
datos_bytearray = bytearray([0x45, 0x46, 0x47, 0x48])  # Mutable

print(f"bytes: {datos_bytes}")
print(f"bytes como string: {datos_bytes.decode('ascii')}")
print(f"bytearray: {datos_bytearray}")
print(f"bytearray como string: {datos_bytearray.decode('ascii')}")

# Modificar bytearray
datos_bytearray[2] = 0x58  # Cambiar 'G' por 'X'
print(f"bytearray modificado: {datos_bytearray}")
print(f"bytearray modificado como string: {datos_bytearray.decode('ascii')}")

# Operaciones bitwise en bytes
resultado = bytes([b1 ^ b2 for b1, b2 in zip(datos_bytes, datos_bytearray)])
print(f"XOR entre bytes y bytearray: {resultado.hex()}")

# 10. Trabajando con estructuras binarias
print("\n10. Trabajando con estructuras binarias")
print("-" * 50)

import struct

# Empaquetar datos en una estructura binaria
# 'I' - entero sin signo (4 bytes)
# 'f' - float (4 bytes)
# 'H' - entero corto sin signo (2 bytes)
# 's' - cadena de caracteres (bytes)
valores = (123456789, 3.14159, 42, b'Hola')
formato = 'IfH4s'
datos_empaquetados = struct.pack(formato, *valores)

print(f"Datos empaquetados (hex): {datos_empaquetados.hex()}")
print(f"Tamaño de datos: {len(datos_empaquetados)} bytes")

# Desempaquetar datos binarios
datos_desempaquetados = struct.unpack(formato, datos_empaquetados)
print(f"Datos desempaquetados: {datos_desempaquetados}")

# Ver el orden de bytes
import sys
print(f"\nOrden de bytes del sistema: {'little-endian' if sys.byteorder == 'little' else 'big-endian'}")
print(f"Ejemplo little-endian (int 1): {(1).to_bytes(4, byteorder='little').hex()}")
print(f"Ejemplo big-endian (int 1): {(1).to_bytes(4, byteorder='big').hex()}")

"""
EJERCICIOS PROPUESTOS:

1. Implementa una función `contar_bits_1(n)` que cuente el número de bits con 
   valor 1 en la representación binaria de un número entero sin utilizar 
   funciones predefinidas como bin() o count().

2. Implementa un sistema de permisos de archivos estilo Unix usando bits:
   - Define constantes para READ (4), WRITE (2), EXECUTE (1)
   - Crea funciones para verificar si un permiso está presente
   - Implementa funciones para añadir y quitar permisos
   - Crea una función para mostrar los permisos en formato rwx (como ls -l)

3. Desarrolla una clase `BitArray` que implemente un array de bits eficiente en 
   memoria con las siguientes operaciones:
   - set_bit(position, value): establece el bit en la posición dada
   - get_bit(position): obtiene el valor del bit en la posición dada
   - flip_bit(position): invierte el bit en la posición dada
   - count_ones(): cuenta el número total de unos
   - to_bytes(): convierte el array de bits a bytes
   - from_bytes(bytes_data): carga el array de bits desde bytes

4. Crea un algoritmo de cifrado más avanzado que use operaciones de bits:
   - Implementa un cifrado que use una clave de longitud variable
   - Combina operaciones XOR con desplazamientos de bits
   - Añade una función para cifrar y descifrar archivos binarios
   - Incluye una verificación de integridad simple (checksum)
"""
