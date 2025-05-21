"""
Ejercicio 7: Validación Avanzada con Descriptores

Objetivo: Implementar un sistema de validación avanzada usando descriptores de Python.

Instrucciones:
1. Crea descriptores para diferentes tipos de validación (entero, flotante, string, etc.).
2. Implementa manejo de errores adecuado para la validación fallida.
3. Crea clases que utilicen estos descriptores para validar sus atributos.
"""

from abc import ABC, abstractmethod
import re
from typing import Any, Optional, Type, Dict, List, Set, Tuple, Union, Callable
import datetime

# Clase base para los descriptores de validación
class Validator(ABC):
    """
    Clase base abstracta para todos los descriptores de validación.
    Implementa la interfaz de descriptor de Python.
    """
    def __init__(self, name: str = None, **kwargs):
        self.name = name        # Nombre del atributo (asignado posteriormente)
        self.private_name = None  # Nombre del atributo privado para almacenar el valor
        
        # Atributos comunes para todos los validadores
        self.required = kwargs.get('required', True)
        self.default = kwargs.get('default', None)
        self.error_msg = kwargs.get('error_msg', None)
    
    def __set_name__(self, owner, name):
        """
        Método llamado al definir el descriptor como variable de clase.
        Guarda el nombre del atributo.
        """
        self.name = name
        # Crear un nombre único para almacenar el valor real
        # Esto evita colisiones con el nombre del descriptor
        self.private_name = f'_{self.__class__.__name__}_{name}'
    
    def __get__(self, instance, owner):
        """
        Método llamado al acceder al atributo.
        """
        if instance is None:
            # Acceso a nivel de clase
            return self
        
        # Obtener el valor almacenado o el valor por defecto
        return getattr(instance, self.private_name, self.default)
    
    def __set__(self, instance, value):
        """
        Método llamado al asignar un valor al atributo.
        Valida el valor antes de almacenarlo.
        """
        # Manejar None para atributos no requeridos
        if value is None:
            if self.required:
                self._raise_error(f"El atributo '{self.name}' es obligatorio y no puede ser None")
            else:
                setattr(instance, self.private_name, None)
                return
        
        try:
            # Validar y posiblemente convertir el valor
            validated_value = self.validate(value)
            # Almacenar el valor validado
            setattr(instance, self.private_name, validated_value)
        except Exception as e:
            # Manejar el error de validación
            self._raise_error(str(e))
    
    def _raise_error(self, message):
        """Lanza un error de validación con un mensaje personalizado o el predeterminado."""
        if self.error_msg:
            raise ValueError(self.error_msg)
        else:
            raise ValueError(message)
    
    @abstractmethod
    def validate(self, value: Any) -> Any:
        """
        Método abstracto que debe implementar la lógica de validación.
        Cada subclase debe implementar su propia validación.
        """
        pass

# Validadores específicos para distintos tipos de datos
class Integer(Validator):
    """Validador para números enteros."""
    
    def __init__(self, min_value=None, max_value=None, **kwargs):
        super().__init__(**kwargs)
        self.min_value = min_value
        self.max_value = max_value
    
    def validate(self, value):
        # Intentar convertir a entero si no lo es
        if not isinstance(value, int):
            try:
                value = int(value)
            except (ValueError, TypeError):
                raise ValueError(f"'{value}' no es convertible a entero")
        
        # Validar rango si se especificó
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"El valor debe ser mayor o igual a {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"El valor debe ser menor o igual a {self.max_value}")
        
        return value

class Float(Validator):
    """Validador para números de punto flotante."""
    
    def __init__(self, min_value=None, max_value=None, **kwargs):
        super().__init__(**kwargs)
        self.min_value = min_value
        self.max_value = max_value
    
    def validate(self, value):
        # Intentar convertir a float si no lo es
        if not isinstance(value, float):
            try:
                value = float(value)
            except (ValueError, TypeError):
                raise ValueError(f"'{value}' no es convertible a float")
        
        # Validar rango si se especificó
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"El valor debe ser mayor o igual a {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"El valor debe ser menor o igual a {self.max_value}")
        
        return value

