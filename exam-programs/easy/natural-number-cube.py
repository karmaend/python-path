import math
x=int(input("enter the limit: "))
sum=0
for i in range(0,x+1):
    sum+=i**3
    
print(f"sum of natural numbers till {x} is: ", sum)