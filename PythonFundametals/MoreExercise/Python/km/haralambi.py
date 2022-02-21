import math
money = float(input())
width = float(input())
lenght = float(input())
a = float(input())
h = float(input())
price_fl = float(input())
price_worker = float(input())


plochki_num  = ((width * lenght)/((a * h)/2)) + 5 
end_sum = price_fl * math.ceil(plochki_num) + price_worker 

if end_sum > money:
    end_sum -= money
    print (f'You will need {end_sum:.2f} lv more.')

else:
    money -= end_sum
    print (f'{money:.2f}')