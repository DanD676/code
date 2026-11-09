from datetime import datetime
# Ask for the user's name and age
name = input("What is your name? ")
age = int(input("How old are you? "))
# Calculate the birth year
birth_year = datetime.now().year - age
print(f"\nHello {name}! You were born in {birth_year}.")
