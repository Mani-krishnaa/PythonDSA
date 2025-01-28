def swap(a,b):
    temp =a
    a=b
    b=temp
    print(a,b)

def swap1(a,b):
    a = a + b # 30
    b = a - b # 10
    a = a - b# 20
    print(a,b)

def swap2(a,b):
    a,b =b,a
    print(a,b)
    
a ,b =10,20

swap(a,b)
swap1(a,b)
swap2(a,b)
