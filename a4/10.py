user_input = input("Enter two strings separated by a comma and a space: ")
s1, s2 = user_input.split(", ")

mixed_string = ""
i = 0
j = 0

while i < len(s1) and j < len(s2):
  mixed_string += s1[i] + s2[j]
  i += 1
  j += 1

mixed_string += s1[i:] + s2[j:]

print(mixed_string)
