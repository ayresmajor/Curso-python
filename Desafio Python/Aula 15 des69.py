print('\033[1mCADASTRO DE PESSOAS\033[M')
mais = hom = mulh = 0
while True:
    print('-' * 50)
    idade = int(input('Idade pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo da pessoa [M/F]: ')).strip().upper()[0]
    print('-' * 50)
    if idade > 18:
        mais += 1
    if sexo == 'M':
        hom += 1
    if idade < 20 and sexo == 'F':
        mulh += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-' * 50)
print(f'''Muito Obrigado, no total foram cadastradas {mais} com 
mais de 18 anos {hom} homens e {mulh} mulheres com menos de 20 anos.''')
