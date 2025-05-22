"""
Ejercicio Avanzado: Operaciones con Conjuntos (Sets) y Operadores de Conjuntos

En este ejercicio aprenderás:
1. Operaciones avanzadas con conjuntos en Python
2. Uso de operadores de conjuntos para resolver problemas complejos
3. Aplicaciones prácticas de la teoría de conjuntos
4. Optimización de operaciones usando conjuntos

Los conjuntos (sets) son estructuras de datos que almacenan elementos únicos y
permiten realizar operaciones matemáticas de teoría de conjuntos como uniones,
intersecciones, diferencias, etc.
"""

# 1. Creación y características básicas de conjuntos
print("1. Creación y características básicas de conjuntos")
print("-" * 50)

# Creación de conjuntos
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}
conjunto_c = {1, 2, 3}
conjunto_vacio = set()  # Set vacío (no se puede usar {})

print(f"Conjunto A: {conjunto_a}")
print(f"Conjunto B: {conjunto_b}")
print(f"Conjunto C: {conjunto_c}")
print(f"Conjunto vacío: {conjunto_vacio}")

# Características de los conjuntos
print("\nCaracterísticas de los conjuntos:")
print(f"Los elementos son únicos: {set([1, 2, 2, 3, 3, 3])}")  # Elimina duplicados
print(f"Los elementos deben ser inmutables (no se pueden incluir listas o diccionarios)")
print(f"Los conjuntos son desordenados (no hay índices)")
print(f"Verificar pertenencia: 3 in conjunto_a = {3 in conjunto_a}")
print(f"Longitud del conjunto A: {len(conjunto_a)}")

# 2. Operadores de conjuntos
print("\n2. Operadores de conjuntos")
print("-" * 50)

# Unión (|): elementos que están en A o en B
union = conjunto_a | conjunto_b
print(f"Unión A | B: {union}")
print(f"Usando método union(): {conjunto_a.union(conjunto_b)}")

# Intersección (&): elementos que están en A y en B
interseccion = conjunto_a & conjunto_b
print(f"Intersección A & B: {interseccion}")
print(f"Usando método intersection(): {conjunto_a.intersection(conjunto_b)}")

# Diferencia (-): elementos que están en A pero no en B
diferencia = conjunto_a - conjunto_b
print(f"Diferencia A - B: {diferencia}")
print(f"Usando método difference(): {conjunto_a.difference(conjunto_b)}")

# Diferencia simétrica (^): elementos que están en A o en B pero no en ambos
dif_simetrica = conjunto_a ^ conjunto_b
print(f"Diferencia simétrica A ^ B: {dif_simetrica}")
print(f"Usando método symmetric_difference(): {conjunto_a.symmetric_difference(conjunto_b)}")

# 3. Relaciones entre conjuntos
print("\n3. Relaciones entre conjuntos")
print("-" * 50)

# Subconjunto (<=): todos los elementos de A están en B
es_subconjunto = conjunto_c <= conjunto_a
print(f"¿C es subconjunto de A?: {es_subconjunto}")
print(f"Usando método issubset(): {conjunto_c.issubset(conjunto_a)}")

# Superconjunto (>=): todos los elementos de B están en A
es_superconjunto = conjunto_a >= conjunto_c
print(f"¿A es superconjunto de C?: {es_superconjunto}")
print(f"Usando método issuperset(): {conjunto_a.issuperset(conjunto_c)}")

# Subconjunto propio (<): A es subconjunto de B y A ≠ B
es_subconjunto_propio = conjunto_c < conjunto_a
print(f"¿C es subconjunto propio de A?: {es_subconjunto_propio}")

# Superconjunto propio (>): A es superconjunto de B y A ≠ B
es_superconjunto_propio = conjunto_a > conjunto_c
print(f"¿A es superconjunto propio de C?: {es_superconjunto_propio}")

# Conjuntos disjuntos (sin elementos en común)
conjunto_d = {10, 11, 12}
son_disjuntos = conjunto_a.isdisjoint(conjunto_d)
print(f"¿A y D son disjuntos?: {son_disjuntos}")

# 4. Métodos de modificación de conjuntos
print("\n4. Métodos de modificación de conjuntos")
print("-" * 50)

# Copiar un conjunto
conjunto_copia = conjunto_a.copy()
print(f"Copia del conjunto A: {conjunto_copia}")

# Agregar un elemento
conjunto_copia.add(10)
print(f"Después de agregar 10: {conjunto_copia}")

# Actualizar con elementos de otro conjunto (unión)
conjunto_copia.update({11, 12, 13})
print(f"Después de update con {{11, 12, 13}}: {conjunto_copia}")

# Eliminar un elemento (error si no existe)
conjunto_copia.remove(10)
print(f"Después de eliminar 10: {conjunto_copia}")

# Eliminar un elemento (sin error si no existe)
conjunto_copia.discard(20)  # No existe, no hay error
print(f"Después de discard 20: {conjunto_copia}")

