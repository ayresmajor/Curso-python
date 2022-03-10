from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
cont = menor = maior = 0
print('Os valores sortedos foram: ', end=' ')
for c in num:
    print(c, end=' ')
print(f'\nO maior é {max(num)}')
print(f'O menor é {min(num)}')
