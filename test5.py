list = ["4", "9", "16", "25", "36"]
word = input()
if word.lower() in list:

    print('число из под корня получается натуральным')
else:
    print('такого корня не существует')

num = word
sqrt = num ** (0.5)
print("Квадратный корень из числа "+str(num)+" это "+str(sqrt))
