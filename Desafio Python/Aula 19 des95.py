time = list()
jogador = dict()
partidas = list()

while True:
    print('-' * 50)
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? : '))
    for c in range(0, tot):
        partidas.append(int(input(f' Quantos golos marcados na {c + 1}ª partida? : ')))
    jogador['golos'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    print('-' * 50)
    while True:
        res = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
        if res in 'SN':
            break
        print('ERRO!! Responda somente com S ou N')
    if res == 'N':
        break
print(time)
print('=-' * 50)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print('\n-' * 50)
for k, v in enumerate(time):
    print(f'{k:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
while True:
    print('-' * 50)
    jog = int(input('Mostrar dados de que jogador?[-1 para parar]: '))
    if jog == -1:
        break

    if jog >= len(time):
        print(f'Não exite jogador com código {jog}. Tente novamente!!')
    else:
        print(f'-- Levantamento dos dados do {time[jog]["nome"]}')
        for np, ng in enumerate(time[jog]["golos"]):
            print(f'   => Na {np + 1}ª partida marcou {ng}.')
print('Brigado e vai jogar fut!!')