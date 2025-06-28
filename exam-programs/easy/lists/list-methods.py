fruits=['orange','cherry','guava','papaya']

#append method
fruits.append('mango')
print(fruits)

#insert method
fruits.insert(1, 'apple')
print(fruits)

#remove method
fruits.remove('mango')
print(fruits)

#remove last item with pop()
last=fruits.pop()
print(fruits)

#count occurences
count=fruits.count('apple')
print(count)

#sort in place, in this case, alphabetical order
fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)