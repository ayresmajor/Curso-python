estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Unidade Federativa: '))
    brasil.append(estado.copy())
    print('-' * 50)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
