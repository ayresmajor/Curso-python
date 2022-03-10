from time import sleep
from random import randint
print('''Ei, vamos jogar JOKENPO!!!
Vou escolher primeiro...''')
sleep(1)
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Já escolhi!!!
Suas opções:
[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura''')
joga = int(input('Agora sua vez: '))
if joga > 2:
    print('OPÇÃO ERRADA')
else:
    print('PEDRA')
    sleep(1)
    print('PAPEL')
    sleep(1)
    print('OU TESOURA')
    print('\033[1:31m-=\033[m' * 10)
    print('Eu joguei {}'.format(itens[computador]))
    print('Você jogou {}'.format(itens[joga]))
    print('\033[1:31m-=\033[m' * 10)
    if joga == computador:
        print('EMPATE')
    else:
        if computador == 0:
            if joga == 1:
                print('Você ganhou!!')
            elif joga == 2:
                print('GANHEI')
        elif computador == 1:
            if joga == 0:
                print('GANHEI')
            elif joga == 2:
                print('Você ganhou!!')
        elif computador == 2:
            if joga == 0:
                print('Você ganhou!!')
            elif joga == 1:
                print('GANHEI')
