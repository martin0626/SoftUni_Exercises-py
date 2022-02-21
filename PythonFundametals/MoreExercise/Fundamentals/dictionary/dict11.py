d = {'1': 5, '2':3, '3': 66, '4':100, '5':22}
biggest = -1111111
biggest_2 = -111111
biggest_3 = -11111111
y = max(d.values())

for x in d.values():
    if x != y:
        
        if x > biggest:
            biggest = x
        elif x > biggest_2:
            biggest_2 = x
    

print (f'The greatest three numbers:\n{y}\n{biggest}\n{biggest_2}')