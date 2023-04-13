# Write a python function that takes the limit as an argument of the Fibonacci series and prints till that limit. 

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=' ')
        a, b = b, a+b
    
fibonacci(1)