class No:

    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def obtervalor(self):
        return self.valor

    def setproximo(self, proximo):
        self.proximo = proximo

    def obterproximo(self):
        return self.proximo


no1 = No(4)
no2 = No(7)

print(no1.obtervalor())
print(no2.obtervalor())

no1.setproximo(no2)

print(no1.obterproximo())
print(no1.obterproximo().obtervalor())