class String(Validator):
    """Validador para cadenas de texto."""
    
    def __init__(self, min_length=None, max_length=None, pattern=None, **kwargs):
        super().__init__(**kwargs)
        self.min_length = min_length
        self.max_length = max_length
        self.pattern = pattern
        
        # Preparar patrón de regex si se proporcionó
        self.regex = re.compile(pattern) if pattern else None
    
    def validate(self, value):
        # Convertir a string si no lo es
        if not isinstance(value, str):
            value = str(value)
        
        # Validar longitud si se especificó
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(f"La cadena debe tener al menos {self.min_length} caracteres")
        if self.max_length is not None and len(value) > self.max_length:
            raise ValueError(f"La cadena debe tener como máximo {self.max_length} caracteres")
        
        # Validar patrón si se especificó
        if self.regex and not self.regex.match(value):
            raise ValueError(f"La cadena no coincide con el patrón requerido: {self.pattern}")
        
        return value

class Email(String):
    """Validador especializado para direcciones de email."""
    
    def __init__(self, **kwargs):
        # Patrón básico para validar emails
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        super().__init__(pattern=pattern, **kwargs)
    
    def validate(self, value):
        # Usar la validación de String y agregar validación específica de email
        value = super().validate(value)
        
        # Verificaciones adicionales específicas de email podrían ir aquí
        
        return value

class Date(Validator):
    """Validador para fechas."""
    
    def __init__(self, formato='%Y-%m-%d', min_date=None, max_date=None, **kwargs):
        super().__init__(**kwargs)
        self.formato = formato
        
        # Convertir strings de fecha a objetos datetime si es necesario
        if isinstance(min_date, str):
            self.min_date = datetime.datetime.strptime(min_date, formato).date()
        else:
            self.min_date = min_date
        
        if isinstance(max_date, str):
            self.max_date = datetime.datetime.strptime(max_date, formato).date()
        else:
            self.max_date = max_date
    
    def validate(self, value):
        # Si ya es un objeto date, usarlo directamente
        if isinstance(value, datetime.date):
            date_value = value
        # Si es datetime, extraer solo la fecha
        elif isinstance(value, datetime.datetime):
            date_value = value.date()
        # Si es string, convertirlo a date
        elif isinstance(value, str):
            try:
                date_value = datetime.datetime.strptime(value, self.formato).date()
            except ValueError:
                raise ValueError(f"La fecha debe tener el formato {self.formato}")
        else:
            raise ValueError(f"El valor '{value}' no es una fecha válida")
        
        # Validar rango si se especificó
        if self.min_date and date_value < self.min_date:
            raise ValueError(f"La fecha debe ser posterior a {self.min_date}")
        if self.max_date and date_value > self.max_date:
            raise ValueError(f"La fecha debe ser anterior a {self.max_date}")
        
        return date_value

class Choice(Validator):
    """Validador para valores que deben estar en un conjunto de opciones."""
    
    def __init__(self, choices, **kwargs):
        super().__init__(**kwargs)
        # Asegurar que las opciones sean un conjunto para búsqueda eficiente
        self.choices = set(choices)
    
    def validate(self, value):
        if value not in self.choices:
            raise ValueError(f"El valor debe ser uno de: {', '.join(map(str, self.choices))}")
        return value

class List(Validator):
    """Validador para listas con elementos de un tipo específico."""
    
    def __init__(self, item_validator=None, min_length=None, max_length=None, **kwargs):
        super().__init__(**kwargs)
        self.item_validator = item_validator
        self.min_length = min_length
        self.max_length = max_length
    
    def validate(self, value):
        # Convertir a lista si es iterable pero no lista
        if not isinstance(value, list):
            try:
                value = list(value)
            except (TypeError, ValueError):
                raise ValueError(f"'{value}' no es convertible a lista")
        
        # Validar longitud si se especificó
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(f"La lista debe tener al menos {self.min_length} elementos")
        if self.max_length is not None and len(value) > self.max_length:
            raise ValueError(f"La lista debe tener como máximo {self.max_length} elementos")
        
        # Validar cada elemento si se especificó un validador de elementos
        if self.item_validator:
            for i, item in enumerate(value):
                try:
                    value[i] = self.item_validator.validate(item)
                except ValueError as e:
                    raise ValueError(f"Error en elemento {i}: {e}")
        
        return value

