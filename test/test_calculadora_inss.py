import pytest
from domain.logic import CalculdoraInss

def test_calculadora_inss():
  #arrange
  valor_salario = 3000
  aliquota = 0.11
  esperado = 330

  #act
  result = CalculdoraInss(valor_salario).calcular()

  #assert
  assert result == esperado