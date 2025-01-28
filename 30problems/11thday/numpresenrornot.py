from unicodedata import digit


def fun1(n, target_digit):
    for i in str(n):
        if digit(i) == target_digit:
            print("Num Is Pesent")
            return
    print("Not found")


def fun2(n, target_digit):
    while n > 0:
        if n == target_digit:
            print("Num found")
            n = n // 10
            return
    print("Not found")


n = int(input("Enter a num"))
target_digit = int(input("Enter the Num want to Find"))
fun2(n, target_digit)
