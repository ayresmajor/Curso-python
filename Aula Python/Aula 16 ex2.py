lanche = ('Hambúguer','Sumo', 'Pizza',  'Pudim')
for paite in lanche:
    print(f'Vou lastrar {paite} na posição.')
print('=' * 50)
for cont in range(0, len(lanche)):
    print(f'Vou lastrar {lanche[cont]} na posição {cont}.')
print('=' * 50)
for pos, paite in enumerate(lanche):
    print(f'Vou lastrar {paite} na posição {pos}.')
print('=' * 50)
print('Tou fabado')
