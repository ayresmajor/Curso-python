numatriz = [[], [], [], [], [], [], [], [], []]
for c in range(0, 3):
    numatriz[c].append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(0, 3):
    numatriz[c+3].append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(0, 3):
    numatriz[c+6].append(int(input(f'Digite um valor para [2, {c}]: ')))
print('-=' * 50)
for c in numatriz[0:3]:
    print(f'[ {c} ]', end=' ')
print('\n',end='')
for c in numatriz[3:6]:
    print(f'[ {c} ]', end=' ')
print('\n',end='')
for c in numatriz[6:9]:
    print(f'[ {c} ]', end=' ')