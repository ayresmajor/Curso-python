print('Sequência de Fibonacci')
print('=' * 20)
num = int(input('Quantos termos quer mostrar? '))
t1 = 0
t2 = 1
print('=-' * 30)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
if cont <= num:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
