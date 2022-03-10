from time import sleep
print('{:=^50}'.format('Fogo de Artificio'))
print('Em...')
sleep(1)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[1:31m***KABOOOM***')
