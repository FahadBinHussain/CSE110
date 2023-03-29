# Initialize the sum and the list of numbers
total = 0
numbers = []

# Read 5 numbers from the user and calculate the partial sums
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
    total += num

# Print the partial sums of all the numbers together
partial_sum = 0
for i in range(5):
    partial_sum += numbers[i]
    print(partial_sum)
