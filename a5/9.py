user_input = input()
user_input += " "
num = ""
num_list = []

for chr in user_input:
  if chr != " ":
    num += chr
  else:
    if int(num) % 2 != 0: 
      num_list.append(int(num))
      num = ""
    else:
      num = ""

print(num_list)