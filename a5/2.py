a = []
str = ""
user_input = input()

user_input += ","

for chr in user_input:
    if chr != ",":
        str += chr
    else:
        a.append(int(str))
        str = ""
    
if len(a) <= 3:
    print("Not possible")
else:
    print(a[2:-2])