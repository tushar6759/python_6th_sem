# 9. find largest number of list of numbers entered at runtime
# first method

x= list(map(int,input().split()))
print(x)
print(max(x))

# second method
import math
n=int(input())
min=-math.inf
for i in range(n):
    temp=int(input())
    if(temp>min):
        min=temp
print(min)
