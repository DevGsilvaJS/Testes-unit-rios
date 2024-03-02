import pytest

def calcular_salario_com_desconto_inss(valor_aula, numero_aulas, percentual_inss):
    valor_desconto = ((valor_aula * numero_aulas) / 100) * percentual_inss
    salario_liquido = valor_aula * numero_aulas
    return salario_liquido - valor_desconto


def test_calcular_salario_case_01():
    assert calcular_salario_com_desconto_inss(6.25, 160, 1.3) == 987.00

def test_calcular_salario_case_02():
    assert calcular_salario_com_desconto_inss(20.5, 240, 1.7) == 4836.36

def test_calcular_salario_case_03():
    assert calcular_salario_com_desconto_inss(13.9, 200, 6.48) == pytest.approx(2599.86, 0.01)
