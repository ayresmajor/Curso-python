n = int(input('Digite um número para saber a tabuada: '))
for tab in range(1, 11):
    res = n * tab
    print('{} * {} =  {}'.format(n, tab, res))
