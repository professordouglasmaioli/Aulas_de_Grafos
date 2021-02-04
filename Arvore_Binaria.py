class No:

    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def obtervalor(self):
        return self.valor

    def setesquerda(self, esquerda):
        self.esquerda = esquerda

    def setdireita(self, direita):
        self.direita = direita

    def obteresquerda(self):
        return self.esquerda

    def obterdireita(self):
        return self.direita


no1 = No(4)
no2 = No(2)
no3 = No(5)

no1.setesquerda(no2)
no1.setdireita(no3)

print(no1.obtervalor())
print(no1.obterdireita())
print(no1.obterdireita().obtervalor())
print(no1.obteresquerda())
print(no1.obteresquerda().obtervalor())