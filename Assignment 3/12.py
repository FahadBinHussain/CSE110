# # Take input from user
# number = int(input("Enter a number: "))

# # Count the number of digits
# count = 0
# temp = number
# while temp > 0:
#     count += 1
#     temp //= 10

# # Calculate 10 to the power (number of digits - 1)
# power = 10 ** (count - 1)

# # Loop through each digit from left to right
# while power > 0:
#     # Extract the leftmost digit
#     digit = number // power
    
#     # Print the digit
#     print(digit, end=" ")
    
#     # Remove the leftmost digit
#     number %= power
    
#     # Update the power
#     power //= 10

n = int(input("Enter a number: "))
divisor = 1
while n // divisor > 10:
    divisor *= 10
while divisor > 0:
    digit = n // divisor
    n %= divisor
    divisor //= 10
    if divisor != 0:
      print(digit, end=', ')
    else:
      print(digit, end='')

