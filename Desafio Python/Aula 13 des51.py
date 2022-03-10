print('=' * 20)
print('Contagem PA')
print('=' * 20)

num = int(input('Primeio termo: '))
raz = int(input('Razão: '))
dez = num + 10 * raz
for c in range(num, dez, raz):
    print(c, end=' -> ')
print('FIM')
