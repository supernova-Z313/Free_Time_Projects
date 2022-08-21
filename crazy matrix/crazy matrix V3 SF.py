from time import perf_counter

number = int(input("pleas enter size of crazy matrix(number should be bigger than 1 and odd): "))
st = perf_counter()
list_k = []
for i in range(number):
    list_k.append([0 for j in range(number)])
list_k[int(number/2)][int(number/2)] = 1

i, j = int(number/2), int(number/2)+1
counter = 2
counter2 = 2

for d in range(int(number/2)):
    for x in range(counter2):
        list_k[i][j] = counter
        counter += 1
        i += 1
    i -= 1
    j -= 1

    for x in range(counter2):
        list_k[i][j] = counter
        counter += 1
        j -= 1
    j += 1
    i -= 1

    for x in range(counter2):
        list_k[i][j] = counter
        counter += 1
        i -= 1
    i += 1
    j += 1

    for x in range(counter2):
        list_k[i][j] = counter
        counter += 1
        j += 1

    counter2 += 2

en = perf_counter()
for i in list_k:
    for j in i:
        print(f"{j:^3} ", end="")
    print()

print("\n", (en-st))
input()
