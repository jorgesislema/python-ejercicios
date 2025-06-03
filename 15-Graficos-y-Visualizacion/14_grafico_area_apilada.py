"""
Ejercicio 14: Gráfico de área apilada

Objetivo: Crear un gráfico de área apilada para mostrar composición a lo largo del tiempo.

Instrucciones:
- Crea un gráfico de área apilada mostrando ventas de diferentes productos a lo largo del tiempo.
"""

import matplotlib.pyplot as plt
import numpy as np

# Datos simulados
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun']
producto_a = [20, 25, 30, 35, 40, 45]
producto_b = [15, 20, 25, 30, 25, 30]
producto_c = [10, 15, 20, 25, 30, 35]

# Crear el gráfico de área apilada
plt.figure(figsize=(10, 6))
plt.stackplot(meses, producto_a, producto_b, producto_c, 
              labels=['Producto A', 'Producto B', 'Producto C'],
              colors=['#ff9999', '#66b3ff', '#99ff99'],
              alpha=0.8)

plt.title('Ventas por Producto a lo Largo del Tiempo')
plt.xlabel('Mes')
plt.ylabel('Ventas (miles)')
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)
plt.show()
