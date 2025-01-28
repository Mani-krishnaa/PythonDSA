import re


def fun1(n):
    return (n * (n + 1)) // 2  # this is formula for sum of natural num


def fun2(n):
    sum = 0
    for i in range(0, n + 1):
        sum = sum + i
    return sum


def fun3(n):  # using recurssion
    if n == 0:
        return 0
    return n + fun3(n - 1)


# print(fun1(5))
# print(fun2(6))
print(fun3(6))



