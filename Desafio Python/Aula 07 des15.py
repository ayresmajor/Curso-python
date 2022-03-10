km = float(input('Quantos kilómetros foram percorridos? '))
dia = float(input('Durante quantos dias esteve alugado? '))
preco = (0.15 * km) + (60 * dia)
print('Para o veículo que percorreu {}Km, e esteve alugado durante {} dias,\no preço final será de {}€'.format(km, dia, preco))