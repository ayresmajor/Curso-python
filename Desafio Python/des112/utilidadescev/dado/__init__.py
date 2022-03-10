def leiadinh(msg):
    while True:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO!!\033[m, {entrada} é um valor inválido')
        else:
            break
    return float(entrada)


def leiaint(n):
    while True:
        a = str(input(f'{n}'))
        if a.isnumeric():
            break
        print('\033[1:31mErro digite um número inteiro válido\033[m')
    return a
