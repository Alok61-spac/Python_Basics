numbers = (82,93,0,93,8,61,199,83,81,84)
print(type(numbers))
print(len(numbers))
#print the occuranc of number at which index
x = 61
i =0 
while i < len(numbers):
    if(numbers[i] == x):

        print("the number occurs at index :",i)
    i += 1