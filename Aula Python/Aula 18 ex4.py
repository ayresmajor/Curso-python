galera = []
dado = list()
totma = totme = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totme += 1
    else:
        print(f'{p[0]} é menor de idade')
        totma += 1
print('*' * 50)
print(f'''Nº de maiores de idade: {totma}
Nº de menores de idade: {totme}''')
print(len(galera))
