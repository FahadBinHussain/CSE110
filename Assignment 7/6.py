def time(x):
    
    year=x//365
    month=(x%365)//30
    days=(x%365)%30
    print(year,'years ',end=',')
    print(month,' months and ',end=' ')
    print(days,' days')
    
time(int(input('enter days ')))