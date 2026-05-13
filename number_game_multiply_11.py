# Number game that multiplies two digits by 11 and
# inserts the sum between digits

# User input in tens and ones

num_in_tens = int(input("Enter the tens digit: "))
num_in_ones = int(input("Enter the ones digit: "))

# Get the sum of tens and ones through multiplication

num_in = num_in_tens * 10 + num_in_ones

# Get the result

print("You entered", num_in)
print(num_in, "* 11 is", num_in * 11 )

# Number out of hundreds and tens
num_out_hundreds = num_in_tens + ((num_in_tens + num_in_ones) // 10)
print("Number out of hundreds:", num_out_hundreds)

num_out_tens = num_in_tens // 10
print("Number out of tens:", num_out_tens)

num_out_ones = num_in_tens % 10
print("Number out of ones:", num_out_ones)

# Telling user the easy way to find the answer
print("An easy mental way to find the answer is:")
print(num_in_tens, ",", num_in_tens, "+", num_in_ones, ",", num_in_ones, ",")

# Build next line from digits on previous line
num_out = str(num_out_hundreds) + str(num_in_tens) + str(num_in_ones)
print("You answer is:", num_out)
