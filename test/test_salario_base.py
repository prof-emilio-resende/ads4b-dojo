from domain import domain_core, salario_base


def test_salario_base():
    salario_bruto = 3000
    inss = 330
    dependente = 0
    calculo_dependente = dependente * 189.59
    salario_base_esperado = salario_bruto - inss - calculo_dependente
    salario_base_real = salario_base(salario_bruto, dependente)
    assert salario_base_esperado == salario_base_real
    
   
