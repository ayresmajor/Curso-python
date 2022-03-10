par = cont = 0
#num = (int(input('Digite um valor: ')),
#       int(input('Digite mais um valor: ')),
#       int(input('Digite só mais um valor: ')),
#       int(input('Ok esse é o último: '))) #outra forma

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite mais um valor: '))
num3 = int(input('Digite só mais um valor: '))
num4 = int(input('Ok esse é o último: '))
num = (num1, num2, num3, num4)
print('-' * 50)
print(f'Você digitou esses números {num}.')
print(f'O número 9 apareceu {num.count(9)} vez(es).')
if 3 not in num:
    print('O 3 não foi digitado logo não tem posição.')
else:
    print(f'A posição do primeiro número 3 está na {num.index(3) + 1}ª posição')
print('Os valores pares são: ', end='')
for c in num:
    par = c % 2
    if par == 0:
        print(c, end=' ')