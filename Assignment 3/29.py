# Get user input for range and check number
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
check_num = int(input("Enter the number to check: "))

# Loop through each number in the range
for num in range(start, end+1):
    # Multiply all the digits of the current number
    all_products = ""
    product = 1
    for digit in str(num):
        product *= int(digit)
    if product % check_num == 0:
        print(product, end=' ')


