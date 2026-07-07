#creat student class that takes name and mark of 3 subject as argument in constructor.then craet a meathod to print average.

class student:
 def __init__(self,name,subject1,subject2,subject3):
     self.name =name
     self.subject1=subject1
     self.subject2=subject2
     self.subject3=subject3
     print(f"{self.name} got an avarage of {(self.subject1+self.subject2+self.subject3)/3}")

name =str(input("Enter your Name:"))
subject1 =float(input("Enter your Mark of subject 1:"))
subject2=float(input("Enter your Mark of subject 2:"))
subject3=float(input("Enter your Mark of subject 3:"))

s=student(name,subject1,subject2,subject3)
