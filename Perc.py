from grafo import Grafo
from itertools import permutations

KEY_INIT = set(['A'])

def perm(k1, k2):# recebo a permutacao e adiciono a chave no inicio e fim
    return list(k1) + list(k2) + list(k1)

##MONTANDO O GRAFO E POPULANDO
gra = Grafo()

gra.addNo('A', {'B': 2, 'E': 5, 'D': 1, 'C': 4})
gra.addNo('B', {'E': 4, 'C': 5, 'D': 3, 'A': 2})
gra.addNo('C', {'B': 5, 'A': 7, 'D': 6, 'E': 8})
gra.addNo('D', {'A': 1, 'B': 3, 'E': 2, 'C': 6})
gra.addNo('E', {'A': 5, 'B': 4, 'C': 8, 'D': 2})
gra.normalize()


keys_dif = set(gra.keys()).difference(KEY_INIT)


camin_At = -1
nos_camin = []
for i in permutations(keys_dif):
    caminho_temp = 0
    permuta = perm(k, i)
    nos = []
    for pos in range(0, len(permuta) - 1): #vai de 0 a n-1
        if (permuta[pos], permuta[pos+1]) in gra.inf or (permuta[pos+1], permuta[pos]) in gra.inf:
            continue #caso nao tenha ligaçao nao precisa saber o custo da rota
        else:
            caminho_temp += gra.getValue(permuta[pos], permuta[pos+1]) #somando custos
            nos.append((permuta[pos], permuta[pos+1]))# fazendo os caminhos
    if caminho_temp < camin_At or camin_At == -1: #atribuindo as variaveis
        camin_At = caminho_temp
        nos_camin = nos

print(camin_At, nos_camin) #resultado
