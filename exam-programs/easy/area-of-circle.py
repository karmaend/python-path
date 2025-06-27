import math
def area(r):
    circle = math.pi * math.pow(r,2)
    return(circle)

r=float(input("enter your radius: "))
ar=area(r)
print("the area of your circle is: ", ar)