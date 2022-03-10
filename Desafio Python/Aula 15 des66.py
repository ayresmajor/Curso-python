print('Soma de números aleatórios')
soma = cont = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos {cont} valores digitados foi de {soma}.')
