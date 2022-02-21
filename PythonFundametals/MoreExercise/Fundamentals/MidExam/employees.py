emloyee_1 = int(input())
emloyee_2 = int(input())
emloyee_3 = int(input())
people_count = int(input())
hours = 0
per_hour = emloyee_1 + emloyee_2 + emloyee_3

while people_count > 0:
    hours += 1
    if not hours % 4 == 0:
        people_count -= per_hour 
    
print (f'Time needed: {hours}h.')