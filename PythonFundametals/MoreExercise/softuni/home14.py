start_hour = int(input())
start_min = int(input())
arrive_hour = int(input())
arrive_min = int(input())
hour_diff = 0
min_diff = 0
early = False
on_time = False
late = False
if start_hour == arrive_hour and start_min == arrive_min:
    print ('On time')
    
    
elif start_hour > arrive_hour and start_min > arrive_min:
    hour_diff = start_hour - arrive_hour 
    min_diff =  start_min - arrive_min 
    if min_diff > 30 or hour_diff > 0:
        print ('Early')
        early = True
    else: 
        print ('On time')
        no_time = True
elif start_hour > arrive_hour and start_min == 0:
    hour_diff = (start_hour - arrive_hour) - 1
    min_diff =  60 - arrive_min
    if min_diff > 30 or hour_diff > 0:
        print ('Early')
        early = True
    else: 
        print ('On time')
        on_time = True
elif start_hour > arrive_hour and start_min < arrive_min:
    hour_diff = start_hour - arrive_hour 
    min_diff = arrive_min  - start_min 
    if min_diff > 30 or hour_diff > 0:
        print ('Early')
        early = True
    else: 
        print ('On time')
        on_time = True
elif start_hour == arrive_hour and start_min < arrive_min:
    hour_diff = 0 
    min_diff = arrive_min  - start_min 
    print ('Late')
    late = True
elif start_hour == arrive_hour and start_min > arrive_min:
    hour_diff = 0 
    min_diff = start_min - arrive_min  
    if min_diff > 30 or hour_diff > 0:
        print ('Early')
        early = True
    else: 
        print ('On time')
        on_time = True 

elif start_hour < arrive_hour and arrive_min > start_min:
    hour_diff = arrive_hour - start_hour
    min_diff = arrive_min - start_min
    print ('Late')
    late = True
elif start_hour < arrive_hour and arrive_min < start_min:
    hour_diff = arrive_hour - start_hour
    min_diff =  start_min - arrive_min 
    print ('Late')
    late = True
elif start_hour < arrive_hour and arrive_min == 0:
    hour_diff = (arrive_hour - start_hour) - 1
    min_diff = 60 - start_min 
    print ('Late')
    late = True
elif start_hour < arrive_hour and start_min == 0:
    hour_diff = (arrive_hour - start_hour) - 1
    min_diff = 60 - arrive_min
    print ('Late')
    late = True


    
if min_diff == 60:
    min_diff = 0
    hour_diff += 1

if early == True:

    if hour_diff < 1:
        print (f'{min_diff} minutes before the start')
    elif hour_diff > 0 and min_diff < 10:
        print (f'{hour_diff}:0{min_diff} hours before the start')  
    elif hour_diff > 0:
        print (f'{hour_diff}:{min_diff} hours before the start')


elif late == True:
    if hour_diff < 1:
        print (f'{min_diff} minutes after the start')
    elif hour_diff > 0 and min_diff < 10:
        print (f'{hour_diff}:0{min_diff} hours after the start')  
    elif hour_diff > 0:
        print (f'{hour_diff}:{min_diff} hours after the start')
elif on_time == True:
    if hour_diff < 1:
        print (f'{min_diff} minutes before the start')
    elif hour_diff > 0 and min_diff < 10:
        print (f'{hour_diff}:0{min_diff} hours before the start')  
    elif hour_diff > 0:
        print (f'{hour_diff}:{min_diff} hours before the start')


    