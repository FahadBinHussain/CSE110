def function_name(list):
    removed=0
    new_list=[]
    for i in list:
        if new_list.count(i)<2:
            new_list.append(i)
        else:
            removed+=1
    print('Removed:',removed)
    print(new_list)
    
        
    
function_name([1, 2, 3, 3, 3, 3, 4, 5, 8, 8])