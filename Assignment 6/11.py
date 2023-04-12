string = input("Enter a string: ")

string = string.lower()

char_freq = {}

str = ""

for char in string:
    if char != " ":
        str += char

for i in str:
    if i not in char_freq:
        char_freq[i] = 1
    else:
        char_freq[i] += 1

print(char_freq)