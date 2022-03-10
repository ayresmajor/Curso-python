print('=' * 50)
print('{:^50}'.format('BANCO SERYA'))
print('=' * 50)
preco = int(input('Quanto deseja levantar [€]: '))
print('-' * 50)
c50 = preco // 50
c20 = (preco - (50 * c50)) // 20
c10 = (preco - (50 * c50) - (20 * c20)) // 10
c1 = (preco - (50 * c50) - (20 * c20) - (10 * c10)) // 1
print('Neste levantamento será necessário:')
if c50 != 0:
    print(f'Um total de {c50} nota(s) de 50€')
if c20 != 0:
    print(f'Um total de {c20} nota(s) de 20€')
if c10 != 0:
    print(f'Um total de {c10} nota(s) de 10€')
if c1 != 0:
    print(f'Um total de {c1} moeda(s) de 1€')
print('-' * 50)
print('Muito obrigado e volte sempre!!')

