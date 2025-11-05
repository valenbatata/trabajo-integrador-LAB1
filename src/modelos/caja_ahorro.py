from .cuenta import Cuenta
from .cliente import Cliente
from datetime import datetime

class CajaAhorro(Cuenta):
    
    def __init__(self, numero_cuenta: str, cliente_asociado: Cliente, saldo_inicial: float = 0.0, interes: float = 0.02):
        
        # Llama al constructor de la clase padre (Cuenta)
        super().__init__(numero_cuenta, cliente_asociado, saldo_inicial)
        
        # Añade su propio atributo
        if not isinstance(interes, (int, float)) or interes < 0:
            raise ValueError("El interés debe ser un número positivo.")
        self.__interes = interes

    # --- Getters y Setters Propios ---
    
    def get_interes(self) -> float:
        """Devuelve la tasa de interés (ej. 0.02 para 2%)."""
        return self.__interes

    def set_interes(self, nuevo_interes: float):
        if not isinstance(nuevo_interes, (int, float)) or nuevo_interes < 0:
            raise ValueError("El interés debe ser un número positivo.")
        self.__interes = nuevo_interes

    # --- Métodos Propios ---    
    def aplicar_interes_mensual(self):
        """Calcula y deposita el interés en la cuenta."""
        if self.get_saldo() > 0:
            interes_generado = self.get_saldo() * self.__interes
            
            # Reutilizamos el método '_depositar' heredado de Cuenta
            self.ingresar_dinero(interes_generado) 
            
            print(f"DEBUG: Interés de ${interes_generado:.2f} aplicado.")
            return True
        return False

    def __repr__(self) -> str:
        """Representación para debugging."""
        return f"CajaAhorro(cuenta={self.get_numero_cuenta()!r}, saldo={self.get_saldo():.2f}, interes={self.__interes})"
