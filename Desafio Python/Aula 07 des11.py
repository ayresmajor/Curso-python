lar = float(input('Diga a largura em metros'))
alt = float(input('Diga a altura em metros'))
area = lar * alt
tinta = area / 2
print('A área da sua parede é {:.2f}m² e a quantidade de tinta necessária para pintar é {:.2f}l'.format(area, tinta))