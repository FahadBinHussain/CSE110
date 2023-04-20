def count_case(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print("No. of Uppercase characters :", upper_count)
    print("No. of Lowercase Characters:", lower_count)

count_case('The quick Sand Man')
