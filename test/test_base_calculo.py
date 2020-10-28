import pytest
from domain.logic.matriz_enquadramento import MatrizEnquadramento


def test_BaseCalculo():
    salario = 2000.00
    esperado = MatrizEnquadramento(salario)
    esperado.texto = "De 1903,99 até 2826,65"
    esperado.aliquota = 7.5

    base = MatrizEnquadramento(salario)
    resultado = base.enquadrar()

    #assert
    assert esperado.texto == resultado.texto