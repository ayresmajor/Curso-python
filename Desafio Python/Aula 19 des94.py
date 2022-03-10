pessoa = dict()
pessoas = list()
mulher = list()
soma = 0
while True:
    print('-' * 40)
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Responda apenas com M ou F!!')
    pessoas.append(pessoa.copy())
    print('-' * 40)
    while True:
        res = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
        if res in 'SN':
            break
        print('ERRO!! Responda apenas com S ou N!!')
    if res == 'N':
        break
print('-' * 40)
print(f'O número de pessoas cadastradas foi de {len(pessoas)}')
print(f'As mulheres cadastradas foram: ', end=' ')
for p in pessoas:
    if p['sexo'] in 'F':
        print(p['nome'], end=' ')
med = soma / len(pessoas)
print(f'\nA média das idades é {med:.2f}.')
print('A lista de pessoas com idade acima da média são: ')
for p in pessoas:
    if p['idade'] >= med:
        print(f'   {p["nome"]} com {p["idade"]} anos.')
print('Muito obrigado pela utilização')

