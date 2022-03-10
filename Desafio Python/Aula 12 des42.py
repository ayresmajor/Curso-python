print('\033[1mVerificação de  segmentos retas e o seu tipo de triângulo\033[m')
print('Atribui medidas aos 3 segmentos')
reta1 = float(input('Valor do primeiro segmento. '))
reta2 = float(input('Valor do segundo segmento. '))
reta3 = float(input('valor do terceiro segmento. '))
if (reta1 + reta2) > reta3 and (reta2 + reta3) > reta1 and (reta3 + reta1) > reta2:
    print('Com esses 3 segmentos é possível formar um triângulo', end='')
    if reta1 == reta2 == reta3:
        print('EQUILÁTERO.')
    elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print('ISÓSELES.')
    else:
        print('ESCALENO.')
else:
    ('Com as medidas atribuídas não formam-se um triângulo')

