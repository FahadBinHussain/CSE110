list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_two = [10, 11, 12, -13, -14, -15, -16]

final = []
for element in list_one:
  if element % 2 == 0:
    final.append(element)
for element in list_two:
  if element % 2 == 0:
    final.append(element)

print(final)