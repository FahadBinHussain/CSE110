list_one = [1, 3, 5, 7, 9, 10]
list_two = [2, 4, 6, 8]

list_one.pop()
for element in list_two:
  list_one.append(element)

print(list_one)