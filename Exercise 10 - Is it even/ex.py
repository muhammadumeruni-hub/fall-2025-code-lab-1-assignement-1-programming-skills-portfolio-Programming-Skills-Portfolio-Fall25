def check_even_odd(number):
    """Determines if a number is even or odd and returns a message."""
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"

def main():
    # Ask the user for a number
    num = int(input("Enter a number: "))
    
    # Pass the number to the function and get the result
    result = check_even_odd(num)
    
    # Print the message returned by the function
    print(result)

if __name__ == "__main__":
    main()

