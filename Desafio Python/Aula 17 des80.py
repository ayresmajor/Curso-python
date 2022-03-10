lista = []
for c in range (0, 5):
    num = int(input('Digite o valor pretendido: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Seu número foi adcionado no final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Seu número foi adcionado na posição {pos}.')
                break
            pos += 1
print(f'A sua lista organizada é {lista}')