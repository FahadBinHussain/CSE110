def area_circumference_generator(x):
    global area
    global circumference
    circumference=2*3.141592653589793*x
    area=3.141592653589793*(x**2)
    
    return area,circumference
    
print(area_circumference_generator(float(input('enter radius'))))
a_tuple=(area,circumference)
a,b=a_tuple
print('Area of the circle is',a,end=' ')
print('and circumference is',circumference)