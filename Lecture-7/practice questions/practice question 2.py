#replace java word with python.
with open("practice.txt","r") as file:
          data = file.read()
          print(data) 
new_data = data.replace("java","python")
print("new_data")

with open("practice.txt","w") as file:
        Data = file.write(new_data)
        print(Data)
          