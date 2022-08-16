import random
highest = 30
answer = random.randint(1, highest)
print('please guess a number between 1 to {}: '.format(highest))
gusse = int(input())
if gusse == answer:
    print('you got it first time .')
elif gusse == 0:
    print('exit game')
else:
    while gusse != answer:
        if gusse >= answer:
            print('please guess lower')
        else:
            print('please guess higher')
        gusse = int(input('please enter a new gusse: '))
        if gusse == 0:
            print('exit game')
            break
    else:
        print('your answer is true ')
x1 = input()
