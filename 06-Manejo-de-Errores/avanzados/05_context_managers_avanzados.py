"""
Ejercicio 5: Uso Avanzado de Context Managers

Objetivo: Utilizar context managers para gestionar recursos avanzados y crear una API elegante.

Instrucciones:
1. Implementa un context manager para gestionar una conexión a una base de datos simulada.
2. Crea otro context manager para transacciones, que pueda hacer rollback si ocurre un error.
3. Anida estos context managers para mostrar un flujo completo.
"""

import contextlib
import time
import random
from typing import List, Dict, Any, Optional

# Simulación de una base de datos en memoria
class BaseDatosSim:
    """
    Simula una base de datos simple con almacenamiento en memoria.
    """
    def __init__(self):
        self._data = {}
        self._conectado = False
        self._en_transaccion = False
        self._snapshot = None  # Para guardar estado antes de una transacción
    
    def conectar(self, retardo=True):
        """Simula la conexión a una base de datos."""
        if self._conectado:
            raise RuntimeError("La base de datos ya está conectada")
        
        # Simular retardo de conexión
        if retardo:
            time.sleep(0.2)
        
        print("BaseDatos: Conectando a la base de datos...")
        self._conectado = True
    
    def desconectar(self):
        """Simula la desconexión de una base de datos."""
        if not self._conectado:
            return
        
        print("BaseDatos: Desconectando de la base de datos...")
        self._conectado = False
    
    def _verificar_conexion(self):
        """Verifica que haya una conexión activa."""
        if not self._conectado:
            raise RuntimeError("No hay conexión activa a la base de datos")
    
    def iniciar_transaccion(self):
        """Inicia una transacción, guardando el estado actual."""
        self._verificar_conexion()
        
        if self._en_transaccion:
            raise RuntimeError("Ya hay una transacción activa")
        
        print("BaseDatos: Iniciando transacción...")
        # Guardar una copia del estado actual
        import copy
        self._snapshot = copy.deepcopy(self._data)
        self._en_transaccion = True
    
    def commit(self):
        """Confirma los cambios de la transacción."""
        self._verificar_conexion()
        
        if not self._en_transaccion:
            raise RuntimeError("No hay una transacción activa")
        
        print("BaseDatos: Commit realizado. Cambios guardados.")
        self._snapshot = None
        self._en_transaccion = False
    
    def rollback(self):
        """Revierte los cambios de la transacción."""
        self._verificar_conexion()
        
        if not self._en_transaccion:
            raise RuntimeError("No hay una transacción activa")
        
        print("BaseDatos: Rollback realizado. Cambios descartados.")
        self._data = self._snapshot
        self._snapshot = None
        self._en_transaccion = False
    
    # Operaciones CRUD
    def crear_tabla(self, nombre_tabla):
        """Crea una tabla vacía."""
        self._verificar_conexion()
        
        if nombre_tabla in self._data:
            raise ValueError(f"La tabla '{nombre_tabla}' ya existe")
        
        self._data[nombre_tabla] = []
        print(f"BaseDatos: Tabla '{nombre_tabla}' creada.")
    
    def insertar(self, tabla: str, registro: Dict[str, Any]):
        """Inserta un registro en una tabla."""
        self._verificar_conexion()
        
        if tabla not in self._data:
            raise ValueError(f"La tabla '{tabla}' no existe")
            
        # Simular un error aleatorio para mostrar rollback
        if random.random() < 0.3 and "forzar_error" in registro and registro["forzar_error"]:
            raise ValueError("Error al insertar registro (simulado)")
            
        # Generar un ID único si no se proporciona
        if "id" not in registro:
            registro = registro.copy()  # No modificar el original
            registro["id"] = len(self._data[tabla]) + 1
            
        self._data[tabla].append(registro)
        print(f"BaseDatos: Registro insertado en '{tabla}': {registro}")
        
        return registro["id"]
    
    def seleccionar(self, tabla: str, filtro: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Selecciona registros que coincidan con el filtro."""
        self._verificar_conexion()
        
        if tabla not in self._data:
            raise ValueError(f"La tabla '{tabla}' no existe")
            
        if filtro is None:
            return self._data[tabla].copy()
            
        # Aplicar filtro simple
        resultados = []
        for registro in self._data[tabla]:
            coincide = True
            for clave, valor in filtro.items():
                if clave not in registro or registro[clave] != valor:
                    coincide = False
                    break
            if coincide:
                resultados.append(registro.copy())
                
        return resultados
    
    def actualizar(self, tabla: str, id_registro: int, nuevos_valores: Dict[str, Any]) -> bool:
        """Actualiza un registro por su ID."""
        self._verificar_conexion()
        
        if tabla not in self._data:
            raise ValueError(f"La tabla '{tabla}' no existe")
            
        # Buscar y actualizar el registro
        for registro in self._data[tabla]:
            if registro.get("id") == id_registro:
                # Simular un error aleatorio
                if random.random() < 0.3 and "forzar_error" in nuevos_valores and nuevos_valores["forzar_error"]:
                    raise ValueError("Error al actualizar registro (simulado)")
                    
                registro.update(nuevos_valores)
                print(f"BaseDatos: Registro {id_registro} actualizado en '{tabla}'")
                return True
                
        print(f"BaseDatos: Registro {id_registro} no encontrado en '{tabla}'")
        return False
    
    def eliminar(self, tabla: str, id_registro: int) -> bool:
        """Elimina un registro por su ID."""
        self._verificar_conexion()
        
        if tabla not in self._data:
            raise ValueError(f"La tabla '{tabla}' no existe")
            
        # Buscar y eliminar el registro
        for i, registro in enumerate(self._data[tabla]):
            if registro.get("id") == id_registro:
                # Simular un error aleatorio
                if random.random() < 0.3:
                    raise ValueError("Error al eliminar registro (simulado)")
                    
                self._data[tabla].pop(i)
                print(f"BaseDatos: Registro {id_registro} eliminado de '{tabla}'")
                return True
                
        print(f"BaseDatos: Registro {id_registro} no encontrado en '{tabla}'")
        return False

# Context Manager 1: Conexión a la base de datos
class ConexionDB:
    """Context manager para gestionar la conexión a la base de datos."""
    
    def __init__(self, db=None):
        """
        Inicializa el context manager.
        Si no se proporciona una instancia de base de datos, se crea una nueva.
        """
        self.db = db if db is not None else BaseDatosSim()
    
    def __enter__(self):
        """Se ejecuta al entrar en el bloque with."""
        self.db.conectar()
        return self.db
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Se ejecuta al salir del bloque with."""
        self.db.desconectar()
        # No suprimimos excepciones
        return False

# Context Manager 2: Transacción
class Transaccion:
    """Context manager para gestionar transacciones."""
    
    def __init__(self, db):
        """
        Inicializa el context manager.
        Requiere una instancia de base de datos ya conectada.
        """
        self.db = db
    
    def __enter__(self):
        """Inicia la transacción al entrar en el bloque with."""
        self.db.iniciar_transaccion()
        return self.db
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Al salir del bloque with:
        - Si no hubo excepción, hace commit
        - Si hubo excepción, hace rollback
        """
        if exc_type is not None:
            # Ocurrió una excepción, hacer rollback
            print(f"Transacción: Error detectado ({exc_type.__name__}), haciendo rollback...")
            self.db.rollback()
        else:
            # Todo bien, hacer commit
            self.db.commit()
        
        # No suprimimos excepciones
        return False

# Context Manager 3: Usando la función contextlib.contextmanager
@contextlib.contextmanager
def tabla_temporal(db, nombre_tabla):
    """
    Context manager que crea una tabla temporal y la usa dentro del bloque.
    Al salir, simula eliminar la tabla (en esta simulación no implementamos drop_table).
    """
    print(f"TablaTemp: Creando tabla temporal '{nombre_tabla}'...")
    db.crear_tabla(nombre_tabla)
    
    try:
        yield nombre_tabla
    finally:
        print(f"TablaTemp: Limpiando tabla temporal '{nombre_tabla}'...")
        # En una DB real, aquí haríamos drop_table

# Ejemplo de uso avanzado con anidación de context managers
def demostrar_uso_avanzado():
    """
    Demuestra el uso avanzado y anidado de context managers.
    """
    db_global = BaseDatosSim()  # Una sola instancia de BD para todo el ejemplo
    
    print("=== Ejemplo 1: Operaciones básicas con conexión ===")
    with ConexionDB(db_global) as db:
        db.crear_tabla("usuarios")
        
        # Insertar algunos registros
        db.insertar("usuarios", {"nombre": "Ana", "edad": 28})
        db.insertar("usuarios", {"nombre": "Luis", "edad": 35})
        
        # Consultar datos
        usuarios = db.seleccionar("usuarios")
        print(f"Usuarios en la base de datos: {usuarios}")
    
    print("\n=== Ejemplo 2: Uso de transacciones (con errores simulados) ===")
    with ConexionDB(db_global) as db:
        # Crear otra tabla
        db.crear_tabla("productos")
        
        # Primera transacción exitosa
        with Transaccion(db):
            db.insertar("productos", {"nombre": "Laptop", "precio": 1200})
            db.insertar("productos", {"nombre": "Monitor", "precio": 300})
        
        # Consultar datos después de la primera transacción
        productos = db.seleccionar("productos")
        print(f"Productos después de transacción 1: {productos}")
        
        # Segunda transacción que fallará y hará rollback
        try:
            with Transaccion(db):
                db.insertar("productos", {"nombre": "Teclado", "precio": 50})
                # Este insertará un error simulado
                db.insertar("productos", {"nombre": "Mouse", "precio": 25, "forzar_error": True})
                print("Este mensaje no debería aparecer si hay error y rollback")
        except ValueError as e:
            print(f"Error capturado fuera de la transacción: {e}")
        
        # Consultar datos después de la segunda transacción (con rollback)
        productos = db.seleccionar("productos")
        print(f"Productos después de transacción 2 (con rollback): {productos}")
    
    print("\n=== Ejemplo 3: Uso de context manager para tabla temporal ===")
    with ConexionDB(db_global) as db:
        with tabla_temporal(db, "estadisticas_temp") as nombre_tabla:
            # Usar la tabla temporal
            db.insertar(nombre_tabla, {"fecha": "2023-01-01", "visitas": 100})
            db.insertar(nombre_tabla, {"fecha": "2023-01-02", "visitas": 120})
            
            # Obtener datos
            stats = db.seleccionar(nombre_tabla)
            print(f"Estadísticas temporales: {stats}")
        
        # Aquí la tabla temporal ya estaría "eliminada" en una DB real

def main():
    print("=== DEMOSTRACIÓN DE USO AVANZADO DE CONTEXT MANAGERS ===")
    demostrar_uso_avanzado()

if __name__ == "__main__":
    main()
