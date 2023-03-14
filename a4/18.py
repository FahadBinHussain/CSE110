# inpu1 = input()
# inpu2 = int(input())

# if inpu2 % 2 == 0:
#   for i in range(inpu2 * 2):
#     print(inpu1, end="")
# else:
#   for i in range(inpu2 * 3):
#     print(inpu1, end="")

string = input("Enter a string: ")
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(string * (2*number))
else:
    print(string * (3*number))
