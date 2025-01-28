def fun1(n):
    return print(n[::-1])


def fun2(n):
    rev = " "

    for char in n:
        rev = char + rev
    print(rev)


n = input("Enter the String")
fun2(n)
