my_dict={
    "student":"harish",
    "class":8,
    "grade":"B",
    "mark":477

}
#return all key
print(my_dict.keys())

#return all valuse
print(my_dict.values())

#return all key value pair
print(my_dict.items())

#return value according key
print(my_dict.get("mark"))

#insert key value pair in dictionary
my_dict.update({"sub":("phy","chem","math")})
print(my_dict)
