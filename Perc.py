from grafo import Grafo
from itertools import permutations

gra = Grafo()
gra.addNo('carlo', {'biel': 2, 'paulo': 5})
gra.addNo('biel', {'paulo': 3, 'pedro': 6, 'ams': 1})

def test_addNo():
    assert gra.viewGraph() == {'carlo': {'biel': 2, 'paulo': 5}, 'biel': {'carlo': 2, 'paulo': 3, 'pedro': 6, 'ams': 1}, 'paulo': {'carlo': 5, 'biel': 3}, 'pedro': {'biel': 6}, 'ams': {'biel': 1}}

print(gra.keys())

for i in permutations(gra.keys()):
    print(i)