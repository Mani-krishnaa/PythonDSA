def fun1(n):
    while n > 0:
        s = n % 10
        print(s)
        n = n // 10


n = int(input("Enter a num"))
fun1(n)
