teste = list()
teste.append('Ayres')
teste.append(18)
galera = []
galera.append(teste[:])
teste[0] = 'Serya'
teste[1] = 22
galera.append(teste[:])
print(galera)
