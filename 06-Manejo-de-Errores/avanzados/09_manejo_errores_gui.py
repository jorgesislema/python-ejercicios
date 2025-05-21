"""
Ejercicio 9: Manejo de Errores en Interfaces Gráficas

Objetivo: Implementar un sistema de manejo de errores para aplicaciones GUI con Tkinter.

Instrucciones:
1. Crea una aplicación Tkinter simple con varios tipos de interacciones.
2. Implementa manejo de errores en diferentes capas (interfaz, lógica, datos).
3. Muestra mensajes de error amigables al usuario mientras registras detalles técnicos.
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import logging
import traceback
import sys
import datetime
import random
import threading
import time
import json
import os
from typing import Dict, Any, Optional, List, Callable, Union

# Configuración del sistema de logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('gui_application.log', encoding='utf-8'),
        # No usar StreamHandler en aplicaciones GUI
    ]
)

# Logger para este módulo
logger = logging.getLogger('gui_error_handler')

# Clase personalizada de excepción para la aplicación
class AppException(Exception):
    """Excepción base para errores de la aplicación."""
    
    def __init__(self, mensaje, detalle=None, error_original=None):
        self.mensaje = mensaje  # Mensaje amigable para el usuario
        self.detalle = detalle  # Detalles técnicos para el log
        self.error_original = error_original  # Excepción original
        self.timestamp = datetime.datetime.now()
        
        # Mensaje para la excepción
        mensaje_completo = mensaje
        if detalle:
            mensaje_completo += f" ({detalle})"
        
        super().__init__(mensaje_completo)

class ErrorValidacion(AppException):
    """Error en la validación de datos de entrada."""
    pass

class ErrorProcesamiento(AppException):
    """Error en el procesamiento de datos."""
    pass

class ErrorArchivo(AppException):
    """Error en operaciones con archivos."""
    pass

class ErrorBaseDatos(AppException):
    """Error en operaciones de base de datos."""
    pass

class ErrorRed(AppException):
    """Error en operaciones de red."""
    pass

# Manejador de errores para la aplicación GUI
class ManejadorErroresGUI:
    """
    Clase para manejar errores en aplicaciones GUI.
    Combina presentación de errores al usuario con registro detallado.
    """
    
    def __init__(self, root=None):
        """
        Inicializa el manejador de errores.
        
        Args:
            root: La ventana raíz de la aplicación Tkinter
        """
        self.root = root
        self.logger = logger
        # Configuración por defecto
        self.mostrar_detalles = False
        self.registrar_acciones_usuario = True
        # Contadores para estadísticas
        self.contador_errores = {
            'validacion': 0,
            'procesamiento': 0,
            'archivo': 0,
            'basedatos': 0,
            'red': 0,
            'otro': 0
        }
    
    def registrar_error(self, error, nivel=logging.ERROR):
        """
        Registra un error en el log.
        
        Args:
            error: La excepción a registrar
            nivel: El nivel de logging a usar
        """
        # Construir mensaje para el log
        mensaje = f"ERROR: {error}"
        
        if isinstance(error, AppException):
            # Para nuestras excepciones propias, incluir detalles adicionales
            if error.detalle:
                mensaje += f"\nDetalle: {error.detalle}"
            
            if error.error_original:
                mensaje += f"\nError original: {error.error_original}"
                # Agregar traceback del error original
                if error.error_original.__traceback__:
                    tb_str = "".join(traceback.format_exception(
                        type(error.error_original),
                        error.error_original,
                        error.error_original.__traceback__
                    ))
                    mensaje += f"\nTraceback:\n{tb_str}"
        else:
            # Para excepciones estándar, incluir el traceback
            if error.__traceback__:
                tb_str = "".join(traceback.format_exception(
                    type(error),
                    error,
                    error.__traceback__
                ))
                mensaje += f"\nTraceback:\n{tb_str}"
        
        # Registrar en el logger
        self.logger.log(nivel, mensaje)
        
        # Actualizar estadísticas
        if isinstance(error, ErrorValidacion):
            self.contador_errores['validacion'] += 1
        elif isinstance(error, ErrorProcesamiento):
            self.contador_errores['procesamiento'] += 1
        elif isinstance(error, ErrorArchivo):
            self.contador_errores['archivo'] += 1
        elif isinstance(error, ErrorBaseDatos):
            self.contador_errores['basedatos'] += 1
        elif isinstance(error, ErrorRed):
            self.contador_errores['red'] += 1
        else:
            self.contador_errores['otro'] += 1
    
    def mostrar_error_usuario(self, error, titulo="Error"):
        """
        Muestra un diálogo de error al usuario.
        
        Args:
            error: La excepción a mostrar
            titulo: El título para la ventana de error
        """
        # Obtener mensaje para mostrar
        if isinstance(error, AppException):
            mensaje = error.mensaje
            detalle = error.detalle if self.mostrar_detalles else None
        else:
            mensaje = str(error)
            detalle = None
        
        # Mostrar diálogo apropiado
        if detalle:
            messagebox.showerror(titulo, f"{mensaje}\n\nDetalle técnico: {detalle}")
        else:
            messagebox.showerror(titulo, mensaje)
    
    def manejar_error(self, error, titulo="Error", nivel=logging.ERROR):
        """
        Maneja un error: lo registra y lo muestra al usuario.
        
        Args:
            error: La excepción a manejar
            titulo: El título para la ventana de error
            nivel: El nivel de logging a usar
        """
        # Registrar el error
        self.registrar_error(error, nivel)
        
        # Mostrar al usuario
        self.mostrar_error_usuario(error, titulo)
    
    def manejar_excepcion_no_esperada(self):
        """
        Maneja excepciones no esperadas de forma global.
        Esta función debe ser conectada al mecanismo de excepciones no manejadas.
        """
        def exception_handler(exc_type, exc_value, exc_traceback):
            # No manejar KeyboardInterrupt
            if issubclass(exc_type, KeyboardInterrupt):
                sys.__excepthook__(exc_type, exc_value, exc_traceback)
                return
            
            # Registrar el error
            self.logger.critical("Excepción no manejada:", exc_info=(exc_type, exc_value, exc_traceback))
            
            # Mostrar diálogo al usuario si la aplicación tiene interfaz
            if self.root and self.root.winfo_exists():
                mensaje = "Ha ocurrido un error inesperado en la aplicación."
                detalle = f"{exc_type.__name__}: {exc_value}"
                messagebox.showerror("Error Crítico", f"{mensaje}\n\nEl error ha sido registrado. " 
                                    f"Considere reiniciar la aplicación.\n\nDetalle: {detalle}")
        
        # Conectar al hook de excepciones no manejadas
        sys.excepthook = exception_handler
    
    def decorador_manejo_errores(self, mensaje_error="Ha ocurrido un error"):
        """
        Decorador para manejar errores en funciones de la aplicación.
        
        Args:
            mensaje_error: Mensaje a mostrar al usuario si ocurre un error
        """
        def decorador(func):
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except AppException as e:
                    # Para nuestras excepciones propias, usar el mensaje de la excepción
                    self.manejar_error(e)
                except Exception as e:
                    # Para otras excepciones, usar el mensaje genérico
                    app_error = AppException(mensaje_error, detalle=str(e), error_original=e)
                    self.manejar_error(app_error, "Error Inesperado", logging.ERROR)
                return None
            return wrapper
        return decorador

# Simulación de servicios para la aplicación
class ServicioArchivo:
    """Servicio para operaciones con archivos."""
    
    def guardar_datos(self, archivo, datos):
        """Guarda datos en un archivo."""
        try:
            # Simular error aleatorio
            if random.random() < 0.3:
                raise IOError("No se pudo escribir en el archivo")
            
            # Convertir datos a JSON si es un diccionario
            if isinstance(datos, dict):
                datos = json.dumps(datos, indent=4)
            
            with open(archivo, 'w', encoding='utf-8') as f:
                f.write(datos)
            
            return True
        except Exception as e:
            raise ErrorArchivo(
                f"No se pudo guardar el archivo '{archivo}'",
                detalle=f"Error al escribir datos: {e}",
                error_original=e
            )
    
    def cargar_datos(self, archivo):
        """Carga datos desde un archivo."""
        try:
            # Verificar si el archivo existe
            if not os.path.exists(archivo):
                raise FileNotFoundError(f"El archivo '{archivo}' no existe")
            
            # Simular error aleatorio
            if random.random() < 0.3:
                raise IOError("Error de lectura del archivo")
            
            with open(archivo, 'r', encoding='utf-8') as f:
                contenido = f.read()
            
            # Intentar parsear como JSON
            try:
                return json.loads(contenido)
            except json.JSONDecodeError:
                # Si no es JSON, devolver el contenido tal cual
                return contenido
        except Exception as e:
            raise ErrorArchivo(
                f"No se pudo leer el archivo '{archivo}'",
                detalle=f"Error de lectura: {e}",
                error_original=e
            )

class ServicioCalculadora:
    """Servicio para operaciones matemáticas."""
    
    def dividir(self, a, b):
        """Divide dos números."""
        try:
            # Validar que sean números
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise TypeError("Los valores deben ser números")
            
            # Validar que el divisor no sea cero
            if b == 0:
                raise ZeroDivisionError("No se puede dividir entre cero")
            
            return a / b
        except TypeError as e:
            raise ErrorValidacion(
                "Valores inválidos para división",
                detalle=str(e),
                error_original=e
            )
        except ZeroDivisionError as e:
            raise ErrorValidacion(
                "No se puede dividir entre cero",
                detalle="El segundo valor no puede ser cero",
                error_original=e
            )
        except Exception as e:
            raise ErrorProcesamiento(
                "Error al realizar la división",
                detalle=str(e),
                error_original=e
            )
    
    def calcular_raiz(self, numero):
        """Calcula la raíz cuadrada de un número."""
        try:
            # Validar que sea un número
            if not isinstance(numero, (int, float)):
                raise TypeError("El valor debe ser un número")
            
            # Validar que sea no negativo
            if numero < 0:
                raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
            
            # Simular procesamiento
            time.sleep(0.1)
            return numero ** 0.5
        except TypeError as e:
            raise ErrorValidacion(
                "Valor inválido para raíz cuadrada",
                detalle=str(e),
                error_original=e
            )
        except ValueError as e:
            raise ErrorValidacion(
                "No se puede calcular la raíz cuadrada de un número negativo",
                detalle=str(e),
                error_original=e
            )
        except Exception as e:
            raise ErrorProcesamiento(
                "Error al calcular la raíz cuadrada",
                detalle=str(e),
                error_original=e
            )

class ServicioAPI:
    """Servicio para operaciones con una API ficticia."""
    
    def obtener_datos(self, endpoint):
        """Simula una petición a una API."""
        try:
            # Simular retardo de red
            time.sleep(0.5)
            
            # Simular error aleatorio
            if random.random() < 0.4:
                error_tipo = random.choice(['timeout', 'conexion', '404', 'servidor'])
                
                if error_tipo == 'timeout':
                    raise TimeoutError("La petición ha excedido el tiempo máximo")
                elif error_tipo == 'conexion':
                    raise ConnectionError("No se pudo conectar al servidor")
                elif error_tipo == '404':
                    raise ValueError("Recurso no encontrado (404)")
                else:
                    raise Exception("Error interno del servidor (500)")
            
            # Datos simulados según el endpoint
            if endpoint == "usuarios":
                return [
                    {"id": 1, "nombre": "Ana", "rol": "admin"},
                    {"id": 2, "nombre": "Carlos", "rol": "usuario"},
                    {"id": 3, "nombre": "Elena", "rol": "moderador"}
                ]
            elif endpoint == "productos":
                return [
                    {"id": 101, "nombre": "Laptop", "precio": 1200},
                    {"id": 102, "nombre": "Monitor", "precio": 300},
                    {"id": 103, "nombre": "Teclado", "precio": 50}
                ]
            else:
                return {"mensaje": f"Endpoint '{endpoint}' no reconocido"}
        except TimeoutError as e:
            raise ErrorRed(
                "La petición ha tardado demasiado tiempo",
                detalle=f"Timeout al conectar a '{endpoint}'",
                error_original=e
            )
        except ConnectionError as e:
            raise ErrorRed(
                "No se pudo establecer conexión con el servidor",
                detalle=f"Error de conexión a '{endpoint}'",
                error_original=e
            )
        except ValueError as e:
            if "404" in str(e):
                raise ErrorRed(
                    f"El recurso '{endpoint}' no fue encontrado",
                    detalle="Error 404",
                    error_original=e
                )
            else:
                raise ErrorProcesamiento(
                    "Error en la petición",
                    detalle=str(e),
                    error_original=e
                )
        except Exception as e:
            raise ErrorRed(
                "Error al comunicarse con el servidor",
                detalle=str(e),
                error_original=e
            )

# Aplicación GUI con manejo de errores
class AplicacionGUI:
    """Aplicación GUI con manejo de errores integrado."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Manejo de Errores GUI")
        self.root.geometry("800x600")
        
        # Inicializar manejador de errores
        self.manejador_errores = ManejadorErroresGUI(root)
        self.manejador_errores.manejar_excepcion_no_esperada()
        
        # Inicializar servicios
        self.servicio_archivo = ServicioArchivo()
        self.servicio_calculadora = ServicioCalculadora()
        self.servicio_api = ServicioAPI()
        
        # Crear interfaz
        self._crear_interfaz()
        
        # Registrar inicio de la aplicación
        logger.info("Aplicación iniciada correctamente")
    
    def _crear_interfaz(self):
        """Crea la interfaz gráfica de la aplicación."""
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Pestaña 1: Calculadora
        tab_calculadora = ttk.Frame(notebook)
        notebook.add(tab_calculadora, text="Calculadora")
        self._crear_tab_calculadora(tab_calculadora)
        
        # Pestaña 2: Gestor de Archivos
        tab_archivos = ttk.Frame(notebook)
        notebook.add(tab_archivos, text="Gestor de Archivos")
        self._crear_tab_archivos(tab_archivos)
        
        # Pestaña 3: API Cliente
        tab_api = ttk.Frame(notebook)
        notebook.add(tab_api, text="API Cliente")
        self._crear_tab_api(tab_api)
        
        # Pestaña 4: Registro de Errores
        tab_log = ttk.Frame(notebook)
        notebook.add(tab_log, text="Registro de Errores")
        self._crear_tab_log(tab_log)
        
        # Barra de estado
        self.barra_estado = ttk.Label(self.root, text="Listo", relief=tk.SUNKEN, anchor=tk.W)
        self.barra_estado.pack(side=tk.BOTTOM, fill=tk.X)
    
    def _crear_tab_calculadora(self, tab):
        """Crea la interfaz de la calculadora."""
        frame = ttk.Frame(tab, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="Calculadora", font=("Arial", 14, "bold")).grid(
            column=0, row=0, columnspan=4, pady=10)
        
        # División
        ttk.Label(frame, text="División:").grid(column=0, row=1, sticky=tk.W, pady=5)
        
        self.div_num1 = ttk.Entry(frame, width=10)
        self.div_num1.grid(column=1, row=1, padx=5)
        
        ttk.Label(frame, text="÷").grid(column=2, row=1)
        
        self.div_num2 = ttk.Entry(frame, width=10)
        self.div_num2.grid(column=3, row=1, padx=5)
        
        ttk.Button(frame, text="Calcular", command=self._calcular_division).grid(
            column=4, row=1, padx=5)
        
        self.div_resultado = ttk.Label(frame, text="")
        self.div_resultado.grid(column=5, row=1, padx=5)
        
        # Raíz cuadrada
        ttk.Label(frame, text="Raíz Cuadrada:").grid(column=0, row=2, sticky=tk.W, pady=5)
        
        self.raiz_num = ttk.Entry(frame, width=10)
        self.raiz_num.grid(column=1, row=2, padx=5)
        
        ttk.Button(frame, text="Calcular", command=self._calcular_raiz).grid(
            column=4, row=2, padx=5)
        
        self.raiz_resultado = ttk.Label(frame, text="")
        self.raiz_resultado.grid(column=5, row=2, padx=5)
        
        # Botón para generar error
        ttk.Button(frame, text="Generar Error", command=self._generar_error_calculadora).grid(
            column=0, row=3, columnspan=2, pady=20)
        
        # Espaciado
        for child in frame.winfo_children():
            child.grid_configure(padx=5, pady=5)
    
    def _crear_tab_archivos(self, tab):
        """Crea la interfaz del gestor de archivos."""
        frame = ttk.Frame(tab, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="Gestor de Archivos", font=("Arial", 14, "bold")).grid(
            column=0, row=0, columnspan=3, pady=10)
        
        # Guardar archivo
        ttk.Label(frame, text="Guardar Texto:").grid(column=0, row=1, sticky=tk.W)
        
        self.guardar_texto = scrolledtext.ScrolledText(frame, width=40, height=5)
        self.guardar_texto.grid(column=0, row=2, columnspan=3, sticky=(tk.W, tk.E))
        
        ttk.Label(frame, text="Nombre Archivo:").grid(column=0, row=3, sticky=tk.W, pady=5)
        self.guardar_nombre = ttk.Entry(frame, width=30)
        self.guardar_nombre.grid(column=1, row=3, sticky=tk.W)
        
        ttk.Button(frame, text="Guardar", command=self._guardar_archivo).grid(
            column=2, row=3, sticky=tk.E, padx=5)
        
        # Cargar archivo
        ttk.Separator(frame, orient=tk.HORIZONTAL).grid(
            column=0, row=4, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        ttk.Label(frame, text="Cargar Archivo:").grid(column=0, row=5, sticky=tk.W)
        
        self.cargar_nombre = ttk.Entry(frame, width=30)
        self.cargar_nombre.grid(column=1, row=5, sticky=tk.W)
        
        ttk.Button(frame, text="Cargar", command=self._cargar_archivo).grid(
            column=2, row=5, sticky=tk.E, padx=5)
        
        ttk.Label(frame, text="Contenido:").grid(column=0, row=6, sticky=tk.W, pady=5)
        
        self.cargar_contenido = scrolledtext.ScrolledText(frame, width=40, height=5)
        self.cargar_contenido.grid(column=0, row=7, columnspan=3, sticky=(tk.W, tk.E))
        
        # Botón para generar error
        ttk.Button(frame, text="Generar Error", command=self._generar_error_archivo).grid(
            column=0, row=8, columnspan=2, pady=10)
        
        # Espaciado
        for child in frame.winfo_children():
            child.grid_configure(padx=5, pady=2)
        
        # Expandir columnas
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=2)
        frame.columnconfigure(2, weight=1)
    
    def _crear_tab_api(self, tab):
        """Crea la interfaz del cliente API."""
        frame = ttk.Frame(tab, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="Cliente API", font=("Arial", 14, "bold")).grid(
            column=0, row=0, columnspan=3, pady=10)
        
        # Selección de endpoint
        ttk.Label(frame, text="Endpoint:").grid(column=0, row=1, sticky=tk.W)
        
        self.api_endpoint = ttk.Combobox(frame, values=["usuarios", "productos", "configuracion"])
        self.api_endpoint.grid(column=1, row=1, sticky=(tk.W, tk.E))
        self.api_endpoint.current(0)
        
        ttk.Button(frame, text="Consultar", command=self._consultar_api).grid(
            column=2, row=1, sticky=tk.E, padx=5)
        
        # Resultados
        ttk.Label(frame, text="Resultados:").grid(column=0, row=2, sticky=tk.NW, pady=5)
        
        self.api_resultados = scrolledtext.ScrolledText(frame, width=50, height=10)
        self.api_resultados.grid(column=0, row=3, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Indicador de estado
        self.api_estado = ttk.Label(frame, text="Listo")
        self.api_estado.grid(column=0, row=4, sticky=tk.W, pady=5)
        
        # Botón para generar error
        ttk.Button(frame, text="Generar Error", command=self._generar_error_api).grid(
            column=2, row=4, sticky=tk.E, padx=5)
        
        # Espaciado
        for child in frame.winfo_children():
            child.grid_configure(padx=5, pady=3)
        
        # Expandir columnas y filas
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(3, weight=1)
    
    def _crear_tab_log(self, tab):
        """Crea la interfaz de registro de errores."""
        frame = ttk.Frame(tab, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="Registro de Errores", font=("Arial", 14, "bold")).grid(
            column=0, row=0, columnspan=2, pady=10)
        
        # Estadísticas de errores
        ttk.Label(frame, text="Estadísticas:").grid(column=0, row=1, sticky=tk.W)
        
        self.estadisticas_frame = ttk.LabelFrame(frame, text="Contadores de Errores")
        self.estadisticas_frame.grid(column=0, row=2, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Etiquetas para estadísticas
        self.stats_validacion = ttk.Label(self.estadisticas_frame, text="Validación: 0")
        self.stats_validacion.grid(column=0, row=0, padx=5, pady=2, sticky=tk.W)
        
        self.stats_procesamiento = ttk.Label(self.estadisticas_frame, text="Procesamiento: 0")
        self.stats_procesamiento.grid(column=1, row=0, padx=5, pady=2, sticky=tk.W)
        
        self.stats_archivo = ttk.Label(self.estadisticas_frame, text="Archivo: 0")
        self.stats_archivo.grid(column=0, row=1, padx=5, pady=2, sticky=tk.W)
        
        self.stats_basedatos = ttk.Label(self.estadisticas_frame, text="Base de Datos: 0")
        self.stats_basedatos.grid(column=1, row=1, padx=5, pady=2, sticky=tk.W)
        
        self.stats_red = ttk.Label(self.estadisticas_frame, text="Red: 0")
        self.stats_red.grid(column=0, row=2, padx=5, pady=2, sticky=tk.W)
        
        self.stats_otro = ttk.Label(self.estadisticas_frame, text="Otros: 0")
        self.stats_otro.grid(column=1, row=2, padx=5, pady=2, sticky=tk.W)
        
        # Opciones
        self.mostrar_detalles_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(frame, text="Mostrar detalles técnicos", 
                       variable=self.mostrar_detalles_var,
                       command=self._toggle_mostrar_detalles).grid(
            column=0, row=3, sticky=tk.W, pady=5)
        
        # Botón para actualizar estadísticas
        ttk.Button(frame, text="Actualizar Estadísticas", command=self._actualizar_estadisticas).grid(
            column=1, row=3, sticky=tk.E, pady=5)
        
        # Log viewer
        ttk.Label(frame, text="Últimas entradas del log:").grid(
            column=0, row=4, sticky=tk.W, pady=5)
        
        self.log_viewer = scrolledtext.ScrolledText(frame, width=60, height=12)
        self.log_viewer.grid(column=0, row=5, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Botón para cargar log
        ttk.Button(frame, text="Cargar Log", command=self._cargar_log).grid(
            column=0, row=6, columnspan=2, pady=10)
        
        # Espaciado
        for child in frame.winfo_children():
            child.grid_configure(padx=5, pady=3)
        
        # Expandir columnas y filas
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(5, weight=1)
        
        # Actualizar estadísticas al inicio
        self._actualizar_estadisticas()
    
    # Funciones de la calculadora
    @ManejadorErroresGUI.decorador_manejo_errores("Error al realizar la división")
    def _calcular_division(self):
        """Realiza la operación de división."""
        try:
            # Obtener valores
            num1 = float(self.div_num1.get())
            num2 = float(self.div_num2.get())
            
            # Calcular división
            resultado = self.servicio_calculadora.dividir(num1, num2)
            
            # Mostrar resultado
            self.div_resultado.config(text=f"= {resultado}")
            self.barra_estado.config(text=f"División calculada: {num1} / {num2} = {resultado}")
            
            # Registrar operación exitosa
            logger.info(f"División calculada: {num1} / {num2} = {resultado}")
            
        except ValueError:
            # Capturar error de conversión
            raise ErrorValidacion(
                "Por favor, ingresa solo números válidos",
                detalle="Error al convertir string a número"
            )
    
    @ManejadorErroresGUI.decorador_manejo_errores("Error al calcular la raíz cuadrada")
    def _calcular_raiz(self):
        """Calcula la raíz cuadrada de un número."""
        try:
            # Obtener valor
            num = float(self.raiz_num.get())
            
            # Calcular raíz cuadrada
            resultado = self.servicio_calculadora.calcular_raiz(num)
            
            # Mostrar resultado
            self.raiz_resultado.config(text=f"= {resultado}")
            self.barra_estado.config(text=f"Raíz calculada: √{num} = {resultado}")
            
            # Registrar operación exitosa
            logger.info(f"Raíz cuadrada calculada: √{num} = {resultado}")
            
        except ValueError:
            # Capturar error de conversión
            raise ErrorValidacion(
                "Por favor, ingresa un número válido",
                detalle="Error al convertir string a número"
            )
    
    def _generar_error_calculadora(self):
        """Genera un error deliberado en la calculadora."""
        try:
            # Generar un error de división por cero
            resultado = 1 / 0
        except Exception as e:
            self.manejador_errores.manejar_error(
                ErrorProcesamiento(
                    "Se generó un error deliberadamente",
                    detalle="División por cero",
                    error_original=e
                ),
                "Error Generado"
            )
    
    # Funciones del gestor de archivos
    @ManejadorErroresGUI.decorador_manejo_errores("Error al guardar el archivo")
    def _guardar_archivo(self):
        """Guarda el texto en un archivo."""
        # Obtener el nombre del archivo
        nombre_archivo = self.guardar_nombre.get().strip()
        if not nombre_archivo:
            raise ErrorValidacion(
                "Por favor, proporciona un nombre de archivo",
                detalle="Nombre de archivo vacío"
            )
        
        # Obtener el contenido
        contenido = self.guardar_texto.get("1.0", tk.END)
        
        # Guardar el archivo
        self.servicio_archivo.guardar_datos(nombre_archivo, contenido)
        
        # Actualizar estado
        self.barra_estado.config(text=f"Archivo guardado: {nombre_archivo}")
        messagebox.showinfo("Éxito", f"El archivo '{nombre_archivo}' se guardó correctamente")
        
        # Registrar operación exitosa
        logger.info(f"Archivo guardado: {nombre_archivo}")
    
    @ManejadorErroresGUI.decorador_manejo_errores("Error al cargar el archivo")
    def _cargar_archivo(self):
        """Carga un archivo y muestra su contenido."""
        # Obtener el nombre del archivo
        nombre_archivo = self.cargar_nombre.get().strip()
        if not nombre_archivo:
            raise ErrorValidacion(
                "Por favor, proporciona un nombre de archivo",
                detalle="Nombre de archivo vacío"
            )
        
        # Cargar el archivo
        contenido = self.servicio_archivo.cargar_datos(nombre_archivo)
        
        # Mostrar el contenido
        self.cargar_contenido.delete("1.0", tk.END)
        
        if isinstance(contenido, dict):
            # Si es un diccionario (JSON), formatearlo
            self.cargar_contenido.insert(tk.END, json.dumps(contenido, indent=4))
        else:
            # Si es texto, mostrarlo directamente
            self.cargar_contenido.insert(tk.END, contenido)
        
        # Actualizar estado
        self.barra_estado.config(text=f"Archivo cargado: {nombre_archivo}")
        
        # Registrar operación exitosa
        logger.info(f"Archivo cargado: {nombre_archivo}")
    
    def _generar_error_archivo(self):
        """Genera un error deliberado en el gestor de archivos."""
        try:
            # Intentar acceder a un archivo que no existe en una ubicación no accesible
            with open("/ruta_invalida/archivo_inexistente.txt", 'r') as f:
                contenido = f.read()
        except Exception as e:
            self.manejador_errores.manejar_error(
                ErrorArchivo(
                    "Se generó un error deliberadamente",
                    detalle="Intento de acceso a archivo inexistente",
                    error_original=e
                ),
                "Error Generado"
            )
    
    # Funciones del cliente API
    def _consultar_api(self):
        """Consulta la API simulada."""
        # Obtener el endpoint seleccionado
        endpoint = self.api_endpoint.get()
        
        # Actualizar estado
        self.api_estado.config(text="Consultando...")
        self.barra_estado.config(text=f"Consultando API: {endpoint}")
        self.root.update()  # Forzar actualización de la interfaz
        
        # Usar un hilo para no bloquear la interfaz
        def consultar_en_segundo_plano():
            try:
                # Consultar la API
                datos = self.servicio_api.obtener_datos(endpoint)
                
                # Mostrar resultados en la interfaz (desde el hilo principal)
                self.root.after(0, lambda: self._mostrar_resultados_api(datos, endpoint))
                
            except AppException as e:
                # Mostrar el error en la interfaz (desde el hilo principal)
                self.root.after(0, lambda: self._mostrar_error_api(e))
            except Exception as e:
                # Convertir a AppError y mostrar
                app_error = ErrorRed(
                    "Error inesperado al consultar la API",
                    detalle=str(e),
                    error_original=e
                )
                self.root.after(0, lambda: self._mostrar_error_api(app_error))
        
        # Iniciar el hilo
        hilo = threading.Thread(target=consultar_en_segundo_plano)
        hilo.daemon = True  # El hilo terminará cuando la aplicación termine
        hilo.start()
    
    def _mostrar_resultados_api(self, datos, endpoint):
        """Muestra los resultados de la consulta API."""
        # Limpiar el área de resultados
        self.api_resultados.delete("1.0", tk.END)
        
        # Mostrar los datos formateados
        self.api_resultados.insert(tk.END, json.dumps(datos, indent=4))
        
        # Actualizar estado
        self.api_estado.config(text="Consulta completada")
        self.barra_estado.config(text=f"API consultada correctamente: {endpoint}")
        
        # Registrar operación exitosa
        logger.info(f"API consultada correctamente: {endpoint}")
    
    def _mostrar_error_api(self, error):
        """Muestra un error de la API en la interfaz."""
        # Actualizar estado
        self.api_estado.config(text="Error en la consulta")
        
        # Manejar el error
        self.manejador_errores.manejar_error(error)
    
    def _generar_error_api(self):
        """Genera un error deliberado en el cliente API."""
        try:
            # Simular un timeout
            raise TimeoutError("Tiempo de espera excedido")
        except Exception as e:
            self.manejador_errores.manejar_error(
                ErrorRed(
                    "Se generó un error de red deliberadamente",
                    detalle="Timeout simulado",
                    error_original=e
                ),
                "Error Generado"
            )
    
    # Funciones de la pestaña de log
    def _toggle_mostrar_detalles(self):
        """Cambia la configuración para mostrar detalles técnicos."""
        valor = self.mostrar_detalles_var.get()
        self.manejador_errores.mostrar_detalles = valor
        logger.info(f"Configuración 'Mostrar detalles técnicos' cambiada a: {valor}")
    
    def _actualizar_estadisticas(self):
        """Actualiza las estadísticas de errores en la interfaz."""
        contadores = self.manejador_errores.contador_errores
        
        self.stats_validacion.config(text=f"Validación: {contadores['validacion']}")
        self.stats_procesamiento.config(text=f"Procesamiento: {contadores['procesamiento']}")
        self.stats_archivo.config(text=f"Archivo: {contadores['archivo']}")
        self.stats_basedatos.config(text=f"Base de Datos: {contadores['basedatos']}")
        self.stats_red.config(text=f"Red: {contadores['red']}")
        self.stats_otro.config(text=f"Otros: {contadores['otro']}")
    
    @ManejadorErroresGUI.decorador_manejo_errores("Error al cargar el archivo de log")
    def _cargar_log(self):
        """Carga y muestra el archivo de log."""
        try:
            # Intentar abrir el archivo de log
            with open('gui_application.log', 'r', encoding='utf-8') as f:
                # Leer las últimas 100 líneas
                lineas = f.readlines()[-100:]
                
                # Mostrar en el visor
                self.log_viewer.delete("1.0", tk.END)
                for linea in lineas:
                    self.log_viewer.insert(tk.END, linea)
                
                # Desplazar al final
                self.log_viewer.see(tk.END)
                
                # Actualizar estado
                self.barra_estado.config(text="Log cargado correctamente")
                
        except FileNotFoundError:
            raise ErrorArchivo(
                "No se encontró el archivo de log",
                detalle="El archivo 'gui_application.log' no existe"
            )
        except Exception as e:
            raise ErrorArchivo(
                "Error al leer el archivo de log",
                detalle=str(e),
                error_original=e
            )

# Función principal
def main():
    # Crear ventana principal
    root = tk.Tk()
    app = AplicacionGUI(root)
    
    # Iniciar el bucle principal
    root.mainloop()

if __name__ == "__main__":
    main()
