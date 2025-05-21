"""
Ejercicio 8: Sistema de Manejo de Errores Centralizado

Objetivo: Implementar un sistema centralizado de manejo de errores para una aplicación.

Instrucciones:
1. Crea un sistema que capture, clasifique y maneje diferentes tipos de errores.
2. Implementa diferentes estrategias de manejo según el tipo y la severidad del error.
3. Incluye opciones como reintentos, notificaciones, y recuperación automática.
"""

import logging
import traceback
import sys
import time
import random
from enum import Enum, auto
from typing import Dict, Any, Optional, List, Callable, Tuple, Type
import datetime
import functools

# Configuración del sistema de logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('sistema_errores.log', encoding='utf-8')
    ]
)

# Crear el logger para este módulo
logger = logging.getLogger('sistema_errores')

# Definir tipos de errores y severidades
class SeveridadError(Enum):
    """Niveles de severidad para los errores."""
    INFORMATIVO = auto()  # No crítico, solo informativo
    BAJO = auto()        # Error menor, puede ignorarse
    MEDIO = auto()       # Error que requiere atención pero no es crítico
    ALTO = auto()        # Error crítico que debe ser atendido
    CRITICO = auto()     # Error que detiene el sistema

class TipoError(Enum):
    """Categorías generales de errores."""
    VALIDACION = auto()   # Errores en la validación de datos
    SISTEMA = auto()      # Errores del sistema operativo
    RED = auto()          # Errores de red y comunicación
    BASE_DATOS = auto()   # Errores de base de datos
    AUTENTICACION = auto()  # Errores de autenticación y autorización
    NEGOCIO = auto()      # Errores de lógica de negocio
    DESCONOCIDO = auto()   # Errores que no se ajustan a otras categorías

# Clase para representar errores específicos de la aplicación
class AppError(Exception):
    """Clase base para errores personalizados de la aplicación."""
    
    def __init__(self, 
                 mensaje: str,
                 tipo: TipoError = TipoError.DESCONOCIDO,
                 severidad: SeveridadError = SeveridadError.MEDIO,
                 error_original: Optional[Exception] = None,
                 datos_contexto: Optional[Dict[str, Any]] = None,
                 codigo_error: Optional[str] = None):
        """
        Inicializa un error de la aplicación.
        
        Args:
            mensaje: Mensaje descriptivo del error
            tipo: Tipo de error (categoría)
            severidad: Nivel de severidad
            error_original: Excepción original que causó este error
            datos_contexto: Datos adicionales sobre el contexto del error
            codigo_error: Código único para identificar este tipo de error
        """
        self.mensaje = mensaje
        self.tipo = tipo
        self.severidad = severidad
        self.error_original = error_original
        self.datos_contexto = datos_contexto or {}
        self.codigo_error = codigo_error
        self.timestamp = datetime.datetime.now()
        
        # Construir el mensaje completo
        mensaje_completo = f"[{self.codigo_error or 'SIN_CODIGO'}] {mensaje}"
        if error_original:
            mensaje_completo += f" Causado por: {type(error_original).__name__}: {error_original}"
        
        super().__init__(mensaje_completo)

# Clases específicas para diferentes tipos de errores
class ErrorValidacion(AppError):
    """Errores relacionados con la validación de datos."""
    
    def __init__(self, mensaje, **kwargs):
        kwargs.setdefault('tipo', TipoError.VALIDACION)
        kwargs.setdefault('severidad', SeveridadError.BAJO)
        kwargs.setdefault('codigo_error', 'VAL')
        super().__init__(mensaje, **kwargs)

class ErrorSistema(AppError):
    """Errores relacionados con el sistema operativo o entorno."""
    
    def __init__(self, mensaje, **kwargs):
        kwargs.setdefault('tipo', TipoError.SISTEMA)
        kwargs.setdefault('severidad', SeveridadError.ALTO)
        kwargs.setdefault('codigo_error', 'SYS')
        super().__init__(mensaje, **kwargs)

class ErrorRed(AppError):
    """Errores relacionados con la red y comunicaciones."""
    
    def __init__(self, mensaje, **kwargs):
        kwargs.setdefault('tipo', TipoError.RED)
        kwargs.setdefault('severidad', SeveridadError.MEDIO)
        kwargs.setdefault('codigo_error', 'NET')
        super().__init__(mensaje, **kwargs)

class ErrorBaseDatos(AppError):
    """Errores relacionados con operaciones de base de datos."""
    
    def __init__(self, mensaje, **kwargs):
        kwargs.setdefault('tipo', TipoError.BASE_DATOS)
        kwargs.setdefault('severidad', SeveridadError.ALTO)
        kwargs.setdefault('codigo_error', 'DB')
        super().__init__(mensaje, **kwargs)

