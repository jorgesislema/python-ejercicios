"""
Ejercicio: Clase Animal
-----------------------
Este ejercicio demuestra los conceptos básicos de clases en Python
a través de la implementación de una clase Animal con atributos y métodos.
"""

class Animal:
    """
    Clase que representa un animal genérico.
    """
    def __init__(self, especie, edad, color):
        """
        Constructor de la clase Animal.
        
        Args:
            especie (str): La especie del animal
            edad (int): La edad del animal en años
            color (str): El color del animal
        """
        self.especie = especie
        self.edad = edad
        self.color = color
        
    def hacer_sonido(self):
        """
        Método que simula el sonido que hace el animal.
        """
        print("Este animal hace un sonido genérico")
    
    def describir(self):
        """
        Método que describe al animal.
        """
        print(f"Este animal es un {self.especie} de {self.edad} años y color {self.color}")
    
    def cumplir_anios(self):
        """
        Método que incrementa la edad del animal en un año.
        """
        self.edad += 1
        print(f"¡Feliz cumpleaños! Ahora el {self.especie} tiene {self.edad} años")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancias de la clase Animal
    perro = Animal("perro", 3, "marrón")
    gato = Animal("gato", 2, "blanco")
    
    # Usar métodos de la clase
    perro.describir()
    perro.hacer_sonido()
    perro.cumplir_anios()
    
    gato.describir()
    gato.hacer_sonido()
