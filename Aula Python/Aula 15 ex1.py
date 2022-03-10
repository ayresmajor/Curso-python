n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma dos núm vale {}'.format(s))
print(f'A soma dos num vale {s}')
