#Genera una lista y retorna 50 numeros randoms desde el 0 al 100

import random
def genrnd():

    lista=[]
    for i in range(50):
        lista.append(random.randint(0,100))

    return lista
