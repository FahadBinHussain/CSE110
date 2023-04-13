def function_name(string):
    upper=0
    lower=0
    
    for i in string:
        
        
        if i!=' ':
            k=i.isupper()
            if k==True:
                upper+=1
            else:
                lower+=1
    print('No. of Uppercase characters : ',upper)
    print('No. of Lowercase Characters : ',lower)
    
function_name(input('Enter a string'))