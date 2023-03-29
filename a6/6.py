tuple1 = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

list1 = list(tuple1)
final_list = []

for i in range(len(list1)-1, -1, -1):
    final_list.append(list1[i])

print(final_list)