from random import randint
from time import sleep
tenta = 0
num = randint(0, 10)
print('\033[:31m=--=\033[m'*15)
print('Vou pensar num número entre 0 e 10...')
print('\033[:31m=--=\033[:m'*15)
sleep(1)
num1 = int(input('Tente acertar o número! '))
while num != num1:
    if num > num1:
        print('Mais...')
    elif num < num1:
        print('Menos...')
    num1 = int(input('TENTE NOVAMENTE: '))
    tenta += 1
print('PARABÉNS, voçê acertou, pensei no número {}. \nVocê tentou {} vezes até conseguir'.format(num, tenta))
