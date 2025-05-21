"""
Ejercicio 4: Monitoreo y Registro de Excepciones

Objetivo: Implementar un sistema completo de monitoreo y registro de excepciones.

Instrucciones:
1. Crea un decorador para registrar excepciones en funciones.
2. Implementa un sistema de registro configurable (consola, archivo, etc.).
3. Incluye información detallada: timestamp, traceback, contexto, etc.
"""

import functools
import traceback
import logging
import datetime
import sys
import os
from enum import Enum, auto

# Configuración del sistema de logging
class NivelLog(Enum):
    """Niveles de registro para nuestro sistema."""
    DEBUG = auto()
    INFO = auto()
    WARNING = auto()
    ERROR = auto()
    CRITICAL = auto()

class DestinoLog(Enum):
    """Posibles destinos para los registros."""
    CONSOLA = auto()
    ARCHIVO = auto()
    AMBOS = auto()

class RegistroExcepciones:
    """
    Sistema configurable para registro de excepciones.
    Permite registrar en consola, archivo o ambos.
    """
    _instancia = None  # Para patrón Singleton
    
    def __new__(cls, *args, **kwargs):
        """Implementa el patrón Singleton."""
        if cls._instancia is None:
            cls._instancia = super(RegistroExcepciones, cls).__new__(cls)
            cls._instancia._inicializado = False
        return cls._instancia
    
    def __init__(self, nivel=NivelLog.INFO, destino=DestinoLog.CONSOLA, 
                 ruta_archivo=None, formato=None):
        # Evitar reinicialización en el patrón Singleton
        if self._inicializado:
            return
        
        # Configurar el logger
        self.logger = logging.getLogger("monitor_excepciones")
        self.logger.setLevel(logging.DEBUG)  # El nivel más bajo para capturar todo
        
        # Limpiar handlers previos (importante en el Singleton)
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)
        
        # Mapeo de nuestros niveles a los de logging
        self.mapeo_niveles = {
            NivelLog.DEBUG: logging.DEBUG,
            NivelLog.INFO: logging.INFO,
            NivelLog.WARNING: logging.WARNING,
            NivelLog.ERROR: logging.ERROR,
            NivelLog.CRITICAL: logging.CRITICAL
        }
        
        # Formato por defecto si no se especifica otro
        if formato is None:
            formato = "%(asctime)s [%(levelname)s] %(message)s"
        
        self.formato = logging.Formatter(formato)
        self.nivel = nivel
        self.nivel_logging = self.mapeo_niveles[nivel]
        
        # Configurar los handlers según el destino seleccionado
        if destino in [DestinoLog.CONSOLA, DestinoLog.AMBOS]:
            self._configurar_consola()
            
        if destino in [DestinoLog.ARCHIVO, DestinoLog.AMBOS]:
            if ruta_archivo is None:
                # Usar directorio actual y nombre basado en fecha
                fecha_actual = datetime.datetime.now().strftime("%Y%m%d")
                ruta_archivo = f"excepciones_{fecha_actual}.log"
            
            self._configurar_archivo(ruta_archivo)
        
        self._inicializado = True
    
    def _configurar_consola(self):
        """Configura el registro en consola."""
        consola = logging.StreamHandler(sys.stdout)
        consola.setLevel(self.nivel_logging)
        consola.setFormatter(self.formato)
        self.logger.addHandler(consola)
    
    def _configurar_archivo(self, ruta_archivo):
        """Configura el registro en archivo."""
        # Asegurar que el directorio existe
        directorio = os.path.dirname(ruta_archivo)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)
            
        archivo = logging.FileHandler(ruta_archivo, encoding="utf-8")
        archivo.setLevel(self.nivel_logging)
        archivo.setFormatter(self.formato)
        self.logger.addHandler(archivo)
    
    def registrar_excepcion(self, excepcion, nivel=None, contexto=None):
        """
        Registra una excepción con la información detallada.
        
        Args:
            excepcion: La excepción a registrar
            nivel: Nivel de severidad (opcional)
            contexto: Información adicional sobre el contexto (opcional)
        """
        if nivel is None:
            nivel = self.nivel
        
        nivel_logging = self.mapeo_niveles[nivel]
        
        # Generar mensaje base
        tipo_exc = type(excepcion).__name__
        mensaje = f"Excepción: {tipo_exc}: {excepcion}"
        
        # Agregar contexto si se proporcionó
        if contexto:
            mensaje += f"\nContexto: {contexto}"
        
        # Agregar traceback
        tb_string = "".join(traceback.format_tb(excepcion.__traceback__))
        mensaje += f"\nTraceback:\n{tb_string}"
        
        # Registrar según el nivel especificado
        self.logger.log(nivel_logging, mensaje)


