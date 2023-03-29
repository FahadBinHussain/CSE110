list_one = [1, 4, 3, 2, 5]
list_two = [8, 7, 6, 9]

common_num = False

for num in list_one:
    if num in list_two:
        common_num = True
        break
 
# Print the results
if common_num:
    print("True")
else:
    print("False")