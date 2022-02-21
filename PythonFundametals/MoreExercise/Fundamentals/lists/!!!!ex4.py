numbers = input().split(', ')
beggars = int(input())
new_list = []
sum1 = 0
sum2 = 0
bigger = False
counter = 0
#print (numbers[0 + beggars])
for x in range (0, len(numbers)):
        
    if beggars < len(numbers):
        bigger = True
        if x % beggars == 0:
            sum1 += int(numbers[x])
        else:
            sum2 += int(numbers[x])
    elif beggars == len(numbers):
        for y in numbers:
            new_list.append(y)
    elif beggars > len(numbers):
        for y in numbers:
            new_list.append(y)


    if y == numbers[-1]:
        break
    

if bigger:       
    new_list.append(sum1)
    new_list.append(sum2)
elif beggars > len(numbers):
    diff = beggars - len(numbers)
    for z in range (diff):
        new_list.append('0')
    
print (new_list)

    