# 8. print integer 1 to n divisible by m and tell the number which is divisible by m is even or odd

n= int(input("Enter n "))
m=int(input("Enter m "))

print()
for i in range(1,n):
    if (i%m==0):
        if(i%2==0):
            print(str(i)+" Even")
        else:
            print(str(i)+" odd")


