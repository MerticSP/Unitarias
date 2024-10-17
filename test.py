import pytest
from calculadora import suma

def test_suma_enteros():
    assert suma(2, 3) == 5

def test_suma_decimales():
    assert suma(2.5, 3.5) == 6.0

def test_suma_entero_y_decimal():
    assert suma(2, 3.5) == 5.5

def test_manejo_error_texto_segundo_parametro():
    assert suma(2, "texto") == "error"

def test_manejo_error_texto_primer_parametro():
    assert suma("texto", 2) == "error"

def test_manejo_error_texto_ambos_parametros():
    assert suma("texto", "otro texto") == "error"

def test_manejo_error_numero_mal_formado():
    assert suma(2, "3.5abc") == "error"

def test_suma_cadenas_validas():
    assert suma("4", "6") == 10

def test_manejo_error_cadenas_no_numericas():
    assert suma("cuatro", "seis") == "error"

if __name__ == "__main__":
    pytest.main()