# Decorador para monitorear excepciones en funciones
def monitorear_excepciones(funcion=None, *, nivel=None, registrar_args=False):
    """
    Decorador para registrar automáticamente excepciones en funciones.
    
    Args:
        funcion: La función a decorar
        nivel: Nivel de registro (opcional)
        registrar_args: Si True, registra los argumentos de la función (opcional)
    """
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Recopilar información de contexto
                contexto = {
                    "funcion": func.__name__,
                    "modulo": func.__module__
                }
                
                # Agregar argumentos si se solicitó
                if registrar_args:
                    # Limita los argumentos para evitar registros muy grandes
                    str_args = [str(arg)[:100] for arg in args]
                    str_kwargs = {k: str(v)[:100] for k, v in kwargs.items()}
                    contexto["args"] = str_args
                    contexto["kwargs"] = str_kwargs
                
                # Registrar la excepción
                registro = RegistroExcepciones()
                registro.registrar_excepcion(
                    e, 
                    nivel=nivel or NivelLog.ERROR,
                    contexto=contexto
                )
                
                # Re-lanzar la excepción para que pueda ser manejada externamente
                raise
                
        return wrapper
    
    # Permitir usar el decorador con o sin paréntesis
    if funcion is None:
        return decorador
    else:
        return decorador(funcion)


# Ejemplos de uso
@monitorear_excepciones
def funcion_simple_con_error():
    """Función simple que siempre falla."""
    return 1 / 0

@monitorear_excepciones(nivel=NivelLog.CRITICAL, registrar_args=True)
def procesar_datos(datos, multiplicador):
    """Procesa datos con un multiplicador."""
    if not datos:
        raise ValueError("Los datos no pueden estar vacíos")
    
    resultado = [item * multiplicador for item in datos]
    
    return resultado

def main():
    # Configurar el sistema de registro
    registro = RegistroExcepciones(
        nivel=NivelLog.DEBUG,
        destino=DestinoLog.AMBOS,
        ruta_archivo="monitor_excepciones.log"
    )
    
    print("=== Demostración del Sistema de Monitoreo de Excepciones ===")
    print("Las excepciones se registrarán en consola y en 'monitor_excepciones.log'")
    
    # Ejemplo 1: Error simple
    try:
        print("\n1. Llamando a función simple que falla:")
        funcion_simple_con_error()
    except Exception as e:
        print(f"  Error capturado en main(): {e}")
    
    # Ejemplo 2: Error con argumentos
    try:
        print("\n2. Llamando a función de procesamiento con datos vacíos:")
        procesar_datos([], 10)
    except Exception as e:
        print(f"  Error capturado en main(): {e}")
    
    # Ejemplo 3: Registrar una excepción manualmente
    try:
        print("\n3. Generando y registrando una excepción manualmente:")
        lista = [1, 2, 3]
        elemento = lista[10]  # Esto provocará IndexError
    except Exception as e:
        registro.registrar_excepcion(
            e,
            nivel=NivelLog.WARNING,
            contexto={"operacion": "acceso a lista", "indice": 10}
        )
        print(f"  Error registrado manualmente: {e}")

if __name__ == "__main__":
    main()
