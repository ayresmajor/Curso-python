from random import randint

block = []
block2 = []
num = []


for c in range(6):
    pos1 = c - 2
    pos2 = c - 1
    print('')
    print("Print do c :", c)
    print("Print do pos1 e 2: ", pos1, pos2)
    n = randint(1, 5)
    print("Primeiro n: ", n )
    if c > 0:
      block.append(n)
      if c > 1:
          while block[pos1] == block[pos2]:
              n = randint(1, 5)
              block[pos2] = n
      print("Primeiro Block: ", block)
    if len(block) > 2:
        block2 = block[0: c -1]
        print("Block2: ", block2)
        while  n in block2:
            d = block.index(n)
            n = randint(1, 5)
            block[d] = n
            print("n modificado: ", n)
            print("block modificado: ", block)
print('Valor final abaixo:')
block.sort()
print(block)