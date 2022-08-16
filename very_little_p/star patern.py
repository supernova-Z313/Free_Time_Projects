f = int(input())
d = 1

for i in range(f):
    
    print(" "*(f-(d)),end="")
    
    for j in range(1,d+(d-1)+1):
        print("*",end="")
    d += 1
    print("")


input()
