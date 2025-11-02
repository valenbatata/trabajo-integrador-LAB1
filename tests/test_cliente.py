import pytest
from src.modelos.cliente import Cliente

# Helper con datos válidos por defecto
def build_cliente_valido(
    nombre="Ana", apellido="Perez",
    email="ana@example.com", password="clave123",
    dni="12345678", telefono="1155555555",
    ciudad="Quilmes", pais="Argentina"
):
    return Cliente(nombre, apellido, email, password, dni, telefono, ciudad, pais)

def test_cliente_setters_validos():
    c = build_cliente_valido()
    assert c.get_nombre() == "Ana"
    assert c.get_apellido() == "Perez"
    assert c.get_dni() == "12345678"
    assert c.get_email() == "ana@example.com"
    assert c.get_ciudad() == "Quilmes"
    assert c.get_pais() == "Argentina"

def test_cliente_nombre_invalido():
    with pytest.raises(ValueError):
        build_cliente_valido(nombre="")

def test_cliente_apellido_invalido():
    with pytest.raises(ValueError):
        build_cliente_valido(apellido="P3rez")

def test_cliente_dni_invalido_no_digitos():
    with pytest.raises(ValueError):
        build_cliente_valido(dni="12A45678")

def test_cliente_dni_longitud_invalida():
    with pytest.raises(ValueError):
        build_cliente_valido(dni="123")  # muy corto

def test_cliente_email_invalido():
    with pytest.raises(ValueError):
        build_cliente_valido(email="correo-malo")
