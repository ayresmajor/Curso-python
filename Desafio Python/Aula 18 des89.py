boletim = []
med = nota = 0
while True:
    print('-' * 50)
    alunos = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    med = (nota2 + nota1) / 2
    boletim.append([alunos, [nota1, nota2], med])
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
print(boletim)
print('=*' * 20)
print(f'{"Nº.":<5}{"NOME":<5}{"MÉDIA":>10}')
print('-' * 30)
for c, a in enumerate(boletim):
    print(f'{c:<5}{a[0]:<5}{a[2]:>10.1f}')
while True:
    print('-' * 50)
    nota = int(input(('Pretende ver a nota de que aluno? [-1 para parar]: ')))
    if nota == -1:
        break
    if nota >= len(boletim) - 1:
        print(f'Notas do {boletim[nota][0]} são: {boletim[nota][1]}')
print('RALA VAGABUNDO')
