numex = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'catorze', 'quinze', 'dezasseis', 'dezassete', 'dezoito', 'dezanove', 'vinte')

while True:
    while True:
        num = int(input('Escreva um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente!!', end=' ')
    print(f'Você digitou o número {numex[num]}.')
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
print('Obrigado pela utilização!')
