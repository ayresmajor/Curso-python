from random import randint
from time import sleep

block= {randint(1,5)}

while len(block) < 5:
    n = randint(1, 5)
    block.add(n)

print(block)