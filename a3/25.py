# Get user input for N
N = int(input("Enter a number N: "))

# Initialize variables for the first two Fibonacci numbers
a = 0
b = 1

# Loop through all Fibonacci numbers up to N
while a <= N:
    print(a)
    c = a + b
    a = b
    b = c
