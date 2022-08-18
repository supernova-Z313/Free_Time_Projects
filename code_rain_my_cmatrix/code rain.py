def main():
    import random, time, os
    size = int(input())
    page = [[" " for i in range(size)] for j in range(size)]
    first_l = {i: [] for i in range(size)}
    word_a = [['A', 'H', 'M', 'A', 'D', 'R', 'E', 'Z', 'A', ' '], ['S', 'U', 'P', 'E', 'R', 'N', 'O', 'V', 'A', ' '],
              ['P', 'Y', 'T', 'H', 'O', 'N', ' '], ["I", "R", "A", "N", " "], ['C', 'O', 'D', 'E', ' '], 
	      ["3", "1", "3", " "], ["H", "A", "C", "K", " "]]
    coun = 0
    while True:
        free_space = []
        for i in first_l:
            if first_l[i] == []:
                free_space.append(i)

        if len(free_space) > (size/3):
            if coun == 0:
                selected_l = random.sample(free_space, k=int(size/10))
                selected_w = random.choices(word_a, k=int(size/10))
                coun = 1
            else:
                selected_l = random.sample(free_space, k=int(size/13))
                selected_w = random.choices(word_a, k=int(size/13))
                coun = 0

        for inx, i in enumerate(selected_l):
            first_l[i] = selected_w[inx].copy()
        for i in range(size-1, 0, -1):
            for j in range(0, size):
                page[i][j] = page[i-1][j]
        for i in first_l:
            if first_l[i] != []:
                char = first_l[i][0]
                page[0][i] = char
                first_l[i].remove(char)

        os.system("cls")
        for i in page:
            print("  ".join(i))
        time.sleep(0.2)


if __name__ == "__main__":
    main()
