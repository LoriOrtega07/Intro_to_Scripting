# Simple program taking the slice of a string
start_index = int(input("Enter start index: "))
end_index = int(input("Enter end index: "))
my_string = "Where there's smoke, there's fire"

# Create conditions of the slice
sub_saying = my_string[start_index:end_index]

print("Full saying:", my_string)
print("Sliced saying:", sub_saying)
