print('+*' * 25)
print('Loja PESADÃÃÃOOOO')
print('+*' * 25)
total = tot1000 = cont = menor = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto €: '))
    total += preco
    cont += 1
    if preco > 1000:
        tot1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    con = ' '
    while con not in 'SN':
        con = str(input('Deseja prosseguir? [S/N]: ')).upper().strip()[0]
    if con == 'N':
        break
print(f'No total foi gasto {total:.2f}€ em compras.')
print(f'{tot1000} produto(s) custaram mais de 1000€.')
print(f'O produto mais barato foi {barato} e custou {menor}€.')
