"""
Ejercicio: Patrones de Diseño - Singleton
---------------------------------------
Este ejercicio demuestra el patrón de diseño Singleton en Python.
El patrón Singleton garantiza que una clase tenga una única instancia
y proporciona un punto de acceso global a ella.
"""

class Configuracion:
    """
    Implementación del patrón Singleton para una clase de configuración.
    Permite tener una única instancia de configuración en toda la aplicación.
    """
    
    # Variable de clase que almacenará la única instancia
    _instancia = None
    
    def __new__(cls):
        """
        Método especial que controla la creación de la instancia.
        Sobreescrito para implementar el patrón Singleton.
        
        Returns:
            Configuracion: La única instancia de la clase Configuracion
        """
        # Si no existe una instancia, la creamos
        if cls._instancia is None:
            # Llamar a __new__ de la clase base para crear la instancia
            cls._instancia = super(Configuracion, cls).__new__(cls)
            # Inicializar con valores por defecto
            cls._instancia._inicializar_por_defecto()
        return cls._instancia
    
    def _inicializar_por_defecto(self):
        """
        Método privado para inicializar con valores por defecto.
        """
        self.modo_debug = False
        self.tema = "claro"
        self.idioma = "es"
        self.tamano_fuente = 12
        self.ruta_datos = "./datos"
        self.tiempo_espera = 30
    
    def establecer_configuracion(self, **kwargs):
        """
        Establece los valores de configuración especificados.
        
        Args:
            **kwargs: Pares clave-valor de configuración
        """
        for clave, valor in kwargs.items():
            if hasattr(self, clave):
                setattr(self, clave, valor)
                print(f"Configuración actualizada: {clave} = {valor}")
            else:
                print(f"Error: '{clave}' no es una opción de configuración válida")
    
    def obtener_configuracion(self, clave):
        """
        Obtiene un valor de configuración específico.
        
        Args:
            clave (str): Nombre de la configuración a obtener
            
        Returns:
            any: Valor de la configuración o None si no existe
        """
        if hasattr(self, clave):
            return getattr(self, clave)
        else:
            print(f"Error: '{clave}' no es una opción de configuración válida")
            return None
    
    def mostrar_configuracion(self):
        """
        Muestra toda la configuración actual.
        """
        print("\nCONFIGURACIÓN ACTUAL:")
        print("-" * 25)
        atributos = [attr for attr in dir(self) if not attr.startswith("_") and not callable(getattr(self, attr))]
        for attr in atributos:
            print(f"{attr} = {getattr(self, attr)}")

class BaseDatos:
    """
    Otra implementación de Singleton para una conexión a base de datos.
    """
    
    # Variable de clase que almacenará la única instancia
    _instancia = None
    
    def __new__(cls, *args, **kwargs):
        """
        Método especial que controla la creación de la instancia.
        
        Returns:
            BaseDatos: La única instancia de la clase BaseDatos
        """
        if cls._instancia is None:
            cls._instancia = super(BaseDatos, cls).__new__(cls)
            cls._instancia.conectado = False
        return cls._instancia
    
    def __init__(self, host="localhost", puerto=3306, usuario="root", contrasena=""):
        """
        Constructor de la clase BaseDatos.
        Se llama cada vez que se crea una "nueva" instancia.
        
        Args:
            host (str, opcional): Nombre del host
            puerto (int, opcional): Puerto para la conexión
            usuario (str, opcional): Nombre de usuario
            contrasena (str, opcional): Contraseña
        """
        # Solo inicializamos una vez
        if not hasattr(self, "inicializado") or not self.inicializado:
            self.host = host
            self.puerto = puerto
            self.usuario = usuario
            self.contrasena = contrasena
            self.conectado = False
            self.inicializado = True
    
    def conectar(self):
        """
        Simula la conexión a la base de datos.
        
        Returns:
            bool: True si la conexión fue exitosa
        """
        if not self.conectado:
            print(f"Conectando a la base de datos en {self.host}:{self.puerto}")
            # Aquí iría el código real de conexión
            self.conectado = True
            return True
        else:
            print("Ya existe una conexión activa a la base de datos")
            return False
    
    def desconectar(self):
        """
        Simula la desconexión de la base de datos.
        
        Returns:
            bool: True si la desconexión fue exitosa
        """
        if self.conectado:
            print("Cerrando conexión a la base de datos")
            # Aquí iría el código real de desconexión
            self.conectado = False
            return True
        else:
            print("No hay una conexión activa para cerrar")
            return False
    
    def ejecutar_consulta(self, consulta):
        """
        Simula la ejecución de una consulta SQL.
        
        Args:
            consulta (str): Consulta SQL a ejecutar
            
        Returns:
            dict: Resultado simulado de la consulta
        """
        if self.conectado:
            print(f"Ejecutando consulta: {consulta}")
            # Aquí iría el código real de ejecución de consulta
            return {"status": "success", "data": ["resultado1", "resultado2"]}
        else:
            print("Error: No hay una conexión activa a la base de datos")
            return {"status": "error", "message": "No hay conexión"}

# Ejemplo de uso
if __name__ == "__main__":
    # Demostración de Singleton con la clase Configuracion
    print("== DEMOSTRACIÓN DE SINGLETON CON CONFIGURACIÓN ==")
    
    # Crear primera instancia
    config1 = Configuracion()
    print("Configuración inicial:")
    config1.mostrar_configuracion()
    
    # Modificar configuración
    config1.establecer_configuracion(
        tema="oscuro",
        idioma="en",
        tamano_fuente=14
    )
    
    # Crear "segunda" instancia (que en realidad es la misma)
    config2 = Configuracion()
    print("\n¿config1 es config2?", config1 is config2)  # Debería ser True
    
    # Verificar que la configuración modificada persiste
    print("\nConfiguración desde la segunda instancia:")
    config2.mostrar_configuracion()
    
    print("\n" + "=" * 50)
    
    # Demostración de Singleton con la clase BaseDatos
    print("\n== DEMOSTRACIÓN DE SINGLETON CON BASE DE DATOS ==")
    
    # Crear primera instancia con parámetros
    db1 = BaseDatos(host="servidor1", puerto=5432, usuario="admin")
    db1.conectar()
    db1.ejecutar_consulta("SELECT * FROM usuarios")
    
    # Crear "segunda" instancia con parámetros diferentes (que se ignoran)
    db2 = BaseDatos(host="servidor2", usuario="otro_usuario")
    print("\n¿db1 es db2?", db1 is db2)  # Debería ser True
    
    # La segunda instancia usa la conexión ya establecida
    resultado = db2.ejecutar_consulta("SELECT * FROM productos")
    print(f"Resultado: {resultado}")
    
    # Desconectar
    db1.desconectar()
