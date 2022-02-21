from collections import deque
from datetime import timedelta


robots = [r for r in input().split(';')]
free_robots = deque([[el for el in r.split('-')] for r in robots])
hours, minutes, seconds = [int(t) for t in input().split(':')]
robots_working = {}
current_time = timedelta(hours=hours, minutes=minutes, seconds=seconds)
# final_time = start_time + timedelta(seconds=68)

queue_products = deque()

while True:
    command = input()
    if command == 'End':
        break
    queue_products.append(command)

while queue_products:
    product = queue_products.popleft()
    current_time += timedelta(seconds=1)
    if free_robots:
        name, work_time = free_robots.popleft()
        work_time = int(work_time)
        if current_time < timedelta(hours=10):
            print(f'{name} - {product} [0{current_time}]')
        else:
            print(f'{name} - {product} [{current_time}]')

        finish_work = current_time + timedelta(seconds=work_time)
        robots_working[name] = [work_time, str(finish_work)]
    else:
        queue_products.append(product)
        best_time_robot = ['', -10000000]
        for name, list_info in robots_working.items():
            work_time, finish_work = list_info
            if int(work_time) < best_time_robot[1]:
                best_time_robot = [name, work_time]
                finis = finish_work
        free_robots.append(best_time_robot)
