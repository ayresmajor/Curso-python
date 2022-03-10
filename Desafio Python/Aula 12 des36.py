casa = float(input('Quanto custa a casa? '))
salario = float(input('Quanto é o seu salário? '))
ano = int(input('Em quantos  anos deseja pagar a casa? ' ))
meses = ano * 12
prest = casa / meses
if prest > salario * 0.3:
    print('Lamentamos mas não será possivel realizar o empréstimo')
else:
    print('Para realizar a compra da casa terá de pagar um prestação de {:.2f}€ durante {} meses'.format(prest, meses))
print('Continuação de um bom dia!')
