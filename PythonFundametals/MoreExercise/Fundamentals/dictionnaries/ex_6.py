course_name = input()
course_list = {}

while course_name != 'end':
    course, student = course_name.split(' : ')

    if course not in course_list:
        course_list[course] = []
    course_list[course].append(student)

    course_name = input()
course_list = dict(sorted(course_list.items(), key=lambda item: len(item[1]), reverse=True))
for k, v in course_list.items():
    course_list[k] = sorted(v)

for x in course_list.keys():
    print (f'{x}: {len(course_list[x])}')
    for y in course_list[x]:
        print (f'-- {y}')
        




