from des109 import moeda

preco = float(input('Digite o preço pretendido: €'))
print(f'''A metade do preço é {(moeda.metade(preco))}
O dobro do preço é {(moeda.dobra(preco))}
Aumentando o preço 10% temos {(moeda.aumentar(preco, 10))}      
Diminuindo o preço 13% temos {(moeda.aumentar(preco, 13))}''')
