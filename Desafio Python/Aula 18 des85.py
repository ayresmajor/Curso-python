numeros = [[], []]
for c in range(0, 7):
    num = int(input(f'Digite o {c + 1}º número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
print('-*' * 50)
print(f'''Os valores pares digitados foram: {numeros[0]}.
OS valores ímpares digitados foram: {numeros[1]}.''')