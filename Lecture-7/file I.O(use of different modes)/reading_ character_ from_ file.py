#reading particular number of character from file
file = open("information.txt","r")

data =file.read(6)
print(data)
file.close()