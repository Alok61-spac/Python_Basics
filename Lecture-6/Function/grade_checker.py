# get your grade according to your mark
def grade_check(mark):
    if mark >=90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >=33:
        return "C"
    else :
        return "F"
mark = int(input("Enter your mark : "))
print("Your grade is :",grade_check(mark))
          