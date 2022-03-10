num = int(input('Digite um número inteiro: '))
print('''\033[1mEscolha uma das bases de conversão\033[m
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('\033[:33mSua opção:\033[m '))
if opcao == 1:
    print('O valor {} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O valor {} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O valor {} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('\033[:31mOpção inválida. Tente novamente.\033[m')
