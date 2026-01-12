answer = input("What is the capital of France? ")

if answer == "Paris":
    print("Correct! ")
else:
    print("Sorry, that's wrong.")

#ADVANCE VERSION 

answer = input("What is the capital of France? ")

if answer.lower() == "paris":
    print("Correct! ")
else:
    print("Sorry, that's wrong.")


# ADVANCED VERSION CAPITALIZATION QUIZ 


questions = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Denmark": "Copenhagen"
}

score = 0

for country, capital in questions.items():
    user_answer = input(f"What is the capital of {country}? ")

    if user_answer.lower() == capital.lower():
        print("Correct! ✅")
        score += 1
    else:
        print(f"Wrong ❌ — the correct answer is {capital}")

print(f"\nYou got {score} out of {len(questions)} correct!")

