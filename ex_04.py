import pytest

def calcular_valor_com_gorjeta(valor_despesa, percentual_gorjeta=10):
    valor_gorjeta = (valor_despesa / 100) * percentual_gorjeta
    valor_total_conta = valor_despesa + valor_gorjeta
    return valor_total_conta, valor_gorjeta


def test_calcular_valor_com_gorjeta_case_01():
    assert calcular_valor_com_gorjeta(75.00) == (82.50, 7.50)

def test_calcular_valor_com_gorjeta_case_02():
    assert calcular_valor_com_gorjeta(125, 15) == (143.75, 18.75)

def test_calcular_valor_com_gorjeta_case_03():
    assert calcular_valor_com_gorjeta(350.87, 10) == pytest.approx((385.96, 35.09), 0.01)
