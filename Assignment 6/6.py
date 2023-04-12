tuple1 = (10, 20, 30, 40, 50, 60)
list1 = []

for element in tuple1:
    list1.append(element)

final_list = []

for i in range(len(list1)-1, -1, -1):
    final_list.append(list1[i])

print(tuple(final_list))