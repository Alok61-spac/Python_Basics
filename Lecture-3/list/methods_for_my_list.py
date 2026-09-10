#add some values in list in random index
data = [739,39,79,738,82,85,82,47,92,99,72,99]
data.append(68)
print(data)
#add some value at particular index
data.insert(2,34)
print(data)
#remove the first occurrence of value in list
data.remove(99)
print(data)
#remove value of particular index
data.pop(4)
print(data)
#print in reverse manner
data.reverse()
print(data)
#print in ascending order
data.sort()
print(data)
#print in descending order
data.sort(reverse = True)
print(data)