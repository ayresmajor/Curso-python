soma = 0
cont = 0
for c in range(3,501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('O somatório dos {} números foi {}'.format(cont, soma))
