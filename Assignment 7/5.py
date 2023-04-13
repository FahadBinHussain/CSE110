def calculate_tax(age,salary,job):
    k=job.upper()
    tax=0
    if age<18 or k=='PRESIDENT' or salary<10000:
        tax=0
    elif 10000<salary<20000:
        tax=(salary*5)/100
    elif salary>20000:
        tax=(salary*10)/100
    return tax
        
    
print(calculate_tax(age=int(input()),salary=int(input()),job=input()))