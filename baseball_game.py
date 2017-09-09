from random import randint

numbers = [randint(0, 9)]

while len(numbers) < 3:
    new_num = randint(0, 9)
    if new_num in numbers:
        continue
    else:
        numbers.append(new_num)

print("We've selected three random number (0 ~ 9).")
print()

throw = []
trial = 0
again = True
while again:
    print("Please provide three numbers between 0 and 9")

    # First attempt
    first = int(input("What's your first number?: "))
    while first < 0 or first > 9:
        print("The number you selected is out of range, a number should be between 0 and 9")
        first = int(input("What's your first number?: "))
    throw.append(first)

    # Second attempt
    second = int(input("What's your second number?: "))
    second_atmpt = True
    while second_atmpt:
        if second == first:
            print("You've already provided the number, please give us a different number")
            second = int(input("What's your second number?: "))
        elif second < 0 or second > 9:
            print("The number you selected is out of range, a number should be between 0 and 9")
            second = int(input("What's your second number?: "))
        else:
            second_atmpt = False
    throw.append(second)

    # Third attempt
    third = int(input("What's your third number?: "))
    third_atmpt = True
    while third_atmpt:
        if third == first or third == second:
            print("You've already provided the number, please give us a different number")
            third = int(input("What's your third number?: "))
        elif third < 0 or third > 9:
            print("The number you selected is out of range, a number should be between 0 and 9")
            third = int(input("What's your third number?: "))
        else:
            third_atmpt = False
    throw.append(third)

    i = 0
    stk = 0
    ball = 0
    while i < len(numbers):
        if throw[i] == numbers[i]:
            stk += 1
        elif throw[i] in numbers:
            ball += 1
        i += 1

    trial += 1
    if stk == 3:
        print("Congrats! your guess is right with %d times of trial!" % (trial))
        again = False
    else:
        print("%dS %dB" % (stk, ball))
        del throw[::]
        print()





