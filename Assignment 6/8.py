user_dict = input()
split_dict = user_dict.split(",")
total = 0
item = 0

for chr in split_dict:
    split_list = chr.split(":")
    total += int(split_list[1])
    item += 1
    
print(f"Average is {int(total/item)}.")