num = int(input())
sum_grade = 0
fail = 0
good = 0
better = 0
best = 0


for x in range (num):

    grade = float(input())
    sum_grade += grade 
    

    if grade < 3:
        fail += 1
    elif 3 <= grade <= 3.99:
        good += 1
    elif 4 <= grade <= 4.99:
        better += 1
    elif grade > 5:
        best += 1

sum_fail = fail / num * 100
sum_good = good /num * 100
sum_better = better / num * 100
sum_best = best / num * 100
end_sum = sum_grade / num

print (f'Top students: {sum_best:.2f}%.')
print (f'Between 4.00 and 4.99: {sum_better:.2f}%.')
print (f'Between 3.00 and 3.99: {sum_good:.2f}%.')
print (f'Fail: {sum_fail:.2f}%.')
print (f'Average: {end_sum:.2f}')