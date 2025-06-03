"""
Ejercicio 1: Gráfico de líneas básico con matplotlib

Objetivo: Crear un gráfico de líneas simple usando matplotlib.

Instrucciones:
- Instala matplotlib: pip install matplotlib
- Crea un gráfico de líneas que muestre los números del 1 al 10 y sus cuadrados.
"""

import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [i**2 for i in x]

# Crear el gráfico
plt.plot(x, y)
plt.title('Gráfico de Cuadrados')
plt.xlabel('Números')
plt.ylabel('Cuadrados')
plt.grid(True)
plt.show()
