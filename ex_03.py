import pytest

def calcular_valor_com_promocao(valor_original, valor_desconto):
    valor_com_promocao = valor_original - valor_desconto
    return valor_com_promocao


def test_calcular_valor_com_promocao_case_01():
    assert calcular_valor_com_promocao(500.0, 50.00) == 450.00

def test_calcular_valor_com_promocao_case_02():
    assert calcular_valor_com_promocao(10500.00, 500.00) == 10000.00

def test_calcular_valor_com_promocao_case_03():
    assert calcular_valor_com_promocao(90.00, 0.80) == 89.20
