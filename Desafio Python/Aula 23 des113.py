def leiaint(n):
    while True:
        try:
            a = int(input(f'{n}'))
        except (TypeError, ValueError, ):
            print('\033[1:31mErro digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print('\nPrograma interrompido pelo usuário')
            return 0
        else:
            return a


def leiafloat(n):
    while True:
        try:
            a = float(input(f'{n}'))
        except (TypeError, ValueError, ):
            print('\033[1:31mErro digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print('\nPrograma interrompido pelo usuário')
            return 0
        else:
            return a


a = leiaint('Digite um número inteiro: ')
b = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {a} e o valor real foi {b}')
