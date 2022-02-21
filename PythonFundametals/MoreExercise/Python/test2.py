a = int(input())
b = int(input())
c = int(input())
min_num = min (a, b, c)
max_num = max (a, b, c)
sum1 = (a + b + c)  - max_num
if max_num == sum1:
    sec = max_num - min_num
    print (f'{min_num} + {sec} = {max_num}')

else:
    print ('No')