# Extraer y eliminar un elemento aleatorio
elemento = conjunto_copia.pop()
print(f"Elemento extraído: {elemento}")
print(f"Conjunto después de pop(): {conjunto_copia}")

# Limpiar el conjunto
conjunto_copia.clear()
print(f"Después de clear(): {conjunto_copia}")

# 5. Aplicaciones prácticas
print("\n5. Aplicaciones prácticas de conjuntos")
print("-" * 50)

# Eliminar duplicados de una lista
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5, 5, 5]
lista_sin_duplicados = list(set(lista_con_duplicados))
print(f"Lista original: {lista_con_duplicados}")
print(f"Lista sin duplicados: {lista_sin_duplicados}")

# Encontrar elementos únicos en cada lista
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
unicos_lista1 = set(lista1) - set(lista2)
unicos_lista2 = set(lista2) - set(lista1)
print(f"Elementos únicos en lista1: {unicos_lista1}")
print(f"Elementos únicos en lista2: {unicos_lista2}")

# Verificar si dos listas tienen elementos en común
tienen_comun = bool(set(lista1) & set(lista2))
print(f"¿Las listas tienen elementos en común?: {tienen_comun}")

# 6. Conjuntos inmutables (frozenset)
print("\n6. Conjuntos inmutables (frozenset)")
print("-" * 50)

# Crear un frozenset
fs = frozenset([1, 2, 3, 4, 5])
print(f"Frozenset: {fs}")
print("Los frozenset son inmutables y pueden usarse como claves en diccionarios")

# Creando un diccionario con frozensets como claves
grupo1 = frozenset(["Ana", "Juan", "Pedro"])
grupo2 = frozenset(["Luis", "María", "Elena"])
equipos = {
    grupo1: "Equipo Alfa",
    grupo2: "Equipo Beta"
}
print(f"Diccionario con frozensets como claves: {equipos}")

# 7. Rendimiento y complejidad
print("\n7. Rendimiento y complejidad")
print("-" * 50)
print("Los conjuntos utilizan tablas hash internamente:")
print("- Verificación de pertenencia (in): O(1) en promedio")
print("- Agregar/eliminar elementos: O(1) en promedio")
print("- Operaciones de conjuntos (unión, intersección): O(len(s)+len(t))")
print("Esto los hace muy eficientes para ciertas operaciones comparado con listas")

# Ejemplo de eficiencia: buscar elementos en lista vs conjunto
import time

print("\nComparación de rendimiento:")
datos = list(range(1000000))
elemento = 999999

# Búsqueda en lista
inicio = time.time()
resultado_lista = elemento in datos
tiempo_lista = time.time() - inicio
print(f"Tiempo de búsqueda en lista: {tiempo_lista:.6f} segundos")

# Búsqueda en conjunto
conjunto_datos = set(datos)
inicio = time.time()
resultado_conjunto = elemento in conjunto_datos
tiempo_conjunto = time.time() - inicio
print(f"Tiempo de búsqueda en conjunto: {tiempo_conjunto:.6f} segundos")
print(f"El conjunto fue {tiempo_lista/tiempo_conjunto:.1f} veces más rápido")

"""
EJERCICIOS PROPUESTOS:

1. Crea dos conjuntos: `vocales` con todas las vocales y `consonantes` con todas 
   las consonantes del alfabeto español. Luego:
   a) Muestra la unión de ambos conjuntos
   b) Verifica si `vocales` es un subconjunto de `consonantes`
   c) Obtén la diferencia simétrica entre ambos conjuntos

2. Dadas tres listas con nombres de estudiantes que toman diferentes cursos:
   python_students = ["Ana", "Juan", "Pedro", "María", "Luis"]
   java_students = ["Pedro", "Luis", "Carlos", "Elena", "Sofía"]
   data_science_students = ["María", "Pedro", "Elena", "Daniel"]
   
   Encuentra:
   a) Estudiantes que toman los tres cursos
   b) Estudiantes que toman Python y Data Science, pero no Java
   c) Estudiantes que toman al menos uno de los cursos
   d) Estudiantes que toman exactamente dos cursos

3. Implementa una función `es_particion(universal, *subconjuntos)` que verifique 
   si un conjunto de subconjuntos forma una partición del conjunto universal.
   Una partición debe cumplir:
   - La unión de todos los subconjuntos debe ser igual al conjunto universal
   - Los subconjuntos deben ser disjuntos entre sí (sin elementos en común)

4. Implementa un sistema de recomendación básico utilizando conjuntos:
   a) Crea diccionarios donde las claves sean usuarios y los valores sean 
      conjuntos de películas que han visto
   b) Implementa una función que reciba dos usuarios y calcule su índice de 
      similitud de Jaccard (tamaño de intersección / tamaño de unión)
   c) Implementa una función que recomiende películas a un usuario basándose 
      en las películas vistas por usuarios similares
"""
