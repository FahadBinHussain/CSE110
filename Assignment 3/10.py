num = int(input("Enter a number: "))
while num > 0:
    print(num % 10, end=" ")
    num //= 10
