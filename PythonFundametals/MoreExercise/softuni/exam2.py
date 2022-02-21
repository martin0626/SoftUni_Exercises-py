import math
income = float(input())
grade = float(input())
min_salary = float(input())
excellent = False
social = False
min_scholarship = 0
max_scholarship = 0
if income < min_salary and grade > 4.5:
    min_scholarship = min_salary * 0.35
    min_scholarship = math.floor(min_scholarship)
    social = True

elif grade >= 5.5:
    max_scholarship = grade * 25
    max_scholarship = math.floor(max_scholarship)
    
    excellent = True

else:
    print (f'You cannot get a scholarship!')

if excellent and social:
    if max_scholarship > min_scholarship:
        print (f'You get a scholarship for excellent results {max_scholarship} BGN')
    else:
        print (f'You get a Social scholarship {min_scholarship} BGN')

elif excellent:
    print (f'You get a scholarship for excellent results {max_scholarship} BGN')

elif social:
    print (f'You get a Social scholarship {min_scholarship} BGN')



