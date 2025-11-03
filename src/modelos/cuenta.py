from __future__ import annotations
from .cliente import Cliente
from .transaccion import Transaccion
from datetime import datetime

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
        
    
        self.__transacciones: list[Transaccion] = []

    # --------- GETTERS ---------
    def get_numero_cuenta(self) -> str:
        return self.__numero_cuenta

    def get_saldo(self) -> float:
        return self.__saldo

    def get_cliente(self) -> Cliente:
        return self.__cliente_asociado

    def get_transacciones(self) -> list[Transaccion]:
        #Devuelve una copia de la lista de transacciones.
        return self.__transacciones.copy()

    # --------- MÉTODOS PÚBLICOS (Interfaz) ---------

    def ingresar_dinero(self, monto: float) -> bool:

        try:
            # Dejamos la validación del monto y la actualización del saldo
            self._depositar(monto)
            
            # Si depositar no lanzó error, registramos la transacción
            nueva_tx = Transaccion(
                tipo="depósito", 
                monto=monto, 
                fecha=datetime.now()
            )
            self.__transacciones.append(nueva_tx)
            
            # print(f"DEBUG: Depósito de ${monto:.2f} OK. Saldo: ${self.__saldo:.2f}")
            return True

        except ValueError as e:
            # Capturamos errores de validación y mostramos mensaje
            print(f"Error al ingresar dinero: {e}")
            return False
        except Exception as e:
            # Captura genérica para otros posibles errores
            print(f"Error inesperado al ingresar dinero: {e}")
            return False

    def retirar_dinero(self, monto: float) -> bool:

        try:
            # Dejamos la validación del monto y la actualización del saldo
            self._retirar(monto)
            
            # Si retirar no lanzó error, registramos la transacción
            nueva_tx = Transaccion(
                    tipo="retiro", 
                    monto=monto, 
                    fecha=datetime.now()
                )
            self.__transacciones.append(nueva_tx)
            
                # print(f"DEBUG: Retiro de ${monto:.2f} OK. Saldo: ${self.__saldo:.2f}")
            return True

        except ValueError as e:
                # Capturamos errores de validación y mostramos mensaje
                print(f"Error al retirar dinero: {e}")
                return False
        except Exception as e:
                # Captura genérica para otros posibles errores
                print(f"Error inesperado al retirar dinero: {e}")
                return False

    # --------- MÉTODOS PROTEGIDOS (Implementación) ---------
    
    def _depositar(self, monto: float) -> None:
      
        try:
            monto = float(monto)
        except Exception as e:
            raise ValueError(f"Monto inválido: {e}") from e
            
        if monto <= 0:
            raise ValueError("El depósito debe ser un monto positivo.")
            
        self.__saldo += monto

    def _retirar(self, monto: float) -> None:
        
        # Lógica interna de retiro. Valida y actualiza el saldo.
        
        try:
            monto = float(monto)
        except Exception as e:
            raise ValueError(f"Monto inválido: {e}") from e
            
        if monto <= 0:
            raise ValueError("El retiro debe ser un monto positivo.")
            
        # Validación de saldo suficiente 
        if monto > self.__saldo:
            raise ValueError("Fondos insuficientes.")
            
        self.__saldo -= monto

    def __repr__(self) -> str:
     
        return f"Cuenta({self.__numero_cuenta!r}, saldo={self.__saldo:.2f}, cliente={self.__cliente_asociado.get_apellido()!r})"