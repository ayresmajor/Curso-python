aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 9.5:
    aluno['Situação'] = 'aprovado'
else:
    aluno['Situação'] = 'reprovado'
print('=' * 30)
for k, v in aluno.items():
    print(f'{"-":>4} {k} é igual a {v}.')
