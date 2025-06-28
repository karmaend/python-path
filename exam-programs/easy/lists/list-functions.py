a=[1,2,3,4,5,6,7]

#lenth of list
print("length of list is: ",len(a))

#sum of elements of list, if numeric

print("sum of elements of list is: ",sum(a))

#max of element of list, if numeric
print("the maximum number in the list is: ",max(a))

#min of elements of list, if numeric
print("the minimum number in the list is: ",min(a))

#list comprehensions
#i want to find the squares of numbers in the range of 5 square
squares=[x*x for x in range(8)]
print("the squares in range of 5 square are: ",squares)