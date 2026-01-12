try:
    num = int(input("Enter a number: "))
    result = 10 / num 
    print(result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid number!")
else:
    print("Success! Result is", result)
finally:
    print("This always runs, no matter what.")

    # Calculate the average of two numbers
    a = 10
    b = 20
    average = a + b / 2  # Logical error
    print(average)

    