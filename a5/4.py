a = []
str = ""
given_list = [1, 2, 3, 4, 5, 6, 7]
sliced_input = given_list[1:-1]
sliced_input += ","

for chr in sliced_input:

    if chr != ",":
        str += chr
    else:
        a.append(int(str) ** 2)
        str = ""
    
print(a)