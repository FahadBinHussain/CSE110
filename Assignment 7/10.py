def make_square(start):
    print(start)
    dictionary={}
    for i in range(start[0],start[1]+1):
        dictionary[i]=i**2
    return dictionary
    
print(make_square((1,3)))