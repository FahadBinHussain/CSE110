num = int(input("Enter a number: "))
while num > 0:
    print(num % 10, end="")
    if num > 10:
      print(", ", end="")
    if num < 10:
      print(" ", end="")
    num //= 10
