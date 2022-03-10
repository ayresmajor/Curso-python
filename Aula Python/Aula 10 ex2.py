n1 = float(input('Digite a 1º nota '))
n2 = float(input('Digite a 2º nota '))
m = (n1 + n2)/2
print('A sua média é {:.2f}'.format(m))
if m >= 10:
    print('Parabéns a sua média é positiva')
else:
    print('Infelizmente sua média é negativa, esforce-se mais.')
