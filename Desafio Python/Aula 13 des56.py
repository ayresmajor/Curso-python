total = 0
maiorh = 0
nomeh = ''
totm = 0
for c in range(1, 5):
    print('-----{}ª Pessoa-----'.format(c))
    nome = str(input('Nome da {}ª pessoa: '.format(c))).strip().lower()
    idade = int(input('Idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Sexo da {}ª pessoa [M/F]: '.format(c))).strip().lower()
    total += idade
    if c == 1 and sexo == 'm' :
        maiorh = idade
        nomeh = nome
    if sexo == 'm' and idade > maiorh:
        maiorh = idade
        nomeh = nome
    if sexo == 'f' and idade < 20:
        totm += 1
med = total / 4
print('A média total das idades é de {} anos'.format(med))
print('O homem mais velho tem {} anos e chama-se {}.'.format(maiorh, nomeh))
print('No total {} mulheres que têm menos de 20 anos.'.format(totm))


