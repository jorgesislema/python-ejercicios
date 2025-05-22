"""
Ejercicio 3: Manipulación de Bytes y Memoria

Objetivo: Aprender a trabajar con datos binarios, bytes y manipulación a nivel de memoria.

Instrucciones:
1. Trabajar con tipos de datos bytes y bytearray.
2. Convertir entre diferentes codificaciones de caracteres.
3. Manipular datos binarios y realizar operaciones bitwise.
4. Explorar módulos como struct y array para manipulación eficiente de datos binarios.
"""

import struct
import array
import binascii
import sys
import io

def main():
    # Tipos de datos bytes y bytearray
    print("=== Tipos de Datos bytes y bytearray ===")
    
    # Crear objetos bytes
    b1 = bytes([65, 66, 67, 68, 69])  # A través de una lista de enteros
    b2 = bytes("Hello", "utf-8")      # A través de una cadena y codificación
    b3 = b"Python"                    # Usando un literal de bytes
    
    print(f"b1: {b1}")
    print(f"b2: {b2}")
    print(f"b3: {b3}")
    
    # Acceder a elementos
    print(f"Primer byte de b1: {b1[0]}")  # Devuelve un entero (código ASCII)
    print(f"Primeros 3 bytes de b2: {b2[:3]}")
    
    # bytes es inmutable
    try:
        b1[0] = 90  # Esto causará un error
    except TypeError as e:
        print(f"Error al modificar bytes: {e}")
    
    # bytearray es mutable
    ba = bytearray([65, 66, 67, 68, 69])
    print(f"bytearray original: {ba}")
    
    ba[0] = 90  # Cambiar 'A' (65) por 'Z' (90)
    print(f"bytearray modificado: {ba}")
    
    # Conversión entre bytes y otros tipos
    print("\n=== Conversión entre bytes y otros tipos ===")
    
    # De bytes a string
    texto_bytes = b"Hello, World!"
    texto_str = texto_bytes.decode("utf-8")
    print(f"bytes: {texto_bytes}")
    print(f"string: {texto_str}")
    
    # De string a bytes
    texto = "¡Hola, Mundo!"
    bytes_utf8 = texto.encode("utf-8")
    bytes_latin1 = texto.encode("latin-1")
    
    print(f"string: {texto}")
    print(f"bytes (UTF-8): {bytes_utf8}")
    print(f"bytes (Latin-1): {bytes_latin1}")
    
    # Comparación de tamaños
    print(f"Tamaño en UTF-8: {len(bytes_utf8)} bytes")
    print(f"Tamaño en Latin-1: {len(bytes_latin1)} bytes")
    
    # Trabajar con diferentes codificaciones
    print("\n=== Trabajar con Diferentes Codificaciones ===")
    
    # Ejemplo con caracteres que varían entre codificaciones
    texto_especial = "áéíóúñ"
    codificaciones = ["utf-8", "latin-1", "cp1252", "ascii"]
    
    print(f"Texto original: {texto_especial}")
    
    for cod in codificaciones:
        try:
            bytes_cod = texto_especial.encode(cod)
            hex_repr = binascii.hexlify(bytes_cod).decode('ascii')
            print(f"Codificación {cod}: {bytes_cod} (hex: {hex_repr})")
        except UnicodeEncodeError as e:
            print(f"Error con {cod}: {e}")
    
    # Manipulación binaria con el módulo struct
    print("\n=== Manipulación Binaria con el Módulo struct ===")
    
    # Empaquetar datos en bytes
    # 'i' para entero, 'f' para float, '10s' para string de 10 bytes
    packed = struct.pack('if10s', 42, 3.14, b'Python\0\0\0\0')
    print(f"Datos empaquetados: {packed}")
    print(f"Representación hex: {binascii.hexlify(packed)}")
    
    # Desempaquetar datos
    unpacked = struct.unpack('if10s', packed)
    print(f"Datos desempaquetados: {unpacked}")
    print(f"Entero: {unpacked[0]}")
    print(f"Float: {unpacked[1]}")
    print(f"String: {unpacked[2].decode('ascii').rstrip('\\x00')}")
    
    # Calcular el tamaño de una estructura
    struct_size = struct.calcsize('if10s')
    print(f"Tamaño de la estructura: {struct_size} bytes")
    
    # Uso del módulo array para manipulación eficiente
    print("\n=== Uso del Módulo array para Manipulación Eficiente ===")
    
    # Crear un array de enteros
    arr_i = array.array('i', [10, 20, 30, 40, 50])
    print(f"Array de enteros: {arr_i}")
    
    # Crear un array de flotantes
    arr_f = array.array('f', [1.1, 2.2, 3.3, 4.4, 5.5])
    print(f"Array de flotantes: {arr_f}")
    
    # Modificar elementos
    arr_i[0] = 100
    print(f"Array de enteros modificado: {arr_i}")
    
    # Convertir a bytes
    bytes_arr_i = arr_i.tobytes()
    print(f"Array de enteros como bytes: {binascii.hexlify(bytes_arr_i)}")
    
    # Crear un array a partir de bytes
    arr_i2 = array.array('i')
    arr_i2.frombytes(bytes_arr_i)
    print(f"Array recreado desde bytes: {arr_i2}")
    
    # Manipulación de bits
    print("\n=== Manipulación de Bits ===")
    
    # Crear un entero y mostrar su representación binaria
    num = 42
    bin_repr = bin(num)
    print(f"Número: {num}, Representación binaria: {bin_repr}")
    
    # Operaciones bit a bit
    print(f"NOT (~): {~num} (binario: {bin(~num & 0xFFFFFFFF)})")
    print(f"AND (&) con 15: {num & 15} (binario: {bin(num & 15)})")
    print(f"OR (|) con 15: {num | 15} (binario: {bin(num | 15)})")
    print(f"XOR (^) con 15: {num ^ 15} (binario: {bin(num ^ 15)})")
    print(f"Desplazamiento izquierda (<<) 2 bits: {num << 2} (binario: {bin(num << 2)})")
    print(f"Desplazamiento derecha (>>) 2 bits: {num >> 2} (binario: {bin(num >> 2)})")
    
    # Manipulación de bits individuales
    def get_bit(num, pos):
        """Obtiene el valor del bit en la posición pos."""
        return (num >> pos) & 1
    
    def set_bit(num, pos, value):
        """Establece el bit en la posición pos al valor dado."""
        if value:
            return num | (1 << pos)
        else:
            return num & ~(1 << pos)
    
    print(f"\nValor del bit 3 en {num}: {get_bit(num, 3)}")
    
    new_num = set_bit(num, 3, 0)  # Establecer el bit 3 a 0
    print(f"Número después de establecer el bit 3 a 0: {new_num} (binario: {bin(new_num)})")
    
    # Tamaño y alineación en memoria
    print("\n=== Tamaño y Alineación en Memoria ===")
    
    print(f"Tamaño de int: {sys.getsizeof(0)} bytes")
    print(f"Tamaño de float: {sys.getsizeof(0.0)} bytes")
    print(f"Tamaño de bool: {sys.getsizeof(False)} bytes")
    print(f"Tamaño de una cadena vacía: {sys.getsizeof('')} bytes")
    print(f"Tamaño de una lista vacía: {sys.getsizeof([])} bytes")
    
    # Ejemplo práctico: Leer y escribir un archivo binario
    print("\n=== Ejemplo Práctico: Archivo Binario ===")
    
    # Estructura de un registro simple: ID (int), Precio (float), Nombre (20 chars)
    formato_registro = 'if20s'
    tamano_registro = struct.calcsize(formato_registro)
    
    print(f"Tamaño de cada registro: {tamano_registro} bytes")
    
    # Datos de ejemplo
    productos = [
        (1, 19.99, b'Laptop\0\0\0\0\0\0\0\0\0\0\0\0\0\0'),
        (2, 5.99, b'Mouse\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'),
        (3, 29.99, b'Teclado\0\0\0\0\0\0\0\0\0\0\0\0\0')
    ]
    
    # Escribir en un buffer de bytes (en lugar de un archivo)
    buffer = io.BytesIO()
    
    for producto in productos:
        registro_bytes = struct.pack(formato_registro, *producto)
        buffer.write(registro_bytes)
    
    # Leer los registros
    buffer.seek(0)  # Volver al inicio del buffer
    
    print("Registros leídos:")
    for i in range(len(productos)):
        registro_bytes = buffer.read(tamano_registro)
        if not registro_bytes:
            break
        
        registro = struct.unpack(formato_registro, registro_bytes)
        id_prod, precio, nombre_bytes = registro
        nombre = nombre_bytes.decode('ascii').rstrip('\0')
        
        print(f"ID: {id_prod}, Precio: ${precio:.2f}, Nombre: {nombre}")
    
    # Ejercicios para el usuario
    print("\n=== EJERCICIOS PARA PRACTICAR ===")
    print("1. Crea una función que convierta un archivo de texto a binario y viceversa")
    print("2. Implementa un sistema simple de serialización para guardar y cargar objetos en formato binario")
    print("3. Desarrolla un programa que cifre y descifre texto usando operaciones XOR a nivel de byte")
    print("4. Crea una función que lea un archivo de imagen BMP y extraiga su información de cabecera")

if __name__ == "__main__":
    main()
