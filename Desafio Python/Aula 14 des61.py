print('=' * 20)
print('Contagem PA V2')
print('=' * 20)
num = int(input('Primeio termo: '))
raz = int(input('Razão: '))
cont = 1
while cont <= 10:
    print(num, end=' -> ')
    num += raz
    cont += 1
print('FIM')
