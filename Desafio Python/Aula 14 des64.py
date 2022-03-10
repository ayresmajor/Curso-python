print('\033[1:35mSomatório de números aleatórios!\033[m')
print('Digite qualquer número inteiro e pare a soma digitando o número \033[1m999.\033[m')
num = cont = soma = 0
num = int(input('Digite um número para somar: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número para somar: '))
print('A quantidade de números somados foram {} e a sua soma total é {}.'.format(cont, soma))
