import math
def fib_check(n):
    cond1=(5*(n*n)+4)
    cond2=(5*(n*n)-4)
    
    sqrt1=math.isqrt(cond1)
    sqrt2=math.isqrt(cond2)
    
    if sqrt1*sqrt1==cond1 or sqrt2*sqrt2==cond2:
        return True
    return False
    
n=int(input("enter the number to be checked: "))

if fib_check(n):
    print("fibonacci number")
else:
    print("not a fibonacci number")