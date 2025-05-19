"""
Ejercicio: Composición de Clases
------------------------------
Este ejercicio demuestra el concepto de composición en la programación orientada a objetos,
usando un ejemplo de un sistema de gestión de tienda.
"""

class Direccion:
    """
    Clase que representa una dirección postal.
    """
    def __init__(self, calle, ciudad, codigo_postal, pais):
        """
        Constructor de la clase Direccion.
        
        Args:
            calle (str): Nombre de la calle y número
            ciudad (str): Nombre de la ciudad
            codigo_postal (str): Código postal
            pais (str): Nombre del país
        """
        self.calle = calle
        self.ciudad = ciudad
        self.codigo_postal = codigo_postal
        self.pais = pais
    
    def __str__(self):
        """
        Representación en string de la dirección.
        
        Returns:
            str: Representación formateada de la dirección
        """
        return f"{self.calle}, {self.ciudad}, CP {self.codigo_postal}, {self.pais}"

class Producto:
    """
    Clase que representa un producto en la tienda.
    """
    def __init__(self, codigo, nombre, precio, stock=0):
        """
        Constructor de la clase Producto.
        
        Args:
            codigo (str): Código único del producto
            nombre (str): Nombre del producto
            precio (float): Precio del producto
            stock (int, opcional): Cantidad en stock, por defecto 0
        """
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def __str__(self):
        """
        Representación en string del producto.
        
        Returns:
            str: Representación formateada del producto
        """
        return f"Producto: {self.nombre} (Código: {self.codigo}) - Precio: ${self.precio} - Stock: {self.stock}"

class Cliente:
    """
    Clase que representa un cliente de la tienda.
    """
    def __init__(self, id_cliente, nombre, email, direccion):
        """
        Constructor de la clase Cliente.
        
        Args:
            id_cliente (str): Identificador único del cliente
            nombre (str): Nombre completo del cliente
            email (str): Correo electrónico del cliente
            direccion (Direccion): Objeto Direccion con la dirección del cliente
        """
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.direccion = direccion  # Composición: Cliente contiene una Direccion
    
    def __str__(self):
        """
        Representación en string del cliente.
        
        Returns:
            str: Representación formateada del cliente
        """
        return f"Cliente: {self.nombre} (ID: {self.id_cliente})\nEmail: {self.email}\nDirección: {self.direccion}"

class LineaPedido:
    """
    Clase que representa una línea de un pedido (un producto y su cantidad).
    """
    def __init__(self, producto, cantidad):
        """
        Constructor de la clase LineaPedido.
        
        Args:
            producto (Producto): Objeto Producto pedido
            cantidad (int): Cantidad del producto
        """
        self.producto = producto  # Composición: LineaPedido contiene un Producto
        self.cantidad = cantidad
    
    def calcular_subtotal(self):
        """
        Calcula el subtotal de la línea (precio * cantidad).
        
        Returns:
            float: Subtotal de la línea
        """
        return self.producto.precio * self.cantidad
    
    def __str__(self):
        """
        Representación en string de la línea de pedido.
        
        Returns:
            str: Representación formateada de la línea
        """
        return f"{self.cantidad} x {self.producto.nombre} (${self.producto.precio}) = ${self.calcular_subtotal()}"

class Pedido:
    """
    Clase que representa un pedido completo.
    """
    def __init__(self, numero_pedido, cliente):
        """
        Constructor de la clase Pedido.
        
        Args:
            numero_pedido (str): Número identificativo del pedido
            cliente (Cliente): Objeto Cliente que realiza el pedido
        """
        self.numero_pedido = numero_pedido
        self.cliente = cliente  # Composición: Pedido contiene un Cliente
        self.lineas = []  # Composición: Pedido contiene una lista de LineaPedido
        self.pagado = False
    
    def agregar_producto(self, producto, cantidad):
        """
        Agrega un producto al pedido.
        
        Args:
            producto (Producto): Objeto Producto a agregar
            cantidad (int): Cantidad del producto
            
        Returns:
            bool: True si se agregó con éxito, False en caso contrario
        """
        if producto.stock >= cantidad:
            linea = LineaPedido(producto, cantidad)
            self.lineas.append(linea)
            producto.stock -= cantidad
            return True
        else:
            print(f"Error: No hay suficiente stock de {producto.nombre}")
            return False
    
    def calcular_total(self):
        """
        Calcula el total del pedido.
        
        Returns:
            float: Total del pedido
        """
        return sum(linea.calcular_subtotal() for linea in self.lineas)
    
    def marcar_como_pagado(self):
        """
        Marca el pedido como pagado.
        """
        self.pagado = True
        print(f"El pedido {self.numero_pedido} ha sido marcado como pagado")
    
    def __str__(self):
        """
        Representación en string del pedido.
        
        Returns:
            str: Representación formateada del pedido
        """
        estado = "PAGADO" if self.pagado else "PENDIENTE"
        resultado = [
            f"PEDIDO #{self.numero_pedido} - {estado}",
            f"Cliente: {self.cliente.nombre}",
            f"Dirección de envío: {self.cliente.direccion}",
            "\nDETALLES DEL PEDIDO:",
            "-" * 40
        ]
        
        for linea in self.lineas:
            resultado.append(str(linea))
        
        resultado.append("-" * 40)
        resultado.append(f"TOTAL: ${self.calcular_total()}")
        
        return "\n".join(resultado)

