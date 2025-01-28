def fun1(n):
    rev = 0
    while n > 0:
        s = n % 10
        rev = rev * 10 + s  # formula for reverse num
        n = n // 10
    print(rev)


def fun2(n):
    rev = 0
    for i in str(n)[::-1]:
        rev = rev * 10 + int(i)
    print(rev)


def fun3(n):
    print(str(n)[::-1])


n = int(input("Enter a num"))
fun2(n)
fun3(n)
fun1(n)
