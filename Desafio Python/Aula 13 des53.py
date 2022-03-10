frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
print(junto)
'''inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]'''  # Outra Solução
inverso = junto[::-1]
print('A frase: {}, inversamente fica: {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não é um palíndromo')
