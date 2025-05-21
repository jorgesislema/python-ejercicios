"""
Ejercicio 2: Gestión de Excepciones con Contexto

Objetivo: Implementar un Context Manager personalizado para manejar recursos y excepciones.

Instrucciones:
1. Crea una clase que actúe como Context Manager para un archivo de registro (log).
2. La clase debe abrir el archivo al entrar en el contexto y cerrarlo al salir.
3. Debe registrar todas las excepciones que ocurran dentro del contexto.
4. Implementa también una versión usando el decorador @contextmanager.
"""

import datetime
import traceback
from contextlib import contextmanager

class RegistroContextManager:
    """
    Context Manager para gestionar un archivo de registro (log).
    Registra eventos y excepciones que ocurren dentro del contexto.
    """
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.archivo = None
    
    def __enter__(self):
        """Método que se ejecuta al entrar en el contexto 'with'."""
        self.archivo = open(self.nombre_archivo, 'a', encoding='utf-8')
        self.registrar_evento("INICIO", "Inicio del contexto")
        return self  # Devuelve el objeto Context Manager para usar dentro del bloque with
    
    def __exit__(self, tipo_exc, valor_exc, traceback_exc):
        """
        Método que se ejecuta al salir del contexto 'with'.
        
        Args:
            tipo_exc: Tipo de excepción que ocurrió (o None si no hubo excepción)
            valor_exc: Valor de la excepción (o None)
            traceback_exc: Traceback de la excepción (o None)
        
        Returns:
            bool: True para suprimir la excepción, False para propagarla
        """
        if tipo_exc is not None:
            # Si ocurrió una excepción, registrarla
            self.registrar_excepcion(tipo_exc, valor_exc, traceback_exc)
        
        self.registrar_evento("FIN", "Fin del contexto")
        
        if self.archivo:
            self.archivo.close()
        
        # Devolver False significa que no suprimimos la excepción (se propaga)
        return False
    
    def registrar_evento(self, tipo, mensaje):
        """Registra un evento en el archivo de log."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.archivo.write(f"[{timestamp}] {tipo}: {mensaje}\n")
        self.archivo.flush()  # Asegurar que se escriba inmediatamente
    
    def registrar_excepcion(self, tipo_exc, valor_exc, traceback_exc):
        """Registra una excepción en el archivo de log."""
        self.registrar_evento("EXCEPCIÓN", f"{tipo_exc.__name__}: {valor_exc}")
        
        # Registrar el traceback completo
        if traceback_exc:
            lineas_traceback = traceback.format_tb(traceback_exc)
            self.archivo.write("Traceback:\n")
            for linea in lineas_traceback:
                self.archivo.write(f"  {linea}")
            self.archivo.flush()


# Versión alternativa usando el decorador @contextmanager
@contextmanager
def registro_context(nombre_archivo):
    """
    Context Manager para gestionar un archivo de registro usando decorador.
    Similar a RegistroContextManager pero implementado como generador.
    """
    archivo = None
    try:
        archivo = open(nombre_archivo, 'a', encoding='utf-8')
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo.write(f"[{timestamp}] INICIO: Inicio del contexto\n")
        archivo.flush()
        
        yield archivo  # Ceder el control al bloque with
        
    except Exception as e:
        # Capturar cualquier excepción que ocurra
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo.write(f"[{timestamp}] EXCEPCIÓN: {type(e).__name__}: {e}\n")
        
        # Registrar el traceback
        tb_lines = traceback.format_exc().splitlines()
        archivo.write("Traceback:\n")
        for line in tb_lines:
            archivo.write(f"  {line}\n")
        archivo.flush()
        
        # Re-lanzar la excepción para que pueda ser manejada fuera
        raise
    
    finally:
        # Este bloque se ejecuta siempre, haya o no excepción
        if archivo:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            archivo.write(f"[{timestamp}] FIN: Fin del contexto\n")
            archivo.close()


def probar_clase_context_manager():
    """Función para probar la clase RegistroContextManager."""
    print("=== Probando clase RegistroContextManager ===")
    
    try:
        with RegistroContextManager("registro_clase.log") as registro:
            print("Dentro del bloque with usando la clase...")
            registro.registrar_evento("INFO", "Realizando algunas operaciones...")
            
            # Simular una operación
            print("Realizando operación 1: Éxito")
            registro.registrar_evento("OPERACIÓN", "Operación 1 completada")
            
            # Provocar un error
            print("Intentando operación 2: División por cero...")
            resultado = 1 / 0  # Esto lanzará ZeroDivisionError
            
    except ZeroDivisionError:
        print("Error capturado fuera del contexto: División por cero")
    
    print("Comprueba el archivo 'registro_clase.log' para ver el registro")


def probar_decorador_context_manager():
    """Función para probar el decorador @contextmanager."""
    print("\n=== Probando decorador @contextmanager ===")
    
    try:
        with registro_context("registro_decorador.log") as archivo:
            print("Dentro del bloque with usando el decorador...")
            
            # Simular algunas operaciones
            archivo.write("Realizando algunas operaciones...\n")
            print("Realizando operación 1: Éxito")
            
            # Provocar un error
            print("Intentando operación 2: Acceso a índice inválido...")
            lista = [1, 2, 3]
            elemento = lista[10]  # Esto lanzará IndexError
            
    except IndexError:
        print("Error capturado fuera del contexto: Índice fuera de rango")
    
    print("Comprueba el archivo 'registro_decorador.log' para ver el registro")


def main():
    probar_clase_context_manager()
    probar_decorador_context_manager()


if __name__ == "__main__":
    main()
