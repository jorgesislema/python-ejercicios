"""
Ejercicio 20: Dashboard Interactivo Completo
==========================================

Objetivo:
Crear un dashboard interactivo completo que combine múltiples tipos de 
visualizaciones y widgets de interacción usando matplotlib y tkinter.

Conceptos a practicar:
- Dashboard con múltiples gráficos
- Interfaz gráfica con tkinter
- Actualización en tiempo real
- Widgets de control (botones, sliders, combobox)
- Datos simulados dinámicos

Instrucciones:
1. Crear una interfaz con múltiples gráficos
2. Añadir controles interactivos
3. Implementar actualización de datos en tiempo real
4. Mostrar diferentes tipos de visualizaciones
"""

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import threading
import time

class DashboardInteractivo:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard Interactivo - Análisis de Ventas")
        self.root.geometry("1200x800")
        
        # Variables de control
        self.tiempo_actual = 0
        self.actualizacion_activa = False
        self.intervalo_actualizacion = 1000  # milisegundos
        
        # Datos simulados
        self.generar_datos_iniciales()
        
        # Crear la interfaz
        self.crear_interfaz()
        
        # Inicializar gráficos
        self.actualizar_graficos()
    
    def generar_datos_iniciales(self):
        """Genera datos iniciales para el dashboard"""
        # Datos de ventas por mes
        meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun']
        self.ventas_mensuales = [120, 140, 110, 160, 180, 200]
        self.productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D']
        self.ventas_productos = [45, 30, 15, 10]
        
        # Datos de tiempo real (simulados)
        self.datos_tiempo_real = []
        for i in range(50):
            valor = 50 + 30 * np.sin(i * 0.2) + np.random.normal(0, 5)
            self.datos_tiempo_real.append(max(0, valor))
        
        # Datos de regiones
        self.regiones = ['Norte', 'Sur', 'Este', 'Oeste', 'Centro']
        self.ventas_regiones = [25, 20, 30, 15, 10]
    
    def crear_interfaz(self):
        """Crea la interfaz principal del dashboard"""
        # Frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Panel de control superior
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Título
        titulo = ttk.Label(control_frame, text="Dashboard de Ventas", 
                          font=('Arial', 16, 'bold'))
        titulo.pack(side=tk.LEFT)
        
        # Controles
        ttk.Label(control_frame, text="Actualización:").pack(side=tk.RIGHT, padx=(10, 5))
        self.btn_toggle = ttk.Button(control_frame, text="Iniciar", 
                                   command=self.toggle_actualizacion)
        self.btn_toggle.pack(side=tk.RIGHT, padx=5)
        
        # Selector de intervalo
        ttk.Label(control_frame, text="Intervalo (s):").pack(side=tk.RIGHT, padx=(10, 5))
        self.combo_intervalo = ttk.Combobox(control_frame, values=[0.5, 1, 2, 5], 
                                          width=5, state="readonly")
        self.combo_intervalo.set("1")
        self.combo_intervalo.pack(side=tk.RIGHT, padx=5)
        self.combo_intervalo.bind("<<ComboboxSelected>>", self.cambiar_intervalo)
        
        # Frame para gráficos
        graficos_frame = ttk.Frame(main_frame)
        graficos_frame.pack(fill=tk.BOTH, expand=True)
        
        # Crear la figura con subplots
        self.fig = Figure(figsize=(12, 8), facecolor='white')
        
        # Subplot 1: Ventas mensuales (línea)
        self.ax1 = self.fig.add_subplot(2, 3, 1)
        self.ax1.set_title('Ventas Mensuales')
        
        # Subplot 2: Productos (barras)
        self.ax2 = self.fig.add_subplot(2, 3, 2)
        self.ax2.set_title('Ventas por Producto')
        
        # Subplot 3: Regiones (pie)
        self.ax3 = self.fig.add_subplot(2, 3, 3)
        self.ax3.set_title('Ventas por Región')
        
        # Subplot 4: Tiempo real (línea animada)
        self.ax4 = self.fig.add_subplot(2, 3, 4)
        self.ax4.set_title('Datos en Tiempo Real')
        
        # Subplot 5: Correlación (scatter)
        self.ax5 = self.fig.add_subplot(2, 3, 5)
        self.ax5.set_title('Correlación Precio-Cantidad')
        
        # Subplot 6: Distribución (histograma)
        self.ax6 = self.fig.add_subplot(2, 3, 6)
        self.ax6.set_title('Distribución de Ventas')
        
        # Ajustar layout
        self.fig.tight_layout(pad=3.0)
        
        # Canvas para matplotlib
        self.canvas = FigureCanvasTkAgg(self.fig, graficos_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Frame de estadísticas
        stats_frame = ttk.LabelFrame(main_frame, text="Estadísticas en Vivo", padding=10)
        stats_frame.pack(fill=tk.X, pady=(10, 0))
        
        # Labels para estadísticas
        stats_inner = ttk.Frame(stats_frame)
        stats_inner.pack(fill=tk.X)
        
        self.label_total = ttk.Label(stats_inner, text="Total Ventas: $0", 
                                   font=('Arial', 10, 'bold'))
        self.label_total.pack(side=tk.LEFT, padx=(0, 20))
        
        self.label_promedio = ttk.Label(stats_inner, text="Promedio: $0", 
                                      font=('Arial', 10, 'bold'))
        self.label_promedio.pack(side=tk.LEFT, padx=(0, 20))
        
        self.label_max = ttk.Label(stats_inner, text="Máximo: $0", 
                                 font=('Arial', 10, 'bold'))
        self.label_max.pack(side=tk.LEFT, padx=(0, 20))
        
        self.label_tiempo = ttk.Label(stats_inner, text="Última actualización: --", 
                                    font=('Arial', 10))
        self.label_tiempo.pack(side=tk.RIGHT)
    
    def actualizar_graficos(self):
        """Actualiza todos los gráficos del dashboard"""
        # Limpiar todos los axes
        for ax in [self.ax1, self.ax2, self.ax3, self.ax4, self.ax5, self.ax6]:
            ax.clear()
        
        # 1. Gráfico de ventas mensuales
        meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun']
        self.ax1.plot(meses, self.ventas_mensuales, marker='o', linewidth=2, 
                     color='#2E86AB', markersize=6)
        self.ax1.set_title('Ventas Mensuales', fontweight='bold')
        self.ax1.set_ylabel('Ventas ($k)')
        self.ax1.grid(True, alpha=0.3)
        self.ax1.tick_params(axis='x', rotation=45)
        
        # 2. Gráfico de barras por producto
        colores = ['#A23B72', '#F18F01', '#C73E1D', '#592941']
        barras = self.ax2.bar(self.productos, self.ventas_productos, color=colores)
        self.ax2.set_title('Ventas por Producto', fontweight='bold')
        self.ax2.set_ylabel('Ventas (%)')
        
        # Añadir valores en las barras
        for barra, valor in zip(barras, self.ventas_productos):
            self.ax2.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 0.5,
                         f'{valor}%', ha='center', va='bottom', fontweight='bold')
        
        # 3. Gráfico de pie por región
        colores_pie = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
        wedges, texts, autotexts = self.ax3.pie(self.ventas_regiones, labels=self.regiones, 
                                               autopct='%1.1f%%', colors=colores_pie,
                                               startangle=90)
        self.ax3.set_title('Ventas por Región', fontweight='bold')
        
        # 4. Datos en tiempo real
        x_tiempo = list(range(len(self.datos_tiempo_real)))
        self.ax4.plot(x_tiempo, self.datos_tiempo_real, color='#E74C3C', linewidth=2)
        self.ax4.fill_between(x_tiempo, self.datos_tiempo_real, alpha=0.3, color='#E74C3C')
        self.ax4.set_title('Datos en Tiempo Real', fontweight='bold')
        self.ax4.set_ylabel('Valor')
        self.ax4.set_xlim(0, 50)
        self.ax4.grid(True, alpha=0.3)
        
        # 5. Correlación precio-cantidad
        precios = np.random.uniform(10, 100, 50)
        cantidades = 100 - precios + np.random.normal(0, 10, 50)
        cantidades = np.maximum(cantidades, 0)
        
        scatter = self.ax5.scatter(precios, cantidades, c=cantidades, 
                                 cmap='viridis', alpha=0.6, s=60)
        self.ax5.set_title('Correlación Precio-Cantidad', fontweight='bold')
        self.ax5.set_xlabel('Precio ($)')
        self.ax5.set_ylabel('Cantidad')
        self.ax5.grid(True, alpha=0.3)
        
        # 6. Distribución de ventas
        datos_dist = np.random.normal(100, 20, 1000)
        self.ax6.hist(datos_dist, bins=30, color='#3498DB', alpha=0.7, edgecolor='black')
        self.ax6.set_title('Distribución de Ventas', fontweight='bold')
        self.ax6.set_xlabel('Valor de Venta')
        self.ax6.set_ylabel('Frecuencia')
        self.ax6.grid(True, alpha=0.3)
        
        # Ajustar layout y redibujar
        self.fig.tight_layout(pad=3.0)
        self.canvas.draw()
        
        # Actualizar estadísticas
        self.actualizar_estadisticas()
    
    def actualizar_estadisticas(self):
        """Actualiza las estadísticas mostradas"""
        total = sum(self.ventas_mensuales)
        promedio = total / len(self.ventas_mensuales)
        maximo = max(self.ventas_mensuales)
        
        self.label_total.config(text=f"Total Ventas: ${total}k")
        self.label_promedio.config(text=f"Promedio: ${promedio:.1f}k")
        self.label_max.config(text=f"Máximo: ${maximo}k")
        self.label_tiempo.config(text=f"Última actualización: {datetime.now().strftime('%H:%M:%S')}")
    
    def simular_datos_tiempo_real(self):
        """Simula nuevos datos en tiempo real"""
        # Añadir nuevo punto
        nuevo_valor = 50 + 30 * np.sin(self.tiempo_actual * 0.2) + np.random.normal(0, 5)
        nuevo_valor = max(0, nuevo_valor)
        
        self.datos_tiempo_real.append(nuevo_valor)
        if len(self.datos_tiempo_real) > 50:
            self.datos_tiempo_real.pop(0)
        
        # Variar ligeramente las ventas mensuales
        for i in range(len(self.ventas_mensuales)):
            variacion = np.random.normal(0, 2)
            self.ventas_mensuales[i] = max(50, self.ventas_mensuales[i] + variacion)
        
        self.tiempo_actual += 1
    
    def toggle_actualizacion(self):
        """Activa/desactiva la actualización automática"""
        self.actualizacion_activa = not self.actualizacion_activa
        
        if self.actualizacion_activa:
            self.btn_toggle.config(text="Detener")
            self.actualizar_automaticamente()
        else:
            self.btn_toggle.config(text="Iniciar")
    
    def actualizar_automaticamente(self):
        """Actualiza el dashboard automáticamente"""
        if self.actualizacion_activa:
            self.simular_datos_tiempo_real()
            self.actualizar_graficos()
            
            # Programar la próxima actualización
            self.root.after(self.intervalo_actualizacion, self.actualizar_automaticamente)
    
    def cambiar_intervalo(self, event):
        """Cambia el intervalo de actualización"""
        intervalo_segundos = float(self.combo_intervalo.get())
        self.intervalo_actualizacion = int(intervalo_segundos * 1000)

def main():
    """Función principal"""
    print("Iniciando Dashboard Interactivo...")
    print("Características del dashboard:")
    print("- 6 tipos diferentes de gráficos")
    print("- Actualización en tiempo real")
    print("- Controles interactivos")
    print("- Estadísticas en vivo")
    print("- Interfaz moderna con tkinter")
    
    # Crear ventana principal
    root = tk.Tk()
    
    # Crear el dashboard
    dashboard = DashboardInteractivo(root)
    
    # Centrar la ventana
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    print("\n✅ Dashboard iniciado correctamente!")
    print("Uso:")
    print("- Haz clic en 'Iniciar' para activar actualización automática")
    print("- Cambia el intervalo de actualización con el combobox")
    print("- Observa cómo los datos se actualizan en tiempo real")
    print("- Las estadísticas se muestran en la parte inferior")
    
    # Ejecutar la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()
