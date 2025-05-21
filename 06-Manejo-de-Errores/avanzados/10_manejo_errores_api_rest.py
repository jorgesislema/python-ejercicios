"""
Ejercicio 10: Manejo de Errores en API REST

Objetivo: Implementar un sistema de manejo de errores para una API REST con Flask.

Instrucciones:
1. Implementa una API REST simple con Flask.
2. Diseña un sistema de códigos de error consistentes y mensajes informativos.
3. Incluye middleware para capturar excepciones y convertirlas en respuestas JSON.
"""
from flask import Flask, request, jsonify, g
import logging
import traceback
import sqlite3
import time
import random
from functools import wraps
from datetime import datetime
from typing import Dict, Any, Optional, List
from werkzeug.exceptions import HTTPException

# Configuración del logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='api_rest.log',
    filemode='a'
)
logger = logging.getLogger('api_errores')

# Códigos de error personalizados
class CodigosError:
    AUTH_REQUIRED = "AUTH_001"
    AUTH_INVALID = "AUTH_002"
    AUTH_EXPIRED = "AUTH_003"
    AUTH_INSUFFICIENT = "AUTH_004"

    VAL_MISSING_FIELD = "VAL_001"
    VAL_INVALID_TYPE = "VAL_002"
    VAL_INVALID_VALUE = "VAL_003"
    VAL_DUPLICATE = "VAL_004"

    RES_NOT_FOUND = "RES_001"
    RES_CONFLICT = "RES_002"
    RES_GONE = "RES_003"

    SYS_DB_ERROR = "SYS_001"
    SYS_INTERNAL = "SYS_002"
    SYS_DEPENDENCY = "SYS_003"
    SYS_NOT_IMPLEMENTED = "SYS_004"
    SYS_UNAVAILABLE = "SYS_005"

# Excepciones personalizadas
class APIError(Exception):
    def __init__(self, codigo: str, mensaje: str, http_status: int = 400, detalles: Optional[Dict[str, Any]] = None):
        self.codigo = codigo
        self.mensaje = mensaje
        self.http_status = http_status
        self.detalles = detalles
        self.timestamp = datetime.now().isoformat()
        super().__init__(f"[{codigo}] {mensaje}")

class AuthError(APIError):
    def __init__(self, codigo, mensaje, **kwargs):
        kwargs.setdefault('http_status', 401)
        super().__init__(codigo, mensaje, **kwargs)

class ValidationError(APIError):
    def __init__(self, codigo, mensaje, **kwargs):
        kwargs.setdefault('http_status', 400)
        super().__init__(codigo, mensaje, **kwargs)

class ResourceError(APIError):
    def __init__(self, codigo, mensaje, **kwargs):
        kwargs.setdefault('http_status', 404)
        super().__init__(codigo, mensaje, **kwargs)

class SystemError(APIError):
    def __init__(self, codigo, mensaje, **kwargs):
        kwargs.setdefault('http_status', 500)
        super().__init__(codigo, mensaje, **kwargs)

# Creación de la aplicación Flask
app = Flask(__name__)

@app.before_request
def antes_peticion():
    g.tiempo_inicio = time.time()
    g.id_peticion = random.randint(10000, 99999)
    logger.info(f"[{g.id_peticion}] Nueva petición: {request.method} {request.path}")

@app.after_request
def despues_peticion(response):
    tiempo_respuesta = time.time() - g.tiempo_inicio
    response.headers["X-Response-Time"] = f"{tiempo_respuesta:.4f}s"
    logger.info(
        f"[{g.id_peticion}] Petición completada: {request.method} {request.path} "
        f"- Status: {response.status_code} - Tiempo: {tiempo_respuesta:.4f}s"
    )
    return response

@app.errorhandler(Exception)
def manejar_excepcion(e):
    if isinstance(e, APIError):
        respuesta = {
            "error": {
                "codigo": e.codigo,
                "mensaje": e.mensaje,
                "timestamp": e.timestamp
            }
        }
        if app.debug and e.detalles:
            respuesta["error"]["detalles"] = e.detalles
        return jsonify(respuesta), e.http_status

    if isinstance(e, HTTPException):
        respuesta = {
            "error": {
                "codigo": f"HTTP_{e.code}",
                "mensaje": e.description,
                "timestamp": datetime.now().isoformat()
            }
        }
        return jsonify(respuesta), e.code

    logger.error(f"Error no controlado: {str(e)}")
    logger.error(traceback.format_exc())
    respuesta = {
        "error": {
            "codigo": CodigosError.SYS_INTERNAL,
            "mensaje": "Error interno del servidor",
            "timestamp": datetime.now().isoformat()
        }
    }
    if app.debug:
        respuesta["error"]["detalles"] = {
            "excepcion": type(e).__name__,
            "mensaje": str(e),
            "traceback": traceback.format_exc()
        }
    return jsonify(respuesta), 500
