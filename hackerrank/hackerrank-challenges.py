""" Introduction """

# Say Hello World with Python

print("Hello, World!")

# Python If/Else

N = int(input())

if N % 2 != 0:
    print("Weird")
elif N % 2 == 0 and N >= 2 and N <= 5:
    print("Not Weird")
elif N % 2 == 0 and N >= 6 and N <= 20:
    print("Weird")
elif N % 2 == 0 and N > 20:
    print("Not Weird")

## Python Arithmetic

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print("{} \n{} \n{}".format(a + b, a - b, a * b))

# Python Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print("{} \n{}".format(a//b, a/b))

# Write a function

def is_leap(year):
    leap = False
    if year % 4 == 0 and year % 400 == 0:
        leap = True
    elif year % 4 == 0 and year % 100 != 0:
        leap = True
    else:
        leap = False
    return leap

year = int(input())

# Loops

if __name__ == '__main__':
    n = int(input())

    for number in range(n):
        print(number ** 2)

# print function

if __name__ == '__main__':
    n = int(input())

    print(*range(1, n + 1), sep="")

# List Comprehensions
if __name__=='__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print[[i, j, k] for i in range (x + 1) for j in range (y + 1) for k in range (z + 1) if ((i + j + k ) != n)]

# Power and Mod Power

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    m = int(input())

    print(a ** b)
    print((a ** b) % m)

# Integers come in all sizes

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    print((a ** b) + (c ** d))

# Triangle Quest
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print('i' * i)

# Find the Runner-Up Score

if __name__ == '__main__':
    n =  int(input())
    arr = map(int, input().split())
