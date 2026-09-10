class student:
    def __init__(self, name ,Class,mark,subject):
        self.name = name
        self.Class = Class
        self.mark = mark
        self.subject = subject
        print("hello")


s = student("harish",8,69,"geography")
print(s.name,s.mark,s.Class,s.subject)
