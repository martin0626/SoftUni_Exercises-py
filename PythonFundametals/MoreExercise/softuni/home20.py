n = int(input())
salary = int(input())
summ = 0

for x in range (n):
    web_site = input()
    if web_site == 'Facebook':
        summ += 150
    elif web_site == 'Instagram':
        summ += 100
    elif web_site == 'Reddit':
        summ += 50
    if summ >= salary:
        print (f'You have lost your salary.')
        break

if salary > summ:
    end_sum = salary - summ
    print (end_sum)