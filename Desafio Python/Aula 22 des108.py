from des108 import moeda

preco = float(input('Digite o preço pretendido: €'))
print(f'''A metade do preço é {moeda.dinheiro(moeda.metade(preco))}
O dobro do preço é {moeda.dinheiro(moeda.dobra(preco))}
Aumentando o preço 10% temos {moeda.dinheiro(moeda.aumentar(preco, 10))}      
Diminuindo o preço 13% temos {moeda.dinheiro(moeda.aumentar(preco, 13))}''')
