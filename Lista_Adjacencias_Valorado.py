class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def adiciona_aresta(self, u, v, peso):
        # estamos pensando em grafo direcionado com peso nas arestas
        self.grafo[u-1].append([v, peso])

        # self.grafo[v-1].append([u,peso]) se o grafo não for direcionado

    def mostra_lista(self):
        for i in range(self.vertices):
            print(f'{i+1}:', end='  ')
            for j in self.grafo[i]:
                print(f'{j}  ->', end='  ')
            print('')

g = Grafo(4)

g.adiciona_aresta(1, 2, 5)
g.adiciona_aresta(1, 3, 7)
g.adiciona_aresta(1, 4, 6)
g.adiciona_aresta(2, 3, 9)

g.mostra_lista()