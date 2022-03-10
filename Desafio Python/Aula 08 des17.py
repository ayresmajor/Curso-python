from math import hypot
cato = float(input('Digite o cateto oposto '))
cata = float(input('Digite o cateto adjacente '))
hipo = hypot(cato, cata)
print('O comprimento do c.oposto é {}, \n o comprimento do c.adjacente é {}, \n e a hipotenusa é {:.2f}'.format(cato, cata, hipo))

