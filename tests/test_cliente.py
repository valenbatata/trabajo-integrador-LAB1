from src.modelos.cliente import Cliente


def test_mostrar_datos_formato_correcto():
    
    # Objeto de prueba
    cliente_prueba = Cliente(nombre="Alan", apellido="Gonzales", dni="987654" , email="alangonzales1@gmail.com", password="123456", telefono="299648551", ciudad="cipolletti", pais="argentina")
    
    # Resultado esperado
    resultado_esperado = "Cliente: Gonzales, Alan\nDNI: 987654"

    # metodo a probar
    resultado_obtenido = cliente_prueba.mostrar_datos()

    # verificacion del resultado
    assert resultado_obtenido == resultado_esperado