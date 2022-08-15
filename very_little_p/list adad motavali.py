n = int(input())
x = list(range(n))
v = 1
for i in range(1,n+1):
    if i == 1:
        k = 1
        x[0] = [1]
    else:
        m = (k*4) + 4
        k = (m//4)+1
        x[i-1] = list(range(v+1, m+v+1))
        v += m
print(x)
input()
