from .cuenta import Cuenta

class CajaDeAhorro(Cuenta):

    def __init__(self, numero_cuenta: str, cliente_asociado, saldo_inicial: float = 0.0):
        super().__init__(numero_cuenta, cliente_asociado, saldo_inicial)

    # Polimorfismo: si quisieras, podrías redefinir el retiro para reglas específicas.
    # En este caso, la base ya bloquea extraer más que el saldo, por lo que reutilizamos.
    def depositar(self, monto: float) -> None:
        self._depositar(monto)

    def retirar(self, monto: float) -> None:
        # La base ya valida que no se pueda retirar más que el saldo disponible.
        self._retirar(monto)
