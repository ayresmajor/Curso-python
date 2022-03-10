def area(a, b):
    m = a * b
    print(f'A área do terreno {a}X{b} é de {m}m²')

# Programa principal
print('Controle de Terrenos')
print('-' * 30)
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
area(a, b)
