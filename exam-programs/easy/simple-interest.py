def interest(p,r,t):
    si=(p*r*t)/100
    return si

p=float(input("enter your principle amount: "))
r=float(input("enter your rate of interest: "))
t=float(input("enter your time: "))

simple_interest=interest(p,r,t)

print("your simple interest is: ",simple_interest)
print("your total amount is: ",p+simple_interest)


