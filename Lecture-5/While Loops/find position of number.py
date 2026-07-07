A = (82,93,0,93,8,61,199,83,81,84)
print(type(A))
print(len(A))
#print the occuranc of number at which index
x = 61
i =0 
while i < len(A):
    if(A[i] == x):

        print("the number occurs at index :",i)
    i += 1