class ErrorAutenticacion(AppError):
    """Errores relacionados con autenticación y autorización."""
    
    def __init__(self, mensaje, **kwargs):
        kwargs.setdefault('tipo', TipoError.AUTENTICACION)
        kwargs.setdefault('severidad', SeveridadError.ALTO)
        kwargs.setdefault('codigo_error', 'AUTH')
        super().__init__(mensaje, **kwargs)

class ErrorNegocio(AppError):
    """Errores relacionados con la lógica de negocio."""
    
    def __init__(self, mensaje, **kwargs):
        kwargs.setdefault('tipo', TipoError.NEGOCIO)
        kwargs.setdefault('severidad', SeveridadError.MEDIO)
        kwargs.setdefault('codigo_error', 'BIZ')
        super().__init__(mensaje, **kwargs)

# Sistema centralizado de manejo de errores
class GestorErrores:
    """
    Sistema centralizado para gestionar todos los errores de la aplicación.
    Implementa el patrón Singleton para garantizar una única instancia.
    """
    _instancia = None  # Instancia única para el patrón Singleton
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(GestorErrores, cls).__new__(cls)
            cls._instancia._inicializado = False
        return cls._instancia
    
    def __init__(self):
        # Evitar reinicialización en el patrón Singleton
        if self._inicializado:
            return
        
        # Configuración del gestor
        self.notificaciones_activas = True
        self.nivel_log = logging.INFO
        self.max_reintentos = 3
        self.logger = logger
        
        # Manejadores registrados para diferentes tipos de errores
        # Formato: {TipoError: [funciones_manejadoras]}
        self.manejadores: Dict[TipoError, List[Callable]] = {
            tipo: [] for tipo in TipoError
        }
        
        # Estrategias de recuperación
        self.estrategia_reintento = self._estrategia_reintento_exponencial
        self.estrategia_recuperacion = {}
        
        self._inicializado = True
    
    def registrar_manejador(self, tipo_error: TipoError, manejador: Callable):
        """
        Registra un manejador para un tipo específico de error.
        
        Args:
            tipo_error: El tipo de error a manejar
            manejador: Función que maneja el error, debe aceptar un AppError como argumento
        """
        self.manejadores[tipo_error].append(manejador)
        self.logger.debug(f"Registrado manejador para {tipo_error.name}: {manejador.__name__}")
    
    def registrar_estrategia_recuperacion(self, tipo_error: TipoError, estrategia: Callable):
        """
        Registra una estrategia de recuperación para un tipo específico de error.
        
        Args:
            tipo_error: El tipo de error a manejar
            estrategia: Función que intenta recuperarse del error, debe aceptar un AppError y
                       los argumentos de la función original
        """
        self.estrategia_recuperacion[tipo_error] = estrategia
        self.logger.debug(f"Registrada estrategia de recuperación para {tipo_error.name}: {estrategia.__name__}")
    
    def manejar_error(self, error: AppError) -> bool:
        """
        Maneja un error específico según su tipo y severidad.
        
        Args:
            error: El error a manejar
            
        Returns:
            bool: True si el error fue manejado, False en caso contrario
        """
        # Registrar el error
        self._registrar_error(error)
        
        # Notificar si es necesario
        if self.notificaciones_activas and error.severidad in [SeveridadError.ALTO, SeveridadError.CRITICO]:
            self._notificar_error(error)
        
        # Ejecutar manejadores específicos para el tipo de error
        manejado = False
        for manejador in self.manejadores[error.tipo]:
            try:
                resultado = manejador(error)
                if resultado:
                    manejado = True
            except Exception as e:
                self.logger.error(f"Error en manejador {manejador.__name__}: {e}")
        
        return manejado
    
    def _registrar_error(self, error: AppError):
        """
        Registra un error en el log según su severidad.
        
        Args:
            error: El error a registrar
        """
        # Obtener el nivel de log según la severidad del error
        nivel_log = {
            SeveridadError.INFORMATIVO: logging.INFO,
            SeveridadError.BAJO: logging.WARNING,
            SeveridadError.MEDIO: logging.WARNING,
            SeveridadError.ALTO: logging.ERROR,
            SeveridadError.CRITICO: logging.CRITICAL
        }.get(error.severidad, logging.ERROR)
        
        # Construir el mensaje de log
        mensaje = f"{error.tipo.name} - {error.mensaje}"
        
        # Agregar datos de contexto si existen
        if error.datos_contexto:
            mensaje += f" - Contexto: {error.datos_contexto}"
        
        # Agregar traceback si hay un error original
        if error.error_original:
            tb = "".join(traceback.format_exception(
                type(error.error_original),
                error.error_original,
                error.error_original.__traceback__
            ))
            mensaje += f"\nError original: {tb}"
        
        # Registrar el mensaje
        self.logger.log(nivel_log, mensaje)
    
    def _notificar_error(self, error: AppError):
        """
        Envía una notificación sobre un error crítico.
        En un sistema real, esto podría enviar emails, SMS, etc.
        
        Args:
            error: El error a notificar
        """
        self.logger.critical(
            f"NOTIFICACIÓN: Error {error.severidad.name} detectado: "
            f"[{error.codigo_error}] {error.mensaje}"
        )
        
        # Aquí se implementaría el código para enviar notificaciones reales
        # (email, SMS, webhook, etc.)
    
    def _estrategia_reintento_exponencial(self, intento: int) -> float:
        """
        Estrategia de reintento con backoff exponencial.
        
        Args:
            intento: Número de intento actual (empezando desde 1)
            
        Returns:
            float: Tiempo de espera en segundos antes del siguiente reintento
        """
        # Backoff exponencial con jitter aleatorio
        tiempo_base = min(30, 2 ** intento)  # Limitar a 30 segundos máximo
        jitter = random.uniform(0, 0.5 * tiempo_base)
        return tiempo_base + jitter
    
    def with_error_handling(self, *,
                           reintentos: bool = True,
                           tipos_reintentables: Optional[List[TipoError]] = None,
                           max_reintentos: Optional[int] = None,
                           valor_por_defecto: Any = None):
        """
        Decorador para funciones que pueden generar errores.
        Maneja automáticamente los errores usando el gestor centralizado.
        
        Args:
            reintentos: Si debe reintentar operaciones fallidas
            tipos_reintentables: Tipos de errores que se pueden reintentar
            max_reintentos: Número máximo de reintentos
            valor_por_defecto: Valor a devolver en caso de error no recuperable
        """
        # Tipos por defecto para reintentar
        if tipos_reintentables is None:
            tipos_reintentables = [TipoError.RED, TipoError.BASE_DATOS]
        
        # Usar el máximo de reintentos configurado si no se especifica
        if max_reintentos is None:
            max_reintentos = self.max_reintentos
            
        def decorador(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                ultimo_error = None
                
                # Intentar la operación con reintentos si es necesario
                for intento in range(1, max_reintentos + 1 if reintentos else 2):
                    try:
                        return func(*args, **kwargs)
                    except AppError as e:
                        ultimo_error = e
                        self.manejar_error(e)
                        
                        # Verificar si podemos reintentar
                        puede_reintentar = (
                            reintentos and 
                            intento < max_reintentos and
                            e.tipo in tipos_reintentables
                        )
                        
                        if puede_reintentar:
                            # Calcular tiempo de espera y reintentar
                            espera = self.estrategia_reintento(intento)
                            self.logger.info(
                                f"Reintentando {func.__name__} en {espera:.2f} segundos "
                                f"(intento {intento}/{max_reintentos})"
                            )
                            time.sleep(espera)
                        else:
                            # No se puede reintentar, intentar recuperación
                            if e.tipo in self.estrategia_recuperacion:
                                try:
                                    return self.estrategia_recuperacion[e.tipo](e, *args, **kwargs)
                                except Exception as e_rec:
                                    self.logger.error(f"Error en estrategia de recuperación: {e_rec}")
                            break
                    except Exception as e:
                        # Convertir a AppError para manejo estándar
                        app_error = self._convertir_a_app_error(e, func.__name__)
                        ultimo_error = app_error
                        self.manejar_error(app_error)
                        
                        # No reintentar excepciones no controladas
                        break
                
                # Si llegamos aquí, todas las operaciones fallaron
                return valor_por_defecto
            
            return wrapper
        
        return decorador
    
    def _convertir_a_app_error(self, error: Exception, contexto: str) -> AppError:
        """
        Convierte una excepción estándar en un AppError.
        
        Args:
            error: Excepción a convertir
            contexto: Información adicional sobre dónde ocurrió
            
        Returns:
            AppError: La excepción convertida
        """
        # Mapeo de tipos de excepciones estándar a nuestros tipos
        mapeo_errores = {
            ValueError: ErrorValidacion,
            TypeError: ErrorValidacion,
            KeyError: ErrorValidacion,
            IndexError: ErrorValidacion,
            FileNotFoundError: ErrorSistema,
            PermissionError: ErrorSistema,
            OSError: ErrorSistema,
            ConnectionError: ErrorRed,
            TimeoutError: ErrorRed
        }
        
        # Buscar el tipo de AppError más adecuado
        for tipo_exception, tipo_app_error in mapeo_errores.items():
            if isinstance(error, tipo_exception):
                return tipo_app_error(
                    f"Error en {contexto}: {error}",
                    error_original=error,
                    datos_contexto={"contexto": contexto}
                )
        
        # Si no coincide con ninguno, es un error desconocido
        return AppError(
            f"Error no clasificado en {contexto}: {error}",
            tipo=TipoError.DESCONOCIDO,
            severidad=SeveridadError.MEDIO,
            error_original=error,
            datos_contexto={"contexto": contexto}
        )

# Ejemplos de uso del sistema
def ejemplo_funcion_validacion(edad):
    """Función de ejemplo que valida una edad."""
    if not isinstance(edad, int):
        raise ErrorValidacion(
            "La edad debe ser un número entero",
            datos_contexto={"valor_recibido": edad, "tipo": type(edad).__name__}
        )
    
    if edad < 0 or edad > 120:
        raise ErrorValidacion(
            "La edad debe estar entre 0 y 120",
            datos_contexto={"valor_recibido": edad}
        )
    
    return f"La edad {edad} es válida"

def ejemplo_funcion_bd():
    """Función de ejemplo que simula una operación de base de datos."""
    # Simular un error aleatorio
    if random.random() < 0.7:
        raise ErrorBaseDatos(
            "Error al conectar con la base de datos",
            datos_contexto={"servidor": "db.ejemplo.com", "puerto": 5432},
            severidad=SeveridadError.ALTO
        )
    
    return "Conexión exitosa a la base de datos"

def ejemplo_funcion_red():
    """Función de ejemplo que simula una operación de red."""
    # Simular un error aleatorio
    if random.random() < 0.7:
        # Simular un error de conexión rechazada
        try:
            # Simular una excepción interna
            raise ConnectionRefusedError("Conexión rechazada por el servidor")
        except ConnectionRefusedError as e:
            raise ErrorRed(
                "No se pudo conectar al servidor API",
                error_original=e,
                datos_contexto={"url": "https://api.ejemplo.com/datos"}
            )
    
    return "Datos obtenidos correctamente de la API"

# Configuración del sistema y manejadores específicos
def configurar_sistema_errores():
    """Configura el sistema de manejo de errores con manejadores específicos."""
    gestor = GestorErrores()
    
    # Registrar manejadores específicos
    gestor.registrar_manejador(TipoError.VALIDACION, lambda e: print(f"VALIDACIÓN: {e.mensaje}"))
    gestor.registrar_manejador(TipoError.BASE_DATOS, lambda e: print(f"BASE DE DATOS: Reintentando conexión..."))
    gestor.registrar_manejador(TipoError.RED, lambda e: print(f"RED: Verificando conectividad..."))
    
    # Registrar estrategias de recuperación
    gestor.registrar_estrategia_recuperacion(
        TipoError.BASE_DATOS,
        lambda e, *args, **kwargs: "Usando datos en caché mientras se resuelve el problema"
    )
    
    return gestor

# Función principal para demostración
def main():
    # Configurar el sistema de manejo de errores
    gestor = configurar_sistema_errores()
    
    print("=== SISTEMA DE MANEJO DE ERRORES CENTRALIZADO ===\n")
    
    # Decorador para manejo automático de errores
    validar_edad_segura = gestor.with_error_handling()(ejemplo_funcion_validacion)
    conectar_bd_segura = gestor.with_error_handling(
        reintentos=True, 
        max_reintentos=3,
        valor_por_defecto="Usando modo sin conexión"
    )(ejemplo_funcion_bd)
    
    llamar_api_segura = gestor.with_error_handling(
        reintentos=True,
        tipos_reintentables=[TipoError.RED],
        max_reintentos=2
    )(ejemplo_funcion_red)
    
    # Ejemplo 1: Validación
    print("=== Ejemplo 1: Validación de datos ===")
    print(validar_edad_segura(25))     # Valor válido
    print(validar_edad_segura("30"))   # Tipo inválido
    print(validar_edad_segura(150))    # Valor fuera de rango
    
    print("\n=== Ejemplo 2: Operación de base de datos (con reintentos) ===")
    print(f"Resultado: {conectar_bd_segura()}")
    
    print("\n=== Ejemplo 3: Operación de red (con reintentos) ===")
    print(f"Resultado: {llamar_api_segura()}")
    
    print("\n=== Ejemplo 4: Manejo manual de error ===")
    try:
        # Crear y lanzar un error de autenticación
        raise ErrorAutenticacion(
            "Credenciales inválidas",
            severidad=SeveridadError.ALTO,
            datos_contexto={"usuario": "usuario123", "intento": 3}
        )
    except AppError as e:
        # Manejar el error con el gestor
        gestor.manejar_error(e)
        print("Error de autenticación manejado correctamente")

if __name__ == "__main__":
    main()
