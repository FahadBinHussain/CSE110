total = 0
for i in range(1, 601):
    if (i % 7 == 0 or i % 9 == 0) and not (i % 7 == 0 and i % 9 == 0):
        total += i

print(total)
