class Grafo():
    def __init__(self):
        self.grafo = {}

    def addNo(self, no: str, vizinhos: dict):
        ex = self.exist(no)  # verifica se o no existe
        for k, c in vizinhos.items():  # para toda key custo in vizinhos
            # verificar se ja faz parte das keys do no, caso ele ja tenha sido adicionado como vizinho
            if ex and k in self.grafo[no].keys():
                if self.grafo[no][k] != c:  # se o custo estiver diferente, atualiza
                    self.grafo[no][k] = c
                    self.grafo[k][no] = c
            elif ex and k in self.grafo.keys():  # caso o no exista e k nao encontrado
                self.grafo[no].update({k: c})
                self.grafo[k].update({no: c})
            elif ex:  # caso o no exista e k nao encontrado
                self.grafo[no].update({k: c})
                self.grafo[k] = {no: c}
            else:  # caso o no nao exista
                self.grafo[no] = vizinhos
                for key, custo in vizinhos.items():
                    self.addNo(key, {no: custo})
                break

    def viewGraph(self):
        return self.grafo

    def exist(self, key):
        if key in self.grafo.keys():
            return True
        return False


gra = Grafo()
gra.addNo('carlo', {'biel': 2, 'paulo': 5})
gra.addNo('biel', {'paulo': 3, 'pedro': 6, 'ams': 1})

print(gra.viewGraph())
