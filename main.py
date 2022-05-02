import math

n = str(input())
n = n.split()
numbers = [int(i) for i in n]
x = numbers[0]
y = numbers[1]




if y > x:
    print(0)
elif y == 1 or y == x: print(1)
else:
    a = math.factorial(x)
    b = math.factorial(y)
    div = a // (b*(x-y))
    print(div)

