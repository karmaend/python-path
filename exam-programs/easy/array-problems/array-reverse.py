lst=list(map(int, input("enter your numeric elements separated by a space: ").split()))
print("your list is: ",lst)

n=len(lst)
print("the length of your array is: ", n)

last_element=lst[-1]
print("the last element of your array is: ", last_element)

for i in range(n-1,0,-1):
    lst[i]=lst[i-1]

lst[0]=last_element

print("the rotated array one element from the right is: ",lst)
    

