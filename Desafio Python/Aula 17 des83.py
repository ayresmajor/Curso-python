espr = str(input('Escreva a sua expresão: '))
pard = espr.count('(')
pare = espr.count(')')
if pard == pare:
    print('A sua expressão é válida')
else:
    print('A sua expressão é inválida')
