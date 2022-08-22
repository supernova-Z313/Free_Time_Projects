from time import perf_counter
n = int(input())
st = perf_counter()
mat = []
def make_next_matrix(previous_mat, next_n):
    if(next_n == 1):
        return [[1]]
    else:
        result = []
        first_row = []
        last_row = []
        for i in range(next_n):
            first_row += [(next_n ** 2) - next_n + 1 + i]
        result += [first_row]
        for i in range(next_n - 2):
            row = [(next_n ** 2) - next_n - i] + previous_mat[i] + [((next_n - 2) ** 2) + 1 + i]
            result += [row]
        for i in range(next_n):
            last_row += [((next_n - 2) ** 2) + next_n + next_n - 2 - i]
        result += [last_row]
    return result
for i in range(int((n + 1)/2)):
    mat = make_next_matrix(mat, (i * 2) + 1)
def print_matrix(mat):
    for row in range(len(mat)):
        for column in range(len(mat[0])):
            print('{:^5s}'.format(str(mat[row][column])), end='')
        print()
en = perf_counter()
print_matrix(mat)
print("\n", (en-st))
input()