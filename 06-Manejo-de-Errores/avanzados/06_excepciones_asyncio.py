"""
Ejercicio 6: Excepciones en Código Asíncrono

Objetivo: Comprender y manejar excepciones en entornos asíncronos usando asyncio.

Instrucciones:
1. Implementa funciones asíncronas que puedan generar excepciones.
2. Maneja adecuadamente las excepciones tanto en tareas individuales como en grupos de tareas.
3. Crea un ejemplo que simule operaciones asíncronas que pueden fallar.
"""

import asyncio
import random
import time
from typing import List, Dict, Any

class ServidorError(Exception):
    """Excepción base para errores del servidor simulado."""
    pass

class TimeoutError(ServidorError):
    """Error debido a que una operación excede el tiempo máximo permitido."""
    pass

class RecursoNoEncontradoError(ServidorError):
    """Error cuando un recurso solicitado no existe."""
    pass

class ServicioNoDisponibleError(ServidorError):
    """Error cuando un servicio no está disponible."""
    pass

class ErrorInterno(ServidorError):
    """Error interno del servidor."""
    pass

# Simulación de una API asíncrona
class ServidorAPI:
    """Simula un servidor con operaciones asíncronas."""
    
    def __init__(self, tiempo_respuesta_base=0.5, probabilidad_error=0.3):
        self.tiempo_respuesta_base = tiempo_respuesta_base
        self.probabilidad_error = probabilidad_error
        self.recursos = {
            "usuarios": {
                1: {"id": 1, "nombre": "Ana", "rol": "admin"},
                2: {"id": 2, "nombre": "Carlos", "rol": "usuario"},
                3: {"id": 3, "nombre": "Elena", "rol": "editor"}
            },
            "productos": {
                101: {"id": 101, "nombre": "Laptop", "precio": 1200},
                102: {"id": 102, "nombre": "Monitor", "precio": 300},
                103: {"id": 103, "nombre": "Teclado", "precio": 50}
            }
        }
        self.servicios_activos = {
            "auth": True,
            "pagos": False,  # Este servicio está inactivo
            "notificaciones": True
        }
    
    async def _simular_retardo(self, factor=1.0):
        """Simula un retardo en la respuesta."""
        tiempo_espera = self.tiempo_respuesta_base * factor * random.uniform(0.8, 1.5)
        await asyncio.sleep(tiempo_espera)
    
    async def _verificar_error_aleatorio(self):
        """Genera un error aleatorio según la probabilidad configurada."""
        if random.random() < self.probabilidad_error:
            errores = [TimeoutError, RecursoNoEncontradoError, ServicioNoDisponibleError, ErrorInterno]
            error = random.choice(errores)
            
            if error is TimeoutError:
                await asyncio.sleep(2)  # Simular un timeout largo
                raise TimeoutError("Tiempo de espera excedido")
            elif error is RecursoNoEncontradoError:
                raise RecursoNoEncontradoError("Recurso solicitado no encontrado")
            elif error is ServicioNoDisponibleError:
                raise ServicioNoDisponibleError("Servicio temporalmente no disponible")
            else:
                raise ErrorInterno("Error interno del servidor")
    
    async def obtener_recurso(self, tipo, id_recurso):
        """Obtiene un recurso por su ID."""
        # Simular retardo en red
        await self._simular_retardo()
        
        # Verificar posible error aleatorio
        await self._verificar_error_aleatorio()
        
        # Verificar si el tipo de recurso existe
        if tipo not in self.recursos:
            raise RecursoNoEncontradoError(f"Tipo de recurso '{tipo}' no encontrado")
        
        # Verificar si el recurso existe
        if id_recurso not in self.recursos[tipo]:
            raise RecursoNoEncontradoError(f"Recurso con ID {id_recurso} no encontrado")
        
        return self.recursos[tipo][id_recurso]
    
    async def invocar_servicio(self, nombre_servicio, payload=None):
        """Invoca un servicio del servidor."""
        # Simular retardo en red
        await self._simular_retardo(factor=1.2)
        
        # Verificar posible error aleatorio
        await self._verificar_error_aleatorio()
        
        # Verificar si el servicio existe y está activo
        if nombre_servicio not in self.servicios_activos:
            raise RecursoNoEncontradoError(f"Servicio '{nombre_servicio}' no encontrado")
        
        if not self.servicios_activos[nombre_servicio]:
            raise ServicioNoDisponibleError(f"Servicio '{nombre_servicio}' no disponible")
        
        # Procesar el servicio (simulado)
        return {
            "servicio": nombre_servicio,
            "estado": "completado",
            "timestamp": time.time(),
            "resultado": f"Operación en {nombre_servicio} exitosa" if payload is None else 
                        f"Procesado {payload} en {nombre_servicio}"
        }

# Funciones para manejar excepciones en código asíncrono
async def obtener_con_manejo_basico(api, tipo, id_recurso):
    """Manejo básico de excepciones en código asíncrono."""
    try:
        resultado = await api.obtener_recurso(tipo, id_recurso)
        print(f"✓ Recurso obtenido: {resultado}")
        return resultado
    except TimeoutError:
        print(f"✗ Timeout al obtener {tipo}/{id_recurso}")
    except RecursoNoEncontradoError as e:
        print(f"✗ Recurso no encontrado: {e}")
    except ServicioNoDisponibleError:
        print(f"✗ Servicio para obtener {tipo}/{id_recurso} no disponible")
    except ErrorInterno:
        print(f"✗ Error interno al obtener {tipo}/{id_recurso}")
    except Exception as e:
        print(f"✗ Error inesperado: {e}")
    
    return None

