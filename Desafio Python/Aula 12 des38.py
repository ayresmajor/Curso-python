print('Vou comparar 2 valores inteiros')
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
if num1 > num2:
    print('O {} é maior.'.format(num1))
elif num2 > num1:
    print('O {} é maior.'.format(num2))
else:
    print('Não existe valor maior, os dois são iguais.')
