from time import sleep
online = True
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
while online:
    print(f'\033[1:31m{"Menu":=^50}\033[m')
    print('''Escolha uma das opções abaixo.
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    print('\033[1:31m=\033[m'*50)
    opcoes = int(input('Que opção deseja? '))
    if opcoes == 1:
        print('A Soma de {} com {} é igual a {}'.format(num1, num2, num2+num1))
    elif opcoes == 2:
        print('A multiplicação de {} com {} é igual a {}'.format(num1, num2, num2 * num1))
    elif opcoes == 3:
        if num1 > num2:
            print('{} é o maior valor'.format(num1))
        elif num1 < num2:
            print('{} é o maior valor'.format(num2))
        else:
            print('Não existe maior os dois são iguais')
    elif opcoes == 4:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    elif opcoes == 5:
        print('A finalizar o programa...')
        sleep(2)
        print('Obrigado pela utilização. Volte sempre')
        online = False
    else:
        print('Opção INVÁLIDA. Tente novamente')
