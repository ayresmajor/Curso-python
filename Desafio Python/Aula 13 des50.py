s = 0
c = 0
for cont in range(1, 7):
    n = int(input('Digite {}º numero inteiro: '.format(cont)))
    if n % 2 == 0:
        s += n
        c += 1
print('O somátorio  dos {} números pares foi de {}.'.format(c, s))
print('Obrigado')
