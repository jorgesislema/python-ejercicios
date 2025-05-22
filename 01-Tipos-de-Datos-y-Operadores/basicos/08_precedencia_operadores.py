"""
Ejercicio 8: Precedencia de Operadores

Objetivo: Comprender el orden de evaluación de los operadores en Python.

Instrucciones:
1. Estudia las reglas de precedencia de operadores en Python.
2. Crea ejemplos que demuestren el orden de evaluación.
3. Usa paréntesis para alterar el orden de evaluación natural.
4. Demuestra cómo la precedencia puede afectar el resultado de expresiones.
"""

def main():
    # Tabla de precedencia de operadores en Python (de mayor a menor)
    print("=== Precedencia de Operadores en Python ===")
    print("1. () - Paréntesis")
    print("2. ** - Exponenciación")
    print("3. +x, -x, ~x - Positivo, negativo, complemento bit a bit")
    print("4. *, /, //, % - Multiplicación, división, división entera, módulo")
    print("5. +, - - Suma, resta")
    print("6. <<, >> - Desplazamiento bit a bit")
    print("7. & - AND bit a bit")
    print("8. ^ - XOR bit a bit")
    print("9. | - OR bit a bit")
    print("10. ==, !=, >, >=, <, <=, is, is not, in, not in - Comparaciones")
    print("11. not - Negación lógica")
    print("12. and - AND lógico")
    print("13. or - OR lógico")
    
    # Ejemplos de precedencia en expresiones aritméticas
    print("\n=== Ejemplos de Precedencia en Expresiones Aritméticas ===")
    
    # Ejemplo 1: Multiplicación tiene precedencia sobre suma
    expresion1 = 2 + 3 * 4
    print(f"2 + 3 * 4 = {expresion1}")
    print("(La multiplicación se realiza antes que la suma)")
    
    # Con paréntesis para cambiar la precedencia
    expresion1_parentesis = (2 + 3) * 4
    print(f"(2 + 3) * 4 = {expresion1_parentesis}")
    print("(Los paréntesis tienen la mayor precedencia)")
    
    # Ejemplo 2: Exponenciación tiene precedencia sobre multiplicación
    expresion2 = 2 * 3 ** 2
    print(f"2 * 3 ** 2 = {expresion2}")
    print("(La exponenciación se realiza antes que la multiplicación)")
    
    # Con paréntesis para cambiar la precedencia
    expresion2_parentesis = (2 * 3) ** 2
    print(f"(2 * 3) ** 2 = {expresion2_parentesis}")
    
    # Ejemplo 3: División y multiplicación tienen la misma precedencia (evaluación de izquierda a derecha)
    expresion3 = 8 / 4 * 2
    print(f"8 / 4 * 2 = {expresion3}")
    print("(División y multiplicación tienen la misma precedencia, se evalúan de izquierda a derecha)")
    
    # Ejemplo 4: Operadores unarios tienen precedencia sobre operadores binarios
    expresion4 = -3 ** 2
    print(f"-3 ** 2 = {expresion4}")
    print("(La exponenciación se aplica al 3, luego se aplica el signo negativo)")
    
    # Con paréntesis para cambiar la precedencia
    expresion4_parentesis = (-3) ** 2
    print(f"(-3) ** 2 = {expresion4_parentesis}")
    
    # Ejemplos de precedencia en expresiones lógicas y de comparación
    print("\n=== Ejemplos de Precedencia en Expresiones Lógicas y de Comparación ===")
    
    # Ejemplo 5: Comparaciones tienen precedencia sobre operadores lógicos
    a, b, c = 5, 10, 15
    expresion5 = a < b and b < c
    print(f"a = {a}, b = {b}, c = {c}")
    print(f"a < b and b < c = {expresion5}")
    print("(Las comparaciones se realizan antes que el AND lógico)")
    
    # Ejemplo 6: NOT tiene precedencia sobre AND, y AND sobre OR
    x, y, z = True, False, True
    expresion6 = x or y and z
    print(f"x = {x}, y = {y}, z = {z}")
    print(f"x or y and z = {expresion6}")
    print("(AND se evalúa antes que OR)")
    
    # Con paréntesis para cambiar la precedencia
    expresion6_parentesis = (x or y) and z
    print(f"(x or y) and z = {expresion6_parentesis}")
    
    # Ejemplo 7: Precedencia entre operadores bit a bit y comparación
    m, n = 5, 3
    expresion7 = m & n == 1
    print(f"m = {m}, n = {n}")
    print(f"m & n == 1 = {expresion7}")
    print("(El AND bit a bit se realiza antes que la comparación de igualdad)")
    
    # Con paréntesis para mayor claridad
    expresion7_parentesis = (m & n) == 1
    print(f"(m & n) == 1 = {expresion7_parentesis}")
    
    # Expresiones complejas
    print("\n=== Expresiones Complejas ===")
    
    # Ejemplo 8: Expresión compleja con múltiples operadores
    d, e, f = 2, 3, 4
    expresion8 = d + e * f ** 2 % 3
    print(f"d = {d}, e = {e}, f = {f}")
    print(f"d + e * f ** 2 % 3 = {expresion8}")
    print("Orden de evaluación: 1. f ** 2, 2. e * (f ** 2), 3. (e * (f ** 2)) % 3, 4. d + ((e * (f ** 2)) % 3)")
    
    # Desglose paso a paso
    paso1 = f ** 2
    paso2 = e * paso1
    paso3 = paso2 % 3
    paso4 = d + paso3
    print(f"Paso 1: f ** 2 = {paso1}")
    print(f"Paso 2: e * (f ** 2) = {paso2}")
    print(f"Paso 3: (e * (f ** 2)) % 3 = {paso3}")
    print(f"Paso 4: d + ((e * (f ** 2)) % 3) = {paso4}")
    
    # Ejercicios para el usuario
    print("\n=== EJERCICIOS PARA PRACTICAR ===")
    print("1. ¿Cuál es el resultado de 3 + 4 * 2 / (1 - 5) ** 2? Escribe el desglose paso a paso")
    print("2. Evalúa la expresión: 10 > 5 and 7 < 10 or 3 == 3 and not 10 > 20")
    print("3. Escribe una expresión que calcule el promedio de tres números, pero que multiplique el primer número por 2 antes de calcular el promedio")
    print("4. Crea una expresión que determine si un número es divisible por 2 y por 3, pero no por 5")

if __name__ == "__main__":
    main()
