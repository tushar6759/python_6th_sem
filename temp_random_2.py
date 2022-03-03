import math
import random
def ran(limit):
    return math.floor(random.random()*limit)
n=int(input())
l=1
while(n>0):
    l=l*10
    n=n//10
print(ran(l))