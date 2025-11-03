import pytest
from src.modelos.cliente import Cliente
from src.modelos.cuenta import Cuenta

def _cli():
    return Cliente("Ana","Perez","ana@example.com","clave123","12345678","1155555555","Quilmes","Argentina")

def test_cuenta_base_getters():
    cli = _cli()
    cta = Cuenta("CA-0001", cli, 1000.0)
    assert cta.get_numero_cuenta() == "CA-0001"
    assert cta.get_saldo() == 1000.0
    assert cta.get_cliente() is cli

def test_cuenta_base_validaciones_constructor():
    cli = _cli()
    with pytest.raises(ValueError):
        Cuenta("", cli, 0.0)                # numero de cuenta vacío
    with pytest.raises(ValueError):
        Cuenta("CA-0001", "no-cliente", 0)  # cliente no es instancia de Cliente
    with pytest.raises(ValueError):
        Cuenta("CA-0001", cli, -10)         # saldo negativo
