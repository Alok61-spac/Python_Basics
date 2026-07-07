dict={
    "student":"harish",
    "class":8,
    "grade":"B",
    "mark":477

}
#return all key
print(dict.keys())

#return all valuse
print(dict.values())

#return all key value pair
print(dict.items())

#return value according key
print(dict.get("mark"))

#insert key value pair in dictionary
dict.update({"sub":("phy","chem","math")})
print(dict)
