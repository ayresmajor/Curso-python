valores = list()
maior = menor =  0
for c in range (0, 5):
    valores.append((int(input(f'Digita um valor para a posição {c}: '))))
for p, v in enumerate(valores):
    if p == 0:
        maior = menor = v
    if v >= maior:
        maior = v
    if v <= menor:
        menor = v
print('-' * 50)
print(f'Você digitou {valores}')
print(f'O maior falor digitado foi {maior} na(s) posições ', end='')
for pos, valor in enumerate(valores):
    if maior == valor:
        print(pos, end=' ')
print(f'\nO menor falor digitado foi {menor} na(s) posições ', end='')
for pos, valor in enumerate(valores):
    if menor == valor:
        print(pos, end=' ')
