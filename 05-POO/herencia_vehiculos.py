"""
Ejercicio: Herencia de Clases
----------------------------
Este ejercicio demuestra el concepto de herencia en la programación orientada a objetos,
usando vehículos como ejemplo.
"""

class Vehiculo:
    """
    Clase base que representa un vehículo genérico.
    """
    def __init__(self, marca, modelo, anio):
        """
        Constructor de la clase Vehiculo.
        
        Args:
            marca (str): Marca del vehículo
            modelo (str): Modelo del vehículo
            anio (int): Año de fabricación
        """
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.encendido = False
        
    def encender(self):
        """
        Método para encender el vehículo.
        """
        if not self.encendido:
            self.encendido = True
            print(f"El {self.marca} {self.modelo} ha sido encendido")
        else:
            print(f"El {self.marca} {self.modelo} ya está encendido")
    
    def apagar(self):
        """
        Método para apagar el vehículo.
        """
        if self.encendido:
            self.encendido = False
            print(f"El {self.marca} {self.modelo} ha sido apagado")
        else:
            print(f"El {self.marca} {self.modelo} ya está apagado")
            
    def describir(self):
        """
        Método que describe el vehículo.
        """
        estado = "encendido" if self.encendido else "apagado"
        return f"{self.marca} {self.modelo} ({self.anio}), {estado}"

class Coche(Vehiculo):
    """
    Clase que hereda de Vehiculo y representa un coche específicamente.
    """
    def __init__(self, marca, modelo, anio, puertas):
        """
        Constructor de la clase Coche.
        
        Args:
            marca (str): Marca del coche
            modelo (str): Modelo del coche
            anio (int): Año de fabricación
            puertas (int): Número de puertas
        """
        # Llamada al constructor de la clase padre
        super().__init__(marca, modelo, anio)
        self.puertas = puertas
        self.velocidad = 0
        
    def acelerar(self, incremento):
        """
        Método para acelerar el coche.
        
        Args:
            incremento (int): Incremento de velocidad en km/h
        """
        if self.encendido:
            self.velocidad += incremento
            print(f"El coche acelera a {self.velocidad} km/h")
        else:
            print("No puedes acelerar un coche apagado")
            
    def frenar(self, decremento):
        """
        Método para frenar el coche.
        
        Args:
            decremento (int): Decremento de velocidad en km/h
        """
        if self.encendido and self.velocidad > 0:
            self.velocidad = max(0, self.velocidad - decremento)
            print(f"El coche frena a {self.velocidad} km/h")
        else:
            print("No puedes frenar un coche apagado o que ya está detenido")
            
    def describir(self):
        """
        Método que describe el coche (sobreescribe el método de la clase padre).
        """
        descripcion_base = super().describir()
        return f"{descripcion_base}, {self.puertas} puertas, velocidad: {self.velocidad} km/h"

class Moto(Vehiculo):
    """
    Clase que hereda de Vehiculo y representa una moto específicamente.
    """
    def __init__(self, marca, modelo, anio, cilindrada):
        """
        Constructor de la clase Moto.
        
        Args:
            marca (str): Marca de la moto
            modelo (str): Modelo de la moto
            anio (int): Año de fabricación
            cilindrada (int): Cilindrada del motor en cc
        """
        super().__init__(marca, modelo, anio)
        self.cilindrada = cilindrada
        
    def hacer_caballito(self):
        """
        Método específico para hacer un caballito con la moto.
        """
        if self.encendido:
            print(f"La moto {self.marca} {self.modelo} está haciendo un caballito")
        else:
            print("No puedes hacer un caballito con la moto apagada")
            
    def describir(self):
        """
        Método que describe la moto (sobreescribe el método de la clase padre).
        """
        descripcion_base = super().describir()
        return f"{descripcion_base}, {self.cilindrada}cc"

# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancias
    vehiculo = Vehiculo("Genérico", "Base", 2020)
    coche = Coche("Toyota", "Corolla", 2021, 4)
    moto = Moto("Honda", "CBR", 2022, 600)
    
    # Usar los métodos
    print(vehiculo.describir())
    vehiculo.encender()
    print(vehiculo.describir())
    
    print("\n" + "-"*50 + "\n")
    
    print(coche.describir())
    coche.encender()
    coche.acelerar(60)
    coche.frenar(20)
    print(coche.describir())
    
    print("\n" + "-"*50 + "\n")
    
    print(moto.describir())
    moto.encender()
    moto.hacer_caballito()
    print(moto.describir())
