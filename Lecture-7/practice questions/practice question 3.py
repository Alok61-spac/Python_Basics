# find a word and print is it exist or not
def check_word():
   word = "learning"
   with open("practice.txt","r")as file:
     data = file.read()
     if(data.find(word) != -1):
         print("Found")
     else:
         print("Not Found")
        
check_word()


def check_line():
   data = True
   word = "learning"
   line = 1
   with open("practice.txt","r") as file:
        while data:
            data = file.readline()
            if(word in data):
                 print(line)
                 return
            line += 1
   return -1
check_line()