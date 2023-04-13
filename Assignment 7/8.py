def show_palindromic_triangle(x):
    for k in range(1,x+1):
        print((x-k)*' ',end='')
        print(show_palindrome(k))
        
    
show_palindromic_triangle(int(input('enter a number ')))