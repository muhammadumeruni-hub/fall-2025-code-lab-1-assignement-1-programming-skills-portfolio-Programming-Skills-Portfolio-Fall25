# list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# searching for "Sam"
if "Sam" in names:
    print("Found Sam in the list!")
else:
    print("Sam is not in the list.")


#ADVANCED 

# list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# ask the user what name to search for
search_name = input("Enter the name you want to search for: ").strip()

# check if the name is in the list
if search_name in names:
    print(f"Found {search_name} in the list!")
else:
    print(f"{search_name} is not in the list.")
