# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# print('The first 50 fibonacci numbers are:')
# print(','.join([str(fib(n)) for n in range(50)]))

# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return 

def fib(n, memo={}):
    if n in memo:
        return memo[n]

    if n == 0:
        return 0

    if (n <= 2):
        return 1

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    print(n, memo)
    return memo[n]

print('The first ** fibonacci numbers are:')
print(','.join([str(fib(n)) for n in range(1000, 1010)]))
# print(fib(1000))

