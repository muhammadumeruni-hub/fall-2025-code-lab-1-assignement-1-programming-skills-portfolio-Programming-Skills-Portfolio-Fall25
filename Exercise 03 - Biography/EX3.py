# storing a small biography in a dictionary
bio = {
    "name": "John Doe",
    "hometown": "Springfield",
    "age": 25
}

# printing everything on separate lines in one print statement
print(bio["name"], bio["hometown"], bio["age"], sep="\n")
# getting input from the user
name = input("Enter your full name: ")
hometown = input("Enter your hometown: ")

# keep asking for age until the user enters a valid number
while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("Please enter a number for your age.")

# storing everything in a dictionary
bio = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# printing the values on separate lines
print(bio["name"], bio["hometown"], bio["age"], sep="\n")




