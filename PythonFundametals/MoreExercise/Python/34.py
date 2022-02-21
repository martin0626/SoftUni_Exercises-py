n = int(input())
max_num = -1000000
sum_all = 0
for x in range (n):
    y = int(input())
    if y > max_num:
        max_num = y
    sum_all += y
    

if sum_all / max_num == 2:
    print (f'Yes \nsum = {max_num}')
else: 
    sum_all -= max_num
    max_num -= sum_all
    print (f'No\ndiff = {max_num}')