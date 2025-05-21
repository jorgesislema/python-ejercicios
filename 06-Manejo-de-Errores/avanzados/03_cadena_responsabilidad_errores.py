"""
Ejercicio 3: Cadena de Responsabilidad para Errores

Objetivo: Implementar el patrón Cadena de Responsabilidad para gestionar diferentes tipos de excepciones.

Instrucciones:
1. Crea una jerarquía de manejadores de excepciones.
2. Cada manejador debe procesar solo un tipo específico de error.
3. Si un manejador no puede procesar un error, lo pasa al siguiente en la cadena.
"""

from abc import ABC, abstractmethod
import json
import re

# 1. Definir errores personalizados
class ValidacionError(Exception):
    """Clase base para errores de validación."""
    pass

class ErrorFormatoJSON(ValidacionError):
    """Error de formato en un documento JSON."""
    pass

class ErrorCampoObligatorio(ValidacionError):
    """Error de campo obligatorio faltante."""
    pass

class ErrorFormatoEmail(ValidacionError):
    """Error de formato de correo electrónico."""
    pass

class ErrorRangoNumerico(ValidacionError):
    """Error de valor numérico fuera de rango."""
    pass

# 2. Implementar el Manejador Abstracto (Handler)
class ManejadorError(ABC):
    """Clase base para la cadena de responsabilidad."""
    
    def __init__(self):
        self._siguiente = None
    
    def establecer_siguiente(self, manejador):
        """
        Establece el siguiente manejador en la cadena.
        Permite encadenar: manejador1.establecer_siguiente(manejador2)
        """
        self._siguiente = manejador
        return manejador  # Devolver el manejador permite encadenamientos
    
    def manejar(self, error):
        """
        Intenta manejar el error o lo pasa al siguiente manejador.
        """
        if self.puede_manejar(error):
            return self.procesar(error)
        elif self._siguiente is not None:
            return self._siguiente.manejar(error)
        else:
            # Si llegamos al final de la cadena sin manejar el error
            return f"Error no manejado: {error}"
    
    @abstractmethod
    def puede_manejar(self, error):
        """
        Determina si este manejador puede procesar el error.
        Debe ser implementado por subclases.
        """
        pass
    
    @abstractmethod
    def procesar(self, error):
        """
        Procesa el error si este manejador puede manejarlo.
        Debe ser implementado por subclases.
        """
        pass

# 3. Implementar Manejadores Concretos
class ManejadorErrorJSON(ManejadorError):
    """Maneja errores de formato JSON."""
    
    def puede_manejar(self, error):
        return isinstance(error, (json.JSONDecodeError, ErrorFormatoJSON))
    
    def procesar(self, error):
        if isinstance(error, json.JSONDecodeError):
            linea = error.lineno
            columna = error.colno
            return (f"Error de formato JSON en línea {linea}, columna {columna}. "
                   f"Detalles: {error.msg}")
        else:
            return f"Error de formato JSON: {error}"

class ManejadorCampoObligatorio(ManejadorError):
    """Maneja errores de campos obligatorios faltantes."""
    
    def puede_manejar(self, error):
        return isinstance(error, ErrorCampoObligatorio)
    
    def procesar(self, error):
        return f"Campo obligatorio faltante: {error}"

class ManejadorFormatoEmail(ManejadorError):
    """Maneja errores de formato de email."""
    
    def puede_manejar(self, error):
        return isinstance(error, ErrorFormatoEmail)
    
    def procesar(self, error):
        return f"Formato de email inválido: {error}"

class ManejadorRangoNumerico(ManejadorError):
    """Maneja errores de valores fuera de rango."""
    
    def puede_manejar(self, error):
        return isinstance(error, ErrorRangoNumerico)
    
    def procesar(self, error):
        return f"Valor numérico fuera de rango: {error}"

class ManejadorGenerico(ManejadorError):
    """Maneja cualquier otro tipo de error."""
    
    def puede_manejar(self, error):
        return True  # Este manejador acepta cualquier error
    
    def procesar(self, error):
        return f"Error genérico: {type(error).__name__} - {error}"

# 4. Funciones de validación que generan errores
def validar_json(texto_json):
    """Valida que un texto sea JSON válido."""
    try:
        return json.loads(texto_json)
    except json.JSONDecodeError as e:
        raise ErrorFormatoJSON(f"JSON inválido: {e}")

def validar_campos_obligatorios(datos, campos):
    """Valida que los campos obligatorios existan en los datos."""
    for campo in campos:
        if campo not in datos or datos[campo] == "":
            raise ErrorCampoObligatorio(f"El campo '{campo}' es obligatorio")

def validar_email(email):
    """Valida que un email tenga formato correcto."""
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(patron, email):
        raise ErrorFormatoEmail(f"'{email}' no es un email válido")

def validar_rango_numerico(valor, minimo, maximo):
    """Valida que un valor esté dentro de un rango."""
    if valor < minimo or valor > maximo:
        raise ErrorRangoNumerico(
            f"El valor {valor} está fuera del rango permitido [{minimo}, {maximo}]")

# 5. Ejemplo de uso
def procesar_datos_usuario(datos_json):
    """Procesa datos de usuario en formato JSON."""
    # Crear la cadena de manejadores
    manejador_json = ManejadorErrorJSON()
    manejador_campo = ManejadorCampoObligatorio()
    manejador_email = ManejadorFormatoEmail()
    manejador_rango = ManejadorRangoNumerico()
    manejador_generico = ManejadorGenerico()
    
    # Establecer la cadena
    manejador_json.establecer_siguiente(manejador_campo) \
                  .establecer_siguiente(manejador_email) \
                  .establecer_siguiente(manejador_rango) \
                  .establecer_siguiente(manejador_generico)
    
    try:
        # Paso 1: Validar formato JSON
        datos = validar_json(datos_json)
        
        # Paso 2: Validar campos obligatorios
        validar_campos_obligatorios(datos, ["nombre", "email", "edad"])
        
        # Paso 3: Validar formato de email
        validar_email(datos["email"])
        
        # Paso 4: Validar rango de edad
        validar_rango_numerico(datos["edad"], 18, 99)
        
        # Si llegamos aquí, todo está bien
        return f"Datos válidos: {datos}"
        
    except Exception as e:
        # Usar la cadena de responsabilidad para manejar el error
        return manejador_json.manejar(e)

def main():
    # Ejemplos con diferentes tipos de errores
    print("=== Ejemplo 1: JSON inválido ===")
    json_invalido = '{"nombre": "Juan", "email": "juan@example.com", "edad": 25'  # Falta }
    print(procesar_datos_usuario(json_invalido))
    
    print("\n=== Ejemplo 2: Campo obligatorio faltante ===")
    json_campo_faltante = '{"nombre": "Ana", "edad": 30}'  # Falta email
    print(procesar_datos_usuario(json_campo_faltante))
    
    print("\n=== Ejemplo 3: Email inválido ===")
    json_email_invalido = '{"nombre": "Pedro", "email": "pedro@", "edad": 40}'
    print(procesar_datos_usuario(json_email_invalido))
    
    print("\n=== Ejemplo 4: Edad fuera de rango ===")
    json_edad_invalida = '{"nombre": "María", "email": "maria@example.com", "edad": 15}'
    print(procesar_datos_usuario(json_edad_invalida))
    
    print("\n=== Ejemplo 5: Datos válidos ===")
    json_valido = '{"nombre": "Carlos", "email": "carlos@example.com", "edad": 35}'
    print(procesar_datos_usuario(json_valido))

if __name__ == "__main__":
    main()
