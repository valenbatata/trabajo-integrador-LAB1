import pytest
from src.modelos.cliente import Cliente
from src.modelos.caja_ahorro import CajaDeAhorro

def _cli():
    return Cliente("Ana","Perez","ana@example.com","clave123","12345678","1155555555","Quilmes","Argentina")

def test_caja_ahorro_operaciones_basicas():
    cli = _cli()
    ca = CajaDeAhorro("CA-0002", cli, 100.0)

    ca.depositar(50)
    assert ca.get_saldo() == 150.0

    ca.retirar(40)
    assert ca.get_saldo() == 110.0

def test_caja_ahorro_no_permite_descubierto():
    cli = _cli()
    ca = CajaDeAhorro("CA-0003", cli, 50.0)
    with pytest.raises(ValueError):
        ca.retirar(60)  # más que el saldo

