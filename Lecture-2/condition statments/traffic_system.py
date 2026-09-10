#maintain traffic system
light =str(input("Enter the colour of light by traffic police :"))
if (light.lower() == "red"):
    print("stop")
elif(light.lower == "green"):
    print("go")
elif(light.lower() == "orange"):
    print("wait")
else:
    print("light is broken")

