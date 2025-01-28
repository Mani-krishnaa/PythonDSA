def fun1(n):
    count = 0
    while n > 0:
        count = count + 1
        n = n // 10
    print(count)


def fun2(n):
    count = 0
    for _ in str(n):
        count = count + 1
    print(count)


n = int(input("Enter a Num"))
fun2(n)
fun1(n)
