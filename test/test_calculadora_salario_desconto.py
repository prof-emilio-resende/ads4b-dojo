from domain.logic import SalarioDesconto

def test_calculadora_salario_desconto():
  #arrange
  salario_base = 5000
  faixa_insen = 1903.98
  esperado = 3096.02

  
  result = SalarioDesconto(salario_base)

  #assert
  assert result.desconto() == esperado
