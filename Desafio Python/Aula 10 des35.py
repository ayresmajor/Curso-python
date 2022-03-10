print('\033[1:33mVamos verificar se as medidas das 3 retas formam um triângulo!!')
reta1 = float(input('Medida da primeira reta: '))
reta2 = float(input('Medida da segunda reta: '))
reta3 = float(input('Medida da terceira reta: '))
if (reta1 + reta2) > reta3 and (reta1 + reta3) > reta2 and (reta3 + reta2) > reta1:
    print('\033[:32mCom as medidas das retas colocadas formam-se um triângulo. ')
else:
    print('\033[:31mCom as medidas colocadas não formam-se um triângulo. ')
