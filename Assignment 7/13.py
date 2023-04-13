def my_funct(operator,val1,val2):
    
    if operator=='+':
        result=val1+val2
    elif operator=='-':
        result=val1-val2
    
    elif operator=='/':
        result=val1/val2
    elif operator=='*':
        
        result=val1*val2
    return result
    
    
print(my_funct(operator=input(),val1=float(input()),val2=float(input())))