# Clases de ejemplo que utilizan los descriptores de validación
class Persona:
    """Clase de ejemplo que utiliza varios descriptores de validación."""
    
    nombre = String(min_length=2, max_length=50, required=True,
                   error_msg="El nombre debe tener entre 2 y 50 caracteres")
    
    apellido = String(min_length=2, max_length=50, required=True,
                     error_msg="El apellido debe tener entre 2 y 50 caracteres")
    
    edad = Integer(min_value=0, max_value=120, required=True,
                  error_msg="La edad debe ser un número entre 0 y 120")
    
    email = Email(required=False, error_msg="El email no tiene un formato válido")
    
    fecha_nacimiento = Date(required=False, 
                           min_date="1900-01-01",
                           max_date=datetime.date.today(),
                           error_msg="La fecha de nacimiento no es válida")
    
    genero = Choice(choices=['M', 'F', 'Otro'], required=False,
                   error_msg="El género debe ser 'M', 'F' u 'Otro'")
    
    intereses = List(item_validator=String(), min_length=0, max_length=10, 
                    required=False,
                    error_msg="Los intereses deben ser una lista de texto (máx. 10)")
    
    def __init__(self, nombre, apellido, edad, email=None, fecha_nacimiento=None, 
                 genero=None, intereses=None):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.email = email
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
        self.intereses = intereses
    
    def __str__(self):
        atributos = []
        for attr in ['nombre', 'apellido', 'edad', 'email', 'fecha_nacimiento', 
                     'genero', 'intereses']:
            valor = getattr(self, attr)
            if valor is not None:
                atributos.append(f"{attr}={valor}")
        
        return f"Persona({', '.join(atributos)})"

class Producto:
    """Otra clase de ejemplo que utiliza descriptores de validación."""
    
    nombre = String(min_length=3, max_length=100, required=True)
    precio = Float(min_value=0.01, required=True)
    categoria = Choice(choices=['Electrónica', 'Ropa', 'Hogar', 'Alimentación', 'Otros'])
    stock = Integer(min_value=0, default=0)
    fecha_creacion = Date(required=False, default=datetime.date.today)
    
    def __init__(self, nombre, precio, categoria, stock=0, fecha_creacion=None):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
        if fecha_creacion:
            self.fecha_creacion = fecha_creacion
    
    def __str__(self):
        return f"Producto(nombre='{self.nombre}', precio={self.precio}, " \
               f"categoria='{self.categoria}', stock={self.stock}, " \
               f"fecha_creacion={self.fecha_creacion})"

# Función principal para demostrar el uso
def main():
    print("=== DEMOSTRACIÓN DE VALIDACIÓN CON DESCRIPTORES ===\n")
    
    # Ejemplo 1: Crear una persona válida
    try:
        print("Ejemplo 1: Creando una persona con datos válidos")
        persona1 = Persona(
            nombre="Juan",
            apellido="Pérez",
            edad=30,
            email="juan.perez@example.com",
            fecha_nacimiento="1993-05-15",
            genero="M",
            intereses=["Programación", "Cine", "Viajes"]
        )
        print(f"✓ Persona creada correctamente: {persona1}")
    except ValueError as e:
        print(f"✗ Error: {e}")
    
    print("\n" + "-" * 50 + "\n")
    
    # Ejemplo 2: Intentar crear una persona con datos inválidos
    try:
        print("Ejemplo 2: Intentando crear una persona con datos inválidos")
        persona2 = Persona(
            nombre="A",  # Muy corto
            apellido="García",
            edad=150,    # Fuera de rango
            email="correo_invalido",  # Email inválido
            genero="X"   # No está en las opciones permitidas
        )
        print(f"✓ Persona creada correctamente: {persona2}")
    except ValueError as e:
        print(f"✗ Error: {e}")
    
    print("\n" + "-" * 50 + "\n")
    
    # Ejemplo 3: Modificar un atributo a un valor inválido
    try:
        print("Ejemplo 3: Modificando un atributo a un valor inválido")
        persona1.edad = -5
        print(f"✓ Edad modificada: {persona1}")
    except ValueError as e:
        print(f"✗ Error: {e}")
        print(f"  La edad actual sigue siendo: {persona1.edad}")
    
    print("\n" + "-" * 50 + "\n")
    
    # Ejemplo 4: Crear un producto
    try:
        print("Ejemplo 4: Creando un producto con datos válidos")
        producto = Producto(
            nombre="Laptop HP Pavilion",
            precio=899.99,
            categoria="Electrónica",
            stock=10
        )
        print(f"✓ Producto creado correctamente: {producto}")
    except ValueError as e:
        print(f"✗ Error: {e}")

if __name__ == "__main__":
    main()
