num = int(input("Enter a number: "))
count = 0
while num != 0:
    count += 1
    num //= 10
print("The number of digits is:", count)
