from random import randint
from time import sleep
num = randint(0, 5)
print('\033[:31m=--=\033[m'*20)
print('Vou pensar num número entre 0 e 5...')
print('\033[:31m=--=\033[:m'* 20)
sleep(2)
num1 = int(input('Tente acertar o numéro! '))
if num == num1:
    print('Acerto MIZERAVI')
else:
    print('ERROOOOOUU, pensei no {} e não no {}.'.format(num, num1))
