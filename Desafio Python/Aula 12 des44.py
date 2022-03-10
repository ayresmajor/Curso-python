print('\033[1:31m{:=^50}\033[m'.format('Serya Shop'))
preco = float(input('Preço das compras €: '))
print('Selecione o método de pagamento:')
print('''[ 1 ] Dinheiro / Cheque
[ 2 ] Cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
metodo = int(input('Método de pagamento: '))
print('Com o método de pagamento selecionado terá', end=' ')
if metodo == 1:
    print('10% de desconto e o preço final será de {:.2f}€'.format(preco - (preco * 0.1)))
elif metodo == 2:
    print('5% de desconto e o preço final será de {:.2f}€'.format(preco - (preco * 0.05)))
elif metodo == 3:
    print('de pagar {:.2f}€'.format(preco))
elif metodo == 4:
    print('20% de juros e o preço final será de {:.2f}€'.format(preco + (preco * 0.2)))
else:
    print('método de pagamento INVÁLIDO.')




