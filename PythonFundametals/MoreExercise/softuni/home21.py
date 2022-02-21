name = input()
counter = 0
grade_sum = 0
counter_fails = 0
while counter != 12:
    counter += 1
    grade = float(input())
    if grade < 4:
        counter -= 1
        counter_fails += 1
        if counter_fails > 1:
            print (f'{name} has been excluded at {counter + 1} grade')
            break
    else:
        grade_sum += grade
grade_sum /= 12
if counter == 12:
    print (f'{name} graduated. Average grade: {grade_sum:.2f}')


