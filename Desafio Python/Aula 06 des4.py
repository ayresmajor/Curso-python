algo = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(algo)))
print('Só tem espaço?:', algo.isspace())
print('É alfanumérico:', algo.isalnum())
print('É numérico:', algo.isnumeric())
print('É alfabetico:', algo.isalpha())
print('Está em maiúsculas?:', algo.isupper())
print('Está em minúsculas?:', algo.islower())
print('Está captalizada', algo.istitle())
