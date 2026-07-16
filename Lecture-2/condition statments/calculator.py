# Basic calculator

first_Value = float(input("enter your first value :"))
second_value= float(input("enter your second value :"))


print("option 1 for sum")
print("option 2 for substraction")
print("option 3 for multipiction")
print("option 4 for quotient")
print("option 5 for reminder")
print("option 6 for power")


O = int(input("Enter Your Option :"))


if O == 1:
    print(float( first_Value + second_value))

elif O == 2:
    print(float(first_Value - second_value))
    

elif O == 3:
    print(float(first_Value * second_value))

elif O == 4 :
    if second_value == 0:
        print("Can not divided by zero")
    else:
        print(float(first_Value / second_value))
elif O == 5:
    if second_value == 0:
        print("Can not divisible by zero")
    else:
        print(float(first_Value % second_value))

elif O == 6:
    print(int(first_Value ** second_value))
else :
    print("ERROR")
                        

            

        


