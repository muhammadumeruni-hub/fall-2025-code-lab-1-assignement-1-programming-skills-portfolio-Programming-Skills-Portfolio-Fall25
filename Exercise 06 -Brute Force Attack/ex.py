# the correct password we want the user to guess
correct_password = "12345"

user_input = input("Enter the password: ")

# keep asking until the user gets it right
while user_input != correct_password:
    user_input = input("Wrong password. Try again: ")

print("Access granted. Welcome!")


#ADVANCED 

correct_password = "12345"
attempts_left = 5

while attempts_left > 0:
    user_input = input("Enter the password: ")

    if user_input == correct_password:
        print("Access granted. Welcome!")
        break
    else:
        attempts_left -= 1

        if attempts_left > 0:
            print(f"Incorrect. You have {attempts_left} attempts left.")
        else:
            print("Too many failed attempts. The authorities have been alerted.")
