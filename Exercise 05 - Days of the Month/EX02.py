# dictionary that maps month numbers to the number of days
days_in_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

month = input("Enter a month number (1–12): ")

if month.isdigit():
    month = int(month)

    if 1 <= month <= 12:
        print(f"This month has {days_in_month[month]} days.")
    else:
        print("That month number doesn’t exist.")
else:
    print("Please enter a valid number.")

#ADVANCED 


# same basic dictionary, but February may change based on leap year
days_in_month = {
    1: 31,
    2: 28,  # default; we'll adjust if it's a leap year
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

month = input("Enter the month number (1–12): ")

if month.isdigit():
    month = int(month)

    if 1 <= month <= 12:

        if month == 2:
            leap = input("Is it a leap year? (yes/no): ").lower().strip()

            if leap == "yes":
                print("February has 29 days this year.")
            else:
                print("February has 28 days.")
        else:
            print(f"This month has {days_in_month[month]} days.")

    else:
        print("That month number isn't valid.")
else:
    print("Please type a number.")