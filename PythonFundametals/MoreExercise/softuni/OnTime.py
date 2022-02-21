start_hour = int(input())
start_min = int(input())
arrive_hour = int(input())
arrive_min = int(input())

total_min_exam = start_min + (start_hour * 60)
total_min_arrive = arrive_min + (arrive_hour * 60)
total_diff = total_min_exam - total_min_arrive



hour_diff = total_diff // 60
min_diff = total_diff % 60

if 0 <= total_diff <= 30:
    print ('On time')
    if total_diff != 0:
        print (f'{total_diff} minutes before the start')

elif total_diff > 30:
    print ('Early')
  
    hour_diff = total_diff // 60
    min_diff = total_diff % 60
    if hour_diff < 1:
        print (f'{total_diff} minutes before the start')
    elif min_diff < 10:
        print (f'{hour_diff}:0{min_diff} hours before the start')
    else:
        print (f'{hour_diff}:{min_diff} hours before the start')


else: 
    total_diff = abs(total_diff)
    hour_diff = total_diff // 60
    min_diff = total_diff % 60

    print ('Late')
    if hour_diff < 1:
        print (f'{total_diff} minutes after the start')
    elif min_diff < 10:
        print (f'{hour_diff}:0{min_diff} hours after the start')
    else:
        print (f'{hour_diff}:{min_diff} hours after the start')






    
        
        