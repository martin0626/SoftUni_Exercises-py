import math 
students_count = int(input())
lectures_count = int(input())
bonus = int(input())
biggest = 0
current_attendence = None
for student in range (students_count):
    attendance = int(input())
    total_bonus = attendance / lectures_count * (5 + bonus)
    total_bonus = math.ceil(total_bonus)
    if total_bonus > biggest:
        biggest = total_bonus
        current_attendence = attendance

print (f'Max bonus: {biggest}.\nThe student has attended {current_attendence} lectures.')
