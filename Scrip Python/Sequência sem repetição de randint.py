from random import randint

lista = []
lista2 = []
num = []


for c in range(6):
    n = randint(1, 5)
    if c > 0:
      lista.append(n)
      print("lista : ", lista)
    if len(lista) >= 2:
        lista2 = lista[0: c -1]
        print("lista2: ", lista2)
        while  n in lista2:
            d = lista.index(n)
            n = randint(1, 5)
            print('n modificado2: ', n)
            lista[d] = n
print('Valor final abaixo:')
lista.sort()
print(lista)