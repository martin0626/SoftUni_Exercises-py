from math import floor
record = float(input())
lenght = float(input())
time_for_m = float(input())

water_resistance = floor(lenght / 15)
sum_time = time_for_m * lenght + water_resistance * 12.5

if sum_time > record:
    sum_time -= record
    print (f'No, he failed! He was {sum_time:.2f} seconds slower.')
else:
    record -= sum_time
    print (f'Yes, he succeeded! The new world record is {sum_time:.2f} seconds.')

#....................END!.......................                

