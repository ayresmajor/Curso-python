from random import randint

block = []
block2 = []
num = []


for c in range(6):
    n = randint(1, 5)
    print("Primeiro n: ", n )
    if c > 0:
      block.append(n)
      print("Primeiro Block: ", block)
    if len(block) == 2:
        block2 = block[0]
    elif len(block) > 2:
        block2 = block[0: c -1]
        print("Block2: ", block2)
print('Valor final abaixo:')
block.sort()
print(block)
