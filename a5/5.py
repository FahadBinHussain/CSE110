given_list = ["hey", "there", "", "what's", "", "up", "", "?"]
output = []

for element in given_list:
    if element != "":
        output.append(element)

print(f"Original List: {given_list}")
print(f"Modified List: {output}")