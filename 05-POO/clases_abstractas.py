"""
Ejercicio: Clases Abstractas
--------------------------
Este ejercicio demuestra el uso de clases abstractas en Python
usando el módulo abc (Abstract Base Classes).
"""

from abc import ABC, abstractmethod

class InterfazProducto(ABC):
    """
    Clase abstracta que define la interfaz para productos.
    """
    
    @abstractmethod
    def calcular_precio(self):
        """
        Método abstracto para calcular el precio del producto.
        
        Returns:
            float: Precio calculado
        """
        pass
    
    @abstractmethod
    def obtener_descripcion(self):
        """
        Método abstracto para obtener la descripción del producto.
        
        Returns:
            str: Descripción del producto
        """
        pass
    
    @abstractmethod
    def obtener_id(self):
        """
        Método abstracto para obtener el ID del producto.
        
        Returns:
            str: ID del producto
        """
        pass

class Producto(InterfazProducto):
    """
    Clase concreta que implementa la interfaz InterfazProducto.
    """
    
    def __init__(self, id_producto, nombre, precio_base):
        """
        Constructor de la clase Producto.
        
        Args:
            id_producto (str): Identificador único del producto
            nombre (str): Nombre del producto
            precio_base (float): Precio base del producto
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio_base = precio_base
    
    def calcular_precio(self):
        """
        Implementación del método abstracto para calcular el precio.
        
        Returns:
            float: Precio base del producto
        """
        return self.precio_base
    
    def obtener_descripcion(self):
        """
        Implementación del método abstracto para obtener la descripción.
        
        Returns:
            str: Descripción del producto
        """
        return f"Producto: {self.nombre}"
    
    def obtener_id(self):
        """
        Implementación del método abstracto para obtener el ID.
        
        Returns:
            str: ID del producto
        """
        return self.id_producto

class ProductoFisico(Producto):
    """
    Clase que hereda de Producto para representar productos físicos.
    """
    
    def __init__(self, id_producto, nombre, precio_base, peso, dimensiones):
        """
        Constructor de la clase ProductoFisico.
        
        Args:
            id_producto (str): Identificador único del producto
            nombre (str): Nombre del producto
            precio_base (float): Precio base del producto
            peso (float): Peso del producto en kg
            dimensiones (tuple): Dimensiones del producto (ancho, alto, profundidad) en cm
        """
        super().__init__(id_producto, nombre, precio_base)
        self.peso = peso
        self.dimensiones = dimensiones
    
    def calcular_precio(self):
        """
        Sobrescribe el método calcular_precio para incluir costos de envío.
        
        Returns:
            float: Precio con costos de envío incluidos
        """
        precio_base = super().calcular_precio()
        # Añadir costo de envío basado en el peso
        costo_envio = self.peso * 10  # 10 por cada kg
        return precio_base + costo_envio
    
    def obtener_descripcion(self):
        """
        Sobrescribe el método obtener_descripcion para incluir detalles físicos.
        
        Returns:
            str: Descripción con detalles físicos
        """
        ancho, alto, profundidad = self.dimensiones
        return f"{super().obtener_descripcion()} - Físico - Peso: {self.peso}kg, Dimensiones: {ancho}x{alto}x{profundidad}cm"

class ProductoDigital(Producto):
    """
    Clase que hereda de Producto para representar productos digitales.
    """
    
    def __init__(self, id_producto, nombre, precio_base, tamano_archivo, formato):
        """
        Constructor de la clase ProductoDigital.
        
        Args:
            id_producto (str): Identificador único del producto
            nombre (str): Nombre del producto
            precio_base (float): Precio base del producto
            tamano_archivo (float): Tamaño del archivo en MB
            formato (str): Formato del archivo (PDF, MP3, etc.)
        """
        super().__init__(id_producto, nombre, precio_base)
        self.tamano_archivo = tamano_archivo
        self.formato = formato
    
    def calcular_precio(self):
        """
        Sobrescribe el método calcular_precio para aplicar descuento digital.
        
        Returns:
            float: Precio con descuento digital
        """
        precio_base = super().calcular_precio()
        # Descuento por ser digital
        descuento = precio_base * 0.1  # 10% de descuento
        return precio_base - descuento
    
    def obtener_descripcion(self):
        """
        Sobrescribe el método obtener_descripcion para incluir detalles digitales.
        
        Returns:
            str: Descripción con detalles digitales
        """
        return f"{super().obtener_descripcion()} - Digital - Tamaño: {self.tamano_archivo}MB, Formato: {self.formato}"

class Servicio(InterfazProducto):
    """
    Clase que implementa InterfazProducto para representar servicios.
    """
    
    def __init__(self, id_servicio, nombre, precio_hora, horas):
        """
        Constructor de la clase Servicio.
        
        Args:
            id_servicio (str): Identificador único del servicio
            nombre (str): Nombre del servicio
            precio_hora (float): Precio por hora del servicio
            horas (float): Cantidad de horas estimadas
        """
        self.id_servicio = id_servicio
        self.nombre = nombre
        self.precio_hora = precio_hora
        self.horas = horas
    
    def calcular_precio(self):
        """
        Implementación del método abstracto para calcular el precio.
        
        Returns:
            float: Precio calculado según horas y tarifa
        """
        return self.precio_hora * self.horas
    
    def obtener_descripcion(self):
        """
        Implementación del método abstracto para obtener la descripción.
        
        Returns:
            str: Descripción del servicio
        """
        return f"Servicio: {self.nombre} - {self.horas} horas a ${self.precio_hora}/hora"
    
    def obtener_id(self):
        """
        Implementación del método abstracto para obtener el ID.
        
        Returns:
            str: ID del servicio
        """
        return self.id_servicio

def mostrar_catalogo(items):
    """
    Función para mostrar un catálogo de productos o servicios.
    
    Args:
        items (list): Lista de objetos que implementan InterfazProducto
    """
    print("\nCATÁLOGO DE PRODUCTOS Y SERVICIOS:")
    print("-" * 50)
    for item in items:
        print(f"ID: {item.obtener_id()}")
        print(f"Descripción: {item.obtener_descripcion()}")
        print(f"Precio: ${item.calcular_precio():.2f}")
        print("-" * 50)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancias
    libro = ProductoFisico("P001", "Libro Python", 29.99, 0.5, (15, 23, 2))
    ebook = ProductoDigital("P002", "Ebook Python", 19.99, 3.5, "PDF")
    consultoria = Servicio("S001", "Consultoría Python", 50, 2)
    
    # Usar polimorfismo a través de la interfaz común
    catalogo = [libro, ebook, consultoria]
    mostrar_catalogo(catalogo)
    
    # Intentar crear una instancia de una clase abstracta (esto generará un error)
    try:
        producto_abstracto = InterfazProducto()
    except TypeError as e:
        print(f"\nError al intentar crear una instancia de clase abstracta: {e}")
