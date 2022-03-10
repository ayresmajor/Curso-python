lista = []
while True:
    num = int(input('Digita um número: '))
    lista.append(num)
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    if resp == 'n':
        break
print('=*' * 50)
print(f'Foi digitado {len(lista)} elementos')
lista.sort(reverse=True)
print(f'A lista na ordem decresecente fica {lista}')
if lista.count(5) == 0:
    print('Não está presente o valor 5 na lista')
else:
    print('O número 5 está presente na lista')
