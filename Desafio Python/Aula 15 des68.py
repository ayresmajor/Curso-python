from random import randint
from time import sleep
print('''\033[1mVamos jogar PAR ou ÍMPAR\033[m
Vou escolher um número de 0 a 10...''')
sleep(1)
com = randint(0,10)
joga = int(input('Já escolhi agora sua vez: '))
parim = str(input('Par ou Ímpar? [P/I]: ').strip().upper()[0])
res = joga + com
cont = 0
while True:
    if res % 2 == 0 and parim == 'P':
        print(f'Parabens vc venceu eu tirei {com} e vc tirou {joga} deu {res} Par')
        print('*+' * 15)
        joga = int(input('Mais uma vez!! : '))
        com = randint(0, 10)
        parim = str(input('Par ou Ímpar? [P/I]: ').strip().upper()[0])
        print('*+' * 15)
        cont += 1
        res = joga + com
    elif res % 2 != 0 and parim == 'I':
        print(f'Parabens vc venceu eu tirei {com} e vc tirou {joga} deu {res} Ímpar')
        print('*+' * 15)
        joga = int(input('Mais uma vez!! : '))
        com = randint(0, 11)
        parim = str(input('Par ou Ímpar? [P/I]: ').strip().upper()[0])
        print('*+' * 15)
        cont += 1
        res = joga + com
    else:
        break
print(f'VENCII!! eu tirei {com} e vc tirou {joga} deu {res}', end=' ')
print('logo par.') if res % 2 == 0 else print('logo ímpar.')
print(f'Você me venceu {cont} vezes seguidas')