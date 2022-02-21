bad_grades = int(input())
name = input()
counter = 0
counter_grades = 0
sum_grades = 0
last_exc = ''
while name != 'Enough':
    grade = int(input())
    counter_grades += 1
    sum_grades += grade
    last_exc = name
    if grade <= 4:
        counter += 1
        if counter >= bad_grades:
            print (f'You need a break, {counter} poor grades.')
            break
    name = input()
avr = sum_grades / counter_grades
if name == 'Enough':
    print (f'Average score: {avr:.2f}\nNumber of problems: {counter_grades}\nLast problem: {last_exc}')

        