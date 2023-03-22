a = []

for i in range(5):
    user_input = int(input())
    a.append(user_input)

reversed = a[::-1]
print("Printing values from the list in reverse order:")

for element in reversed:
    print(element)