async def obtener_con_reintentos(api, tipo, id_recurso, max_reintentos=3):
    """Manejo de excepciones con reintentos."""
    for intento in range(1, max_reintentos + 1):
        try:
            print(f"Intento {intento}/{max_reintentos} para obtener {tipo}/{id_recurso}")
            resultado = await api.obtener_recurso(tipo, id_recurso)
            print(f"✓ Recurso obtenido en intento {intento}: {resultado}")
            return resultado
        except (TimeoutError, ServicioNoDisponibleError) as e:
            # Estos errores son recuperables, podemos reintentar
            print(f"  Reintentable ({type(e).__name__}): {e}")
            # Esperar antes de reintentar (backoff exponencial)
            await asyncio.sleep(0.5 * intento)
        except RecursoNoEncontradoError as e:
            # Este error no es recuperable, no tiene sentido reintentar
            print(f"✗ Error no recuperable: {e}")
            return None
        except Exception as e:
            print(f"✗ Error inesperado: {e}")
            if intento == max_reintentos:
                return None
    
    print(f"✗ Agotados {max_reintentos} reintentos para {tipo}/{id_recurso}")
    return None

async def procesar_multiples_recursos(api, recursos):
    """
    Procesa múltiples recursos en paralelo y maneja sus excepciones.
    
    Args:
        api: Instancia de ServidorAPI
        recursos: Lista de tuplas (tipo, id)
    
    Returns:
        Diccionario con resultados exitosos
    """
    # Crear tareas para cada recurso
    tareas = [
        api.obtener_recurso(tipo, id_recurso) 
        for tipo, id_recurso in recursos
    ]
    
    # Ejecutar tareas y recopilar resultados
    resultados = {}
    for i, tarea_futura in enumerate(asyncio.as_completed(tareas)):
        tipo, id_recurso = recursos[i]
        clave = f"{tipo}/{id_recurso}"
        
        try:
            resultado = await tarea_futura
            print(f"✓ Completado {clave}: {resultado}")
            resultados[clave] = resultado
        except Exception as e:
            print(f"✗ Error en {clave}: {e}")
    
    return resultados

async def ejecutar_con_timeout(api, tipo, id_recurso, timeout=1.0):
    """Ejecuta una operación con un timeout específico."""
    try:
        # wait_for lanzará asyncio.TimeoutError si se excede el tiempo
        resultado = await asyncio.wait_for(
            api.obtener_recurso(tipo, id_recurso),
            timeout=timeout
        )
        print(f"✓ Recurso obtenido dentro del timeout: {resultado}")
        return resultado
    except asyncio.TimeoutError:
        print(f"✗ La operación excedió el timeout de {timeout}s")
        return None
    except Exception as e:
        print(f"✗ Error durante la operación: {e}")
        return None

async def procesar_grupo_con_gather(api):
    """
    Demuestra el uso de asyncio.gather para manejar múltiples tareas.
    Si una tarea falla, las demás continuarán.
    """
    try:
        # Procesar varias tareas en paralelo
        resultados = await asyncio.gather(
            api.obtener_recurso("usuarios", 1),
            api.obtener_recurso("productos", 101),
            api.invocar_servicio("auth"),
            api.invocar_servicio("pagos"),  # Este fallará
            return_exceptions=True  # Importante: capturar excepciones en lugar de propagarlas
        )
        
        # Procesar resultados
        for i, resultado in enumerate(resultados):
            if isinstance(resultado, Exception):
                print(f"✗ Tarea {i+1} falló: {type(resultado).__name__}: {resultado}")
            else:
                print(f"✓ Tarea {i+1} completada: {resultado}")
        
        return resultados
    except Exception as e:
        # Esto solo ocurriría si hay un error en gather mismo, no en las tareas
        print(f"✗ Error inesperado en gather: {e}")
        return None

# Función principal para ejecutar las demostraciones
async def main_async():
    # Crear instancia de la API simulada
    api = ServidorAPI(tiempo_respuesta_base=0.2, probabilidad_error=0.3)
    
    print("=== 1. Manejo básico de excepciones ===")
    await obtener_con_manejo_basico(api, "usuarios", 1)
    await obtener_con_manejo_basico(api, "productos", 999)  # No existe
    
    print("\n=== 2. Manejo con reintentos ===")
    await obtener_con_reintentos(api, "productos", 101, max_reintentos=3)
    
    print("\n=== 3. Procesamiento múltiple con as_completed ===")
    recursos = [
        ("usuarios", 1), 
        ("usuarios", 999),  # No existe
        ("productos", 101), 
        ("productos", 102)
    ]
    resultados = await procesar_multiples_recursos(api, recursos)
    print(f"Recursos obtenidos correctamente: {len(resultados)}/{len(recursos)}")
    
    print("\n=== 4. Ejecución con timeout ===")
    await ejecutar_con_timeout(api, "usuarios", 2, timeout=0.5)
    
    print("\n=== 5. Procesamiento en grupo con gather ===")
    await procesar_grupo_con_gather(api)

def main():
    # Ejecutar el loop de eventos asíncrono
    asyncio.run(main_async())

if __name__ == "__main__":
    main()
