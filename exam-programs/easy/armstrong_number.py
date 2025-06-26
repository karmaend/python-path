def armstrong(n):
    s=n
    num=str(n)
    length=len(num)
    sum=0
    
    while n!=0:
        r=n%10
        sum=sum+(r**length)
        n=n//10
        
    return s==sum

n=int(input("enter your number: "))
if armstrong(n):
    print("armstrong number")
else:
    print("not an armstrong number")

