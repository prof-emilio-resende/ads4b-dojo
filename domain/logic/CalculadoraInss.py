class CalculadoraInss(object):
    def __init__(self, salario_bruto):
        self.salario_bruto = salario_bruto

    def calcular(self):
        return self.salario_bruto * 0.11

