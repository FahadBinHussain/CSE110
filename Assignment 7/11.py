def rem_duplicate(tupl):
    list=[]
    for i in tupl:
        if i not in list:
            list.append(i)
    
    a_tuple=tuple(list)
    print(a_tuple)
    
rem_duplicate((1,1,1,2,3,4,5,6,6,6,6,4,0,0,0))