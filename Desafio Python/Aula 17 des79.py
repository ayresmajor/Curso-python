valores = list()
while True:
    num = (int(input('Digite um valor: ')))
    if num not in valores:
        valores.append(num)
        print('Valor adcionado')
    else:
        print('Valor repetido não será adcionado')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
valores.sort()
print(f'Os valores digitados foram {valores}')
