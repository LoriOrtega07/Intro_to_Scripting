# Greet the user with their birthyear assignment
# Import data set
from datetime import date

# Get user data
name = input("What is your name? ")
age = input("How old are you? ")

# Get current year and calculation
current_year = date.today().year
birth_year = current_year - int(age)

print(f"Hello {name}! You were born in {birth_year}")
