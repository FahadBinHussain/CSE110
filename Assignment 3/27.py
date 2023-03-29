# Get user input for binary number
binary = input("Enter a binary number: ")

# Initialize variables
decimal = 0
power = len(binary) - 1

# Convert binary to decimal using positional notation
for digit in binary:
    decimal += int(digit) * (2 ** power)
    power -= 1

# Print decimal representation of binary
print(decimal)
