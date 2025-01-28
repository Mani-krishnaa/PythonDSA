def fun(n):
    L = []
    a = -1
    b = +1
    
    for i in range(n):
        c = a+ b
        L.append(c)
        a =b
        b = c
    return L
n = int(input("Enter a number"))

print(fun(n))