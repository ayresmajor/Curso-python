def leiaint(n):
    while True:
        a = str(input(f'{n}'))
        if a.isnumeric():
            break
        print('\033[1:31mErro digite um número inteiro válido\033[m')
    return a


#Programa principal
num = leiaint('Digita um número: ')
print(f'O numero digitado foi: {num}')