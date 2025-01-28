def _oddorEven(n):
        if(n % 2 == 0):
            return True
        return False

def _oddorEven1(n):
    return n % 2 == 0 # # Returns True for even, False for odd

def _oddorEven2(n):
     return (n&1) == 0

for n in range(100):
    print(n,_oddorEven(n,),_oddorEven1(n), _oddorEven2(n),sep='\t')