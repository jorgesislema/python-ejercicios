"""
Ejercicio: Clase CuentaBancaria
-------------------------------
Este ejercicio implementa una clase para simular una cuenta bancaria
con operaciones básicas como depósito y retiro de dinero.
"""

class CuentaBancaria:
    """
    Clase que simula una cuenta bancaria básica.
    """
    def __init__(self, numero_cuenta, titular, saldo=0.0):
        """
        Constructor de la clase CuentaBancaria.
        
        Args:
            numero_cuenta (str): Número de identificación de la cuenta
            titular (str): Nombre del titular de la cuenta
            saldo (float, opcional): Saldo inicial de la cuenta, por defecto 0.0
        """
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, cantidad):
        """
        Método para depositar dinero en la cuenta.
        
        Args:
            cantidad (float): Cantidad a depositar
            
        Returns:
            float: El nuevo saldo de la cuenta
        """
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se depositaron ${cantidad}. Nuevo saldo: ${self.saldo}")
        else:
            print("La cantidad a depositar debe ser positiva")
        return self.saldo
        
    def retirar(self, cantidad):
        """
        Método para retirar dinero de la cuenta.
        
        Args:
            cantidad (float): Cantidad a retirar
            
        Returns:
            float: El nuevo saldo de la cuenta o None si el retiro falló
        """
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Se retiraron ${cantidad}. Nuevo saldo: ${self.saldo}")
                return self.saldo
            else:
                print(f"Saldo insuficiente. Saldo actual: ${self.saldo}")
                return None
        else:
            print("La cantidad a retirar debe ser positiva")
            return None
            
    def consultar_saldo(self):
        """
        Método para consultar el saldo actual de la cuenta.
        
        Returns:
            float: El saldo actual de la cuenta
        """
        print(f"Saldo actual de la cuenta {self.numero_cuenta}: ${self.saldo}")
        return self.saldo
        
    def __str__(self):
        """
        Método que devuelve una representación en string de la cuenta bancaria.
        
        Returns:
            str: Representación en string de la cuenta bancaria
        """
        return f"Cuenta: {self.numero_cuenta}, Titular: {self.titular}, Saldo: ${self.saldo}"

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una cuenta bancaria
    mi_cuenta = CuentaBancaria("123456789", "Juan Pérez", 1000)
    
    # Realizar operaciones
    print(mi_cuenta)
    mi_cuenta.consultar_saldo()
    mi_cuenta.depositar(500)
    mi_cuenta.retirar(200)
    mi_cuenta.retirar(2000)  # Intentar retirar más de lo que hay
    print(mi_cuenta)
