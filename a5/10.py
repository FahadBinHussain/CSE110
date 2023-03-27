user_input = input()
user_input += ", "
num = ""
input_list = []

for chr in user_input:
  if chr != "," and chr != " ":
    num += chr
  else:
    input_list.append(int(num))
    num = ""
      
print(input_list)