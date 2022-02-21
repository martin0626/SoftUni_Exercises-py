n1 = int(input())
n2 = int(input())
magic_n = int(input())
counter = 0
have_num = False
for x in range (n1, n2 + 1):
    for y in range (n1, n2 + 1):
        counter += 1 
        if (x + y) == magic_n:
            print (f'Combination N:{counter} ({x} + {y} = {magic_n})')
            have_num = True
            break
    if have_num:
        break
if have_num == False:
    print (f'{counter} combinations - neither equals {magic_n}')        


        
