print('=' * 50)
print('{:^50}'.format('BANCO SERYA'))
print('=' * 50)
preco = int(input('Quanto deseja levantar [€]: '))
total = preco
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de {ced}€')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('-' * 50)
print('Muito obrigado e volte sempre!!')