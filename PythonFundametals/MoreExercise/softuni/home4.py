import math 
income = float(input())
grade = float(input())
min_income = float(input())
ex_boole = False 
soc_boole = False
social = math.floor(min_income * 0.35)
excellent = math.floor(grade * 25)

if grade >= 5.5:
    ex_boole = True 

if income < min_income and grade > 4.5:
    soc_boole = True 

if ex_boole and soc_boole:
    if social > excellent:
        print (f'You get a Social scholarship {social} BGN')   
    else:
        print (f'You get a scholarship for excellent results {excellent} BGN')
elif ex_boole:
    print (f'You get a scholarship for excellent results {excellent} BGN')

elif soc_boole: 
    print (f'You get a Social scholarship {social} BGN')
else:
    print (f'You cannot get a scholarship!')




    




