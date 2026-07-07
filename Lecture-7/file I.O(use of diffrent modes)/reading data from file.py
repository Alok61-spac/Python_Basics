#use r mode for reading
file = open("information.txt","r")

data = file.read()
print(data)
file.close