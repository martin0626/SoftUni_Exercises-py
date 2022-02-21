from collections import deque


pumps = int(input())
queue = deque([[int(e) for e in input().split()] for _ in range(pumps)])
tank = 0
index = 0
counter = 0
smallest_index = 0

while counter != pumps:
    curr_pump = queue.popleft()
    petrol, distance = curr_pump
    tank += petrol
    if tank >= distance:
        tank -= distance
        counter += 1
        if counter == 1:
            smallest_index = index

    else:
        tank = 0
        counter = 0

    queue.append(curr_pump)
    index += 1

print(smallest_index)
