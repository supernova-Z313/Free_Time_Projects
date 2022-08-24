def main():
    di = input()
    text = {}
    text1 = "text.update(" + di + ")"
    exec(text1)
    for i in text:
        text[i] = len(set(text[i]))
    max_1 = -1
    anw = None
    for i in  text:
        if text[i] > max_1:
            max_1 = text[i]
            anw = i
    print(anw)


if __name__ == "__main__":
    main()
    # {"y" : [5, 6, 5], "k" : [2, 1, 9]}
    # {"G" : [5,7,7,7,7], "is" : [6,7,7,7], "B" : [9, 9, 6, 5, 5]}

