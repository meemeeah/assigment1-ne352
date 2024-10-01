#welcome message for the user
print("Welcome to the program!")

#ask user for name , age and height to store it 
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height: "))

#print the information 
print("\nThank you for giving this information!!")
print("Your name is " + name)
print("Your age is " + str(age))
print("Your height is " + str(height))

#Display a message that have all information 
print(f"\nHello {name}, you are {age} years old and {height} tall!")