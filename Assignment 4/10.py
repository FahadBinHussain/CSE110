input_str = input("Enter two strings separated by a comma and a space: ")

# find the index of the comma and space
comma_space_index = None
for i in range(len(input_str)):
    if input_str[i] == "," and input_str[i+1] == " ":
        comma_space_index = i
        break

# extract the two input strings
input_str1 = ""
for i in range(comma_space_index):
    input_str1 += input_str[i]

input_str2 = ""
for i in range(comma_space_index + 2, len(input_str)):
    input_str2 += input_str[i]

# initialize an empty string to store the mixed string
mixed_str = ""

# determine the length of the shorter input string
shorter_len = len(input_str1)
if len(input_str2) < shorter_len:
    shorter_len = len(input_str2)

# loop through the input strings
for i in range(shorter_len):
    mixed_str += input_str1[i]
    mixed_str += input_str2[i]

# add any leftover characters to the mixed string
if len(input_str1) > shorter_len:
    mixed_str += input_str1[shorter_len:]
if len(input_str2) > shorter_len:
    mixed_str += input_str2[shorter_len:]

print(mixed_str)
