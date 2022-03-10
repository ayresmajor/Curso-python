print('\033[1:41m Média de números \033[m')
print('=*' * 10)
soma = cont = 0
num = int(input('Digite um número '))
maior = num
menor = num
res = str(input('Deseja continuar [S/N]? ').strip().lower()[0])
while res == 's':
    test = num
    num = int(input('Digite um número '))
    cont += 1
    soma += num
    res = str(input('Deseja continuar [S/N]? ').strip().lower()[0])
    if num > maior:
        maior = num
    if num < menor:
        menor = num
med = soma / cont
print('=*' * 50)
print('A média total dos números digitados é de {}, o maior número digitado foi {} e o menor foi {}.'.format(med, maior, menor))
print('=*' * 50)
