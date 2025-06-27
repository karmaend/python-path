x=int(input("enter your number: "))
y=int(input("enter the multiple you want: "))

a=0
b=1
count=0

while True:
    if a%x==0:
        count+=1
        if count == y:
            print(f"the {y}th/rd multiple of {x} in fibonacci series is {a}")
            break
    a, b=b, a+b
    


