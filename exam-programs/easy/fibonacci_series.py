def fibo(n):
    a=0
    b=1
    
    if n<0:
        print("enter a positive integer, smartass.")
        
    elif n==1:
        print(a)
    
    else:
        print(a)
        print(b)
    
        for i in range(2,n):
            c=a+b
            a=b
            b=c
        
            print(c)
        
print("how long do you want the fibonacci series to be? ")
n=int(input())
fib=fibo(n)    