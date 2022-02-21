speed = int(input())
furst_time = int(input())
second_time = int(input())
third_time = int(input())
sec_1 = furst_time / 60
sec_2 = second_time / 60
sec_3 = third_time / 60

fur_speed = speed * sec_1
sec_speed = (speed + (speed * 0.1)) * sec_2
thir_speed = (speed + (speed * 0.05)) * sec_3

sum_all = fur_speed + sec_speed + thir_speed
print (f'{sum_all:.2f}')
