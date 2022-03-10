nome = str(input('Qual o seu nome? '))
if nome.upper() == 'AYRES':
    print('Que nome sexy')
elif nome.lower() == 'pedro' or nome.lower() == 'joão' or nome.lower() == 'maria':
    print('Borra nome vodôô.')
elif nome.lower() in 'bete ana peter juliana':
    print('Bom nome!!')
else:
    print('O seu nome é normal')
print('\033[1:32mTenha um bom dia {}'.format(nome.capitalize()))
