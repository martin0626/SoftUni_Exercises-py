def average(grades_list):
    result = sum(grades_list) / len(grades_list)
    return f'{result:.2f}'


n = int(input())
students = ([input() for _ in range(n)])

students_grades = {}

for info in students:
    info = info.split()
    name, grade = info[0], float(info[1])
    if name not in students_grades:
        students_grades[name] = []
    students_grades[name].append(grade)

for student, grades in students_grades.items():
    grades_f = " ".join([f'{g:.2f}' for g in grades])
    print(f'{student} -> {grades_f} (avg: {average(grades)})')



