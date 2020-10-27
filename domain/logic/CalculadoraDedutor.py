class CalculadoraDedutor(object):
  def __init__(self, num_dependentes):
    self.num_dependentes = num_dependentes
    self.valor_dependente = 189.59

  def calcular(self):
    return self.num_dependentes * self.valor_dependente