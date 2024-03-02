import pytest

def calcular_valor_com_desconto(valor_produto, percentual_desconto):
    desconto = (valor_produto / 100) * percentual_desconto
    valor_com_desconto = valor_produto - desconto
    return valor_com_desconto, desconto


def test_calcular_valor_com_desconto_case_01():
    assert calcular_valor_com_desconto(100, 9) == (91.00, 9.00)

def test_calcular_valor_com_desconto_case_02():
    assert calcular_valor_com_desconto(1500, 9) == (1365.00, 135.00)

def test_calcular_valor_com_desconto_case_03():
    assert calcular_valor_com_desconto(60000, 9) == pytest.approx((54600.00, 5400.00), 0.01)
