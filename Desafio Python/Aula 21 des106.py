from time import sleep


def escreva(lst):
    com = len(lst) + 4
    print('~' * com)
    print(f'  {lst}')
    print('~' * com)


def ajuda(comando):
    print('\033[41m', end='')
    escreva(f"A acessar o manual do comando '{comando}'")
    print('\033[m', end='')
    sleep(1.5)
    print()
    print('\033[7m', end='')
    help(comando)
    print('\033[m', end='')


# Programa Principal
while True:
    print()
    print('\033[42m', end='')
    escreva('SISTEMA DE AJUDA PyHELP')
    print('\033[m', end='')
    print('=' * 30)
    comando = str(input('Função ou Biblioteca ("fim" para parar): ')).strip().lower()
    print('=' * 30)
    if comando == 'fim':
        break
    ajuda(comando)

print('Obrigado pela utilização volte sempre')
