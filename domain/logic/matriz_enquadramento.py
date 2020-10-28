

"""
Criar o componente que:
. Com base em um valor de entrada (salario base)
. Entregar o OBJETO que representa a linha da matriz de enquadramento (slide 74)
=> base de calculo (texto), alíquota (float)
"""


class MatrizEnquadramento(object):
    def __init__(self, salario_base = None):
        if salario_base != None:
            self.salario_base = salario_base
            self.dicio_tabela = {
                1903.98:self.cria_matriz("Ate 1903.98",0),
                2826.65:self.cria_matriz("De 1903,99 até 2826,65",7.5),
                3751.05:self.cria_matriz("De 2826,66 até 3751,05", 15),
                4664.68:self.cria_matriz("De 3751,06 até  4664,68", 22.50),
                4664.69:self.cria_matriz("De Acima até 4664,68", 27.50)
            }

    def cria_matriz(self, texto, aliquota):
        m = MatrizEnquadramento()
        m.texto = texto
        m.aliquota = aliquota
        return m

    def enquadrar(self):
        for chave, valor in self.dicio_tabela.items():
            if self.salario_base <= chave:
                return valor
