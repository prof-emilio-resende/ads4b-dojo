import pytest
from domain.logic import BaseCalculo


def test_BaseCalculo():
    salario = 2000.00
    esperado = BaseCalculo()
    esperado.texto = "De 1903,99 até 2826,65"
    esperado.aliquota = 7.5

    base = BaseCalculo()
    resultado = base.calcular(salario)

    #assert
    assert esperado == resultado