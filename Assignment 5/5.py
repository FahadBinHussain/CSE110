list = ["hey", "there", "", "what's", "", "up", "", "?"]
output = []

for element in list:
    if element != "":
        output.append(element)

print(f"Original List: {list}")
print(f"Modified List: {output}")