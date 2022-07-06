import random 
from itertools import combinations

def genrnd():
    for i in range(50):
        lista.append(random.randint(0,1000))
    return lista


def combinacion_prod(lista):
    for c in combinations(lista,2):
        print(c)
        print("El producto de la combinación es",c[0]*c[1])

lista=[]
combinacion_prod(genrnd())








