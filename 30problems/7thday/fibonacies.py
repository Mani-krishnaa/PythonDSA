def fibo(n):
    L = []
    a = -1
    b = +1

    for _ in range(n):
        c = a + b
        L.append(c)
        a = b
        b = c
    print(L)


n = int(input("Enter N value"))

fibo(n)
