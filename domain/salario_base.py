from domain.logic import CalculadoraInss
from domain.logic import CalculadoraDedutor

def salario_base(salario,dependente):
    inss = CalculadoraInss(salario).calcular()
    calculo_dependentes = CalculadoraDedutor(dependente).calcular()
    return salario-inss-calculo_dependentes
        