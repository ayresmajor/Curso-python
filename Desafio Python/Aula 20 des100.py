from random import randint
from  time import sleep
numeros = []


def sorteia(lst):
    for c in range(0, 5):
        lst.append(randint(0, 10))
    print('Sorteando 5 valores da lista:', end=' ')
    for n in lst:
        print(n, end=' ')
        sleep(0.3)
    print('PRONTO!')


def somapar(lst):
    par = 0
    for p in lst:
        if p % 2 == 0:
            par += p
    print(f'Somando os valores par de {lst}, temos {par}')

# Programa Principal
sorteia(numeros)
somapar(numeros)
