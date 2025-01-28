a = input("Enter a 1st Value")
b = input("Enter a 2nd Value")
c = input("Enter a 3nd Value")




def findMax(a,b,c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    return c
    
    
def findMax1(a,b,c):
    return a if a > b and a > c else b if b > c else c

def findMax2(a,b,c):
    return max(a,b,c)
    
print("fun1",findMax(a,b,c),findMax1(a,b,c),findMax2(a,b,c))

