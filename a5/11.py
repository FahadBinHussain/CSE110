List_one = [1, 4, 3, 2, 5]

List_two = [8, 7, 6, 9]

common_num = False

for num in List_one:
    if num in List_two:
        common_num = True
        break

# Print the results
if common_num:
    print("True")
else:
    print("False")