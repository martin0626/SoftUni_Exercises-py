import operator
n = int(input())

students = {}

for x in range (n):
    name = input()
    grade = float(input())
    
    if name not in students:
        students[name] = []

    students[name].append(grade)

sorted_d = dict(sorted(students.items(), key=lambda item: (sum(item[1]) / len(item[1])), reverse=True))

for key, value in sorted_d.items():
    if (sum(value) / len(value)) >= 4.5:
        print (f'{key} -> {(sum(value) / len(value)):.2f}')
