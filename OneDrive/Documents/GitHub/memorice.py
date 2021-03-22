n= int(input('Ingrese numero de cartas a jugar:'))
from random import shuffle
i=1
lista=[]
for g in range(n):
    lista.append(i)
    lista.append(i)
    i+=1
shuffle(lista)
print(lista)