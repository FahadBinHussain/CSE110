# Get user input for decimal number
decimal = int(input("Enter a decimal integer number: "))

# Initialize variables
binary = ""
remainder = 0

# Convert decimal to binary using repeated division by 2
while decimal > 0:
    remainder = decimal % 2
    binary = str(remainder) + binary
    decimal = decimal // 2

# Print binary representation of decimal
print(binary)
