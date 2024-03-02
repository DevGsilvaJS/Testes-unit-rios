import pytest

def desconto_inss(vlr_aula, nro_aulas, vlr_inss):
    vlr_desconto = ((vlr_aula * nro_aulas) / 100) * vlr_inss
    vlr_salario = vlr_aula * nro_aulas
    return vlr_salario - vlr_desconto

def test_calc_salario_case_01():
    assert desconto_inss(6.25, 160, 1.3) == (987.00)

def test_calc_salario_case_02():
    assert desconto_inss(20.5, 240, 1.7) == (4836.36)

def test_calc_salario_case_03():
    assert desconto_inss(13.9, 200, 6.48) == pytest.approx(2599.86, 0.01)