#python program for string manipulation
#remove all the vowels
#replace the digits with their corresponding ASCII values
#replace the consonant with its next lowercase consonant character

user = input("Enter a string: ")

answer = ""

for i in user:
  if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
    answer += ""
  elif i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
    answer += ""
  elif i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
    answer += str(ord(i))
  elif 65 <= ord(i) <= 90:
    answer += chr(ord(i) + 32 + 1)
  elif 97 <= ord(i) <= 122:
    answer += chr(ord(i) + 1)
  else:
    answer += i

print(answer)
