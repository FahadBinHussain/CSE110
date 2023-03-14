string = input("Enter a string: ")
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(string * (2*number))
else:
    print(string * (3*number))
