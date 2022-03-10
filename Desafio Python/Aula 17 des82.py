lista = []
listpar = []
listimpar = []
while True:
    num = int(input('Número please [666 para parar]: '))
    if num == 666:
        break
    lista.append(num)
for c in lista:
    if c % 2 == 0:
        listpar.append(c)
    else:
        listimpar.append(c)
print('-' * 50)
print(f'Lista completa: {lista}')
print(f'Lista dos pares: {listpar}')
print(f'Lista dos impares: {listimpar}')
