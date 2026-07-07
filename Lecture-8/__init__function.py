#collect students details
class student:
    def __init__(self,name, Class, subject,mark):
        self.name=name
        self.Class=Class
        self.subject = subject
        self.mark=mark
        print(f"My name is{self.name}.\n ")

while True:

    name = input("Enter Your Name :")
    Class = input("Enter Your Class:")
    subject =input("Enter Your Subject:")
    mark = input("Enter Your Mark :")
    s=student(name,Class,subject,mark)
# print(s.name,s.mark,s.Class,s.subject,)
   


