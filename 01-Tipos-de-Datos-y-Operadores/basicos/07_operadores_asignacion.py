"""
Ejercicio 7: Operadores de Asignación

Objetivo: Comprender y utilizar los diferentes operadores de asignación en Python.

Instrucciones:
1. Explora los operadores de asignación: =, +=, -=, *=, /=, //=, %=, **=.
2. Comprende cómo funcionan los operadores de asignación compuestos.
3. Muestra ejemplos de uso práctico de estos operadores.
4. Aplica operadores de asignación con diferentes tipos de datos.
"""

def main():
    # Operador de asignación básico (=)
    print("=== Operador de Asignación Básico ===")
    x = 10
    print(f"x = 10 → x = {x}")
    
    # Asignación múltiple
    a, b, c = 1, 2, 3
    print(f"a, b, c = 1, 2, 3 → a = {a}, b = {b}, c = {c}")
    
    # Intercambio de valores con asignación múltiple
    a, b = b, a
    print(f"a, b = b, a → a = {a}, b = {b}")
    
    # Operadores de asignación compuestos
    print("\n=== Operadores de Asignación Compuestos con Enteros ===")
    
    # Asignación con suma (+=)
    x = 10
    x += 5  # Equivalente a x = x + 5
    print(f"x = 10, x += 5 → x = {x}")
    
    # Asignación con resta (-=)
    x = 10
    x -= 3  # Equivalente a x = x - 3
    print(f"x = 10, x -= 3 → x = {x}")
    
    # Asignación con multiplicación (*=)
    x = 10
    x *= 2  # Equivalente a x = x * 2
    print(f"x = 10, x *= 2 → x = {x}")
    
    # Asignación con división (/=)
    x = 10
    x /= 2  # Equivalente a x = x / 2
    print(f"x = 10, x /= 2 → x = {x}")
    
    # Asignación con división entera (//=)
    x = 10
    x //= 3  # Equivalente a x = x // 3
    print(f"x = 10, x //= 3 → x = {x}")
    
    # Asignación con módulo (%=)
    x = 10
    x %= 3  # Equivalente a x = x % 3
    print(f"x = 10, x %= 3 → x = {x}")
    
    # Asignación con potencia (**=)
    x = 2
    x **= 3  # Equivalente a x = x ** 3
    print(f"x = 2, x **= 3 → x = {x}")
    
    # Operadores de asignación con strings
    print("\n=== Operadores de Asignación con Strings ===")
    
    # Asignación con concatenación (+=)
    mensaje = "Hola"
    mensaje += " Mundo"  # Equivalente a mensaje = mensaje + " Mundo"
    print(f'mensaje = "Hola", mensaje += " Mundo" → mensaje = "{mensaje}"')
    
    # Asignación con repetición (*=)
    simbolo = "*"
    simbolo *= 5  # Equivalente a simbolo = simbolo * 5
    print(f'simbolo = "*", simbolo *= 5 → simbolo = "{simbolo}"')
    
    # Operadores de asignación con listas
    print("\n=== Operadores de Asignación con Listas ===")
    
    # Asignación con concatenación (+=)
    lista = [1, 2, 3]
    lista += [4, 5]  # Equivalente a lista = lista + [4, 5]
    print(f"lista = [1, 2, 3], lista += [4, 5] → lista = {lista}")
    
    # Asignación con repetición (*=)
    lista = [1, 2]
    lista *= 3  # Equivalente a lista = lista * 3
    print(f"lista = [1, 2], lista *= 3 → lista = {lista}")
    
    # Aplicaciones prácticas
    print("\n=== Aplicaciones Prácticas ===")
    
    # Contador
    contador = 0
    print(f"Valor inicial del contador: {contador}")
    
    # Incrementar el contador
    contador += 1
    print(f"Después de incrementar: {contador}")
    
    # Acumular valores
    suma = 0
    numeros = [10, 20, 30, 40, 50]
    
    for num in numeros:
        suma += num
    
    print(f"Suma de {numeros}: {suma}")
    
    # Construcción de cadenas
    html = "<ul>\n"
    
    elementos = ["Elemento 1", "Elemento 2", "Elemento 3"]
    for elem in elementos:
        html += f"    <li>{elem}</li>\n"
    
    html += "</ul>"
    print(f"HTML construido:\n{html}")
    
    # Ejercicios para el usuario
    print("\n=== EJERCICIOS PARA PRACTICAR ===")
    print("1. Escribe un programa que calcule la suma de los primeros n números naturales usando operadores de asignación")
    print("2. Crea una función que construya una pirámide de asteriscos de altura n usando operadores de asignación")
    print("3. Implementa un programa que calcule el factorial de un número usando operadores de asignación")
    print("4. Escribe una función que concatene todas las cadenas de una lista en una sola, usando operadores de asignación")

if __name__ == "__main__":
    main()
