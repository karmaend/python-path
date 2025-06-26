def compound_interest(p,r,t):
    ca=p*(1+(r/100))**t
    return(ca)

p=float(input("enter your principle amount: "))
r=float(input("enter your rate of interest: "))
t=float(input("enter your time: "))

tot_amt=compound_interest(p,r,t)
print("your total amount is: ",tot_amt)
print("your interest earned is: ", tot_amt-p)