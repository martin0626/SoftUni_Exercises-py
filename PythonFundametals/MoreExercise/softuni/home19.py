numbers = int(input())
sum_even = 0
sum_odd = 0
even_max = -1000000000
even_min = 1000000000
odd_max = -10000000000
odd_min = 1000000000


for x in range (1, numbers + 1):
    num = float(input())

    if x % 2 == 0:
        sum_even += num
        if num < even_min:
            even_min = num
        if num > even_max: 
            even_max = num
    if x % 2 != 0:
        sum_odd += num
        if num < odd_min:
            odd_min = num
        if num > odd_max:
            odd_max = num

print(f'OddSum={sum_odd:.2f},')
if odd_min == 1000000000:
    print ('OddMin=No,')
elif odd_min != 1000000000:
    print (f'OddMin={odd_min:.2f},')
if odd_max == -10000000000:
    print ('OddMax=No,')
elif odd_max != -1000000000:
    print (f'OddMax={odd_max:.2f},')   

print (f'EvenSum={sum_even:.2f},')
if even_min == 1000000000:
    print ('EvenMin=No,')
elif even_min != 1000000000:
    print (f'EvenMin={even_min:.2f},')
if even_max == -1000000000:
    print ('EvenMax=No')
elif even_max != -1000000000:
    print (f'EvenMax={even_max:.2f}')



                



    


