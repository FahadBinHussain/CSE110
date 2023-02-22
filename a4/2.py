user = input("Enter a string: ")
index = int(input("Enter an index: "))
a = user[index::-1]
b = user[index+1::1]

print(a+b)
