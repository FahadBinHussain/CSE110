num = int(input("Enter a number: "))
digits = 0

# count number of digits
while num != 0:
    digits += 1
    num //= 10

# calculate 10 to the power of (number of digits - 1)
power = 10 ** (digits - 1)

# print digits from left to right
while power != 0:
    digit = num // power
    print(digit, end=" ")
    num %= power
    power //= 10
