matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = ter = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))
        if c == 2:
            ter += matriz[l][c]
        if l == 1 and c == 0:
            maior = matriz[l][c]
        elif l == 1:
            if matriz[l][c] >= maior:
                maior = matriz[l][c]
    for n in matriz[l]:
        if n % 2 == 0:
            par += n
print('-=' * 50)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('-=' * 50)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da tericeira coluna é {ter}')
print(f'O maior valor da segunda coluna é {maior}')
