def foo_moo(x):
    
    if x%2==0 and x%3==0:
        result='FooMoo'
    elif x%2==0:
        result='Foo'
    elif x%3==0:
        result='Moo'
    else:
        result='Boo'
    return result
    
print(foo_moo(int(input('enter a number'))))