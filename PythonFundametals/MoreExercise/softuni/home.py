hour = int(input())
mins = int(input())
boole = True
mins += 15

if mins >= 60:
    hour += 1
    mins -= 60
    if mins == 60:
        mins = 0
        print (f'{hour}:{mins}0')
if hour > 23:
    hour = 0
if mins < 10:
    print (f'{hour}:0{mins}')
    boole = False
    

if boole == True:
    print (f'{hour}:{mins}')

