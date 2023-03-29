num = int(input("Enter the quantity of numbers: "))
max_num = 0
min_num = 0
sum = 0

for i in range(num):
    x = int(input("Enter a number: "))
    if max_num == 0 or x > max_num:
        max_num = x
    if min_num == 0 or x < min_num:
        min_num = x
    sum += x

avg = sum / num

print("Maximum", max_num)
print("Minimum", min_num)
print("Average is", avg)
