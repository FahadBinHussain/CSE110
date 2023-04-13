def function_name(list):
    removed=0
    new_list=[]
    for i in list:
        if new_list.count(i)<2:
            new_list.append(i)
        else:
            removed+=1
    print(new_list)
    print('Removed:',removed)
        
    
function_name([int(element) for element in input("please enter a list:").split(",")])