class Tienda:
    """
    Clase que representa una tienda completa.
    """
    def __init__(self, nombre, direccion):
        """
        Constructor de la clase Tienda.
        
        Args:
            nombre (str): Nombre de la tienda
            direccion (Direccion): Objeto Direccion con la dirección de la tienda
        """
        self.nombre = nombre
        self.direccion = direccion  # Composición: Tienda contiene una Direccion
        self.productos = {}  # Diccionario de productos indexado por código
        self.clientes = {}  # Diccionario de clientes indexado por ID
        self.pedidos = []  # Lista de pedidos
    
    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario de la tienda.
        
        Args:
            producto (Producto): Objeto Producto a agregar
        """
        self.productos[producto.codigo] = producto
        print(f"Producto '{producto.nombre}' agregado al inventario")
    
    def buscar_producto(self, codigo):
        """
        Busca un producto por su código.
        
        Args:
            codigo (str): Código del producto
            
        Returns:
            Producto: Objeto Producto si se encuentra, None en caso contrario
        """
        return self.productos.get(codigo)
    
    def registrar_cliente(self, cliente):
        """
        Registra un cliente en la tienda.
        
        Args:
            cliente (Cliente): Objeto Cliente a registrar
        """
        self.clientes[cliente.id_cliente] = cliente
        print(f"Cliente '{cliente.nombre}' registrado correctamente")
    
    def buscar_cliente(self, id_cliente):
        """
        Busca un cliente por su ID.
        
        Args:
            id_cliente (str): ID del cliente
            
        Returns:
            Cliente: Objeto Cliente si se encuentra, None en caso contrario
        """
        return self.clientes.get(id_cliente)
    
    def crear_pedido(self, id_cliente):
        """
        Crea un nuevo pedido para un cliente.
        
        Args:
            id_cliente (str): ID del cliente
            
        Returns:
            Pedido: Objeto Pedido creado o None si el cliente no existe
        """
        cliente = self.buscar_cliente(id_cliente)
        if cliente:
            numero_pedido = f"P{len(self.pedidos) + 1:04d}"
            pedido = Pedido(numero_pedido, cliente)
            self.pedidos.append(pedido)
            print(f"Pedido {numero_pedido} creado para {cliente.nombre}")
            return pedido
        else:
            print(f"Error: Cliente con ID {id_cliente} no encontrado")
            return None
    
    def __str__(self):
        """
        Representación en string de la tienda.
        
        Returns:
            str: Representación formateada de la tienda
        """
        return f"Tienda: {self.nombre}\nDirección: {self.direccion}\nProductos en inventario: {len(self.productos)}\nClientes registrados: {len(self.clientes)}\nPedidos realizados: {len(self.pedidos)}"

# Ejemplo de uso
if __name__ == "__main__":
    # Crear dirección para la tienda
    direccion_tienda = Direccion("Calle Principal 123", "Madrid", "28001", "España")
    
    # Crear la tienda
    mi_tienda = Tienda("Tienda Python", direccion_tienda)
    
    # Agregar productos
    producto1 = Producto("P001", "Teclado", 29.99, 10)
    producto2 = Producto("P002", "Ratón", 19.99, 15)
    producto3 = Producto("P003", "Monitor", 199.99, 5)
    
    mi_tienda.agregar_producto(producto1)
    mi_tienda.agregar_producto(producto2)
    mi_tienda.agregar_producto(producto3)
    
    # Registrar cliente
    direccion_cliente = Direccion("Calle Secundaria 456", "Barcelona", "08001", "España")
    cliente1 = Cliente("C001", "Ana García", "ana@example.com", direccion_cliente)
    mi_tienda.registrar_cliente(cliente1)
    
    # Crear pedido
    pedido1 = mi_tienda.crear_pedido("C001")
    
    if pedido1:
        # Agregar productos al pedido
        pedido1.agregar_producto(producto1, 1)
        pedido1.agregar_producto(producto2, 2)
        pedido1.agregar_producto(producto3, 1)
        
        # Mostrar pedido
        print("\nResumen del pedido:")
        print(pedido1)
        
        # Marcar como pagado
        pedido1.marcar_como_pagado()
        
        # Mostrar pedido actualizado
        print("\nResumen del pedido actualizado:")
        print(pedido1)
    
    # Mostrar información de la tienda
    print("\nInformación de la tienda:")
    print(mi_tienda)
