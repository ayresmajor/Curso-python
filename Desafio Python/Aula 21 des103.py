def ficha(nome='desconhecido', gols=0 ):
    print(f'O jogador {nome} marcou {gols} no campeonato.')


jogador = str(input('Nome do jogador: '))
golos = str(input('Quantos golos marcados: '))
if golos.isnumeric():
    golos = int(golos)
else:
    golos = 0
    if jogador.strip() == '':
        ficha(gols=golos)
    else:
        ficha(jogador, golos)