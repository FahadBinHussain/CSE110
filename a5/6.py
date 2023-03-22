user_input = input("Enter a string of 7 comma-separated numbers: ")
user_list = []
str = ""

for chr in user_input:
    if chr != ",":
       str += chr
    else:
        user_list.append(int(str))
        str = ""     

large_num = user_list[0]
large_index = 0

for i in range(1, len(user_list)):
    if user_list[i] > large_num:
        large_num = user_list[i]
        large_index = i

print("My list:", user_list)
print(f"Largest number in the list is {large_num} which was found at index {large_index}.")