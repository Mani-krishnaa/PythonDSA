# Swapping two numbers


def swapUsingTemp(a, b):
    # using temp variable
    temp = a
    a = b
    b = temp
    print(a)
    print(b)


def swapUsingaddsub(a, b):
    # using add and sub
    a = a + b
    b = a - b
    a = a - b
    print(a)
    print(b)


def swapUsingtupleUnpacking(a, b):
    a, b = b, a
    print(a)
    print(b)


a = int(input("Enter a value"))
b = int(input("Enter second Value"))

swapUsingaddsub(a, b)
swapUsingTemp(a, b)
swapUsingtupleUnpacking(a, b)
