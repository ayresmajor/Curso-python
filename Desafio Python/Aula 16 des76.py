lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2,
         'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
cont = 0
print('-' * 50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('-' * 50)
for compra in lista:
    cont += 1
    if cont % 2 != 0:
        print(f'{compra:.<40}', end='')
    else:
        print(f'{compra:>9.2f}€')
print('-' * 50)
