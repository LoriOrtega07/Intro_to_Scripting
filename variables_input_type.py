# Simple program that reads and outputs different data types
from pickletools import unicodestring1

# Get user input
user_int = int(input("Enter integer (32 - 126):\n"))

#Set-up additional variables and produce output on single line
enter_float = float(input("Enter float:\n"))
enter_char = str(input("Enter character:\n"))
enter_str = str(input("Enter string:\n"))

print(user_int, enter_float, enter_char, enter_str)

# Output the four values in reverse
print(enter_str, enter_char, enter_float, user_int)

# Convert integer to a character and produce output
old_val = user_int
change_type = chr(old_val)
print(old_val,"converted to a character is",change_type)
