# Divide integer inputs three times using floor division.

user_num = int(input())
div_num = int(input())

# First floor division
first = user_num % div_num
print(first)

# Second floor division
second = user_num // div_num
print(second)

# Third floor division
third = user_num % div_num
print(third)
