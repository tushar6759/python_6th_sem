T = int(input())
while T > 0:
    n = int(input())
    l=n%10
    f=n
    count=0
    while(n>0):
      f=n
      n=n//10
    print(f+l)
    T -= 1