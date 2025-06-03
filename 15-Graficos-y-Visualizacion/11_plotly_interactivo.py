"""
Ejercicio 11: Gráfico interactivo con plotly

Objetivo: Crear gráficos interactivos usando plotly.

Instrucciones:
- Instala plotly: pip install plotly
- Crea un gráfico interactivo de líneas.
"""

import plotly.graph_objects as go
import plotly.offline as pyo
import numpy as np

# Datos
x = np.linspace(0, 4*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Crear el gráfico interactivo
fig = go.Figure()

# Agregar trazas
fig.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='sin(x)', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='cos(x)', line=dict(color='red')))

# Configurar el layout
fig.update_layout(
    title='Funciones Trigonométricas Interactivas',
    xaxis_title='X',
    yaxis_title='Y',
    hovermode='x unified'
)

# Mostrar el gráfico
fig.show()
