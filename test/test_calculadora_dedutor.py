import pytest
from domain.logic import CalculadoraDedutor

#Criar o componente de cálculo para a regra de abatimento de dependentes
#qtde de dependentes (parametro entrada) * 189.59 (fixo)
def test_CalculadoraDedutor():
    quantidade_dependentes = 5
    valor_por_dependente = 189.59
    esperado = 947,95

    dedutor = CalculadoraDedutor(quantidade_dependentes)
    #calcular
    result = dedutor.calcular()

    #assert
    assert result == esperado

