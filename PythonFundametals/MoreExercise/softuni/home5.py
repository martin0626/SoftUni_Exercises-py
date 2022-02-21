import math 
record = float(input())
lenght = float(input())
time_for_meter = float(input())

sum_time = time_for_meter * lenght
water_resistance = math.floor(lenght // 15)
water_resistance = water_resistance * 12.5
end_sum = sum_time + water_resistance

if record < end_sum:
    end_sum -= record
    print (f'No, he failed! He was {end_sum:.2f} seconds slower.')
elif record > end_sum:
    record -= end_sum
    print (f'Yes, he succeeded! The new world record is {end_sum:.2f} seconds.')

