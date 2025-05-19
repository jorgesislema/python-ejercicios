"""
Ejercicio: Encapsulamiento
-------------------------
Este ejercicio demuestra el concepto de encapsulamiento en la programación orientada a objetos,
usando una clase Empleado como ejemplo.
"""

class Empleado:
    """
    Clase que representa un empleado con atributos privados y métodos de acceso.
    """
    def __init__(self, nombre, apellido, salario):
        """
        Constructor de la clase Empleado.
        
        Args:
            nombre (str): Nombre del empleado
            apellido (str): Apellido del empleado
            salario (float): Salario mensual del empleado
        """
        self.__nombre = nombre
        self.__apellido = apellido
        self.__salario = salario
        
    # Getters (métodos de acceso)
    def get_nombre(self):
        """
        Método getter para obtener el nombre del empleado.
        
        Returns:
            str: Nombre del empleado
        """
        return self.__nombre
        
    def get_apellido(self):
        """
        Método getter para obtener el apellido del empleado.
        
        Returns:
            str: Apellido del empleado
        """
        return self.__apellido
        
    def get_salario(self):
        """
        Método getter para obtener el salario del empleado.
        
        Returns:
            float: Salario del empleado
        """
        return self.__salario
        
    def get_nombre_completo(self):
        """
        Método getter para obtener el nombre completo del empleado.
        
        Returns:
            str: Nombre completo del empleado (nombre y apellido)
        """
        return f"{self.__nombre} {self.__apellido}"
        
    # Setters (métodos de modificación)
    def set_nombre(self, nombre):
        """
        Método setter para modificar el nombre del empleado.
        
        Args:
            nombre (str): Nuevo nombre del empleado
        """
        if isinstance(nombre, str) and nombre.strip():
            self.__nombre = nombre
        else:
            print("Error: El nombre debe ser una cadena no vacía")
            
    def set_apellido(self, apellido):
        """
        Método setter para modificar el apellido del empleado.
        
        Args:
            apellido (str): Nuevo apellido del empleado
        """
        if isinstance(apellido, str) and apellido.strip():
            self.__apellido = apellido
        else:
            print("Error: El apellido debe ser una cadena no vacía")
            
    def set_salario(self, salario):
        """
        Método setter para modificar el salario del empleado.
        
        Args:
            salario (float): Nuevo salario del empleado
        """
        if isinstance(salario, (int, float)) and salario >= 0:
            self.__salario = salario
        else:
            print("Error: El salario debe ser un número positivo")
            
    # Métodos adicionales
    def calcular_salario_anual(self):
        """
        Calcula el salario anual del empleado (12 meses).
        
        Returns:
            float: Salario anual del empleado
        """
        return self.__salario * 12
        
    def aumentar_salario(self, porcentaje):
        """
        Aumenta el salario del empleado en el porcentaje especificado.
        
        Args:
            porcentaje (float): Porcentaje de aumento (0-100)
            
        Returns:
            float: Nuevo salario del empleado
        """
        if 0 <= porcentaje <= 100:
            self.__salario += self.__salario * (porcentaje / 100)
            return self.__salario
        else:
            print("Error: El porcentaje debe estar entre 0 y 100")
            return self.__salario
            
    def __str__(self):
        """
        Método que devuelve una representación en string del empleado.
        
        Returns:
            str: Representación en string del empleado
        """
        return f"Empleado: {self.__nombre} {self.__apellido}, Salario: ${self.__salario:.2f}"

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un empleado
    empleado = Empleado("Juan", "Pérez", 3000)
    
    # Usar getters
    print(f"Nombre: {empleado.get_nombre()}")
    print(f"Apellido: {empleado.get_apellido()}")
    print(f"Salario: ${empleado.get_salario():.2f}")
    print(f"Nombre completo: {empleado.get_nombre_completo()}")
    print(f"Salario anual: ${empleado.calcular_salario_anual():.2f}")
    
    # Usar setters
    empleado.set_nombre("Carlos")
    empleado.set_apellido("González")
    empleado.set_salario(3500)
    
    # Verificar cambios
    print("\nDespués de modificar los datos:")
    print(empleado)
    
    # Aumentar salario
    print("\nDespués de un aumento del 10%:")
    empleado.aumentar_salario(10)
    print(empleado)
    
    # Intento de acceso directo (generará un error o comportamiento inesperado)
    try:
        print("\nIntento de acceso directo a atributos privados:")
        print(empleado.__nombre)  # Esto generará un AttributeError
    except AttributeError as e:
        print(f"Error: {e}")
