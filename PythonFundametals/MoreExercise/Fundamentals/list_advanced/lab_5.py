# empoyees = input().split()
# empoyees = list(map(int, empoyees))
# factor = int(input())
# employees_factor = [i * factor for i in empoyees]
# average = sum(employees_factor) / len(employees_factor)


# happy_employers = []


# for number in employees_factor:
#     if number >= average:
#         happy_employers.append(number)
# if not len(happy_employers) >= (len(employees_factor) // 2):
#     print (f'Score: {len(happy_employers)}/{len(employees_factor)}. Employees are not happy!')

# else:
#     print (f'Score: {len(happy_employers)}/{len(employees_factor)}. Employees are happy!')
numbers = [int(num) for num in input().split()]
factor = int(input())
after_factor = [x * factor for x in numbers]
average_happiness = sum(after_factor) / len(after_factor)
after_filtration = [number for number in after_factor if number >= average_happiness]

if len(after_filtration) >= len(after_factor) // 2:
    print (f'Score: {len(after_filtration)}/{len(after_factor)}. Employees are happy!')
else:
    print (f'Score {len(after_filtration)}/{len(after_factor)}. Employees are not happy!')
