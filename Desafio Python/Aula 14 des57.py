sexo = str(input('Qual é o seu sexo? [M/F] ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, digite novamente ')).upper().strip()[0]
print('Sexo registrado com sucesso')



