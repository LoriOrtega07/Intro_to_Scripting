# This program will calculate the average calories
# burned for a person when exercising.

# Get input values
age_years = int(input())
weight_pounds = int(input())
heart_rate = int(input())
time_minutes = int(input())

# Apply the equation
Calories = (((age_years * 0.2757) + (weight_pounds * 0.03295)
            + (heart_rate * 1.0781)- 75.4991)
            * time_minutes / 8.368)

# Produce the output
print(f"Calories: {Calories:.2f} Calories")

