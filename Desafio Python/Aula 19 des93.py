jogfut = {'Nome': str(input('Nome do jogador: '))}
partidas = int(input(f'Quantas partidas {jogfut["Nome"]} jogou? : '))
ngol = []
for c in range(0, partidas):
    ngol.append(int(input(f'Quantos golos marcados na {c + 1}ª partida? : ')))
jogfut['golos'] = ngol
jogfut['total'] = sum(ngol)
print('=-' * 25)
print(jogfut)
print('=-' * 25)
for k, v in jogfut.items():
    print(f'O campo {k} tem valor {v}')
print('=-' * 25)
print(f'O jogador {jogfut["Nome"]} jogou em {partidas} partida(s).')
for np, ng in enumerate(jogfut['golos']) :
    print(f'   => Na {np + 1}ª partida marcou {ng}.')
print(f'No total marcou {jogfut["total"]} golos.')
