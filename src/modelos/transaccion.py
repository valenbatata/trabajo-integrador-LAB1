from datetime import datetime

class Transaccion:
  
  
    def __init__(self, tipo: str, monto: float, fecha: datetime):
        
        # --- Validación de Atributos ---

        # Validación tipo
        tipo_limpio = str(tipo).strip().lower()
        if tipo_limpio not in ("depósito", "retiro"):
            raise ValueError("El tipo de transacción debe ser 'depósito' o 'retiro'.")
        
        # Validación monto
        try:
            monto = float(monto)
        except Exception as e:
            raise ValueError(f"Monto inválido para la transacción: {e}") from e
        
        if monto <= 0:
            raise ValueError("El monto de la transacción debe ser positivo.")

        # Validación fecha
        if not isinstance(fecha, datetime):
            raise ValueError("La fecha debe ser un objeto datetime válido.")

        # --- Asignación de Atributos Privados ---
        # Requisito: Encapsulamiento 
        self.__tipo = tipo_limpio
        self.__monto = monto
        self.__fecha = fecha

    # --------- GETTERS ---------
    # Requisito: Acceso mediante getters 

    def get_tipo(self) -> str:
        """Devuelve el tipo de transacción (depósito o retiro)."""
        return self.__tipo

    def get_monto(self) -> float:
        """Devuelve el monto de la transacción."""
        return self.__monto

    def get_fecha(self) -> datetime:
        """Devuelve la fecha y hora de la transacción."""
        return self.__fecha

    def __repr__(self) -> str:
        """Representación textual de la instancia para debugging."""
        return f"Transaccion(tipo={self.__tipo!r}, monto={self.__monto:.2f}, fecha={self.__fecha.isoformat()})"