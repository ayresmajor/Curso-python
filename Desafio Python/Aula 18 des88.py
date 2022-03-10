from random import randint
from time import sleep
print('=-' * 25)
print('{:^50}'.format('EUROMILHÕES'))
print('=-' * 25)
njogo = int(input('Quantos palpites deseja?: '))
print(f'''=*=*=*=*=\033[1:35m A SORTEAR {njogo} JOGOS \033[m=*=*=*=*=''')
print('-' * 30)
for c in range(0, njogo):
    numeros = [randint(1, 51), randint(1, 51), randint(1, 51), randint(1, 51), randint(1, 51)]
    estrela = [randint(1, 13), randint(1, 13)]
    print(f'Números do jogo {c + 1}: {sorted(numeros)}')
    print(f'Estrelas do jogo {c + 1}: {sorted(estrela)}')
    print('-' * 30)
    sleep(1)
print(f'''=*=*=*=*=*=*\033[1:35m< BOA SORTE! >\033[m*=*=*=*=*=*=''')
