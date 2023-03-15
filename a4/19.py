inpu = input()

outpu = ""

prev = "l"
  
for i in inpu:

  if 65 <= ord(i) <= 90:
    
    if prev == "u":
      low_inpu = chr(ord(i) + 32)
      outpu += low_inpu
      prev = "l"
      
    elif prev == "l":
      outpu += i
      prev = "u"
    
  elif 97 <= ord(i) <= 122:
    
    if prev == "u":
      outpu += i
      prev = "l"
      
    elif prev == "l":
      up_inpu = chr(ord(i) - 32)
      outpu += up_inpu
      prev = "u"
      
  else:
    outpu += i
  
    
  

print(outpu)