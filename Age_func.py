def checkDriverAge(n):
    if int(n) < 18:
          print("Sorry, you are too young to drive this car. Powering off")
    elif int(n) > 18:
          print("Powering On. Enjoy the ride!")
    elif int(n) == 18: 
          print("Congratulations on your first year of driving. Enjoy the ride!")
	   

age=int(input("Enter your age:"))
s=checkDriverAge(age)
print(s)