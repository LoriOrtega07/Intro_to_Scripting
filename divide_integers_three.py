# Divide integer inputs three times using floor division.

user_num = int(input())
div_num = int(input())

# First floor division
first = user_num // div_num
print(first, end=" ")

# Second floor division
second = first // div_num
print(second, end=" ")

# Third floor division
third = second // div_num
print(third)
