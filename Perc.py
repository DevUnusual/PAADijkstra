from grafo import Grafo
from itertools import permutations

gra = Grafo()
# gra.addNo('carlo', {'biel': 2, 'paulo': 5})
# gra.addNo('biel', {'paulo': 3, 'pedro': 6, 'ams': 1})
gra.addNo('A', {'B': 2, 'E': 5, 'D': 1, 'C': 4})
gra.addNo('B', {'E': 4, 'C': 5, 'D': 3, 'A': 2})
gra.addNo('C', {'B': 5, 'A': 7, 'D': 6, 'E': 8})
gra.addNo('D', {'A': 1, 'B': 3, 'E': 2, 'C': 6})
gra.addNo('E', {'A': 5, 'B': 4, 'C': 8, 'D': 2})
gra.normalize()


k = set(['A'])
k_d = set(gra.keys()).difference(k)
print(gra.inf)


camin_At = -1
nos_camin = []


def perm(k1, k2):
    return list(k1) + list(k2) + list(k1)


for i in permutations(k_d):
    caminho_temp = 0
    permuta = perm(k, i)
    nos = []
    print(f'permuta : {permuta} ')
    for pos in range(0, len(permuta) - 1):
        if (permuta[pos], permuta[pos+1]) in gra.inf or (permuta[pos+1], permuta[pos]) in gra.inf:
            continue
        else:
            caminho_temp += gra.getValue(permuta[pos], permuta[pos+1])
            nos.append((permuta[pos], permuta[pos+1]))
    if caminho_temp < camin_At or camin_At == -1:
        camin_At = caminho_temp
        nos_camin = nos

print(camin_At, nos_camin)
