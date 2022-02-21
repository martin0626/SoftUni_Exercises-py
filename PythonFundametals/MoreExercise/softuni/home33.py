jury = int(input())
presentation_name = input()
sum_grades = 0
counter_grades = 0

counter_for_one = 0
while presentation_name != 'Finish':
    grades_for_one = 0

    for x in range (1, jury + 1):
        grade = float(input())
        counter_grades += 1
        sum_grades += grade
        grades_for_one += grade
        
        if x == jury:
            end_grade = grades_for_one / jury
            print (f'{presentation_name} - {end_grade:.2f}.')
            
            break
    presentation_name = input()
end_sum = sum_grades / counter_grades
print (f"Student's final assessment is {end_sum:.2f}.")