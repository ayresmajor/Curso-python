pessoas = {'nome': 'Ayres', 'sexo': 'MACHO', 'idade': 18}
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas['peso'] = 22
print('=' * 50)
for k, v in pessoas.items():
    print(f'{k}: {v}')
print('=' * 50)
del pessoas['sexo']
print(pessoas.items())
