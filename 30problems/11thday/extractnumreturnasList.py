from unicodedata import digit


def fun1(n):
    L = []
    while n > 0:
        s = n % 10
        # print(s)
        L.append(s)
        n = n // 10
    return L


def fun2(n):
    L = []
    for i in str(n)[::-1]:
        
        L.append(digit(i))
    return L


n = int(input("Enter a Num"))
print(fun2(n))
