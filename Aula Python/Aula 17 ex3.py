valores = list()
for cont in range(0, 5):
    valores.append(int(input('Escreva um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} tem o valor {v}!!')
print('Cabou - se')
print(valores)