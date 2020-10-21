import pytest
from domain.logic import CalculadoraInss

def test_calculadora_inss():
  #arrange
  valor_salario = 3000
  aliquota = 0.11
  esperado = 330

  #act
  result = CalculadoraInss(valor_salario)
  print(type(result))

  #assert
  assert result.calcular() == esperado