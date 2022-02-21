import sys
factor = int(input())
count = int(input())
counter = 0
list_nums = []
for num in range (1, sys.maxsize):
    
    if num % factor == 0:
        list_nums.append(num)
        counter += 1
    if counter == count:
        print (list_nums)
        break