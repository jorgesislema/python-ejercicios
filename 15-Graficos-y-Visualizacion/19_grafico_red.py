"""
Ejercicio 19: Gráfico de red (network graph)

Objetivo: Crear un gráfico de red para mostrar relaciones entre nodos.

Instrucciones:
- Instala networkx: pip install networkx
- Crea un gráfico de red mostrando conexiones entre personas.
"""

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Crear un grafo
G = nx.Graph()

# Agregar nodos (personas)
personas = ['Ana', 'Bob', 'Carlos', 'Diana', 'Eva', 'Frank', 'Grace', 'Hugo']
G.add_nodes_from(personas)

# Agregar aristas (relaciones/conexiones)
conexiones = [
    ('Ana', 'Bob'), ('Ana', 'Carlos'), ('Ana', 'Diana'),
    ('Bob', 'Eva'), ('Bob', 'Frank'),
    ('Carlos', 'Grace'), ('Carlos', 'Hugo'),
    ('Diana', 'Eva'), ('Diana', 'Grace'),
    ('Eva', 'Frank'), ('Eva', 'Hugo'),
    ('Frank', 'Grace'),
    ('Grace', 'Hugo')
]
G.add_edges_from(conexiones)

# Crear el gráfico
plt.figure(figsize=(12, 10))

# Calcular posiciones usando un algoritmo de layout
pos = nx.spring_layout(G, k=2, iterations=50)

# Dibujar los nodos
nx.draw_networkx_nodes(G, pos, 
                      node_color='lightblue', 
                      node_size=1500,
                      alpha=0.9)

# Dibujar las aristas
nx.draw_networkx_edges(G, pos, 
                      edge_color='gray', 
                      width=2,
                      alpha=0.6)

# Dibujar las etiquetas
nx.draw_networkx_labels(G, pos, 
                       font_size=12, 
                       font_weight='bold')

# Configurar el gráfico
plt.title('Red Social - Conexiones entre Personas', fontsize=16, pad=20)
plt.axis('off')  # Quitar los ejes
plt.tight_layout()

# Mostrar información del grafo
print(f"Número de nodos: {G.number_of_nodes()}")
print(f"Número de aristas: {G.number_of_edges()}")
print(f"Densidad del grafo: {nx.density(G):.3f}")

plt.show()
