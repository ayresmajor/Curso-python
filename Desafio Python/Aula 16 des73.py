equipas = ('Sporting', 'FC Porto', 'Sp. Braga', 'Benfica', 'Paços Ferreira', 'V. Guimarães', 'Moreirense', 'Santa Clara'
           , 'Rio Ave', 'Nacional', 'Tondela', 'Portimonense', 'Belenenses', 'Farense', 'Marítimo', 'Gil Vicente',
           'Boavista', 'Famalicão', 'Académica', 'Estoril Praia')
print('{:=^50}'.format('Campeonato Português 18/02/2020'))
print('-' * 50)
print(f'Os primeiros cinco colocados são: {equipas[0:5]}')
print('-' * 50)
print(f'Os ultimos colocados da liga são: {equipas[-4:]}')
print('-' * 50)
print(f'''As equipas por oderm alfabética são:
{sorted(equipas)}''')
print('-' * 50)
print(f'O Benfica está situado na posição {equipas.index("Benfica") + 1}')

