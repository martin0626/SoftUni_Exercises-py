hour = int(input())
day = input()

if 10 <= hour <= 18:
    if day == 'Monday':
        print ('open')
    if day == 'Tuesday':
        print ('open')
    if day == 'Wednesday':
        print ('open')
    if day == 'Thursday':
        print ('open')   
    if day == 'Friday':
        print ('open')
    if day == 'Saturday':
        print ('open')
    if day == "Sunday":
        print ('close')

if 18 < hour or hour < 10:
    print ('close')

