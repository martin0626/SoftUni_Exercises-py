n = int(input())
p1 = 0 
p2 = 0
p3 = 0
for x in range (n):
    num = int(input())

    if num % 2 == 0:
        p1 += 1

    if num % 3 == 0:
        p2 += 1
    
    if num % 4 == 0:
        p3 += 1

p1_sum = p1 / n * 100
p2_sum = p2 / n * 100
p3_sum = p3 / n * 100

print (f'{p1_sum:.2f}%\n{p2_sum:.2f}%\n{p3_sum:.2f}%')
