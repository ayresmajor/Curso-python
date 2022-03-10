pessoas = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(float(input('Massa Corporal: ')))
    pessoas.append(dados[:])
    dados.clear()
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
    maior = menor = pessoas[0][1]
for p in pessoas:
    if p[1] >= maior:
        maior = p[1]
    if p[1] <= menor:
        menor = p[1]
print('-=' * 50)
print(f'O número de pessoas cadastradas foi {len(pessoas)}.')
print(f'O maior peso foi {maior}. Peso de ', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end=' ')
print(f'\nO menor peso foi {menor}. Peso de ', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(p[0], end=' ')
