palavras = ('aprender', 'estudar', 'dinheiro', 'mulher')
for palavra in palavras:
    print(f'\nNa {palavra.upper()} temos as seguintes vogais: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
