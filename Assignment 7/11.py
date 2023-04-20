def rem_duplicate(tupl):
    list=[]
    for i in tupl:
        if i not in list:
            list.append(i)
    
    a_tuple=tuple(list)
    print(a_tuple)
    
rem_duplicate(("Hi", 1, 2, 3, 3, "Hi",'a', 'a', [1,2]))