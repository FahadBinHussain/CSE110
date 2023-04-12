list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]


dict_1 = {}


for tup in list_1:
    
    if tup[0] not in dict_1:
        
        dict_1[tup[0]] = [tup[1]]
    else:
      
        dict_1[tup[0]].append(tup[1])


print(dict_1)