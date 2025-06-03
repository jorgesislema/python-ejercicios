"""
Ejercicio 2: Gráfico de barras

Objetivo: Crear un gráfico de barras para mostrar datos categóricos.

Instrucciones:
- Crea un gráfico de barras que muestre las ventas de diferentes productos.
"""

import matplotlib.pyplot as plt

# Datos
productos = ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Auriculares']
ventas = [120, 85, 75, 95, 110]

# Crear el gráfico de barras
plt.bar(productos, ventas, color=['blue', 'green', 'red', 'orange', 'purple'])
plt.title('Ventas por Producto')
plt.xlabel('Productos')
plt.ylabel('Cantidad Vendida')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
