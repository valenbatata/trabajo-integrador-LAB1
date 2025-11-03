from __future__ import annotations
from .cliente import Cliente

class Cuenta:
   

    def __init__(self, numero_cuenta: str, cliente_asociado: Cliente, saldo_inicial: float = 0.0):
        # Validación número de cuenta (string no vacío)
        if not isinstance(numero_cuenta, str) or not numero_cuenta.strip():
            raise ValueError("El número de cuenta debe ser una cadena no vacía.")
        self.__numero_cuenta = numero_cuenta.strip()

        # Validación cliente
        if not isinstance(cliente_asociado, Cliente):
            raise ValueError("cliente_asociado debe ser instancia de Cliente.")
        self.__cliente_asociado = cliente_asociado

        # Validación saldo
        try:
            saldo_inicial = float(saldo_inicial)
        except Exception as e:
            raise ValueError(f"Saldo inicial inválido: {e}") from e
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")
        self.__saldo = saldo_inicial

    # --------- GETTERS ---------
    def get_numero_cuenta(self) -> str:
        return self.__numero_cuenta

    def get_saldo(self) -> float:
        return self.__saldo

    def get_cliente(self) -> Cliente:
        return self.__cliente_asociado

    
    def _depositar(self, monto: float) -> None:
        try:
            monto = float(monto)
        except Exception as e:
            raise ValueError(f"Monto inválido: {e}") from e
        if monto <= 0:
            raise ValueError("El depósito debe ser mayor a 0.")
        self.__saldo += monto

    def _retirar(self, monto: float) -> None:
        try:
            monto = float(monto)
        except Exception as e:
            raise ValueError(f"Monto inválido: {e}") from e
        if monto <= 0:
            raise ValueError("El retiro debe ser mayor a 0.")
        # La política de sobregiro se define en subclases (polimorfismo)
        if monto > self.__saldo:
            raise ValueError("Fondos insuficientes en cuenta base.")
        self.__saldo -= monto

    def __repr__(self) -> str:
        return f"Cuenta({self.__numero_cuenta!r}, saldo={self.__saldo:.2f}, cliente={self.__cliente_asociado!r})"
