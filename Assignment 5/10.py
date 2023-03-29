user_input = input()
user_input += ", "
num = ""
input_list = []
modified_list = []

for chr in user_input:
  if chr != ",":
    if chr != " ":
      num += chr
  else:
    input_list.append(int(num))
    if int(num) not in modified_list:
      modified_list.append(int(num))
      num = ""
    else:
      num = ""
      
print(f"Input list: {input_list}")
print(f"Modified list: {modified_list}")