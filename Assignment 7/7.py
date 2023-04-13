def show_palindrome(x):
    result=''
    for i in range(1,x):
        result=result+str(i)
    for j in range(x,0,-1):
        result=result+str(j)
    
    return result
    
print(show_palindrome(int(input('enter a number'))))