a = int(input('Primeiro valor '))
b = int(input('Segundo Valor '))
c = int(input('Terceiro valor '))
# A verificar o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor é {}'.format(menor))
# A verificar o maior
maior = b
if a > b and a > c:
    maior = a
if c > b and c > a:
    maior = c
print('O maior valor é {}'.format(maior))
