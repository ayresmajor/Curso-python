from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Diga o seu ano de nascimento da {}ª pessoa: '.format(c)))
    if atual - ano >= 21:
        maior += 1
    else:
        menor += 1
print('Neste grupo {}, já são maiores e {} ainda não.'.format(maior, menor))
