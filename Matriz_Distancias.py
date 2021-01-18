class Grafo:


    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v, peso):
        # estou pensando em grafos direcionados simples
        self.grafo[u-1][v-1] = peso  #trocar = por += ser for grafo múltiplo

       # self.grafo[v-1][u-1] = 1 (caso o grafo não seja direcionado)

    def mostra_matriz(self):
        print('A matriz de adjacências é:')
        for i in range(self.vertices):
            print(self.grafo[i])

#g = Grafo(4)

#g.adiciona_aresta(1, 2, 5)
#g.adiciona_aresta(3, 4, 9)
#g.adiciona_aresta(2, 3, 3)

#g.mostra_matriz()

v = int(input('Digite a quantidade de vértices'))
g = Grafo(v)

a = int(input('Digite a quantidade de arestas'))
for i in range(a):
    u = int(input('De qual vértice parte esta aresta?'))
    v = int(input('Para qual vértice chega esta aresta?'))
    p = int(input('Qual é o peso desta aresta?'))
    g.adiciona_aresta(u, v, p)

g.mostra_matriz()
